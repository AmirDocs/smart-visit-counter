from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from app.services.visit_counter import record_visit
from app.services.ai_greetings import generate_greeting
from app.utils.github_api import get_github_repo_contents
import random

router = APIRouter()

DEVOPS_TOOLS = [
    {
        "name": "Docker",
        "image": "https://www.docker.com/sites/default/files/d8/2019-07/Moby-logo.png",
        "link": "https://docs.docker.com/"
    },
    {
        "name": "Kubernetes",
        "image": "https://upload.wikimedia.org/wikipedia/commons/3/39/Kubernetes_logo_without_workmark.svg",
        "link": "https://kubernetes.io/docs/home/"
    },
    {
        "name": "Terraform",
        "image": "https://www.terraform.io/assets/images/logo-hashicorp-terraform.svg",
        "link": "https://developer.hashicorp.com/terraform/docs"
    },
    {
        "name": "GitHub Actions",
        "image": "https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png",
        "link": "https://docs.github.com/en/actions"
    },
    {
        "name": "Prometheus",
        "image": "https://prometheus.io/assets/prometheus_logo_grey.svg",
        "link": "https://prometheus.io/docs/introduction/overview/"
    }
]

# Mapping GitHub directory names to friendly display names
REPO_NAME_MAP = {
    "learning-aws": "Learn AWS",
    "learning-bash": "Learn Bash",
    "learning-cicd": "Learn CI/CD",
    "learning-linux": "Learn Linux",
    "learning-terraform": "Learn Terraform",
    "learning-kubernetes": "Learn Kubernetes",
    "learning-networking": "Learn Kubernetes",
    "learning-terraform-iac": "Learn Terraform IAC"
}

@router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    client_ip = request.client.host
    count = record_visit(client_ip)
    greeting = generate_greeting(client_ip)

    tools_to_show = random.sample(DEVOPS_TOOLS, 3)
    tools_html = ""
    for tool in tools_to_show:
        tools_html += f"""
        <a href="{tool['link']}" target="_blank" class="tool-card" title="Go to {tool['name']} docs">
            <img src="{tool['image']}" alt="{tool['name']} logo"/>
            <span>{tool['name']}</span>
        </a>"""

    repo_contents = await get_github_repo_contents()
    repos_html = ""
    if repo_contents:
        for item in repo_contents:
            if item.get("type") == "dir":
                display_name = REPO_NAME_MAP.get(item["name"], item["name"])
                repos_html += f'<li><a href="{item["html_url"]}" target="_blank">{display_name}</a></li>'
    else:
        repos_html = "<li>No submodules or directories found.</li>"

    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <title>Amir's DevOps Hub</title>
        <style>
            * {{
                box-sizing: border-box;
            }}
            body {{
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: #121212;
                color: #ddd;
                margin: 0; padding: 0;
                min-height: 100vh;
                display: flex;
                flex-direction: column;
                align-items: center;
            }}
            .header {{
                width: 100%;
                background-color: #1f2937;
                padding: 1rem 2rem;
                display: flex;
                align-items: center;
                justify-content: space-between;
                box-shadow: 0 3px 6px rgba(0,0,0,0.6);
            }}
            .logo {{
                display: flex;
                align-items: center;
                gap: 0.5rem;
                color: #61dafb;
                font-weight: bold;
                font-size: 1.5rem;
            }}
            .logo svg {{
                width: 32px;
                height: 32px;
                fill: #61dafb;
            }}
            .live-time {{
                color: #82cfff;
                font-weight: 600;
                font-family: monospace;
            }}
            .container {{
                display: flex;
                justify-content: center;
                gap: 4rem;
                padding: 2rem;
                max-width: 1000px;
                width: 95vw;
                flex-wrap: wrap;
                flex-grow: 1;
            }}
            .left-panel, .right-panel {{
                background: #1f2937;
                border-radius: 12px;
                padding: 1.5rem 2rem;
                box-shadow: 0 6px 15px rgba(0,0,0,0.7);
                flex: 1 1 400px;
                min-width: 300px;
            }}
            h1 {{
                margin-top: 0;
                color: #61dafb;
                letter-spacing: 1.3px;
            }}
            h2 {{
                color: #82cfff;
                margin-bottom: 1rem;
                border-bottom: 1px solid #3b4a62;
                padding-bottom: 0.25rem;
            }}
            h3 {{
                color: #a0cfff;
                margin-top: 1rem;
                margin-bottom: 0.25rem;
            }}
            p, li {{
                color: #ccc;
                line-height: 1.4;
            }}
            .ip, .visit-count {{
                font-style: italic;
                color: #999;
                margin-bottom: 1rem;
                text-align: center;
                margin-top: 0;
            }}
            .visit-count {{
                font-size: 1.5rem;
                font-weight: 700;
                color: #61dafb;
            }}
            .tools {{
                display: flex;
                gap: 1.5rem;
                margin-bottom: 2rem;
                flex-wrap: wrap;
                justify-content: center;
            }}
            .tool-card {{
                background: #2e3a4c;
                border-radius: 12px;
                padding: 1rem 1.25rem;
                width: 120px;
                display: flex;
                flex-direction: column;
                align-items: center;
                text-decoration: none;
                color: #ddd;
                transition: transform 0.3s ease, box-shadow 0.3s ease;
            }}
            .tool-card:hover {{
                transform: translateY(-8px);
                box-shadow: 0 10px 25px rgba(97,218,251,0.5);
            }}
            .tool-card img {{
                width: 64px;
                height: 64px;
                object-fit: contain;
                margin-bottom: 0.5rem;
                filter: brightness(1.1);
            }}
            .tool-card span {{
                font-weight: 600;
                color: #61dafb;
            }}
            ul {{
                list-style-type: none;
                padding-left: 0;
            }}
            li {{
                margin: 0.3rem 0;
            }}
            a {{
                color: #82cfff;
                text-decoration: none;
            }}
            a:hover {{
                text-decoration: underline;
            }}
            footer {{
                width: 100%;
                text-align: center;
                padding: 1rem 0;
                font-size: 0.85rem;
                color: #666;
                border-top: 1px solid #333;
                background-color: #121212;
                margin-top: auto;
            }}
            .container > div {{
                opacity: 0;
                transform: translateY(20px);
                animation: fadeInUp 0.7s ease forwards;
            }}
            .container > div:nth-child(1) {{
                animation-delay: 0.1s;
            }}
            .container > div:nth-child(2) {{
                animation-delay: 0.3s;
            }}
            @keyframes fadeInUp {{
                to {{
                    opacity: 1;
                    transform: translateY(0);
                }}
            }}
        </style>
    </head>
    <body>
        <header class="header" role="banner">
            <div class="logo" aria-label="Amir Beile's DevOps Hub Logo">
                <svg viewBox="0 0 64 64" aria-hidden="true" focusable="false">
                    <circle cx="32" cy="32" r="30" stroke="#61dafb" stroke-width="3" fill="none"/>
                    <path d="M16 32a16 16 0 1 1 32 0 16 16 0 1 1 -32 0" stroke="#61dafb" stroke-width="2" fill="none"/>
                    <circle cx="32" cy="32" r="8" fill="#61dafb"/>
                </svg>
                Amir Beile DevOps Hub
            </div>
            <div class="live-time" aria-live="polite" aria-atomic="true" id="time-display"></div>
        </header>
        <main class="container" role="main">
            <section class="left-panel" aria-labelledby="greeting-title">
                <h1 id="greeting-title">{greeting}</h1>
                <p class="ip">Your IP address: {client_ip}</p>
                <p class="visit-count">Number of visits from you: {count}</p>
                <h2>DevOps Tools</h2>
                <div class="tools" role="list">
                    {tools_html}
                </div>
            </section>
            <section class="right-panel" aria-labelledby="repo-title">
                <h2 id="repo-title">GitHub Learning Submodules</h2>
                <ul>
                    {repos_html}
                </ul>
            </section>
        </main>
        <footer role="contentinfo">
            Amir Beile &copy; 2024 - Powered by FastAPI and GitHub
        </footer>
        <script>
            function updateTime() {{
                const now = new Date();
                const timeString = now.toLocaleTimeString();
                document.getElementById('time-display').textContent = timeString;
            }}
            setInterval(updateTime, 1000);
            updateTime();
        </script>
    </body>
    </html>
    """

    return HTMLResponse(content=html_content)

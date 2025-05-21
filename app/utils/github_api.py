import httpx

GITHUB_API_URL = "https://api.github.com"
GITHUB_REPO = "AmirDocs/devops-learning"

async def get_github_repo_contents(path=""):
    url = f"{GITHUB_API_URL}/repos/{GITHUB_REPO}/contents/{path}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        if response.status_code != 200:
            return []
        return response.json()

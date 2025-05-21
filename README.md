# DevOps Hub - FastAPI Homepage

A simple, AI-enhanced FastAPI-powered homepage designed to showcase and learn essential DevOps tools while tracking visitor interactions with a sleek, modern UI.

## Features

- **AI-powered greeting:** Personalised greeting dynamically generated based on visitor IP using intelligent logic.
- **Visitor tracking:** Displays visitor's IP address and counts the number of visits.
- **DevOps tools highlights:** Randomly displays three popular DevOps tools with official documentation links.
- **GitHub repository listing:** Fetches and displays submodules and directories from my linked GitHub repository.
- **Live clock:** Real-time clock in the header.
- **Dark-themed responsive design:** Clean, modern interface with accessible styling and animations.

## Technology Stack

- Python 3.10+
- [FastAPI](https://fastapi.tiangolo.com/)
- Async HTTP requests for GitHub API integration
- Custom CSS for styling and animations

## Usage

1. **Clone the repository:**
   ```
   git clone git@github.com:AmirDocs/smart-visit-counter.git
   ```

## Set Up the Image

1. **Build the Docker Image:**

   ```
   docker build -t ai-visit-timer .
   ```

2. **Run the Dockerfile**

   ```
   docker run -p 8000:8000 ai-visit-timer
   ```
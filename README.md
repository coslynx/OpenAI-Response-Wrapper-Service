<div class="hero-icon" align="center">
  <img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
</div>

<h1 align="center">
AI Wrapper for OpenAI Responses
</h1>
<h4 align="center">A Python backend service that simplifies and enhances interactions with OpenAI's powerful AI models.</h4>
<h4 align="center">Developed with the software and tools below.</h4>
<div class="badges" align="center">
  <img src="https://img.shields.io/badge/Framework-FastAPI-blue" alt="Framework used: FastAPI" />
  <img src="https://img.shields.io/badge/Backend-Python-red" alt="Backend Language: Python" />
  <img src="https://img.shields.io/badge/Database-PostgreSQL-blue" alt="Database: PostgreSQL" />
  <img src="https://img.shields.io/badge/LLMs-OpenAI-black" alt="Language Models: OpenAI" />
</div>
<div class="badges" align="center">
  <img src="https://img.shields.io/github/last-commit/coslynx/AI-Wrapper-for-OpenAI-Responses?style=flat-square&color=5D6D7E" alt="git-last-commit" />
  <img src="https://img.shields.io/github/commit-activity/m/coslynx/AI-Wrapper-for-OpenAI-Responses?style=flat-square&color=5D6D7E" alt="GitHub commit activity" />
  <img src="https://img.shields.io/github/languages/top/coslynx/AI-Wrapper-for-OpenAI-Responses?style=flat-square&color=5D6D7E" alt="GitHub top language" />
</div>

## 📑 Table of Contents
- 📍 Overview
- 📦 Features
- 📂 Structure
- 💻 Installation
- 🏗️ Usage
- 🌐 Hosting
- 📄 License
- 👏 Authors

## 📍 Overview

This repository houses the AI Wrapper for OpenAI Responses, a Python-based backend service designed to streamline and enhance interactions with OpenAI's powerful AI models. It addresses the challenge of interacting directly with the OpenAI API, which can be complex for developers due to the need for managing API keys, handling authentication, and processing raw JSON responses.  

## 📦 Features
|    | Feature            | Description                                                                                                        |
|----|--------------------|--------------------------------------------------------------------------------------------------------------------|
| ⚙️ | **Architecture**   | The codebase follows a modular architectural pattern with separate directories for different functionalities, ensuring easier maintenance and scalability.             |
| 📄 | **Documentation**  | This README file provides a detailed overview of the MVP, its dependencies, and usage instructions.|
| 🔗 | **Dependencies**   | The codebase relies on various external libraries and packages such as `fastapi`, `openai`, `sqlalchemy`, `pyjwt`, `psycopg2-binary`, `pydantic`, `pytest`, `black`, `dotenv`, and `requests`, which are essential for building and styling the UI components, and handling external services.|
| 🧩 | **Modularity**     | The modular structure allows for easier maintenance and reusability of the code, with separate directories and files for different functionalities such as `api`, `routers`, `models`, `utils`, `database`, `middleware`, `scripts`, and `tests`.|
| 🧪 | **Testing**        | Implement unit tests using frameworks like `pytest` to ensure the reliability and robustness of the codebase.       |
| ⚡️  | **Performance**    | The performance of the system can be optimized based on factors such as the browser and hardware being used. Consider implementing performance optimizations for better efficiency.|
| 🔐 | **Security**       | Enhance security by implementing measures such as input validation, data encryption, and secure communication protocols.|
| 🔀 | **Version Control**| Utilizes Git for version control with GitHub Actions workflow files for automated build and release processes.|
| 🔌 | **Integrations**   | Interacts with browser APIs, external services through HTTP requests, and includes integrations with speech recognition and synthesis APIs.|
| 📶 | **Scalability**    | Design the system to handle increased user load and data volume, utilizing caching strategies and cloud-based solutions for better scalability.           |

## 📂 Structure

```text
ai-wrapper/
├── requirements.txt
├── .env
├── config
│   └── settings.py
├── api
│   └── main.py
├── routers
│   └── ai_router.py
├── models
│   ├── generate_request.py
│   └── generate_response.py
├── utils
│   ├── generate_text.py
│   └── config.py
├── database
│   ├── models.py
│   └── engine.py
├── middleware
│   ├── auth.py
│   └── error_handler.py
├── scripts
│   └── create_database.py
├── startup.sh
├── commands.json
└── tests
    ├── test_ai_router.py
    ├── test_utils.py
    └── test_database.py
```

## 💻 Installation

### 🔧 Prerequisites

- Python 3.9+
- PostgreSQL (database server)

### 🚀 Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/coslynx/AI-Wrapper-for-OpenAI-Responses.git
   cd AI-Wrapper-for-OpenAI-Responses
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up the database:
   ```bash
   python scripts/create_database.py
   ```
4. Configure environment variables:
   ```bash
   cp .env.example .env
   # Fill in the necessary environment variables
   ```

## 🏗️ Usage

### 🏃‍♂️ Running the MVP
1. Start the FastAPI server:
   ```bash
   uvicorn api.main:app --host 0.0.0.0 --port 8000 --reload
   ```

## 🌐 Hosting

### 🚀 Deployment Instructions

#### Deploying to Heroku

1. Install the Heroku CLI:
   ```bash
   pip install heroku
   ```
2. Login to Heroku:
   ```bash
   heroku login
   ```
3. Create a new Heroku app:
   ```bash
   heroku create AI-Wrapper-for-OpenAI-Responses-production
   ```
4. Set up environment variables:
   ```bash
   heroku config:set OPENAI_API_KEY=sk-YOUR_API_KEY_HERE
   heroku config:set DATABASE_URL=postgresql://user:password@host:port/database_name
   heroku config:set JWT_SECRET_KEY=YOUR_SECRET_KEY_HERE
   ```
5. Deploy the code:
   ```bash
   git push heroku main
   ```
6. Run database migrations (if applicable):
   ```bash
   heroku run python scripts/create_database.py
   ```

### 🔑 Environment Variables
Provide a comprehensive list of all required environment variables, their purposes, and example values:

- `OPENAI_API_KEY`:  Your OpenAI API key.
   Example: `sk-YOUR_API_KEY_HERE`
- `DATABASE_URL`:  Connection string for the PostgreSQL database.
   Example: `postgresql://user:password@host:port/database_name`
- `JWT_SECRET_KEY`:  Secret key for JWT token generation.
   Example: `YOUR_SECRET_KEY_HERE`

## 📜 API Documentation

### 🔍 Endpoints

- **POST /api/v1/ai/generate**
  - Description: Generates text using the OpenAI API.
  - Request Body: 
    ```json
    {
      "model": "text-davinci-003", // OpenAI model name
      "prompt": "Write a short story about a cat.",
      "temperature": 0.7, // (Optional) Controls randomness
      "max_tokens": 100 // (Optional) Limits response length
    }
    ```
  - Response Body:
    ```json
    {
      "success": true,
      "result": "This is the generated text."
    }
    ```


## 📜 License & Attribution

### 📄 License
This Minimum Viable Product (MVP) is licensed under the [GNU AGPLv3](https://choosealicense.com/licenses/agpl-3.0/) license.

### 🤖 AI-Generated MVP
This MVP was entirely generated using artificial intelligence through [CosLynx.com](https://coslynx.com).

No human was directly involved in the coding process of the repository: AI-Wrapper-for-OpenAI-Responses

### 📞 Contact
For any questions or concerns regarding this AI-generated MVP, please contact CosLynx at:
- Website: [CosLynx.com](https://coslynx.com)
- Twitter: [@CosLynxAI](https://x.com/CosLynxAI)

<p align="center">
  <h1 align="center">🌐 CosLynx.com</h1>
</p>
<p align="center">
  <em>Create Your Custom MVP in Minutes With CosLynxAI!</em>
</p>
<div class="badges" align="center">
  <img src="https://img.shields.io/badge/Developers-Drix10,_Kais_Radwan-red" alt="" />
  <img src="https://img.shields.io/badge/Website-CosLynx.com-blue" alt="" />
  <img src="https://img.shields.io/badge/Backed_by-Google,_Microsoft_&_Amazon_for_Startups-red" alt="" />
  <img src="https://img.shields.io/badge/Finalist-Backdrop_Build_v4,_v6-black" alt="" />
</div>
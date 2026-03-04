📖 What is Sous & You?
Sous & You is an AI-powered recipe recommendation chatbot that helps you decide what to cook based on your:

⏱️ Time constraints — Quick meals or elaborate dishes
🥗 Dietary restrictions — Vegan, gluten-free, allergies
👨‍🍳 Cooking skill level — Beginner to advanced
🥕 Available ingredients — Use what's in your fridge
💰 Budget — Affordable meal options

Simply tell the AI what you're in the mood for, and it provides personalized recipe recommendations with ingredients, instructions, and cooking tips.

✨ Features
FeatureDescription💬 Conversational AIChat-based interface to find recipes naturally🔍 Smart SearchSearch by ingredients, cuisine, or dietary needs🧑‍🍳 Personalized TipsGet cooking recommendations tailored to each recipe👤 User ProfilesRemembers your preferences across sessions⚡ Fast ResponsesRedis caching for instant recipe retrieval📱 Responsive DesignWorks on desktop and mobile

🎯 How It Works
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│                 │     │                 │     │                 │
│   User Input    │────▶│   Flask API     │────▶│   AI Engine     │
│  "pasta recipe" │     │   + Redis       │     │   (Search)      │
│                 │     │                 │     │                 │
└─────────────────┘     └─────────────────┘     └─────────────────┘
                                                        │
                                                        ▼
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│                 │     │                 │     │                 │
│   Chat UI       │◀────│   Angular App   │◀────│   Recipe Data   │
│   (Response)    │     │                 │     │                 │
│                 │     │                 │     │                 │
└─────────────────┘     └─────────────────┘     └─────────────────┘

User asks — "What can I make with chicken?"
API processes — Flask receives query, checks Redis cache
AI searches — Finds matching recipes based on context
Results returned — Personalized recipes with ingredients & tips
Chat continues — User can ask follow-up questions


🛠️ Tech Stack
LayerTechnologyFrontendAngular 17, TypeScript, RxJSBackendPython 3, FlaskCachingRedisCloudAWS (EC2, S3)CI/CDGitHub ActionsTestingKarma, Jasmine, pytest

🚀 Getting Started
Prerequisites

Node.js v18+
Python 3.x
Docker (for Redis)
Angular CLI

Quick Start
1. Clone the repo
bashgit clone https://github.com/CSCI-577A/SousAndYou.git
cd SousAndYou
2. Start Redis
bashdocker run --name redis-local -p 6379:6379 -d redis
3. Run Backend
bashcd backend
pip install -r requirements.txt
python3 flask_api.py
Backend runs at http://127.0.0.1:5000
4. Run Frontend
bashcd frontend
npm install
ng serve
Frontend runs at http://localhost:4200

📁 Project Structure
SousAndYou/
├── frontend/                    # Angular application
│   ├── src/
│   │   ├── app/
│   │   │   ├── pages/
│   │   │   │   ├── home/       # Chat interface & recipe search
│   │   │   │   └── about/      # About page & team info
│   │   │   ├── shared/
│   │   │   │   └── navbar/     # Navigation component
│   │   │   ├── app.routes.ts   # Route definitions
│   │   │   └── app.config.ts   # App configuration
│   │   ├── assets/             # Logo & static files
│   │   └── environments/       # Dev/Prod configs
│   └── angular.json
├── backend/                     # Flask API
│   ├── flask_api.py            # API endpoints
│   └── requirements.txt
└── .github/workflows/          # CI/CD

🔌 API Endpoints
MethodEndpointDescriptionGET/user/createCreate new user sessionPOST/searchSearch for recipes
Search Request:
json{
  "query": "quick pasta recipe",
  "user_id": "abc123"
}
Search Response:
json{
  "results": [
    {
      "text": "Here's a quick Aglio e Olio pasta...",
      "ingredients": ["spaghetti", "garlic", "olive oil"],
      "instructions": "..."
    }
  ]
}

👥 Team
Developed as part of USC CSCI-577A: Software Engineering — Spring 2025
NameRoleAlex HunterBackend DeveloperAnkita KhatriFrontend & DeploymentApril DawoudFrontend DeveloperBenson LiBackend & DeploymentCharlotte HausmanProject Manager & Scrum MasterEmily KochDatabase DeveloperMahati MalladiDatabase & QA TestingParis AcostaBackend & DatabaseShweta SankaranarayananFrontend & QA Testing

📄 License
This project was developed for educational purposes as part of USC's Software Engineering curriculum.

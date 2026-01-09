Wiki Quiz App
An AI-powered application that generates educational quizzes from Wikipedia articles. Built with FastAPI (Python backend), React (frontend), and Google Gemini AI.

🚀 Features
Quiz Generation: Enter any Wikipedia URL to automatically generate a quiz
AI-Powered Questions: Uses Google Gemini to create relevant, diverse questions
Difficulty Levels: Questions categorized as easy, medium, or hard
Take Quiz Mode: Interactive quiz-taking with scoring
Quiz History: View and manage all previously generated quizzes
Key Entity Extraction: Identifies people, organizations, and locations
Related Topics: Suggests related Wikipedia articles for further reading
Caching: Prevents duplicate scraping of the same URL
🛠️ Tech Stack
Backend: FastAPI (Python 3.10+)
Database: PostgreSQL
LLM: Google Gemini API via LangChain
Web Scraping: BeautifulSoup4
Frontend: React 18 + Vite + Tailwind CSS
📋 Prerequisites
Python 3.10 or higher
Node.js 18 or higher
PostgreSQL 14 or higher
Google Gemini API Key (free tier available at https://makersuite.google.com/app/apikey)
🔧 Installation & Setup
1. Clone the Repository
git clone https://github.com/your-username/wiki-quiz-app.git
cd wiki-quiz-app
2. Set Up PostgreSQL Database
# Create the database
psql -U postgres
CREATE DATABASE wiki_quiz_db;
\q
3. Backend Setup
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create .env file
cp .env.example .env

# Edit .env file with your settings:
# DATABASE_URL=postgresql://postgres:password@localhost:5432/wiki_quiz_db
# GOOGLE_API_KEY=your_google_api_key_here
4. Frontend Setup
cd frontend

# Install dependencies
npm install
🚀 Running the Application
Start Backend Server
cd backend
# Activate virtual environment if not already active
uvicorn main:app --reload --host 0.0.0.0 --port 8000
The API will be available at: http://localhost:8000 API Documentation: http://localhost:8000/docs

Start Frontend Development Server
cd frontend
npm run dev
The frontend will be available at: http://localhost:3000

📚 API Endpoints
Method	Endpoint	Description
POST	/api/quiz/generate	Generate quiz from Wikipedia URL
POST	/api/quiz/preview	Preview/validate Wikipedia URL
GET	/api/quiz/history	Get list of all generated quizzes
GET	/api/quiz/{quiz_id}	Get specific quiz by ID
DELETE	/api/quiz/{quiz_id}	Delete a quiz
POST	/api/quiz/attempt	Submit quiz answers for scoring
Example Request
curl -X POST "http://localhost:8000/api/quiz/generate" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://en.wikipedia.org/wiki/Alan_Turing"}'
🧪 Testing
Testing with Sample URLs
Alan Turing: https://en.wikipedia.org/wiki/Alan_Turing
Marie Curie: https://en.wikipedia.org/wiki/Marie_Curie
World War II: https://en.wikipedia.org/wiki/World_War_II
Python Programming: https://en.wikipedia.org/wiki/Python_(programming_language)
Albert Einstein: https://en.wikipedia.org/wiki/Albert_Einstein
📁 Project Structure
wiki-quiz-app/
├── backend/
│   ├── app/
│   │   ├── config.py          # Application configuration
│   │   ├── database.py        # Database connection
│   │   ├── models/            # SQLAlchemy models
│   │   ├── routes/            # API routes
│   │   ├── schemas/           # Pydantic schemas
│   │   └── services/          # Business logic
│   │       ├── scraper.py     # Wikipedia scraping
│   │       ├── llm_service.py # LLM integration
│   │       └── prompts.py     # LangChain prompts
│   ├── main.py                # FastAPI app entry
│   ├── requirements.txt
│   └── .env.example
├── frontend/
│   ├── src/
│   │   ├── api/               # API client
│   │   ├── components/        # React components
│   │   ├── App.jsx
│   │   └── main.jsx
│   ├── package.json
│   └── vite.config.js
├── sample_data/               # Example outputs
└── README.md
🤖 LangChain Prompt Templates
The quiz generation uses carefully crafted prompts located in backend/app/services/prompts.py:

Quiz Generation Prompt
Generates 5-10 multiple choice questions
Ensures questions are answerable from article content only
Includes difficulty distribution (30% easy, 50% medium, 20% hard)
Provides explanations referencing specific article sections
Related Topics Prompt
Suggests 5-8 related Wikipedia topics
Based on extracted entities and article sections
⚠️ Error Handling
The application handles:

Invalid Wikipedia URLs
Network connection errors
Missing article sections
LLM API failures
Database connection issues

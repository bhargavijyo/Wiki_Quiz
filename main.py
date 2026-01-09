from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import Base
from schemas import QuizRequest
from scraper import scrape_wikipedia
from llm import generate_quiz
from crud import save_quiz, get_all_quizzes
from fastapi.middleware.cors import CORSMiddleware


Base.metadata.create_all(bind=engine)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/generate")
def generate_quiz_api(req: QuizRequest, db: Session = Depends(get_db)):
    print("URL RECEIVED:", req.url)
    try:
        title, text, sections = scrape_wikipedia(req.url)
        text = text[:6000]
        ai_data = generate_quiz(text)

        quiz = save_quiz(db, req.url, title, ai_data["summary"], ai_data)

        return {
            "id": quiz.id,
            "url": req.url,
            "title": title,
            "summary": ai_data["summary"],
            "sections": sections,
            "quiz": ai_data["quiz"],
            "related_topics": ai_data["related_topics"]
        }
    except Exception as e:
        print("ERROR OCCURRED:", e)
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/history")
def history(db: Session = Depends(get_db)):
    return get_all_quizzes(db)

from sqlalchemy.orm import Session
from models import Quiz

def save_quiz(db: Session, url, title, summary, data):
    quiz = Quiz(url=url, title=title, summary=summary, data=data)
    db.add(quiz)
    db.commit()
    db.refresh(quiz)
    return quiz

def get_all_quizzes(db: Session):
    return db.query(Quiz).all()

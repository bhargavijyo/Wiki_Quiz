from sqlalchemy import Column, Integer, String, JSON, Text
from database import Base

class Quiz(Base):
    __tablename__ = "quizzes"

    id = Column(Integer, primary_key=True, index=True)
    url = Column(String, unique=True)
    title = Column(String)
    summary = Column(Text)
    data = Column(JSON)

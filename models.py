from sqlalchemy import Column, Integer, String, Text, ForeignKey
from db import Base

class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(100), nullable=False)

    def __repr__(self):
        return f"<Users(id={self.id}, email={self.email})>"

class Reports(Base):
    __tablename__ = "reports"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    resume_text = Column(Text, nullable=False)
    result = Column(Text, nullable=False)

    def __repr__(self):
        return f"<Reports(id={self.id}, user_id={self.user_id})>"
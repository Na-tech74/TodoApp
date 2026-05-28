from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

RAW_URL = os.getenv("DATABASE_URL") or os.getenv("MYSQL_URL") or ""
if RAW_URL.startswith("mysql://"):
    RAW_URL = RAW_URL.replace("mysql://", "mysql+pymysql://", 1)
if not RAW_URL:
    RAW_URL = "mysql+pymysql://root@localhost:3306/tododb"

DATABASE_URL = RAW_URL
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

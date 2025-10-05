from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

import os

from dotenv import load_dotenv

load_dotenv()

db_url = os.getenv("database_url")

assert db_url is not None, "Environment variable 'database_url' is not set"

engine = create_engine(db_url)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    except Exception as e:
        print("Database Error:", e)
        raise
    finally:
        db.close()

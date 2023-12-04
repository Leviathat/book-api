from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL = "postgresql://shop_admin:488719@db:5432/shop_db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

Base = declarative_base()

Base.metadata.create_all(bind=engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Dependency
def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()

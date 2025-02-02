from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# from sqlalchemy.orm import DeclarativeBase
# from sqlalchemy.orm import declarativeBase


# Connects to the SQLite database
# DATABASE_URL = "postgresql://root:ixPwRm72cxuT8Lzoegq6eUAl@aberama.iran.liara.ir:30140/online-ticket"

DATABASE_URL="sqlite:///./db.sqlite3"
# engine = create_engine('')
engine = create_engine(
    DATABASE_URL
)
SessionLocal = sessionmaker(bind=engine)
# session = Session()

# class Base (DeclarativeBase):
#     pass

Base = declarative_base()


# engine = create_engine('postgresql://postgres:postgres@localhost:5432/tiktok')
# Session = sessionmaker(bind=engine)
# session = Session()

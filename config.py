import os
from pathlib import Path

basedir = Path("__file__").parent.absolute()


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "dev"
    SQLALCHEMY_DATABASE_URI = (
        os.environ.get("DATABASE_URL") or f"sqlite:///{basedir / 'app.db'}"
    )

import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

class Config:
    SECRET_KEY = os.environ.get(
        "SECRET_KEY",
        "minisoc-development-secret-key"
    )

    DATABASE_PATH = BASE_DIR / "data" / "minisoc.db"
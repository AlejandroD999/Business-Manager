import os

class Config:
    
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-only-insecure-key")

    DB_USERNAME = "root"
    DB_PASSWORD = ""
    DB_HOST = "localhost"
    DB_PORT = "3306"
    DB = "business_manager"

    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}"
        f"@{DB_HOST}:{DB_PORT}/{DB}"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False
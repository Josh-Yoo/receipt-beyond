import os

class Config:
    #Flask session security
    SECRET_KEY = os.getenv("SECRET_KEY", "dev")

    #Firebase credentials
    FIREBASE_CREDENTIALS = os.getenv("FIREBASE_CREDENTIALS")
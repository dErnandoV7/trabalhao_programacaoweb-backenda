import os
from datetime import timedelta

class Config:
    SECRET_KEY = 'VcKzHS4g2h+dP33tCbqOghtKaU37wvFECMhVqrfccaoI/17qh/j3+VDV'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///lojinha.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = 'chave_lojinha_jwt'
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=1)

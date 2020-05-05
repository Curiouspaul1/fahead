import os
basedir = os.getcwd()

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    #MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587 or 465
    MAIL_USE_TLS = True
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.getenv('USERNAME')
    MAIL_PASSWORD = os.getenv('PASSWORD')
    MAIL_DEFAULT_SENDER = os.getenv('SENDER_EMAIL')

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir,'dev.db')
    DEBUG=True

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')

config = {
    "production":ProductionConfig,
    "development":DevelopmentConfig,
    "default":DevelopmentConfig
}
import os
basedir = os.getcwd()

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp-relay.gmail.com.'
    #MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get('USERNAME')
    MAIL_PASSWORD = os.environ.get('PASSWORD')
    MAIL_DEFAULT_SENDER = os.getenv('SENDER_EMAIL')
    MAX_N = 1
    MAIL_MAX_EMAILS = 1

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir,'dev.sqlite')
    DEBUG=True

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')

config = {
    "production":ProductionConfig,
    "development":DevelopmentConfig,
    "default":DevelopmentConfig
}
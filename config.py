import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-key-please-change'
    db_database = "postgresql://dblab_9bmz_user:XnKfbcWDrTof7ZaH3LqNTQP0Or2n2qHN@dpg-d6rdfbnpm1nc73bhv58g-a/dblab_9bmz"
    
    # LOCAL POSTGRESQL  test
    # db_database = ""postgresql://postgres:0415@localhost:5432/postgres""
    

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

class TestingConfig(Config): 
    TESTING = True
    DEBUG = True
    db_database = "sqlite:///:memory:"

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing' : TestingConfig,
    'default': DevelopmentConfig
}
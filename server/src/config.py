class Config:
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'secret'
    SQLALCHEMY_DATABASE_URI = 'postgresql://app:app@localhost/deadlineproject'
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024 * 1024
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    JWT_ACCESS_TOKEN_EXPIRES = False
    ADMIN_EMAIL = 'app'
    ADMIN_PASSWORD = 'app'

    @staticmethod
    def init_app(app):
        pass


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True


config = {
    'production': ProductionConfig,
    'development': DevelopmentConfig,
}

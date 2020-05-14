from builtins import object


class Config(object):
    DEBUG = False
    TESTING = False
    QUEUE = "queue"
    REDIS_SERVER = "redis"


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    ENV = "development"
    DEBUG = True


class TestingConfig(Config):
    DEBUG = True

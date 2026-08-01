class configurations():
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite3'
    SECRET_KEY = 'its very secret'
    SECURITY_TRACKABLE = True
    SECURITY_TOKEN_AUTHENTICATION_HEADER = 'Authentication'

    CACHE_TYPE = 'RedisCache'
    CACHE_DEFAULT_TIMEOUT = 120
    CACHE_KEY_PREFIX = 'myCarApp_'
    CACHE_REDIS_HOST = 'localhost'
    CACHE_REDIS_PORT = 6379
    CACHE_REDIS_DB = 0

    MAIL_SERVER = 'localhost'
    MAIL_PORT = 1025
    MAIL_DEFAULT_SENDER = 'noreply@mycarapp.com'

# key = value
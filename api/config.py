import os
import redis
redis_store = redis.Redis(host='127.0.0.1', port=6379, db=4)


class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = os.urandom(64)  # 自生成64位密钥
    SESSION_TYPE = 'redis'
    SESSION_USE_SIGNER = True
    PERMANENT_SESSION_LIFETIME = 600  # redis 键值对生命周期


# 线下开发环境
class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://nick:123xiangjiang@@rm-bp13d4mewh869vg645o.mysql.rds.aliyuncs.com:3306/selfblob'
    SESSION_REDIS = redis.Redis(host='127.0.0.1', port=6397, db=5)
    DEBUG = True

# 线上环境
class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://nick:123xiangjiang@@rm-bp13d4mewh869vg645o.mysql.rds.aliyuncs.com:3306/blob_online'
    SESSION_REDIS = redis.Redis(host='127.0.0.1', port=6397, db=6)

config_mapper = {
    'develop' : DevelopmentConfig,
    'product' : ProductionConfig
}

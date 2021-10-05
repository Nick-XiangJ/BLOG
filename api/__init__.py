from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from .config import redis_store, config_mapper
import pymysql
from flask import Flask

#创建一个无参数据库对象
db = SQLAlchemy()

def create_app(dev_name):
    app = Flask(__name__)
    config_class = config_mapper.get(dev_name)
    app.config.from_object(config_class)
    db.init_app(app) # 实例化数据库对象
    from api.v1.view import main as main_blueprint
    app.register_blueprint(main_blueprint)
   # db.create_all()
   # init_api(app=app)
   # Session(app)
    return app
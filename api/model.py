# 数据库表设计
# 用户表(User)
#  { id , username , password , nickname , img , email , school , phone }
#  { 自增id , 用户名 , 密码 , 笔名 , 电话 , 邮箱 , 学校 , 照片 }


# 文章表(Article)
#  { id , username , title , content , create_time , img , location , read_times , attitude ,hidden }
#  { 自增id , 发表用户名 , 文章头 , 文章内容 , 创建时间 , 所需配图 , 坐标 , 阅读次数 , 心情 , 软删除(0/1) }
# 用户和文章 一对多关系 ， 在用户表使用外键 即可。

#  图库(Img)
#  { id , img , img_url ，username , create_time }
#  { 自增id , 图片 , 图片url ,上传用户 , 上传时间 }


# 阿里云数据库  RDS-MYSQL 外网地址 { rm-bp13d4mewh869vg645o.mysql.rds.aliyuncs.com } mysql -hRDS + url -u root -p password -P 3306

from api import db
from datetime import datetime
import pymysql





# 用户表
# class User(db.Model):
#     __tablename__ = 'User'
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     username = db.Column(db.String(20), primary_key=True)
#     password = db.Column(db.String(20), nullable=False)
#     nickname = db.Column(db.String(50), nullable=False)
#     img = db.Column(db.BLOB)
#     email = db.Column(db.String(20))
#     school = db.Column(db.String(50))
#     phone = db.Column(db.String(11))
#     img_id = db.Column(db.Integer, db.ForeignKey('Img.id'))
#     article_id = db.Column(db.Integer, db.ForeignKey('Article.id'))
#     log_id = db.Column(db.Integer, db.ForeignKey('LoginLog.id'))



# 图库
# class Img(db.Model):
#     __tablename__ = 'Img'
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     img = db.Column(db.LargeBinary(2048), nullable=False)
#     img_url = db.Column(db.String(100))
#     create_time = db.Column(db.DateTime, default=datetime.now())
#     user = db.relationship('User', backref='Img')

# 文章
#  { id , username , title , content , create_time , img , location , read_times , attitude ,hidden }
class Article(db.Model):
    __tablename__ = 'Article'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50), nullable=False)
    context = db.Column(db.Text, nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now())
    img = db.Column(db.LargeBinary(2048))
    location = db.Column(db.String(50))
    read_time = db.Column(db.Integer, default=0)
    attitude = db.Column(db.String(50))
    #hidden = db.Column(db.Enum('0', '1'), default='0') # 枚举类型，0为可读反之
    #user = db.relationship('User', backref='Article')

# 登录日志
# { id , username , ip}
# class LoginLog(db.Model):
#     __tablename__ = 'LoginLog'
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     ip = db.Column(db.String(15), nullable=False)
#     user = db.relationship('User', backref='LoginLog')

import redis
from flask import Flask, session
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.wtf import CSRFProtect
from redis import StrictRedis
from flask_session import Session  # 可以指定session保存到位置
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

class Config(object):  # 项目的配置
    DEBUG = True
    SECRET_KEY = "LzUA6O2R2R/mNSD6cbQ5Fzqkq+5VUa3B9/42IG9uoVSzRFbqf2Q6ZGUSVNa4JDstGSADO7hEsQhwk6papcOs4g=="
    #为数据库添加配置
    SQLAlchemy_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/information27"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    #Redis的配置
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379
    # flask_session的配置信息
    SESSION_TYPE = "redis"  # 指定 session 保存到 redis 中
    SESSION_USE_SIGNER = True  # 让 cookie 中的 session_id 被加密签名处理
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)  # 使用 redis 的实例
    PERMANENT_SESSION_LIFETIME = 86400  # session 的有效期，单位是秒
    SESSION_PERMANENT = False

app = Flask(__name__)
# 加载配置
app.config.from_object(Config)
# 初始化数据库
db = SQLAlchemy(app)
# 初始化redis存储对象
redis_store = StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)
# 开启当前项目csrf保护,只做服务验证工作
CSRFProtect(app)
Session(app)
manager = Manager(app)
# 将app与db关联
Migrate(app, db)
#将迁移命令添加到manager中
manager = ("db", MigrateCommand)


@app.route("/")
def index():
    session["name"] = "itheima"
    return "index112e11"

if __name__ == "__main__":
    manager.run()


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager

# FLASK初始化
app = Flask(__name__)

# 命令行启动Manager初始化
manager = Manager(app)

# 加载配置文件
app.config.from_pyfile("config/base_setting.py")

# 决定环境变量ops_config=local|production

# db初始化
# app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:lky1161@127.0.0.1/mysql"
db = SQLAlchemy(app)



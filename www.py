from controllers.indexController import index_page
from application import app

from flask_debugtoolbar import DebugToolbarExtension
# DEBUG工具栏初始化

toolbar = DebugToolbarExtension(app)

# 拦截器初始化
from interceptors.auth import *

# 错误处理器初始化
from interceptors.errorHandler import *

# blueprint初始化
app.register_blueprint(index_page, url_prefix="/")
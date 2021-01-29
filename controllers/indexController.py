from flask import Blueprint, request, make_response, jsonify, render_template
from common.models.user import User

index_page = Blueprint("index_page ", __name__)


@index_page.route("/template")
def template():
    # 普通传值
    # name = "Lucien"
    # return render_template("index.html", name = name)

    # 字典传值
    context = {"name": "Lucien", "info": {'tel': '114514', 'age': 15}, "hen": [1, 9, 1, 9, 8, 1, 0]}

    # 通过SQLAlchemy查询数据库

    # sql = text("select * from `user`")
    # result = db.engine.execute(sql)

    # 通过Model查询数据库

    result = User.query.all()
    context['sql_result'] = result

    return render_template("index.html", **context)


#
#
# @index_page.route("/")
# def index_page_index():
#     return "index page"
#
#
# @index_page.route("/my")
# def my_index():
#     return "This is my index"
#
#
# @index_page.route("/get")
# def get():
#     req = request.values
#     var_a = req['a'] if 'a' in req else "default"
#     return "request:%s,params:%s,var_a:%s" % (request.method, request.form, var_a)
#
#
# @index_page.route("/post", methods=["POST"])
# def post():
#     req = request.values
#     var_a = req['a'] if 'a' in req else "default"
#     return "request:%s,params:%s,var_a:%s" % (request.method, request.form, var_a)
#
#
# @index_page.route("/upload", methods=["POST"])
# def upload():
#     f = request.files["file"] if "file" in request.files else None
#     return "request:%s,params:%s,file:%s" % (request.method, request.files, f)
#
#
# @index_page.route("/text")
# def text_a():
#     return "text/html"
#
#
# @index_page.route("/text_same")
# def text_same():
#     response = make_response("nb", 200)
#     return response
#
#
# @index_page.route("/json")
# def json():
#     data = {"a": "b"}
#     response = make_response(jsonify(data))
#     return response
#


# @index_page.route("/extend_template")
# def extend_template():
#     return render_template("extend_template.html")

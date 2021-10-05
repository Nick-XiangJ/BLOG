from flask import render_template, session, redirect, request, jsonify
from api.model import *
from . import main
from flask_limiter.util import get_remote_address
from flask_limiter import Limiter


limiter = Limiter(
    app=main,
    key_func=get_remote_address(),
    default_limits=["20 per day", "5 per day"]
)



@main.route('/hi', methods=['POST', 'GET'])
@limiter.limiter("1 per day")
def article():
    if request.method == 'POST':
        print('first step')
        code = request.form.get('code')
        title = request.form.get('title')
        #title = request.form.get('title')
        mess = request.form.get('message')
        str = "123xiangjiang@"
        print(code, title, mess)
        if code == str:
            try:
                art = Article(title=title, create_time=datetime.now(), context=mess)
                db.session.add(art)
                db.session.commit()
                return jsonify(status=1)
            except Exception as e:
                db.session.rollback()
                print(e)
                return jsonify(state='false')
        else:
            return jsonify(state='false')
    elif request.method == 'GET':
        try:
            arts = Article.query.all()
            size = len(arts)
            content = []
            for i in range(size-2, size):
                art = arts[i]
                print(art)
                con = {
                    'title': art.title,
                    'content': art.context,
                    'time': art.create_time
                }
                content.append(con)
            return jsonify(msg=content, status=1)
        except Exception as e:
            print(e)
            db.session.rollback()
            return jsonify(status=0)
    else:
        return jsonify(status=0)


























# @main.route('/', methods=['GET'])
# def index1():
#     return redirect('index')
# @main.route('/index', methods=['GET'])
# def index():
#     return render_template('index.html')
# @main.route('/intro', methods=['GET'])
# def intro():
#     return render_template('intro.html')
# @main.route('/third', methods=['GET'])
# def third():
#     return render_template('3.html')
# @main.route('/fourth', methods=['GET'])
# def fourth():
#     return render_template('4.html')
# @main.route('/hi', methods=['POST'])
# def test():
#     user = request.form.get('name')
#     password = request.form.get('message')
#     print(user, password)
#     str = 'Hello Nick'
#     encode_str = base64.encodebytes(str.encode('utf-8'))
#     print(encode_str)
#     return encode_str
# @main.route('/test', methods=['POST'])
# def testcode():
#     #data = eval(base64.b64decode(request.data))
#     data = code2(request.data)
#     print(data)
#     jj = {
#         'state': '1'
#     }
#     return code1(jj)
#
# @main.route('/md5', methods=['POST', 'GET'])
# def md5():
#     data = {
#         "name": hashlib.md5("nick".encode('utf-8')).hexdigest(),
#         "pass": hashlib.md5("1121".encode('utf-8')).hexdigest()
#     }
#     return jsonify(data)
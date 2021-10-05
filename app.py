from api import create_app
from flask import make_response
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_cors import *
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = create_app('develop')
from api.model import *
CORS(app)
manager = Manager(app=app)
@app.after_request
def af_request(resp):
    """
    #请求钩子，在所有的请求发生后执行，加入headers。
    :param resp:
    :return:
    """
    resp = make_response(resp)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Access-Control-Allow-Methods'] = 'GET,POST'
    resp.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
    return resp
Migrate(app, db)



manager.add_command('db', MigrateCommand)
if __name__ == '__main__':
    manager.run()

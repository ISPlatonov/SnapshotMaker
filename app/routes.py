from flask.globals import request
from flask.json import jsonify
from app import app
from app.worker import *

'''
# temp dev route
@app.route('/')
@app.route('/index')
def index():
    return jsonify(rec_list)
'''


@app.route('/snapshot/make', methods=['POST'])
def make_snap_route():
    make_snapshot(request.get_json()['addresses_list'])
    check_overlimit()

    return {'status': 'done'}


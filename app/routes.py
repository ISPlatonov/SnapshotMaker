from flask import render_template
from flask.globals import request
from flask.json import jsonify
from app import app
from app.worker import Worker

'''
# temp dev route
@app.route('/')
@app.route('/index')
def index():
    return jsonify(rec_list)
'''

worker = Worker()


@app.route('/', methods=['GET'])
def index():
    try:
        return render_template("index.html", mjpg_address=worker.get_mjpg_address())

    except Exception as error:
        print(repr(error))
        return "<h1>Error 404</h1><p>{}</p>".format(error)


@app.route('/channel_list/get', methods=['GET'])
def get_channels():
    try:
        return {"channel_list": worker.get_channel_list()}, 200

    except Exception as error:
        print(repr(error))
        return jsonify(error=str(error)), 500


@app.route('/snapshot/make', methods=['POST'])
def make_snap_route():
    try:
        worker.make_snapshot(request.get_json()['addresses_list'])
        return {"status": "done"}, 200

    except Exception as error:
        print(repr(error))
        return jsonify(error=str(error)), 500


@app.route('/admin/move_camera', methods=['GET'])
def move_camera():
    try:
        worker.move_camera()
        return {"status": "done"}, 200

    except Exception as error:
        print(repr(error))
        return jsonify(error=str(error)), 500


@app.route('/admin/set_camera', methods=['GET'])
def set_camera():
    try:
        worker.set_camera()
        return {"status": "done"}, 200

    except Exception as error:
        print(repr(error))
        return jsonify(error=str(error)), 500

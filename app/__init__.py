from flask import Flask

app = Flask(__name__)

from app import routes
from app.worker import Worker
from app import image_sender
from app import ptz_control


#worker = Worker()

import subprocess, time, json, os
from app.image_sender import send_image
from app.ptz_control import ptzControl
import copy


class Worker:
    def __init__(self):
        with open('app/configs/config.json', encoding='utf-8') as config_file:
            self.__config = json.load(config_file)

    
    def get_rtsp_address(self, camera_id):
        return self.__config['cameras'][camera_id]['rtsp_address']


    def get_mjpg_address(self, camera_id):
        return self.__config['cameras'][camera_id]['rtsp_address']['mjpg_address']


    def get_channel_list(self, camera_id):
        return self.__config['cameras'][camera_id]['rtsp_address']['channel_list']


    def make_snapshot(self, camera_id, addresses_list):
        if not isinstance(addresses_list, list):
            raise TypeError("wrong datatype in request")

        try:
            filename = 'snapshot_{}.jpg'.format(time.time())
            command = ['ffmpeg', '-rtsp_transport', 'tcp', '-i', self.__config['cameras'][camera_id]['rtsp_address'], '-y', '-vframes', '1', '-loglevel', 'error', '-vf', 'perspective=70:225:2520:190:170:1320:2410:1280', 'snapshots/{}'.format(filename)]
            process = subprocess.Popen(args=command, stdout=subprocess.PIPE)
            process.wait()
        except Exception:
            raise
        
        try:
            self.send_snapshot(filename, addresses_list)
        except Exception:
            raise
        

    def send_snapshot(self, filename, address_list):
        for address in address_list:
            try:
                send_image(address['channel'], address['topic'], 'snapshots/' + filename, 'app/configs/.zuliprc')
                self.check_overlimit()
            except Exception:
                raise 
        

    def check_overlimit(self):
        try:
            snaps_number = len(os.listdir())
        except Exception:
            raise

        if snaps_number > self.max_snaps_number:
            try:
                self.remove_overlimit(snaps_number - self.max_snaps_number)
            except Exception:
                raise


    def remove_overlimit(self, overlimit_number):
        try:
            files_list = os.listdir('snapshots/') #files_list.decode('utf-8').split()
        except Exception:
            raise

        files_list.sort()
        files_to_erase = files_list[:overlimit_number]

        for filename in files_to_erase:
            os.remove('snapshots/{}'.format(filename))

        
    def set_camera(self, camera_id):
        ptz = ptzControl(camera_id)
        ptz.set_preset()

    
    def move_camera(self, camera_id):
        ptz = ptzControl(camera_id)
        ptz.goto_preset()
    

    def get_config(self, camera_id):
        return copy.deepcopy(self.__config['cameras'][camera_id])

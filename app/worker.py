import subprocess, time
#from app import app
#import sys
#sys.path.append("./app")
#from app import app
from app.image_sender import send_image


# it should be loaded up from json file! 
camera_address = 'rtsp://admin:Supervisor@172.18.191.177/live/0/MAIN/'
max_snaps_number = 20


def make_snapshot(addresses_list):
    if not isinstance(addresses_list, list):
        raise TypeError("wrong datatype in request")

    command = ['bash', 'app/scripts/make_snapshot.sh', camera_address]
    try:
        process = subprocess.Popen(args=command, stdout=subprocess.PIPE)
        filename = process.stdout.read()
        process.wait()
    except Exception:
        raise
     
    try:
        send_snapshot(filename, addresses_list)
    except Exception:
        raise
    

def send_snapshot(filename, address_list):
    for address in address_list:
        #command = ['python3', 'app/scripts/image_sender.py', '--channel', address['channel'], '--topic', address['topic'], '--image', 'snapshots/' + filename.decode('utf-8').strip(), '--config', 'app/configs/.zuliprc']
        try:
            #process = subprocess.Popen(args=command, stdout=subprocess.PIPE)
            #output = process.stdout.read()
            #print('snapshots/' + filename.decode('utf-8').strip())
            send_image(address['channel'], address['topic'], 'snapshots/' + filename.decode('utf-8').strip(), 'app/configs/.zuliprc')
            check_overlimit()
        except Exception:
            raise 
      

def check_overlimit():
    command = ['bash', 'app/scripts/count_snapshots.sh']
    try:
        process = subprocess.Popen(args=command, stdout=subprocess.PIPE)
        snaps_number = int(process.stdout.read())
    except Exception:
        raise

    if snaps_number > max_snaps_number:
        try:
            remove_overlimit(snaps_number - max_snaps_number)
        except Exception:
            raise


def remove_overlimit(overlimit_number):
    # ... will write it later...
    command = ['bash', 'app/scripts/list_snapshots.sh']
    try:
        process = subprocess.Popen(args=command, stdout=subprocess.PIPE)
        files_list = process.stdout.read()

        files_list = files_list.decode('utf-8').split()
    except Exception:
        raise

    #print(overlimit_number)

    files_list.sort()
    files_to_erase = files_list[:overlimit_number]

    for filename in files_to_erase:
        command = ['bash', 'app/scripts/remove_snapshot.sh', filename]
        process = subprocess.Popen(args=command, stdout=subprocess.PIPE)
        output = process.stdout.read()
        
        if output != '': # ???
            # error
            pass


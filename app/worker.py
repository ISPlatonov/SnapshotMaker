import subprocess, time


# it should be loaded up from json file! 
camera_address = 'rtsp://172.18.191.53:554/Streaming/Channels/1'
max_snaps_number = 20


def make_snapshot(addresses_list):
    if not isinstance(addresses_list, list):
        raise TypeError("wrong datatype in request")

    command = ['bash', 'app/scripts/make_snapshot.sh', camera_address]
    try:
        process = subprocess.Popen(args=command, stdout=subprocess.PIPE)
        filename = process.stdout.read()
    except Exception:
        raise
     
    try:
        send_snapshot(filename, addresses_list)
    except Exception:
        raise

    try:
        check_overlimit()
    except Exception:
        raise
    

def send_snapshot(filename, address_list):
    for address in addresses_list:
        send(address.channel, address.topic, filename)


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


import subprocess, time


# it should be loaded up from json file! 
camera_address = 'rtsp://172.18.191.53:554/Streaming/Channels/1'
max_snaps_number = 20


def make_snapshot(addresses_list):
    command = ['bash', 'app/scripts/make_snapshot.sh', camera_address]
    process = subprocess.Popen(args=command, stdout=subprocess.PIPE)
    filename = process.stdout.read()
    
    send_snapshot(filename, addresses_list)

    check_overlimit()
    

def send_snapshot(filename, address_list):
    # ... will write it later...
    pass


def check_overlimit():
    command = ['bash', 'app/scripts/count_snapshots.sh']
    process = subprocess.Popen(args=command, stdout=subprocess.PIPE)
    snaps_number = int(process.stdout.read())

    if snaps_number > max_snaps_number:
        remove_overlimit(max_snaps_number - snaps_number)


def remove_overlimit(overlimit_number):
    # ... will write it later...
    command = ['bash', 'app/scripts/list_snapshots.sh']
    process = subprocess.Popen(args=command, stdout=subprocess.PIPE)
    files_list = process.stdout.read()

    files_list = files_list.split('\n')

    files_list.sort()
    files_to_erase = files_list[:overlimit_number]

    for filename in files_to_erase:
        command = ['bash', 'app/scripts/remove_snapshot.sh', filename]
        process = subprocess.Popen(args=command, stdout=subprocess.PIPE)
        output = process.stdout.read()
        
        if output != '': # ???
            # error
            pass


# SnapshotMaker

This web service is used for making board snapshots through ONVIF cameras and sending them into selected Zulip topic/channel on tap/click of a button.

## Dependencies

To deploy the server a machine has to have `python3` + `flask`, `ffmpeg`:

    sudo apt install python3 python3-pip ffmpeg
    pip3 install flask

## Run

To start the server run:

    flask run --host=0.0.0.0

Access address will appear in terminal. Usually, it will be on 5000 port.

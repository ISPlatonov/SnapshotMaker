#!/bin/bash

file_name=snapshot_$(date +%s.%N).jpg

ffmpeg -rtsp_transport tcp -i $1 -y -vframes 1 -loglevel error snapshots/$file_name
echo $file_name

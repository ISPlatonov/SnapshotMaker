ffmpeg -rtsp_transport tcp -i $1 -y -vframes 1 snapshots/snapshot_$(date +%s.%N).jpg

taskkill /f /im "vlc.exe"
start /b vlc -vvv -Idummy rtsp://admin:Supervisor@172.18.191.177/live/0/MAIN/ --sout #transcode{vcodec=MJPG,venc=ffmpeg{strict=1},fps=10,width=1280,height=800}:standard{access=http{mime=multipart/x-mixed-replace;boundary=--7b3cc56e5f51db803f790dad720ed50a},mux=mpjpeg,dst=:9911/}
start /b flask run --host=127.0.0.1
"C:\Program Files\Google\Chrome\Application\chrome.exe" 127.0.0.1:5000 --window-size=1280,800 --new-window --start-fullscreen --hide-scrollbars
import cv2
import os

RTSP_URL = 'rtsp://admin:instar@192.168.2.120/livestream/11'

os.environ['OPENCV_FFMPEG_CAPTURE_OPTIONS'] = 'rtsp_transport;udp'

cap = cv2.VideoCapture(RTSP_URL, cv2.CAP_FFMPEG)

if not cap.isOpened():
    print('ERROR :: Cannot open RTSP stream')
    exit(-1)

while True:
    success, img = cap.read()
    cv2.imshow(RTSP_URL, img)

    if cv2.waitKey(1) & 0xFF == ord('q'):  # Keep running until you press `q`
        break

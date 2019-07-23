import cv2
from videostabilizer import VideoStabilizer

video = cv2.VideoCapture("../un4.mp4")
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out2 = cv2.VideoWriter('out5.mp4', fourcc, 15.0, (640,480))
out3 = cv2.VideoWriter('out6.mp4', fourcc, 15.0, (640,480))
stabilizer = VideoStabilizer(video)

while True:
        ret,frame2=video.read()
        out3.write(frame2)
        cv2.imshow("frame2", frame2)
        success, _, frame = stabilizer.read()
        out2.write(frame)
        if not success:
                print("No frame is captured.")
                break
        cv2.imshow("frame", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
                break

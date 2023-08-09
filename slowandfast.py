import cv2
video_path = 'sunset.mp4.mp4'
cap = cv2.VideoCapture(video_path)
if not cap.isOpened():
    print("Error opening video file")
    exit()
fps = int(cap.get(cv2.CAP_PROP_FPS))
cv2.namedWindow('Original Video', cv2.WINDOW_NORMAL)
cv2.namedWindow('Slow Motion', cv2.WINDOW_NORMAL)
cv2.namedWindow('Fast Motion', cv2.WINDOW_NORMAL)
slow_factor = 2
fast_factor = 2
while True:
    ret, frame = cap.read()
    if not ret:
        break  # Break the loop if the video ends
    cv2.imshow('Original Video', frame)
    if slow_factor > 1:
        cv2.imshow('Slow Motion', frame)
        for _ in range(slow_factor - 1):
            cap.read()
    if fast_factor > 1:
        for _ in range(fast_factor - 1):
            cap.read()
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

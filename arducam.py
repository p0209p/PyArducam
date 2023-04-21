import cv2
import time

# Return the id of USB Camera
def find_id():
	for id in range(100):
		cap = cv2.VideoCapture(id) 
		if cap.isOpened():
			print(f"Camera id: {id} is available")
			break
	return cap

# Video length is in seconds
def get_video(cap:cv2.VideoCapture, frame_rate:int, video_length:float) -> list:
    video_frames = []
    nframes  = round(frame_rate*video_length)
    for _ in range(nframes):
        ret,frame = cap.read() # Read a single frame from the camera
        if ret:
            video_frames.append(frame)
            time.sleep(1/frame_rate)
        else:
            print("Cannot read camera data, exiting...")
            exit()
    return video_frames

cap = find_id()
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
cap.set(cv2.CAP_PROP_CONVERT_RGB, 2) # For RGB Mode

# Save video_frames
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # You can change the codec to whatever you like
frame_rate = 15  # Define the frame rate of the output video
out = cv2.VideoWriter('output.mp4', fourcc, frame_rate, (1920, 1080)) 

video_frames = get_video(cap,frame_rate,5.5)

for frame in video_frames:
    out.write(frame)

if cap is not None:
    cap.release()
    out.release()

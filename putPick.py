import cv2
import math

def add_image_to_video(video_path, image_path, timestamp, output_path):
    cap = cv2.VideoCapture(video_path)
    print(cap)
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    
    image = cv2.imread(image_path)
    w,h,c = image.shape
    if w and h < 300:
        image = cv2.resize(image, (0,0), fx=2, fy=2) 
    fourcc = cv2.VideoWriter_fourcc(*'mpv4')
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))
    
    for frame_num in range(total_frames):
        ret, frame = cap.read()
        
        if not ret:
            break
        
        if math.floor(frame_num / fps) == timestamp:
            x_offset=y_offset=250
            frame[y_offset:y_offset+image.shape[0], x_offset:x_offset+image.shape[1]] = image
            print("frame added")
        
        out.write(frame)
    
    cap.release()
    out.release()
    cv2.destroyAllWindows()

# Specify paths and timestamps
video_path = 'input copy.mp4'
image_path = 'images//73b7871b79.jpg'
timestamp = 10  # Timestamp in seconds
output_path = 'output_video_with_image.mp4'

# Add the image to the video
add_image_to_video(video_path, image_path, timestamp, output_path)

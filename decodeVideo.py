import cv2
import os

# Input video file name
input_video = 'output.mkv'  # Replace with the name of your video file

# Output directory for frames
output_dir = 'output_frames/'  # Create this directory if it doesn't exist

# Create the output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Open the video file for reading
cap = cv2.VideoCapture(input_video)

# Initialize frame count
frame_count = 0

# Read frames from the video and save them as individual images
while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Save the frame as an image in the output directory
    frame_filename = os.path.join(output_dir, f'frame_{frame_count:04d}.png')
    cv2.imwrite(frame_filename, frame)
    
    frame_count += 1

# Release the video capture object
cap.release()

print(f'{frame_count} frames extracted and saved in {output_dir}')

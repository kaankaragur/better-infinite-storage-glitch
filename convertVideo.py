import cv2
import os

# Directory containing PNG images
image_dir = 'encodedPhotos/'

# Output video file name
output_video = 'output_video.mp4'

# Get the list of PNG files in the directory
image_files = [os.path.join(image_dir, file) for file in os.listdir(image_dir) if file.endswith('.png')]

# Check if there are any image files
if not image_files:
    print("No PNG images found in the directory.")
    exit()

# Read the first image to get dimensions
first_image = cv2.imread(image_files[0])
height, width, layers = first_image.shape

# Define the codec and create a VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'ffv1')  # Use the appropriate codec for your desired output format
video = cv2.VideoWriter(output_video, fourcc, 30, (width, height), isColor=True)
cv2.VideoWriter()
# Iterate through the image files and add them to the video
for image_file in image_files:
    frame = cv2.imread(image_file)
    video.write(frame)

# Release the video writer
video.release()

print(f"Video saved as '{output_video}'")

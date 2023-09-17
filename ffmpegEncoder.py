import subprocess

# Define the FFmpeg command as a list of arguments
ffmpeg_command = [
    './ffmpeg/bin/ffmpeg.exe',
    '-framerate', '60',
    '-i', 'encodedPhotos/frame_%04d.png',
    '-c:v', 'ffv1',
    'output.mkv'
]

# Execute the FFmpeg command
try:
    subprocess.run(ffmpeg_command, check=True)
except subprocess.CalledProcessError as e:
    print(f"Error executing FFmpeg command: {e}")

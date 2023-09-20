# Better Infinite Storage Glitch (In alpha, generally broken)

Here is a general summary of this repository.

### Currently files are encoded 2x bigger. (1.5x with new update)

## First of all, this is a remake.

Big shoutout to the [Owner of The Idea](https://github.com/DvorakDwarf/Infinite-Storage-Glitch) for the beautiful idea.
That's a remake version. It uses Python and Encodes with Base64. Moreover, it uses an algorithm for lower file sizes (EXPERIMENTAL).

## What is this for?

There is a new glitch that you can have infinite storage by converting files into videos and uploading them to YouTube.
The main goal is to remake it with a stable language and add more features.

## How is it work?

It assigns random RGB numbers for base64 characters and uses AI to make colors unique to reduce losses (Still in development).

# Most importantly:

All for educational purposes, that was an experimental project. Also, that was fun.
Please use it ethically.


# Tutorial

I can't give documentation, but here is what to do:

1. Create an Algorithm by running setupBaseArray.py
2. Use main.py to encode the file on your will. (Anything)
3. Then convert it to a video by running ffmpegEncoder.py (It needs ffmpeg's windows build inside of the directory. mainDirectory/ffmpeg/bin/ffmpeg.exe)

To decode it:

1. Run decodeVideo.py to take out frames out of the video
2. Run decoder.py

Additional note:
It's still in development so I didn't add extension support.
It will decode it as PNG. But you can change it's extension to use it.
For example, I encoded a .rar file and it decoded as .png as default:
Just change .png to .rar of the output file.


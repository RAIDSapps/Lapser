#!/usr/bin/python3

import ffmpeg

input_files = input("Input files: ")
output_file = input("Output file: ")
width = input("Width: ")
height = input("Height: ")
display_framerate = input("Timelapse framerate: ")
file_framerate = input("File framerate: ")
stream = ffmpeg.input(input_files, pattern_type='glob')
stream = ffmpeg.filter_(stream, 'format', 'yuv420p')
stream = ffmpeg.filter_(stream, 'scale', '{}x{}'.format(width, height))
stream = ffmpeg.output(stream, output_file)
ffmpeg.run(stream)

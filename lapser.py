import ffmpeg

input_files = input("Input files: ")
output_file = input("Output file: ")
display_framerate = input("Timelapse framerate: ")
file_framerate = input("File framerate: ")

stream = ffmpeg.input(input_files, r=int(display_framerate))
stream = ffmpeg.filter_(stream, 'format', 'yuv420p')
stream = ffmpeg.output(stream, output_file, r=int(file_framerate))
ffmpeg.run(stream)
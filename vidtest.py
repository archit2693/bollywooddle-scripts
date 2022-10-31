# import os
# os.environ["IMAGEIO_FFMPEG_EXE"] = "/opt/homebrew/Cellar/ffmpeg/5.1.2"

from moviepy.editor import VideoFileClip
import moviepy.video.fx.all as vfx

in_loc = 'video.mp4'
out_loc = 'video_out.mp4'

# Import video clip
clip = VideoFileClip(in_loc)
print("fps: {}".format(clip.fps))

# Modify the FPS
clip = clip.set_fps(clip.fps * 10)

# Apply speed up
final = clip.fx(vfx.speedx, 10)
print("fps: {}".format(final.fps))

# Save video clip
final.write_videofile(out_loc)
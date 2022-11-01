import moviepy.editor as mp
clip = mp.VideoFileClip("ported_too_much.mp4")
clip_resized = clip.resize(height=5, width=5) # make the height 360px ( According to moviePy documenation The width is then computed so that the width/height ratio is conserved.)
clip_fps = clip_resized.set_fps(30)
clip_fps.write_videofile("5x5.mp4")
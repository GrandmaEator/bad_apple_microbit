import moviepy.editor as mp
clip = mp.VideoFileClip("ported_too_much.mp4") #haha
clip_resized = clip.resize(height=5, width=5)
clip_fps = clip_resized.set_fps(30)
clip_fps.write_videofile("5x5.mp4")

import glob

text_video = ''
fil = glob.glob(r"video\*")
print(fil)
if ".mp4" in fil:
    text_video = fil.name
    print()
text = text_video.split("\\")
print(text_video)
res = ''
for i in text:
    if ".mp4" in i:
        res = i
        break
print(res)
video = open(f'video\\{res}', "rb")
if res in video.name.split("\\"):
    print(res)
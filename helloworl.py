import time
import datetime

print("hello world")
ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
print(st)
text_file_name = "output" + st + ".txt"
file_mode = "w"
text_file = open(text_file_name, file_mode)
text_file.write(st)
text_file.close()
#issue job is spawned three times in roll

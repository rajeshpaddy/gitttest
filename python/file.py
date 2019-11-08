import queue

q = queue.Queue()
q.put("rajesh")
print(q.get())

import os

path = os.getcwd()

files = []
# r=root, d=directories, f = files
for r,d,f in os.walk(path):
    for file in f:
        if '.log' in file:
            files.append(os.path.join(file))

for f in files:
    os.remove(f)



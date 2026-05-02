import threading

from get import getRequest

"""GET"""

tGet = []

for i in range(20):
    t = threading.Thread(target=getRequest)
    tGet.append(t)
    t.start

for t in tGet:
    t.join()

import matplotlib.pyplot as plt
import random
from recommendations import recommendation
import time
import MySQLdb

conn1 = MySQLdb.connect(host = "localhost", user = "root", passwd = "40OZlike", db = "plalyst")
cur= conn1.cursor()
cur.execute('select name from Song')
result = cur.fetchall()
result = [item for sublist in result for item in sublist]
cur.close()
conn1.close()
songNameList = []
timeList = []
for i in range(1,11):
    rnumbers = random.sample(range(0, len(result)-1), i)
    for rnum in rnumbers:
        songNameList.append(result[rnum])
    start_time = time.time()
    recommendation(songNameList)
    print('Recommendations received')
    timeTaken = time.time() - start_time
    timeList.append(round(timeTaken,3))


plt.plot([1,2,3,4,5,6,7,8,9,10],timeList)
plt.ylabel('Time taken in s')
plt.xlabel('Number of songs')
plt.show()

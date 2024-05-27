import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from exchangeVC import *
import threading
import queue


def test_presentation():
    test_start = time.time()
    # Load test No 1
    # present credential persoCert on a random port between 11002 and 11009 with 1000 parralel requests for 15 minutes
    # and measure the time it takes to present the credential
    # and plot the results
    success_list = np.array([])
    execution_time_list = np.array([])

    while time.time() - test_start < 900:
        port = np.random.randint(11002, 11009)
        start = time.time()
        presentation = present_credential("persoCert", port)
        end = time.time()
        if presentation is not None and presentation['verified'] == 'true':
            success_list = np.append(success_list, 1)
        else:
            success_list = np.append(success_list, 0)
        execution_time_list = np.append(execution_time_list, end - start)
        success_rate = np.sum(success_list) / len(success_list)
        avg_execution_time = np.mean(execution_time_list)
    # Append the results to the global success list
    q.put(success_rate)
    que.put(avg_execution_time)
    #

# Start 10 threads for the load test
threads = []
q = queue.Queue()
que = queue.Queue()
global_success_list = []
global_avg_ex_time = []
for i in range(200):
    threads.append(threading.Thread(target=test_presentation))
    threads[i].start()
for i in range(200):
    threads[i].join()
while not q.empty():
    global_success_list.append(q.get())
while not que.empty():
    global_avg_ex_time.append(que.get())
print(f"Global success rate: {np.mean(global_success_list)}")
print(f"Global average execution time: {np.mean(global_avg_ex_time)}")
# Plot the results
plt.plot(global_avg_ex_time)
plt.xlabel("Thread No")
plt.ylabel("Average execution time in seconds")
plt.title("Average execution time of 10 threads presenting persoCert")
plt.show()



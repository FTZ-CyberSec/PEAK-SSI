import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from exchangeVC import *
import threading
import queue


def test_presentation(runtime: int):
    test_start = time.time()
    # Load test No 1
    # present credential persoCert on a random port between 11002 and 11009 with 1000 parralel requests for 15 minutes
    # and measure the time it takes to present the credential
    # and plot the results
    success_list = np.array([])
    execution_time_list = np.array([])

    while time.time() - test_start < runtime:
        port = np.random.randint(11002, 11009)
        start = time.time()
        presentation = present_credential("persoCert", port)
        end = time.time()
        if presentation is not None and presentation['verified'] == 'true':
            success_list = np.append(success_list, 1)
        else:
            success_list = np.append(success_list, 0)
        execution_time_list = np.append(execution_time_list, end - start)
        if np.sum(success_list):
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
def test(runtime: int, no_threads: int):
    for i in range(no_threads):
        threads.append(threading.Thread(target=test_presentation, args=(runtime,)))
        threads[i].start()
    for i in range(no_threads):
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
    plt.savefig(f"results/load_test{round(runtime/60)}_{no_threads}.png")
    plt.show()
    # Save the results and the plot to an md file
    with open(f"results/load_test{round(runtime/60)}_{no_threads}.md", "w") as file:
        file.write("## Load Test No 1\n")
        file.write("### Test description\n")
        file.write(f"- Present credential persoCert on a random port between 11002 and 11009 with {no_threads} parallel requests for {runtime/60} minutes\n")
        file.write("- Measure the time it takes to present the credential\n")
        file.write("- Plot the results\n")
        file.write("### Results\n")
        file.write(f"- Global success rate: {np.mean(global_success_list)}\n")
        file.write(f"- Global average execution time in Seconds: {np.mean(global_avg_ex_time)}\n")
        file.write("### Plot\n")
        file.write(f"![Average execution time of 10 threads presenting persoCert](load_test{round(runtime/60)}_{no_threads}.png)\n")

# Run the load test
test(60, 50)






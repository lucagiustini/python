import tracemalloc
import time

def function_with_memory_leak():
    """
    A function that exhibits a memory leak.
    """
    # Simulating a memory leak by creating a large list
    large_list = [0] * (10**7)  # A list with ten million elements

tracemalloc.start()
# ... start your application ...

time.sleep(1)
snapshot1 = tracemalloc.take_snapshot()
# ... call the function leaking memory ...

function_with_memory_leak()

snapshot2 = tracemalloc.take_snapshot()

function_with_memory_leak()

snapshot3 = tracemalloc.take_snapshot()

function_with_memory_leak()

snapshot4 = tracemalloc.take_snapshot()

function_with_memory_leak()

snapshot5 = tracemalloc.take_snapshot()

#top_stats = snapshot2.compare_to(snapshot1, 'lineno')
#top_stats = snapshot3.compare_to(snapshot2, 'lineno')
top_stats = snapshot5.compare_to(snapshot4, 'lineno')

print("[ Top 10 differences ]")
for stat in top_stats[:10]:
    print("{} new KiB {} total KiB {} new {} total memory blocks: ".format(stat.size_diff/1024, stat.size / 1024, stat.count_diff ,stat.count))
    
    
    
import gc
from flask import Flask
from helpers import _get_service_metrics, json_response

app = Flask('pycon')

@app.route('/metrics/<service>')
@json_response

def get_service_metrics(service):
    # return list of metrics data points
    data = _get_service_metrics(service)
    gc.collect()
    return data
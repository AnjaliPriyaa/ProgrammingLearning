#“Write Python code to execute health checks against 100 LPARs concurrently with a maximum concurrency of 10 and a timeout.
from concurrent.futures import ThreadPoolExecutor, as_completed
import time
import random

servers  = [
    "server 1"
    "server 2",
    "server 3",
    "server 4",
    "server 5"
]

def health_check(server):
    # Simulate network delay
    time.sleep(random.uniform(0.5, 2))

    # Simulate healthy/unhealthy server
    is_healthy = random.choice([True, True, True, False])

    if is_healthy:
        return server, "UP"
    else:
        return server, "DOWN"


results = {}


with ThreadPoolExecutor(max_workers=3) as executor:

    # Submit all health checks
    futures = {}

    for server in servers:
        future = executor.submit(health_check, server)
        futures[future] = server

    # Collect results as soon as each task finishes
    for future in as_completed(futures):

        server = futures[future]

        try:
            server_name, status = future.result()
            results[server_name] = status

        except Exception as e:
            results[server] = f"ERROR: {e}"


print(results)

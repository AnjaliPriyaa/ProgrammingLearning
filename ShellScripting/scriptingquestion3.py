# 3. Read a dataset/file and index content based on CPU usage.
"""
Using this data directly without creating txt file - use StringIO

"""
from io import StringIO
data = """PID CPU MEMORY PROCESS
101 12.5 512 python
102 85.2 1024 java
103 45.0 256 nginx
104 92.7 2048 python
105 10.3 128 bash"""

file = StringIO(data)
# Skip header
next(file) #next(file) reads and skips the next line of the file. In our case, the first line is the header:
index={}
for line in file:
    parts = line.split()
    cpu = float(parts[1])
    pid = parts[0]
    if cpu < 30:
        category = "LOW"
    elif cpu <= 70:
        category = "MEDIUM"
    else:
        category = "HIGH"

    index.setdefault(category, []).append(pid)
print(index)
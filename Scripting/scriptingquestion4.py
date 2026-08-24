# 5. Parse and filter a JSON/API response.

data = """
{
    "status": "success",
    "users": [
        {
            "id": 101,
            "name": "Alice",
            "age": 28,
            "active": true,
            "cpu_usage": 25.5
        },
        {
            "id": 102,
            "name": "Bob",
            "age": 35,
            "active": true,
            "cpu_usage": 85.2
        },
        {
            "id": 103,
            "name": "Charlie",
            "age": 22,
            "active": false,
            "cpu_usage": null
        },
        {
            "id": 104,
            "name": "David",
            "age": 41,
            "active": true,
            "cpu_usage": 92.7
        },
        {
            "id": 113,
            "name": "Anjali",
            "age": 26,
            "active": false,
            "cpu_usage": 85.8
        }
    ]
}
"""
import json

# what is Json is Invalid - below will give json.decoder.JSONDecodeError, so we handle it
try:
    response = json.loads(data) #becomes a python dictionary
except json.JSONDecodeError:
    print("Invalid Json data")
    response={}
#if our user doesn't exist
users = response.get("users",[])
if not users:
    print("No user found")

# if we are readind directly from a file use json.loads inside with open
#json.loads() load's' means we are reading it from a string.
# find all users whose cpu usuage is greater than 80%
for user in users:
    #if cpu usage is missing for some of the user    cpu = user.get("cpu_usage")
    cpu = user.get("cpu_usage")
    if cpu is None:
        print(f"CPU usage missing for {user['name']}")
        continue
    if user.get("active") and cpu > 80:
        print(user)

with open('./Misc/access.log',"w") as file:
    file.write( "2026-08-15 10:01:02 GET /api/users responseCode 200 TTL:2200\n"
                "2026-08-15 10:01:05 GET /api/users responseCode 200 TTL:2200\n"
                "2026-08-15 10:02:10 POST /api/login responseCode 401 TTL:2200\n"
                "2026-08-15 10:02:15 GET /api/users responseCode 200 TTL:2200\n"
                "2026-08-15 10:03:20 GET /api/orders responsecode 404 TTL:2200\n"
                "2026-08-15 10:03:25 GET /api/orders ResponseCode 404 TTL:2200\n"
                "2026-08-15 10:04:30 POST /api/login responseCode TTL:2200\n"
                "2026-08-15 10:05:10 GET /api/users responseCode 200 TTL:2200\n"
                "2026-08-15 12:10:10 UIR /home/website responseCode 400 TTL:2200\n"
                "2026-08-15 12:10:10 UIR /home/website responseCode ABC TTL:2000\n"
                "2026-08-15 12:10:10 UIR /home/website TTL:2000\n"
                "2026-08-15 12:10:10 UIR /home/website responsecode 400 TTL:2000\n"
                )

#1. Given a log file, find HTTP response codes along with timestamps and hit counts.
with open('./Misc/access.log', "r") as file:
    count = {}
    counts = {}
    count_error = {}
    totallines = 0
    counttm = {}

    for line in file:
        totallines += 1

        parts = line.split()

        # Find responseCode regardless of capitalization
        responseindex = None

        for i, part in enumerate(parts):
            if part.lower() == "responsecode":
                responseindex = i
                break

        # responseCode is missing
        if responseindex is None:
            continue

        # responseCode exists, but there is no value after it
        if responseindex + 1 >= len(parts):
            continue

        response_code = parts[responseindex + 1]

        # Response code is not numeric
        if not response_code.isdigit():
            continue

        # Count 4xx and 5xx errors
        if response_code.startswith(('4', '5')):
            count_error[response_code] = count_error.get(response_code, 0) + 1

        # Date + hour + minute
        minute = parts[0] + " " + parts[1][:5]

        keytm = (minute, response_code)

        counttm[keytm] = counttm.get(keytm, 0) + 1

        # Full timestamp
        timestamp = parts[0] + " " + parts[1]

        key = (timestamp, response_code)

        # FIX: use counts.get(), not count.get()
        counts[key] = counts.get(key, 0) + 1

        # Total count per response code
        count[response_code] = count.get(response_code, 0) + 1


# Total number of errors
totalerror = sum(count_error.values())

print(count)
print(counts)
print(max(count,key=count.get))
print(count_error)

print("totalErrors", totalerror)
error_rate = (totalerror/totallines) * 100
print(error_rate)
print(counttm)







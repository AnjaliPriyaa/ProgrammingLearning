#2. Find the Top K error types from a huge log file.
import heapq
with open('./Misc/sample_app.log',"r") as file:
   
    k=2
    count = {}
    for line in file:
        # Split the log line into individual words/tokens
        parts = line.split()

        # Ignore lines that do not contain ERROR
        if 'ERROR' not in parts:
            continue
            # error = ' '.join(parts[3:]) - if error index is fixed.
        # Find the position of ERROR
        error_index = parts.index("ERROR")

        # We don't know where "message=" is yet
        message_index = None
        # Search for message= after ERROR
        for word in range(error_index+1,len(parts)):
            if parts[word].startswith('message='):
                message_index = word
                break

        # If message= is missing, skip this malformed log
        if message_index is None:
            continue

        # The first word of the error is attached to "message="
        # Example: message=Failed
        first_error_word = parts[message_index].replace("message=", "", 1)
        error_parts = [first_error_word]
        print(error_parts)

        # Collect the remaining words belonging to the error message
        # Stop when we reach request_id because it is metadata,
        # not part of the actual error type.
        for error in range(message_index+1,len(parts)):
            if parts[error].startswith('request_id='):
                break
            error_parts.append(parts[error])
        error = ' '.join(error_parts).strip('\\n"')

        # Count how many times this error type occurred
        count[error]=count.get(error,0)+1
        top_k = sorted(count.items(),key=lambda x:x[1],reverse=True)

        """
        Lets say we have a 10 million unique errors, we're sorting 10 million entries even though we only need, say, k = 10
        sorting is not a good approach then we will use heapq
        """
        # top_k = heapq.nlargest(k,count.items(),key=lambda x:x[1])
print("Error Counts:",count)
print(top_k[:k])

# How would you make the solution production-ready?
"""
Applications
     ↓
Log collectors
     ↓
Streaming/message layer
     ↓
Parser workers
     ↓
Local aggregation
     ↓
Global aggregation
     ↓
Top-K computation
     ↓
Metrics / dashboard / alerting
"""
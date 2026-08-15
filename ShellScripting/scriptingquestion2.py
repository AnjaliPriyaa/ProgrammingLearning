#2. Find the Top K error types from a huge log file.
with open('./Misc/sample_app.log',"r") as file:
    import heapq
    k=2
    count = {}
    for line in file:
        parts = line.split()
        if 'ERROR' not in parts:
            continue
            # error = ' '.join(parts[3:]) - if error index is fixed.
        error_index = parts.index("ERROR")
        message_index = None
        for word in range(error_index+1,len(parts)):
            if parts[word].startswith('message='):
                message_index = word
                break
        if message_index is None:
            continue
        error = ' '.join(parts[message_index:])
        error = error.replace("message=","",1).strip('\\n"')
        count[error]=count.get(error,0)+1
        top_k = sorted(count.items(),key=lambda x:x[1],reverse=True)

        """
        Lets say we have a 10 million unique errors, we're sorting 10 million entries even though we only need, say, k = 10
        sorting is not a good approach then we will use heapq
        """
        # top_k = heapq.nlargest(k,count.items(),key=lambda x:x[1])
print(count)
print(top_k[:k])
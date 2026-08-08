#Given millions of log lines, find the top 10 error types without loading the entire file into memory.

uniqe_errors = {}
# count_connection_refused = 0
with open('../sample_app.log') as f:
    for line in f:

        if "ERROR" in line:
            split_list= line.split(" ")

            error_type = split_list[-1].strip("message=\n")

            if error_type not in uniqe_errors:
                uniqe_errors[error_type] = 0
            
            uniqe_errors[error_type] = uniqe_errors[error_type] + 1


print(uniqe_errors)
# {
#     PermissionDenied : '',
#     FileNotFound : ''
# }
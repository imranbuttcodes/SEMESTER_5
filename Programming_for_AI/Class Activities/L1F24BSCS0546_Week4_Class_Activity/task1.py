call_count = 0

def execute_task():
    global call_count

    call_count += 1


print(call_count)
execute_task()
print(call_count)
execute_task()
print(call_count)
execute_task()
print(call_count)


# Global state modification is avoided because it creates severe race conditions when multiple threads or GPU
# workers process data simultaneously. Additionally, it relies on hidden
# states that depend on execution order, making machine learning experiments incredibly difficult to debug or reliably
# reproduce. Finally, global variables only exist within a single process's memory, meaning this 
# pattern completely fails in distributed architectures that span across multiple servers or containerized nodes.


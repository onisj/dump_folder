import psutil
import os
import time

def get_cpu_times():
    process = psutil.Process(os.getpid())
    return process.cpu_times()


def get_memory_usage():
    process = psutil.Process(os.getpid())
    return process.memory_info().rss / 1024**2  # Convert bytes to MiB


def main():
    # Your script's main code here
    b = (i**2 for i in range(100000000))
    print(sum(b))

if __name__ == "__main__":
    start_memory = get_memory_usage()
    start_cpu_times = get_cpu_times()
    start_time = time.time()
    
    print(f"Memory usage before: {start_memory:.2f} MiB")
    
    main()
    
    end_memory = get_memory_usage()
    end_cpu_times = get_cpu_times()
    end_time = time.time()

    total_memory_used = end_memory - start_memory
    user_time = end_cpu_times.user - start_cpu_times.user
    system_time = end_cpu_times.system - start_cpu_times.system
    total_time = end_time - start_time
    
    print(f"Total memory used: {total_memory_used:.2f} MiB")
    print(f"python stream_proc.py {user_time:.2f}s user {system_time:.2f}s system 100% CPU {total_time:.3f} total")
    
    
    
    
    
    

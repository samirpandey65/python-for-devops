import psutil

def check_cpu_usage():
    cpu_thereshhold = int(input("Enter the CPU usage thereshhold (%): "))
    current_cpu_usage = psutil.cpu_percent(interval=1)
    print("Current CPU % :", current_cpu_usage)
    if current_cpu_usage > cpu_thereshhold:
        print("email_alert send")
    else:
        print("CPU usage is normal")

check_cpu_usage()


def check_memory_usage():
    memory_thereshhold = int(input("Enter the Memory usage thereshhold (%): "))
    current_memory_usage = psutil.virtual_memory().percent
    print("Current Memory % :", current_memory_usage)
    if current_memory_usage > memory_thereshhold:
        print("email_alert send")
    else:
        print("Memory usage is normal")
check_memory_usage()

def check_disk_usage():
    disk_thereshhold = int(input("Enter the Disk usage thereshhold (%): "))
    current_disk_usage = psutil.disk_usage('/').percent
    print("Current Disk % :", current_disk_usage)
    if current_disk_usage > disk_thereshhold:
        print("email_alert send")
    else:
        print("Disk usage is normal")
check_disk_usage()

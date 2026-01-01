import psutil

def check_disk_usage():
    disk_thereshhold = int(input("Enter the Disk usage thereshhold (%): "))
    current_disk_usage = psutil.disk_usage('/').percent
    print("Current Disk % :", current_disk_usage)
    if current_disk_usage > disk_thereshhold:
        print("email_alert send")
    else:
        print("Disk usage is normal")
check_disk_usage()
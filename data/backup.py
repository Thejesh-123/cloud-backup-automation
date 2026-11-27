import shutil
from datetime import datetime

timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

backup_name = "backup_" + timestamp

shutil.make_archive(backup_name, "zip", "data")

print("Backup created successfully!")
print("Backup file:", backup_name + ".zip")
print("Backup status: SUCCESS")

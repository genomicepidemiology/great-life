import os

def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path, mode=0o777)  # 0o777 permissions for full read/write/execute
        print(f"Directory created: {path}")
    else:
        print(f"Directory already exists: {path}")

directories = [
    "/var/lib/cge",
    "/var/lib/cge/results",
    "/var/lib/cge/database",
    "/var/lib/cge/error_logs"
]

for dir_path in directories:
    create_directory(dir_path)

import os

def create_directory(path):
    old_umask = os.umask(0)  # Temporarily set umask to 0 for full permissions
    try:
        if not os.path.exists(path):
            os.makedirs(path, mode=0o777)  # 0o777 permissions for full read/write/execute
            print(f"Directory created: {path}")
        else:
            print(f"Directory already exists: {path}")
    finally:
        os.umask(old_umask)  # Restore the original umask value

directories = [
    "/var/lib/cge",
    "/var/lib/cge/results",
    "/var/lib/cge/database",
    "/var/lib/cge/error_logs"
]

for dir_path in directories:
    create_directory(dir_path)

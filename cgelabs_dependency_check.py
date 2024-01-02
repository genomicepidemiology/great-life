import os
import subprocess

def check_directory(path, name):
    if os.path.exists(path):
        print(f"\033[92m[CHECK PASSED]\033[0m {name} exists: {path}")
    else:
        print(f"\033[91m[ERROR]\033[0m {name} does not exist: {path}")

def check_conda_env(env_name):
    try:
        result = subprocess.run(['conda', 'env', 'list'], capture_output=True, text=True)
        if env_name in result.stdout:
            print(f"\033[92m[CHECK PASSED]\033[0m Anaconda environment '{env_name}' exists.")
        else:
            print(f"\033[91m[ERROR]\033[0m Anaconda environment '{env_name}' does not exist.")
    except FileNotFoundError:
        print(f"\033[91m[ERROR]\033[0m Anaconda is not installed or not in the system path.")

check_directory("/var/lib/cge", "CGE main directory")
check_directory("/var/lib/cge/results", "CGE results directory")
check_directory("/var/lib/cge/database", "CGE database directory")
check_directory("/var/lib/cge/database/cge_db", "CGE database")
check_conda_env("cge_env")

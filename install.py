import os
import subprocess
import sys

def is_conda_installed():
    try:
        subprocess.run(["conda", "--version"], check=True)
        return True
    except subprocess.CalledProcessError:
        return False

def create_conda_env(env_name, yaml_file):
    if env_name in subprocess.getoutput('conda env list'):
        print(f"Warning: Conda environment '{env_name}' already exists.")
    else:
        subprocess.run(["conda", "env", "create", "-f", yaml_file], check=True)

def install_packages(env_name, packages):
    for package in packages:
        subprocess.run(["conda", "install", "-n", env_name, "-c", package], check=True)

def create_directory(dir_path):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
        os.chmod(dir_path, 0o777)  # Sets full read/write permissions
    else:
        print(f"Directory {dir_path} already exists.")

if not is_conda_installed():
    print("Anaconda, Miniconda, or Mamba is not installed. Please install it to proceed.")
    sys.exit(1)

env_name = "cgeanalysis"
yaml_file = "placeholder.yaml"  # Replace with your actual .yaml file
create_conda_env(env_name, yaml_file)

packages = [("genomicepidemiology", "cgeisolate"), 
            ("genomicepidemiology", "cgevirus"), 
            ("genomicepidemiology", "cgemetagenomics")]
install_packages(env_name, packages)

create_directory("/var/lib/cge")


# Great-Life Project: Laptop and ONT Software Setup Guide
This README will serve as technical documentation for the Great-Life project. It will be updated as the project progresses.

## Technical Stack

The aim of this project is to deploy GPU-powered laptops with bioinformatics software for sequencing and analysis of microbial genomes. The technical stack is as follows:

- **Ubuntu 22.04 LTS**: Operating system.
- **ONT MinKnow-gpu-release**: For sequencing and basecalling.
- **CGE Conda tools**: Conda packages for bioinformatics data analysis.
- **CGELabs**: Electron application for a user-friendly interface.

## Laptop Setup

### Hardware Requirements

- **RAM**: At least 32GB.
- **GPU**: Nvidia GPU. 

**Note**: HP Zbooks have been successfully used in our experience, however installing the correct NVIDIA drivers can be challenging. See below for more details.
In January of 2024 we will experiment with the setup on a Dell computer, perhaps the process will be easier.

### Installing Ubuntu 22.04

- **Method**: Boot the laptop from a USB stick with Ubuntu 22.04 LTS.
- **Recommendation**: Use Rufus from a windows pc for creating a bootable USB stick with the Ubuntu 22.04 LTS ISO file. Alternatively use the Ubuntu Startup Disk Creator from a Linux pc.
- **Guidance**: Instructions for this process are readily available via a Google search.

### Kernel and Nvidia Drivers

Matching the kernel version with the Nvidia driver version is critical for the GPU to work properly.

- **Driver Installation**: If `nvidia-smi` works post Nvidia driver installation (`sudo apt install nvidia-drivers-xxx`), proceed. If not, consider the following steps:
  1. Disable Secure Boot in BIOS.
  2. If issues persist, it may be due to kernel incompatibility with newer drivers. Switching to kernel version 5.15.70 has proven effective.

#### Kernel 5.15.70 Installation

On the HP Zbook, the Nvidia driver was incompatible with the default kernel version (5.15.70). Switching to kernel version 5.15.70 (Or most other 5.15.XX versions) resolved the issue.

- **Download**: Kernel version 5.15.70 `.deb` files are available [here](https://kernel.ubuntu.com/mainline/v5.15.70/). Download all 4 files for Test amd64/build succeeded.
- **Installation**: Install the `.deb` files using `sudo dpkg -i *.deb`.
  - **Grub Configuration**: Modify grub to default to the 5.15 kernel. This can be done by editing the grub file in `/etc/default/grub` and changing the `GRUB_DEFAULT` value to `GRUB_DEFAULT="Advanced options for Ubuntu>Ubuntu, with Linux 5.15.70-051570-generic"`. Then run `sudo update-grub`.  
  - **Reboot**: Reboot the system and verify that the 5.15 kernel is running using `uname -r`. If so, `nvidia-smi` should work.
  - **Note**: If the 5.15 kernel is not running, it may be due to Secure Boot being enabled. Disable Secure Boot in BIOS and try again.
  - **Note**: To check which kernel is running, use `uname -r`.

All the information above can be disregarded if the Nvidia driver works with the default kernel version. To check the Nvidia driver version, use `nvidia-smi`.
The NVIDIA driver MUST work for the basecalling of the Oxford Nanopore Software to work.

### ONT Software

- **Download**: Acquire MinKnow-gpu-release from the ONT community software section. Follow the instructions for installation for ubuntu 22.

### Anaconda3 Installation

- **Purpose**: Anaconda is used to create a Conda environment for the Great-Life project.
- **Source**: Download the latest version from the Anaconda website.
**Note**: The CGELabs app will look for conda packages installed my anaconda3 which should be located in the home repository (~). If you are using microconda, the app will not find the packages. Therefore ONLY install anaconda3.

### Ubuntu 22.04 Installation Cookbook

Below are example commands for setting up a new Ubuntu 22.04 installation. This serves as a guideline and may not be exhaustive.

```markdown
# Assumes a fresh Ubuntu 22.04 installation from a USB stick
# Update and upgrade
sudo apt update 
sudo apt upgrade
# Install Anaconda and place in default path and initialize conda (yes)
wget https://repo.anaconda.com/archive/Anaconda3-2022.05-Linux-x86_64.sh
bash Anaconda3-2022.05-Linux-x86_64.sh
# Restart terminal by closing and reopening
# Install Kernel 5.15.70 (if necessary. Here we simulate the kernel 5.15.70 installation process which will not be necessary if the default kernel works)
# Download the 4 .deb files for Test amd64/build succeeded from https://kernel.ubuntu.com/mainline/v5.15.70/
# Install the .deb files
sudo dpkg -i *.deb
# Modify grub to default to the 5.15.70 kernel
sudo nano /etc/default/grub
# Change GRUB_DEFAULT to "Advanced options for Ubuntu>Ubuntu, with Linux 5.15.70-051570-generic"
# **NOTE**: Make sure the the above GRUB change is correct by checking the grub file in /boot/grub/grub.cfg: ` cat /boot/grub/grub.cfg | grep Linux 5.15`. The string inserted in the grub file dictates which kernel is used on boot. An incorrect/errornous string will cause the system to fail to boot.
# Update grub
sudo update-grub
# Reboot
sudo reboot
# Install Nvidia drivers
sudo apt install nvidia-drivers-535
# Reboot
sudo reboot
# Verify nvidia-smi
nvidia-smi
# Install MinKnow-gpu-release from ONT community software website according to instructions
# https://community.nanoporetech.com/posts/release-of-ubuntu-22-04-j for ubuntu 22.04 download of MinKNOW
# Check MinKNOW is installed in the application menu
# Install git for futures uses
sudo apt install git
# Download the cge conda environment file:
wget https://cge.food.dtu.dk/services/MINTyper/cge_env.yml
# Create the cge conda environment:
conda env create -f cge_env.yml -n cge_env
# Download the CGELabs setup script from the CGE server:
wget https://cge.food.dtu.dk/services/MINTyper/setup_cge.py
# Run the setup script:
sudo python3 setup_cge.py
# Download the cge_db from the CGE server:
wget https://cge.food.dtu.dk/services/MINTyper/cge_db.tar.gz
# Unpack the cge_db:
tar -xvf cge_db.tar.gz
# Move the cge_db to the CGELabs directory:
mv cge_db /var/lib/cge/database/cge_db
# Download the CGELabs .deb file:
wget https://cge.food.dtu.dk/services/MINTyper/cge-labs_1.0.0-1_amd64.deb
# Install the CGELabs .deb file:
sudo dpkg -i cge-labs_1.0.0-1_amd64.deb
# To check if all dependencies are installed correctly, download the dependency check script from the CGE server:
wget https://cge.food.dtu.dk/services/MINTyper/cgelabs_dependency_check.py
# Execute the script:
python3 cgelabs_dependency_check.py

```

## CGELabs App
For details on the CGELabs app, see the [CGELabs App](https://github.com/genomicepidemiology/CGELabs) repository.

## CGE analysis tools

The following tools can be run from the CGELabs app:

- cgeisolate (https://github.com/genomicepidemiology/cgeisolate). This tool is design to analyse bacterial isolates.
- cgevirus (https://github.com/genomicepidemiology/cgevirus). This tool is designed to analyse viral genomes.
- cgemetagenomics (https://github.com/genomicepidemiology/cgemetagenomics). This tool is designed to analyse metagenomic samples containing microbes, not viruses. Primarily designed for surveillance of AMR.

All these tools are installed at once in the cge_env conda environment if the following steps are used:

`wget https://cge.food.dtu.dk/services/MINTyper/cge_env.yml`

`conda env create -f cge_env.yml -n cge_env`

CGELabs requires all the tools to be installed in the cge_env conda environment. If the tools are installed in a different conda environment, CGELabs will not find them.

### CGE analysis tools development

For future development of the CGE tools the implementations can be made into the respective repositories. 
When the newly developed features are tested and ready to be released, a new version of the conda package can be deployed to the CGE conda channel by following the steps below:

`git add --a`

`git commit -m "<version>"` #Should be major.minor.patch (e.g. 1.0.1)

`git tag <version>` #Should be major.minor.patch (e.g. 1.0.1)

`git push && git push --tags`

The above commands will trigger a GitHub action that will build the conda package and deploy it to the CGE conda channel (anaconda.org/genomicepidemiology).

Once the conda package is deployed, the cge_env on the deployed laptops can be updated by running the following command:

`conda update --all -n cge_env -c genomicepidemiology`
.



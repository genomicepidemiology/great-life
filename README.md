# Great-Life Project: Laptop and ONT Software Setup Guide
This README will serve as technical documentation for the Great-Life project. It will be updated as the project progresses.

## Technical Stack

- **Ubuntu 22.04 LTS**: Operating system.
- **ONT MinKnow-gpu-release**: For sequencing and basecalling.
- **CGE Analysis Tools**: Conda packages for data analysis.
- **CGE Analysis Tools GUI**: Electron application for a user-friendly interface.

## Laptop Setup

### Hardware Requirements

- **RAM**: At least 32GB.
- **GPU**: Nvidia GPU recommended. 
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
# Check MinKNOW is installed in the application menu
# Install git for futures uses
sudo apt install git
# Download the CGELabs setup script from the CGE server:
`wget https://cge.cbs.dtu.dk/services/CGELabs/setup.py`
# Run the setup script:
`sudo python3 setup.py`
# Download the cge_db from the CGE server:
`wget https://cge.cbs.dtu.dk/services/CGELabs/cge_db.tar.gz`
# Unpack the cge_db:
`tar -xvf cge_db.tar.gz`
# Move the cge_db to the CGELabs directory:
`mv cge_db /var/lib/cge/database/cge_db`
# Download the CGELabs .deb file:
`wget https://cge.cbs.dtu.dk/services/CGELabs/cge-labs_1.0.0-1_amd64.deb`
# Install the CGELabs .deb file:
`sudo dpkg -i cge-labs_1.0.0-1_amd64.deb`
# To check if all dependencies are installed correctly, download the dependency check script from the CGE server:
`wget https://cge.cbs.dtu.dk/services/CGELabs/cgelabs_dependency_check.py`
# Execute the script:
`python3 cgelabs_dependency_check.py`

```

## CGE analysis tools
CONTINUE HERE

Anaconda must be installed to run the CGE analysis tools. Installation of the tools can be found in their respective github repos.

- cgeisolate (https://github.com/genomicepidemiology/cgeisolate). This tool is design to analyse bacterial isolates.
- cgevirus (https://github.com/genomicepidemiology/cgevirus). This tool is designed to analyse viral genomes.
- cgemetagenomics (https://github.com/genomicepidemiology/cgemetagenomics). This tool is designed to analyse metagenomic samples containing microbes, not viruses.
- 
## CGE analysis tools GUI



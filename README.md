# Great-Life Project: Laptop and ONT Software Setup Guide

## Technical Stack

- **ONT MinKnow-gpu-release**: For sequencing and basecalling.
- **CGE Analysis Tools**: Conda packages for data analysis.
- **CGE Analysis Tools GUI**: Electron application for a user-friendly interface.

## Laptop Setup

### Hardware Requirements

- **RAM**: At least 32GB.
- **GPU**: Nvidia GPU recommended. HP Zbooks have been successfully used in our experience.

### Installing Ubuntu 22.04

- **Method**: Boot the laptop from a USB stick with Ubuntu 22.04 LTS.
- **Recommendation**: Use Rufus from a windows pc for creating a bootable USB stick with the Ubuntu 22.04 LTS ISO file.
- **Guidance**: Instructions for this process are readily available via a Google search.

### Kernel and Nvidia Drivers

- **Nvidia Compatibility**: The integration of `nvidia-smi` with the kernel can be challenging.
- **Driver Installation**: If `nvidia-smi` works post Nvidia driver installation (`sudo apt install nvidia-drivers-xxx`), proceed. If not, consider the following steps:
  1. Disable Secure Boot in BIOS.
  2. If issues persist, it may be due to kernel incompatibility with newer drivers. Switching to kernel version 5.15.0 has proven effective.

#### Kernel 5.15.0 Installation

- **Download**: Kernel version 5.15.0 `.deb` files are available [here](https://kernel.ubuntu.com/mainline/v5.15.70/).
- **Instructions**: For installation guidance, consult Google or ChatGPT.
- **Grub Configuration**: Modify `/etc/default/grub` to set kernel 5.15.0 as the default.

### ONT Software

- **Download**: Acquire MinKnow-gpu-release from the ONT community software section.
- **Compatibility Note**: Though listed for Ubuntu 20.04, it should work on Ubuntu 22.04.

### Anaconda Installation

- **Purpose**: Anaconda is used to create a Conda environment for the Great-Life project.
- **Source**: Download the latest version from the Anaconda website.

### Ubuntu 22.04 Installation Cookbook

Below are example commands for setting up a new Ubuntu 22.04 installation. This serves as a guideline and may not be exhaustive.

```markdown
# Assumes a fresh Ubuntu 22.04 installation
# Update and upgrade
sudo apt update 
sudo apt upgrade
# Install Anaconda
wget https://repo.anaconda.com/archive/Anaconda3-2022.05-Linux-x86_64.sh
bash Anaconda3-2022.05-Linux-x86_64.sh
# Install Kernel 5.15
# [Download kernel files from kernel.ubuntu.com]
sudo dpkg -i *.deb
# Modify grub to default to the 5.15 kernel
# Install Nvidia drivers
sudo apt install nvidia-drivers-535
# Reboot
sudo reboot
# Verify nvidia-smi
nvidia-smi
# Install MinKnow-gpu-release from ONT community software website

# Install git
sudo apt install git
# Install anaconda. Location should just be default path, so just press enter when prompted
# When prompted to initialize conda, type yes
wget https://repo.anaconda.com/archive/Anaconda3-2023.09-Linux-x86_64.sh
bash Anaconda3-2023.09-Linux-x86_64.sh
# You might need to restart your terminal for conda to work
# Install mamba in base environment
conda install -n base -c conda-forge mamba
```

## CGE analysis tools

Anaconda must be installed to run the CGE analysis tools. Installation of the tools can be found in their respective github repos.

- cgeisolate (https://github.com/genomicepidemiology/cgeisolate). This tool is design to analyse bacterial isolates.
- cgevirus (https://github.com/genomicepidemiology/cgevirus). This tool is designed to analyse viral genomes.
- cgemetagenomics (https://github.com/genomicepidemiology/cgemetagenomics). This tool is designed to analyse metagenomic samples containing microbes, not viruses.

## CGE analysis tools GUI



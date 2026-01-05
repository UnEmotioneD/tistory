# Developer Environment

- [python](#python)
- [venv](#python-virtual-environment)
- [jupyter](#jupyter-notebooks)
- [ros2](#ros2-dev-env)
  - [pinky](#pinky-pro)

## Python

- python3-pip
- python3-ipykernel

```bash
sudo apt install python3-full python3-pip python3-ipykernel
```

update `pip3` to latest version

`--break-system-packages`: for py ver higher then 3.12

```bash
pip3 install --upgrade pip --break-system-packages
```

---

## Python Virtual Environment

create venv to desired location

```bash
python3 -m venv {dir/venv-name}
```

activate venv

you can use `.` instead of `source`

```bash
source {venv-path}/bin/activate
```

- also update the `pip` inside the venv

turn if off

```bash
deactivate
```

---

## Jupyter Notebooks

Inside the python venv install jupyter module

```bash
pip3 install jupyter
```

Launch jupyter notebook

This will start server on localhost and web browser.
Root directory will be set to where you ran the commands.

```bash
jupyter notebook
```

Stop the server by pressing `Ctrl + c`

Closing the browser tab won't effect anything

## ROS2 Dev Env

- Use to connect to `Pinky` robot

- [ROS2 - Ubuntu](https://docs.ros.org/en/jazzy/Installation/Ubuntu-Install-Debs.html)

---

```bash
locale  # check for UTF-8

sudo apt update && sudo apt install locales
sudo locale-gen en_US en_US.UTF-8
sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
export LANG=en_US.UTF-8

locale  # verify settings
```

Enable `ubuntu universe` repository

```bash
sudo apt install software-properties-common
sudo add-apt-repository universe
```

Install ros2 package. And set up to update automatically

```bash
sudo apt update && sudo apt install curl -y
export ROS_APT_SOURCE_VERSION=$(curl -s https://api.github.com/repos/ros-infrastructure/ros-apt-source/releases/latest | grep -F "tag_name" | awk -F\" '{print $4}')
curl -L -o /tmp/ros2-apt-source.deb "https://github.com/ros-infrastructure/ros-apt-source/releases/download/${ROS_APT_SOURCE_VERSION}/ros2-apt-source_${ROS_APT_SOURCE_VERSION}.$(. /etc/os-release && echo ${UBUNTU_CODENAME:-${VERSION_CODENAME}})_all.deb"
sudo dpkg -i /tmp/ros2-apt-source.deb
```

Update apt and packages

```bash
sudo apt update && sudo apt upgrade -y
```

Install ros2 desktop

```bash
sudo apt install ros-jazzy-desktop
```

Add this to `.bashrc` to set up your environment

```bash
. /opt/ros/jazzy/setup.sh
```

Or with alias

```bash
alias jazzy=". /opt/ros/jazzy/setup.zsh"
```

Open two separate terminal session and run each commands to check if it works

Source `jazzy` if `ros2` command is not working

```bash
ros2 run demo_nodes_cpp talker
```

```bash
ros2 run demo_nodes_py listener
```

Set domain id to only talk with specific `talker`

```bash
export ROS_DOMAIN_ID=25
```

Extra packages to install

```bash
sudo apt install ros-dev-tools                    # needed for rosdep
sudo apt install python3-colcon-common-extensions # to build pkg
```

### Pinky Pro

For pink pro guide check out

- [pinky.md](./pinky.md)

---

### Happy Hacking 🎉

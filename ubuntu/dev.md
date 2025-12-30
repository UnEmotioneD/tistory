# Developer Environment

- vscode
- python
- jupyter
- cuda

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

- jupyter-core

inside the python venv

```bash
pip install jupyter
```

launch jupyter notebook

This will start server on localhost and web browser. Root directory will be set to where you ran the commands.

```bash
jupyter notebook
```

stop the server by pressing `Ctrl + c`

closing the browser tab won't effect anything

## ROS2 Dev Env

- use to connect to `Pinky` robot

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

Enable reqruied repositories

- `ubuntu universe repository`

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

set up your environment

```bash
. /opt/ros/jazzy/setup.sh
```

setup alias

```bash
alias jazzy=". /opt/ros/jazzy/setup.zsh"
```

- Open two separate terminal session source jazzy and run each commands to check
  if it works

```bash
ros2 run demo_nodes_cpp talker
```

```bash
ros2 run demo_nodes_py listener
```

Change domain

```bash
export ROS_DOMAIN_DI=69
```

Extra packages

```bash
sudo apt install ros-dev-tools                    # needed for rosdep
sudo apt install python3-colcon-common-extensions # to build pkg
```

---

## Pinky Pro

Make directory for pink_pro and clone pinky_pro repo

```bash
mkdir -p ~/pinky_pro/src
cd ~/pinky_pro/src
git clone https://github.com/pinklab-art/pinky_pro.git
```

Inside the `pinky_pro/src/` update `rosdep`

```bash
sudo rosdep init
resdep update
```

Install dependencies from `~/pinky_pro/`

```bash
rosdep install --from-paths src --ignore-src -r -y
```

You should see `#All reqruied rosdeps installed successfully`

now build it

```bash
colcon build
```

- Build trouble shoot
  - check if jazzy is sourced
  - check where you ran commands

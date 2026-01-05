# Pinky

- [Build](#build)
- [Connect to Pinky](#connect-to-pinky)
- [Create map](#create-map)
  - [Aliases](#aliases)
- [Run using saved map](#run-with-saved-map)
- [Run using jupyter code](#run-using-jupyter-code)
  - [Install jupyter globally](#install-jupyter-globally)
  - [Usual stuff](#usual-stuff)

---

## Build

Make directory for pink and clone `pinky_pro` repo from github

```bash
mkdir -p ~/pinky_pro/src
cd ~/pinky_pro/src
git clone https://github.com/pinklab-art/pinky_pro.git
```

Inside the `pinky_pro/src/` initialize and update `rosdep`

```bash
sudo rosdep init
rosdep update
```

Install dependencies from `pinky_pro/` directory

```bash
rosdep install --from-paths src --ignore-src -r -y
```

You should see:

```text
#All reqruied rosdeps installed successfully
```

Now build it

```bash
colcon build
```

- Build trouble shoot
  - check if jazzy is sourced
  - check where you ran commands

### Get Required Commands

do one of this command every time you're inside `pinky_pro/`

```sh
source ./install/local_setup.bash
# does the same thing
source ./install/setup.bash
```

---

## Connect to Pinky

After `buzzer` from pinky

### Pinky's Wi-Fi

Look for `pinky_xxxx` from wifi

- pw: `pinkypro`

### SSH into Pinky

```bash
ssh pinky@192.168.4.1
```

### Connect Pinky to Wi-Fi

```bash
./wifi_setup.sh
```

`SSID`: is the name of the wifi
pinky password: `1`

Ping google's public DNS

```bash
ping 8.8.8.8
```

Set `ROS_DOMAIN_ID` to be same as local machine

```bash
export ROS_DOMAIN_ID=25
```

### Bringup Pinky

what is `bringup`? activating pinky's motor

```bash
ros2 launch pinky_bringup bringup_robot.launch.xml
```

Keep this running and open new terminal session for your local machine

### Check Connection

Make sure you have sourced `jazzy`

From the `local`:

```bash
ros2 topic list
```

### Control Pinky

```bash
ros2 run teleop_twist_keyboard teleop_twist_keyboard
```

---

## Create Map

`SSH` into pinky and do `bring up`

```bash
ros2 launch pinky_bringup bringup_robot.launch.xml
```

And start `SLAM`

```bash
ros2 launch pinky_navigation map_building.launch.xml
```

From local open `map` to see what pinky sees

```bash
ros2 launch pinky_navigation map_view.launch.xml
```

open another session for pinky control with your keyboard

```bash
ros2 run teleop_twist_keyboard teleop_twist_keyboard
```

Control pinky around the map nice and slowly for accurate mapping

Save the created map

Run from pinky:

- just save it under the home directory
- no extension needed

```bash
ros2 run nav2_map_server map_saver_cli -f "{map-name}"
```

this will create two map files:

- {map-name}.xml
- {map-name}.yaml

---

### Aliases

Inside the `.bash_aliases` of `pinky`

```bash
alias bringup="ros2 launch pinky_bringup bringup_robot.launch.xml"
alias slam="ros2 launch pinky_navigation map_building.launch.xml"
# use $ savemap {map-name}
alias savemap="ros2 run nav2_map_server map_saver_cli -f"
# use $ loadmap map:={map-name}
alias loadmap="ros2 launch pinky_navigation bringup_launch.xml"
```

Set alias inside local machine

```bash
alias rviz="ros2 launch pinky_navigation map_view.launch.xml"
alias teleop="ros2 run teleop_twist_keyboard teleop_twist_keyboard"
```

---

## Run with Saved Map

From pinky after `bringup` run:

```bash
ros2 launch pinky_navigation bringup_launch.xml map:={map-name}.yaml  # or .xml
```

From `Local` launch `rviz`

Click on `S2 Pose Estimate` from the menubar of rviz
and set the location and direction pinky is facing

Click on `Nav2 Goal` to set way points

---

## Run Using Jupyter Code

Control with Python code

### Install Jupyter Globally

```sh
pip3 install jupyter --break-system-packages
```

### Usual Stuff

1. connect to pinky's wifi
2. ssh into pinky
3. do `bringup`
4. launch with saved map
5. from local launch `rviz`
6. set pinky's location and direction

### Launch Jupyter Notebook

from `~/pinky_pro` directory:

```sh
jupyter notebook
```

---

#### Happy Hacking 🎉

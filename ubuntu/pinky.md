# Pinky

- [Build](#build)
- [Connect](#connect-with-pinky)
  - [Trouble Shoot](#pinky-bring-up-trouble-shooting)
- [Map](#create-map)

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

## Connect with Pinky

After `buzzer` from pinky

Look for `pinky_xxxx` from wifi

- pw: `pinkypro`

After that connect with `ssh`

```bash
ssh pinky@192.168.4.1
```

After `ssh` into pinky run following to connect to wifi

From now on your inside `ssh`

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

Run `bring up` from pinky

```bash
ros2 launch pinky_bringup bringup_robot.launch.xml
```

Keep this running and open new terminal session for your local machine

---

From the local pc check connection

Make sure you have sourced `jazzy`

```bash
ros2 topic list
```

Now you can control it

```bash
ros2 run teleop_twist_keyboard teleop_twist_keyboard
```

### Pinky Trouble Shooting

#### Ping takes receives no packets back

Not a problem

#### Motor Time Out

Just do `bringup` again

#### `ros2 topic list` Not Showing Items Needed

Check if `ubuntu fire wall` is enabled

```bash
sudo ufw status
```

Disable if enabled

```bash
sudo ufw disable
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

Save the created map

Run from pinky:

- just save it under the home directory
- no extension needed

```bash
ros2 run nav2_map_server map_saver_cli -f "{name-of-map-file}"
```

Inside the `.bash_aliases` of `pinky`

```bash
alias bringup="ros2 launch pinky_bringup bringup_robot.launch.xml"
alias slam="ros2 launch pinky_navigation map_building.launch.xml"
alias savemap="ros2 run nav2_map_server map_saver_cli -f"
```

Set alias inside local machine

```bash
alias riv="ros2 launch pinky_navigation map_view.launch.xml"
alias teleop="ros2 run teleop_twist_keyboard teleop_twist_keyboard"
```

---

### Happy Hacking 🎉

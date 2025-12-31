# Pinky

- [build](#build)
- [connect](#connect-with-pinky)
  - [trouble shooting](#pinky-bring-up-trouble-shooting)
- [map](#create-map)

## Build

Make directory for pink_pro and clone pinky_pro repo

```bash
mkdir -p ~/pinky_pro/src
cd ~/pinky_pro/src
git clone https://github.com/pinklab-art/pinky_pro.git
```

Inside the `pinky_pro/src/` update `rosdep`

```bash
sudo rosdep init
rosdep update
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

## Connect with Pinky

After `buzzer` from pinky

Look for `pinky_xxxx` from wifi

- pw: `pinkypro`

Connect with `ssh`

```bash
ssh pinky@192.168.4.1
```

after `ssh` into pinky run following to connect to wifi

- From now on your inside `ssh`

```bash
./wifi_setup.sh
```

`SSID`: is the name of the wifi
pinky password: `1`

ping google's public DNS

```bash
ping 8.8.8.8
```

set `ROS_DOMAIN_ID` to be same as local machine

```bash
export ROS_DOMAIN_ID=25
```

Run `bring up` from pinky

```bash
ros2 launch pinky_bringup bringup_robot.launch.xml
```

keep this running and open new terminal session for your local machine

---

### Pinky bring up trouble shooting

motor is keep timing out

also ping takes receives no packets back

---

From the local pc check connection

- make sure you have sourced `jazzy`

```bash
ros2 topic list
```

Now you can control it

```bash
ros2 run teleop_twist_keyboard teleop_twist_keyboard
```

## Create Map

After you sshed into pinky and after `wifi_setup.sh` do `bring up`

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

run from pinky:

```bash
ros2 run nav2_map_server map_saver_cli -f "{name of the map}"
```

- `.bash_aliases` in pinky

```bash
alias bringup="ros2 launch pinky bringup_robot.launch.xml"
alias slam="ros2 launch pinky_navigation map_building.launch.xml"
alias savemap="ros2 run nav2_map_server map_saver_cli -f"
```

- alias for local

```bash
alias map="ros2 launch pinky_navigation map_view.launch.xml"
alias teleop="ros2 run teleop_twist_keyboard teleop_twist_keyboard"
```

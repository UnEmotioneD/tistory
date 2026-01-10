# Package & Node

- [Running](#running)

## What is Topic

publisher node

subscriber node

when publisher sends data topic collects and distribute to substribers

---

## What is Service

server
client

have to create session before transferring data

---

## What is Action

topic & service combined

---

## Running

### Install Dependencies

```sh
sudo apt update && sudo apt install -y \
python3-flake8-blind-except \
python3-flake8-class-newline \
python3-flake8-deprecated \
python3-mypy \
python3-pip \
python3-pytest \
python3-pytest-cov \
python3-pytest-mock \
python3-pytest-repeat \
python3-pytest-rerunfailures \
python3-pytest-runner \
python3-pytest-timeout \
ros-dev-tools
```

```sh
sudo apt install python3-colcon-common-extensions
```

## Create Package

make directory `~/Developer/ros2-workspace/` and from inside

### Build with Colcon

```sh
colcon build
```

### Package Directory

make `src/` dir under cwd

### Create Package

package name: my_first_package
node name: my_first_node

```sh
ros2 pkg create --build-type ament_python --node-name my_first_node my_first_package
```

### Build Package

main method path should be added to the `setup.py` for the package to properly
build

```sh
colcon build
```

### Run Package

setup environment

```sh
source ~/Developer/ros2-workspace/install/local_setup.zsh
```

run:

```sh
ros2 run my_first_package my_first_node
```

### View with GUI

after subscriber and publisher: makes the turtle to go around

start publisher then subscriber: shows the grid value of turtle

run turtlesim node:

```sh
ros2 run turtlesim turtlesim_node
```

show graph:

- shows a diagram of node's relation

```sh
rqt_graph
```

select `Nodes/Topics(all)` from top left and refresh

all in separate terminal sessions with `local_setup.zsh` sourced

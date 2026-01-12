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

and has much more features

action client and server

client sends goal to server also can cancel goal

can request result

server can give feedback and status

- service
  - send goal
  - cancel goa
  - get result

- topic
  - feedback
  - status

service vs topic

what has to be done is service and data should not be lost

topic is some kind of data that you can lose

action interface is separated into

- request
- reseult
- feedback

after creating action just like service and topic add path to CMakeLists.txt file

add dependency inside the package.xml

```xml
<!-- dependency for action messages -->
<depend>action_msgs</depend>
```

when doing show interface you pass type which is path

```sh
# to check services type
service list -t
```

### Send Goal

```sh
ros2 action send_goal /{action-name} {path-to-action} "{values-for-interface}"

# for feedback
ros2 action send_goal --feedback /{action-name} {path-to-action} "{values-for-interface}"
```

### Multi-Thread

subscriber does not work with action running

add both pub and sub to multithreadexecutor: `my_multi_thread.py`

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

---

## Define Messages

### Build CMake Package

package with cmake

from `~/Developer/ros2-workspace/`

```sh
ros2 pkg create --build-type ament_cmake my_first_package_msg
cd my_first_package_msg
mkdir msg
```

Define `Message` or `Interface`

publisher: msg.msg
sruvice: msg.srv
actino: msg.action

and inside the `msg/` create `CmdAndPoseVel.msg`

to set the data type data you will send and get

### CMake.txt

inside `CMakde.txt`:

to look for interface file we added

```txt
find_package(rosidl_default_generators REQUIRED)

rosidl_generate_interfaces(${PROJECT_NAME}
  "msg/CmdAndPoseVel.msg"
)
```

### package.xml

add dependencies

under `<text_depend>` tag

```xml
  <build_depend>rosidl_default_generators</build_depend>
  <exec_depend>rosidl_default_runtime</exec_depend>
  <member_of_group>rosidl_interface_packages</member_of_group>
```

### Build MSG Package

from `ros2-workspace/` do `colcon build`

if error says `em has no attribute`

install following packages

```sh
pip3 install empy catkin_pkg lark
```

### Check Interface

source the `install/local_setup.zsh`

```sh
ros2 interface show my_first_package_msgs/msg/CmdAndPoseVel
```

this will show the content of the `CmdAndPoseVel.msg`

---

```sh
ros2 topic list -l
```

topic type is a topic's path

---

create 2 topics that sub to 1 topic

---

serve CMakeList.txt has `---` separator to separate data received and sent

FROM ros:noetic-ros-core

SHELL ["/bin/bash","-c"]

RUN apt-get update && \
    apt-get install --no-install-recommends -y \
    build-essential \
    python3-tk \
    python3 \
    python3-pip \
    ros-noetic-effort-controllers \
    ros-noetic-robot-state-controller \
    ros-noetic-rviz \
    ros-noetic-gazebo-ros \
    ros-noetic-xacro \
    ros-noetic-joint-state-publisher \
    ros-noetic-robot-state-publisher \
    ros-noetic-ros-control \
    ros-noetic-gazebo-ros-control \
    gazebo11     

RUN pip3 install numpy

RUN apt-get install -y --no-install-recommends \
    ros-noetic-joint-state-controller \
    ros-noetic-position-controllers

ADD rs_control /workspace/src/rs_control
ADD rs_description /workspace/src/rs_description
ADD rs_gazebo /workspace/src/rs_gazebo
ADD rs_inverse /workspace/src/rs_inverse
ADD rs_msgs /workspace/src/rs_msgs
ADD rs_teleop /workspace/src/rs_teleop
ADD rs_viz /workspace/src/rs_viz
ADD rs_remote /workspace/src/rs_remote

WORKDIR /workspace

RUN chmod +x /workspace/src/rs_inverse/scripts/inverse.sh

RUN . /opt/ros/noetic/setup.bash; \
    catkin_make

RUN echo "source /workspace/devel/setup.bash" >> ~/.bashrc && \
    source ~/.bashrc

CMD source /workspace/devel/setup.bash && roslaunch rs_remote remote.launch





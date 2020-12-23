#!/usr/bin/env python

"""
Forward kinematics is implemented in this scripts.
It is node that publish commands on joints actuators to move Spot in predefined positions
"""

import rospy
import time
from std_msgs.msg import Float64

spot_name = str(input("Tell me spot name: "))
rospy.init_node(spot_name + 'talker')
rate = rospy.Rate(1000)  # 100hz

# ----- Publishers ---
# ---- Front ----
# left front hip_x
pub_front_left_hip_x = rospy.Publisher('/' + spot_name + '/joint_front_left_hip_x_controller/command',
                                       Float64, queue_size=10)

# left front hip_y
pub_front_left_hip_y = rospy.Publisher('/' + spot_name + '/joint_front_left_hip_y_controller/command',
                                       Float64, queue_size=10)

# left front knee
pub_front_left_knee = rospy.Publisher('/' + spot_name + '/joint_front_left_knee_controller/command',
                                      Float64, queue_size=10)

# right front hip_x
pub_front_right_hip_x = rospy.Publisher('/' + spot_name + '/joint_front_right_hip_x_controller/command',
                                        Float64, queue_size=10)

# right front hip_y
pub_front_right_hip_y = rospy.Publisher('/' + spot_name + '/joint_front_right_hip_y_controller/command',
                                        Float64, queue_size=10)

# right front knee
pub_front_right_knee = rospy.Publisher('/' + spot_name + '/joint_front_right_knee_controller/command',
                                       Float64, queue_size=10)

# ---- Rear ----
# left rear hip_x
pub_rear_left_hip_x = rospy.Publisher('/' + spot_name + '/joint_rear_left_hip_x_controller/command',
                                      Float64, queue_size=10)

# left rear hip_y
pub_rear_left_hip_y = rospy.Publisher('/' + spot_name + '/joint_rear_left_hip_y_controller/command',
                                      Float64, queue_size=10)

# left rear knee
pub_rear_left_knee = rospy.Publisher('/' + spot_name + '/joint_rear_left_knee_controller/command',
                                     Float64, queue_size=10)

# right rear hip_x
pub_rear_right_hip_x = rospy.Publisher('/' + spot_name + '/joint_rear_right_hip_x_controller/command',
                                       Float64, queue_size=10)

# right rear hip_y
pub_rear_right_hip_y = rospy.Publisher('/' + spot_name + '/joint_rear_right_hip_y_controller/command',
                                       Float64, queue_size=10)

# right rear knee
pub_rear_right_knee = rospy.Publisher('/' + spot_name + '/joint_rear_right_knee_controller/command',
                                      Float64, queue_size=10)


def talker():
    """Publish the joints command via topics"""
    # Hips in x-direction
    pub_front_left_hip_x.publish(motors_target_pos[0][0])
    pub_front_right_hip_x.publish(motors_target_pos[1][0])
    pub_rear_left_hip_x.publish(motors_target_pos[2][0])
    pub_rear_right_hip_x.publish(motors_target_pos[3][0])

    # Hips in y-direction
    pub_front_left_hip_y.publish(motors_target_pos[0][1])
    pub_front_right_hip_y.publish(motors_target_pos[1][1])
    pub_rear_left_hip_y.publish(motors_target_pos[2][1])
    pub_rear_right_hip_y.publish(motors_target_pos[3][1])

    # Knee
    pub_front_left_knee.publish(motors_target_pos[0][2])
    pub_front_right_knee.publish(motors_target_pos[1][2])
    pub_rear_left_knee.publish(motors_target_pos[2][2])
    pub_rear_right_knee.publish(motors_target_pos[3][2])


# -------Commands on joints actuators to move Spot in predefined positions
sit_down = [[0.20, 1.0, -2.49],  # Front left leg
            [-0.20, 1.0, -2.49],  # Front right leg
            [0.20, 1.0, -2.49],  # Rear left leg
            [-0.20, 1.0, -2.49]]  # Rear right leg

stand_up = [[0.20, 0.7, -1.39],  # Front left leg
            [-0.20, 0.7, -1.39],  # Front right leg
            [0.20, 0.7, -1.39],  # Rear left leg
            [-0.20, 0.7, -1.39]]  # Rear right leg

give_paw = [[-0.30, 1.0, -1.39],  # Front left leg
            [-0.20, -0.6, -1.09],  # Front right leg
            [0.20, 1.0, -2.39],  # Rear left leg
            [-0.20, 1.0, -2.39]]  # Rear right leg

lap_spread = [[1.20, 0.7, -1.39],  # Front left leg
              [-1.20, 0.7, -1.39],  # Front right leg
              [1.20, 0.7, -1.39],  # Rear left leg
              [-1.20, 0.7, -1.39]]  # Rear right leg

fl_lap = [[0.20, -0.2, -1.09],  # Front left leg
          [-0.20, 0.7, -1.39],  # Front right leg
          [0.20, 0.7, -1.39],  # Rear left leg
          [-0.20, 0.7, -1.39]]  # Rear right leg

fr_lap = [[0.20, 0.7, -1.09],  # Front left leg
          [-0.20, -0.2, -1.09],  # Front right leg
          [0.20, 0.7, -1.39],  # Rear left leg
          [-0.20, 0.7, -1.39]]  # Rear right leg

bow_forward = [[0.20, 1.0, -1.79],  # Front left leg
               [-0.20, 1.0, -1.79],  # Front right leg
               [0.20, 0.7, -1.29],  # Rear left leg
               [-0.20, 0.7, -1.29]]  # Rear right leg

lap_spread_left = [[1.20, 0.7, -1.39],  # Front left leg
                   [0.20, 0.7, -1.39],  # Front right leg
                   [1.20, 0.7, -1.39],  # Rear left leg
                   [0.20, 0.7, -1.39]]  # Rear right leg


def myhook():
    # Execute on shutdown.
    pass


if __name__ == '__main__':
    try:
        # sit down
        time.sleep(2.1)
        motors_target_pos = sit_down
        talker()
        rate.sleep()
        # stand up
        time.sleep(2.1)
        motors_target_pos = stand_up
        talker()
        rate.sleep()
        # sit down
        time.sleep(2.1)
        motors_target_pos = sit_down
        talker()
        rate.sleep()
        # stand up
        time.sleep(2.1)
        motors_target_pos = stand_up
        talker()
        rate.sleep()
        # lap_spread
        time.sleep(2.1)
        motors_target_pos = lap_spread
        talker()
        rate.sleep()
        # stand up
        time.sleep(2.1)
        motors_target_pos = stand_up
        talker()
        rate.sleep()
        # front left lap up
        time.sleep(2.1)
        motors_target_pos = fl_lap
        talker()
        rate.sleep()
        # stand up
        time.sleep(0.8)
        motors_target_pos = stand_up
        talker()
        rate.sleep()
        # front right lap up
        time.sleep(0.8)
        motors_target_pos = fr_lap
        talker()
        rate.sleep()
        # stand up
        time.sleep(0.8)
        motors_target_pos = stand_up
        talker()
        rate.sleep()
        # bow forward
        time.sleep(1.8)
        motors_target_pos = bow_forward
        talker()
        rate.sleep()
        # stand up
        time.sleep(1.8)
        motors_target_pos = stand_up
        talker()
        rate.sleep()
        #  lap_spread_left
        time.sleep(1.8)
        motors_target_pos = lap_spread_left
        talker()
        rate.sleep()
        # sit down
        time.sleep(2.1)
        motors_target_pos = sit_down
        talker()
        rate.sleep()
        # give a paw
        time.sleep(1.8)
        motors_target_pos = give_paw
        talker()
        rate.sleep()
        # sit down
        time.sleep(7.1)
        motors_target_pos = sit_down
        talker()
        rate.sleep()

        rospy.on_shutdown(myhook)
    except rospy.ROSInterruptException:
        pass

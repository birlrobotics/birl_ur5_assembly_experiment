#!/usr/bin/env python
import ipdb
import sys
import rospy
import moveit_commander as mc
from birl_ur5_assembly_experiment.moveit_vars_getter import get_moveit_vars
from birl_ur5_assembly_experiment import hardcoded_data as hd
import ipdb

camera_detection_angle = {'elbow_joint': 1.4735589027404785, 'shoulder_pan_joint': 1.986021637916565, 'wrist_3_joint': -1.2961767355548304, 
'wrist_1_joint': -0.7861869970904749, 'shoulder_lift_joint': -3.154273335133688, 'wrist_2_joint': -1.7274764219867151}

natrual_jointAngle =  {'elbow_joint': 1.401339054107666, 'shoulder_pan_joint': 1.9879260063171387, 'wrist_3_joint': -1.2952893416034144, 'wrist_1_joint': -1.147008244191305, 
'shoulder_lift_joint': -2.194500748311178, 'wrist_2_joint': -1.7298420111285608}
if __name__ == '__main__':
    mc.roscpp_initialize(sys.argv) 
    rospy.init_node("ur_move_angle", anonymous=True)

    robot = mc.RobotCommander()
    group = mc.MoveGroupCommander("manipulator")
    group.set_max_velocity_scaling_factor(0.01)
    group.set_max_acceleration_scaling_factor(0.01)
    group.set_goal_joint_tolerance(0.001)
    group.set_goal_position_tolerance(0.001)
    group.set_goal_orientation_tolerance(0.001)
    rospy.sleep(1)

    group.set_joint_value_target(natrual_jointAngle)
    plan = group.plan()
    ipdb.set_trace()
    rospy.sleep(1)
    group.execute(plan)
    if not group.execute(plan):
        raise Exception("exec failed")

    rospy.sleep(1)
    mc.roscpp_shutdown()

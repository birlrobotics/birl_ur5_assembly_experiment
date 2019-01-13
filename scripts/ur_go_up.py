#!/usr/bin/env python
import ipdb
import sys
import rospy
import moveit_commander as mc
from birl_ur5_assembly_experiment.moveit_vars_getter import get_moveit_vars
from birl_ur5_assembly_experiment import hardcoded_data as hd

if __name__ == '__main__':
    mc.roscpp_initialize(sys.argv) 
    rospy.init_node("ur_go_home", anonymous=True)

    robot = mc.RobotCommander()
    group = mc.MoveGroupCommander("manipulator")
    group.set_max_velocity_scaling_factor(1)
    group.set_max_acceleration_scaling_factor(1)
    group.set_goal_joint_tolerance(0.001)
    group.set_goal_position_tolerance(0.001)
    group.set_goal_orientation_tolerance(0.001)
    rospy.sleep(1)

    cur_jointAngle = group.get_current_joint_values()
    group.set_joint_value_target(cur_jointAngle)
    plan = group.plan()
    group.execute(plan)
    
    group.set_joint_value_target(hd.up)
    plan = group.plan()
    rospy.sleep(1)
    group.execute(plan)
    if not group.execute(plan):
        raise Exception("exec failed")

    rospy.sleep(1)
    mc.roscpp_shutdown()

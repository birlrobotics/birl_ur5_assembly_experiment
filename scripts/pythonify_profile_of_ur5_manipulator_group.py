#!/usr/bin/env python
import ipdb
import sys
import rospy
import moveit_commander as mc

from geometry_msgs.msg import Point, Quaternion

if __name__ == '__main__':
    mc.roscpp_initialize(sys.argv) 
    rospy.init_node("ur5_moveit_test", anonymous=True, log_level=rospy.WARN)
    robot = mc.RobotCommander()

    move_group = robot.get_group("manipulator")

    current_joint_dict = dict(zip(
        move_group.get_active_joints(),
        move_group.get_current_joint_values()))

    print current_joint_dict

    current_pose = move_group.get_current_pose().pose
    print "Pose(position=Point(%s), orientation=Quaternion(%s))"%(str(current_pose.position).replace(':', '=').replace('\n', ','), str(current_pose.orientation).replace(':', '=').replace('\n', ','))

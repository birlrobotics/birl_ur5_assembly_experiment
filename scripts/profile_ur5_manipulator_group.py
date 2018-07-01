#!/usr/bin/env python
import ipdb
import sys
import rospy
import moveit_commander as mc

if __name__ == '__main__':
    mc.roscpp_initialize(sys.argv) 
    rospy.init_node("ur5_moveit_test", anonymous=True)
    robot = mc.RobotCommander()

    move_group = robot.get_group("manipulator")

    for attr in dir(move_group):
        if attr.startswith("get_"):
            rospy.loginfo("*"*20)
            rospy.loginfo(attr)
            try:
                rospy.loginfo(getattr(move_group, attr)())
            except:
                rospy.logerr("Failed to call")

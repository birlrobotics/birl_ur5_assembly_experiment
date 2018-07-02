#!/usr/bin/env python
import sys
import rospy
import moveit_commander as mc

if __name__ == '__main__':
    mc.roscpp_initialize(sys.argv) 
    rospy.init_node("profile_ur5", anonymous=True)

    robot = mc.RobotCommander()
    for attr in dir(robot):
        if attr.startswith("get_"):
            rospy.loginfo("*"*20)
            rospy.loginfo(attr)
            try:
                rospy.loginfo(getattr(robot, attr)())
            except:
                rospy.logerr("Failed to call")
    
    

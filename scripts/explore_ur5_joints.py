#!/usr/bin/env python
import sys
import rospy
import moveit_commander as mc
import pprint
from math import pi

if __name__ == '__main__':
    mc.roscpp_initialize(sys.argv) 
    rospy.init_node("explore_ur5_joints", anonymous=True)
    robot = mc.RobotCommander()
    move_group = robot.get_group("manipulator")

    mapping = ['q', 'w', 'e', 'r', 't', 'y']
    jnames = move_group.get_active_joints()

    pp = pprint.PrettyPrinter(indent=4)
    while not rospy.is_shutdown():
        pp.pprint(zip(jnames, [j*180/pi for j in move_group.get_current_joint_values()]))

        i = raw_input()
        try:
            idx = mapping.index(i.lower())
        except ValueError:
            print 'invalid input'
            continue
            
        vals = move_group.get_current_joint_values()
        if i.islower():
            vals[idx] -= pi/18.0
        else:
            vals[idx] += pi/18.0

        if vals[idx] < -pi:
            vals[idx] += 2*pi
        elif vals[idx] > pi:
            vals[idx] -= 2*pi
        move_group.set_joint_value_target(vals)
        move_group.go()
                        







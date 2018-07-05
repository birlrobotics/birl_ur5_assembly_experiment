import moveit_commander 
from moveit_msgs.msg import Constraints, JointConstraint
import hardcoded_data as hd
from math import pi
import numpy as np

def get_constraints():
    c = Constraints(name="ur5_constraint_for_assembly_experiment")
    c.joint_constraints = []
    for joint_name, angle_range in hd.joint_constraints_in_degrees.iteritems():
        jc = JointConstraint()
        jc.joint_name = joint_name
        lower_bound, upper_bound = np.array(angle_range)*pi/180
        jc.position = (lower_bound+upper_bound)/2
        jc.tolerance_above = upper_bound-jc.position
        jc.tolerance_below = jc.position-lower_bound
        jc.weight=1.0
        c.joint_constraints.append(jc)
    return c

def get_moveit_vars():
    robot = moveit_commander.RobotCommander()
    group = moveit_commander.MoveGroupCommander("manipulator")
    group.set_max_velocity_scaling_factor(1)
    group.set_max_acceleration_scaling_factor(1)
    group.set_goal_joint_tolerance(0.001)
    group.set_goal_position_tolerance(0.001)
    group.set_goal_orientation_tolerance(0.001)
    group.set_path_constraints(get_constraints())
    group.set_planning_time(10)
    group.set_num_planning_attempts(100)
    return robot, group

import moveit_commander 

def get_moveit_vars():
    if not hasattr(get_moveit_vars, 'robot'):
        robot = moveit_commander.RobotCommander()
        group = moveit_commander.MoveGroupCommander("manipulator")
        group.set_max_velocity_scaling_factor(0.01)
        group.set_max_acceleration_scaling_factor(0.01)
        group.set_goal_joint_tolerance(0.001)
        group.set_goal_position_tolerance(0.001)
        group.set_goal_orientation_tolerance(0.001)
        get_moveit_vars.robot = robot
        get_moveit_vars.group = group
    get_moveit_vars.group.clear_pose_targets()
    return get_moveit_vars.robot, get_moveit_vars.group

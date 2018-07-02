import moveit_commander 

def get_moveit_vars():
    if not hasattr(get_moveit_vars, 'robot'):
        robot = moveit_commander.RobotCommander()
        group = moveit_commander.MoveGroupCommander("manipulator")
        group.set_max_velocity_scaling_factor(0.1)
        group.set_max_acceleration_scaling_factor(0.1)
        get_moveit_vars.robot = robot
        get_moveit_vars.group = group
    get_moveit_vars.group.clear_pose_targets()
    return get_moveit_vars.robot, get_moveit_vars.group

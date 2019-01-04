# birl_ur5_assembly_experiment

## To Run The Experiment

1. launch UR5 and moveit

```
roslaunch ur_gazebo ur5.launch
roslaunch ur5_moveit_config ur5_moveit_planning_execution.launch  sim:=true
roslaunch ur5_moveit_config moveit_rviz.launch config:=true
```
1. Set up moveit planning scene such that the robot won't hit the desk:
```bash
rosrun birl_ur5_assembly_experiment setup_experiment_planning_scene.py
```

1. run the experiment:
```bash
rosrun birl_ur5_assembly_experiment experiment_runner.py
```

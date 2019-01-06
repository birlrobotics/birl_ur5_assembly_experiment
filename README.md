# birl_ur5_assembly_experiment

## To Run The Experiment

1.launch UR5 in gazebo 
```
roslaunch ur_gazebo ur5.launch
roslaunch ur5_moveit_config ur5_moveit_planning_execution.launch  sim:=true
```
Or launch real UR5 robot
```
roslaunch ur_bringup ur5_bringup.launch robot_ip:=192.168.1.102
roslaunch ur5_moveit_config ur5_moveit_planning_execution.launch  
``` 
Noted : You may need to move robot to zero pose manuly.

2.launch Rviz
```
roslaunch ur5_moveit_config moveit_rviz.launch config:=true
```
3.Set up moveit planning scene such that the robot won't hit the desk:
```bash
rosrun birl_ur5_assembly_experiment setup_experiment_planning_scene.py
```

4.run the experiment:
```bash
rosrun birl_ur5_assembly_experiment experiment_runner.py
```
Shutdown `roslaunch ur_bringup ur5_bringup.launch robot_ip:=192.168.1.102` if you want to make robot move to other pose by teaching box
# birl_ur5_assembly_experiment

## To Run The Experiment

1. launch UR5 and moveit

1. Set up moveit planning scene such that the robot won't hit the desk:
```bash
rosrun birl_ur5_assembly_experiment setup_experiment_planning_scene.py
```

1. run the experiment:
```bash
rosrun birl_ur5_assembly_experiment experiment_runner.py
```

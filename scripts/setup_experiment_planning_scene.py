#!/usr/bin/env python
import ipdb
import sys
import rospy
import moveit_commander as mc
from geometry_msgs.msg import PoseStamped, Pose, Point, Quaternion
from std_msgs.msg import Header
import itertools
import numpy as np

from birl_ur5_assembly_experiment import hardcoded_data as hd
from tf.transformations import (
    quaternion_from_matrix,
)
import ipdb

def create_wall_by_box(wall_points, robot, psi, name):
    if len(wall_points) != 3:
        raise Exception("create_wall_by_box takes 3 wall points")
    vectors = np.array([np.array([i.x, i.y, i.z]) for i in wall_points])
    vector_a = vectors[1]-vectors[0]
    vector_b = vectors[2]-vectors[0]
    vector_n = np.cross(vector_a, vector_b)

    new_z_axis = vector_n
    new_z_axis /= np.linalg.norm(new_z_axis)
    new_x_axis = vector_a
    new_x_axis /= np.linalg.norm(new_x_axis)
    new_y_axis = np.cross(new_z_axis, new_x_axis)
    
    mat = np.zeros((4,4))
    mat[:3, 0] = new_x_axis
    mat[:3, 1] = new_y_axis
    mat[:3, 2] = new_z_axis
    mat[3, 3] = 1

    pos = vectors.mean(axis=0)
    quat = quaternion_from_matrix(mat)
    
    psi.add_sphere(
        name="%s_center"%name, 
        pose=PoseStamped(
            header=Header(frame_id=robot.get_planning_frame()),
            pose=Pose(position=Point(*pos), orientation=Quaternion(x=0, y=0, z=0, w=1))),
        radius=0.05)
    
    psi.add_box(
        name=name, 
        pose=PoseStamped(
            header=Header(frame_id=robot.get_planning_frame()),
            pose=Pose(position=Point(*pos), orientation=Quaternion(*quat))),
        size=(2, 2, 0.01))

if __name__ == '__main__':
    mc.roscpp_initialize(sys.argv) 
    rospy.init_node("setup_experiment_planning_scene", anonymous=True)
    robot = mc.RobotCommander()
    psi = mc.PlanningSceneInterface()
    rospy.sleep(1)

    psi.remove_world_object()

    desk_length = 2
    desk_width = 2
    desk_height = 1

    psi.add_box(
        name="the_desk", 
        pose=PoseStamped(
            header=Header(frame_id=robot.get_planning_frame()),
            pose=Pose(position=Point(x=0, y=0 ,z=-desk_height/2.0-0.01), orientation=Quaternion(x=0, y=0, z=0, w=1))),
        size=(desk_length, desk_width, desk_height))

    for count, wall_pose in enumerate(itertools.chain(hd.left_wall_poses, hd.right_wall_poses)):
        psi.add_sphere(
            name="wall_pose_%s"%count, 
            pose=PoseStamped(
                header=Header(frame_id=robot.get_planning_frame()),
                pose=Pose(position=wall_pose.position, orientation=Quaternion(x=0, y=0, z=0, w=1))),
            radius=0.05)

    create_wall_by_box([i.position for i in hd.left_wall_poses], robot, psi, name='left_wall_box') 
    create_wall_by_box([i.position for i in hd.right_wall_poses], robot, psi, name='right_wall_box') 

    rospy.sleep(1)
    rospy.loginfo(psi.get_known_object_names())
    mc.roscpp_shutdown()

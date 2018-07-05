import smach
from geometry_msgs.msg import (
    Pose,
    Quaternion,
)
import copy
import random
from tf.transformations import (
    translation_matrix,
    quaternion_matrix,
)
import baxter_interface
import numpy
import os
import hardcoded_data
import dill
from ar_track_alvar_msgs.msg import AlvarMarkers
import rospy
from baxter_core_msgs.msg import (
    EndpointState,
)
import tf
import moveit_commander as mc

SIM_MODE = True
pick_hover_height = 0.05
place_hover_height = 0.05

class MoveToHomePose(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['Successful'])
        self.state_no = 0 # Skill tag
        self.depend_on_prev_state = False # Set this flag accordingly

    def get_joint_state_goal(self):
        return copy.deepcopy(hardcoded_data.home_joint_angles)

    def determine_successor(self): # Determine next state
        return 'Successful'


class DeterminePickPose(smach.State):
    pick_pose = None
    already_pick_count = 0
    def __init__(self):
        smach.State.__init__(self, outcomes=['GotOneFromVision', 'VisionSaysNone'])
        self.state_no = 0 # Skill tag
        self.depend_on_prev_state = False # Set this flag accordingly

    def get_joint_state_goal(self):
        return copy.deepcopy(hardcoded_data.get_vision_joint_angles)

    def determine_successor(self): # Determine next state
        if not SIM_MODE:
            # TODO: get pose from Shili's vision system
            raise Exception("TODO: get pose from Shili's vision system")
        else:
            DeterminePickPose.pick_pose = copy.deepcopy(hardcoded_data.ram_fixed_pick_pose)
        return 'GotOneFromVision'

class MoveToPrePickPoseWithEmptyHand(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['Successful'])
        self.state_no = 3 # Skill tag
        self.depend_on_prev_state = True # Set this flag accordingly


    def get_pose_goal(self):
        pose = copy.deepcopy(DeterminePickPose.pick_pose)
        pos = pose.position
        ori = pose.orientation
        base_to_pose_mat = numpy.dot(translation_matrix((pos.x, pos.y, pos.z)), quaternion_matrix((ori.x, ori.y, ori.z, ori.w)))
        pose.position.x -= pick_hover_height*base_to_pose_mat[0, 0]
        pose.position.y -= pick_hover_height*base_to_pose_mat[1, 0]
        pose.position.z -= pick_hover_height*base_to_pose_mat[2, 0]
        return pose

    def determine_successor(self): # Determine next state
        return 'Successful'

class Pick(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['Successful'])
        self.state_no = 4 # Skill tag
        self.depend_on_prev_state = True # Set this flag accordingly

    def before_motion(self):
        # TODO: need API for gripper and sucker
        pass

    def after_motion(self):
        # TODO: need API for gripper and sucker
        pass

    def get_pose_goal(self):
        pose = copy.deepcopy(DeterminePickPose.pick_pose)
        return pose

    def determine_successor(self): # Determine next state
        return 'Successful'

class MoveToPrePickPoseWithFullHand(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['Successful'])
        self.state_no = 5 # Skill tag
        self.depend_on_prev_state = True # Set this flag accordingly

    def get_pose_goal(self):
        robot = mc.RobotCommander()
        move_group = robot.get_group("manipulator")
        pose = move_group.get_current_pose().pose
        pos = [pose.position.x, pose.position.y, pose.position.z]
        ori = [pose.orientation.x, pose.orientation.y, pose.orientation.z, pose.orientation.w]
        listener = tf.TransformListener()
        base_to_pose_mat = listener.fromTranslationRotation(pos, ori) 
        pose.position.x -= pick_hover_height*base_to_pose_mat[0, 0]
        pose.position.y -= pick_hover_height*base_to_pose_mat[1, 0]
        pose.position.z -= pick_hover_height*base_to_pose_mat[2, 0]
        return pose

    def determine_successor(self): # Determine next state
        return 'Successful'

class DeterminePlacePose(smach.State):
    place_pose = None
    already_plac_count = 0
    def __init__(self):
        smach.State.__init__(self, outcomes=['Successful'])
        self.state_no = 0 # Skill tag
        self.depend_on_prev_state = False # Set this flag accordingly

    def determine_successor(self): # Determine next state
        DeterminePlacePose.place_pose = copy.deepcopy(hardcoded_data.ram_fixed_place_pose)
        return 'Successful'

class MoveToPrePlacePoseWithFullHand(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['Successful'])
        self.state_no = 7 # Skill tag
        self.depend_on_prev_state = True # Set this flag accordingly


    def get_pose_goal(self):
        pose = copy.deepcopy(DeterminePlacePose.place_pose)
        pos = pose.position
        ori = pose.orientation
        base_to_pose_mat = numpy.dot(translation_matrix((pos.x, pos.y, pos.z)), quaternion_matrix((ori.x, ori.y, ori.z, ori.w)))
        pose.position.x -= place_hover_height*base_to_pose_mat[0, 0]
        pose.position.y -= place_hover_height*base_to_pose_mat[1, 0]
        pose.position.z -= place_hover_height*base_to_pose_mat[2, 0]
        return pose

    def determine_successor(self): # Determine next state
        return 'Successful'

class Place(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['Successful'])
        self.state_no = 8 # Skill tag
        self.depend_on_prev_state = True # Set this flag accordingly

    def after_motion(self):
        # TODO: need API for gripper and sucker
        pass


    def get_pose_goal(self):
        robot = mc.RobotCommander()
        move_group = robot.get_group("manipulator")
        pose = move_group.get_current_pose().pose
        pos = [pose.position.x, pose.position.y, pose.position.z]
        ori = [pose.orientation.x, pose.orientation.y, pose.orientation.z, pose.orientation.w]
        listener = tf.TransformListener()
        base_to_pose_mat = listener.fromTranslationRotation(pos, ori) 
        pose.position.x += (place_hover_height)*base_to_pose_mat[0, 0]
        pose.position.y += (place_hover_height)*base_to_pose_mat[1, 0]
        pose.position.z += (place_hover_height)*base_to_pose_mat[2, 0]
        return pose

    def determine_successor(self): # Determine next state
        DeterminePlacePose.already_plac_count += 1
        return 'Successful'

class MoveToPrePlacePoseWithEmptyHand(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['Successful'])
        self.state_no = 9 # Skill tag
        self.depend_on_prev_state = True # Set this flag accordingly

    def get_pose_goal(self):
        robot = mc.RobotCommander()
        move_group = robot.get_group("manipulator")
        pose = move_group.get_current_pose().pose
        pos = [pose.position.x, pose.position.y, pose.position.z]
        ori = [pose.orientation.x, pose.orientation.y, pose.orientation.z, pose.orientation.w]
        listener = tf.TransformListener()
        base_to_pose_mat = listener.fromTranslationRotation(pos, ori) 
        pose.position.x -= (place_hover_height)*base_to_pose_mat[0, 0]
        pose.position.y -= (place_hover_height)*base_to_pose_mat[1, 0]
        pose.position.z -= (place_hover_height)*base_to_pose_mat[2, 0]
        return pose

    def determine_successor(self): # Determine next state
        return 'Successful'

def assembly_user_defined_sm():  # interface
    sm = smach.StateMachine(outcomes=['TaskFailed', 'TaskSuccessful'])
    with sm:
        smach.StateMachine.add(
            MoveToHomePose.__name__,
            MoveToHomePose(),
            transitions={
                'Successful': DeterminePickPose.__name__
            }
        )
        smach.StateMachine.add(
            DeterminePickPose.__name__,
            DeterminePickPose(),
            transitions={
                'GotOneFromVision': MoveToPrePickPoseWithEmptyHand.__name__,
                'VisionSaysNone': 'TaskSuccessful',
            }
        )
        smach.StateMachine.add(
            MoveToPrePickPoseWithEmptyHand.__name__,
            MoveToPrePickPoseWithEmptyHand(),
            transitions={
                'Successful': Pick.__name__
            }
        )
        smach.StateMachine.add(
            Pick.__name__,
            Pick(),
            transitions={
                'Successful': MoveToPrePickPoseWithFullHand.__name__
            }
        )
        smach.StateMachine.add(
            MoveToPrePickPoseWithFullHand.__name__,
            MoveToPrePickPoseWithFullHand(),
            transitions={
                'Successful': DeterminePlacePose.__name__
            }
        )
        smach.StateMachine.add(
            DeterminePlacePose.__name__,
            DeterminePlacePose(),
            transitions={
                'Successful': MoveToPrePlacePoseWithFullHand.__name__
            }
        )
        smach.StateMachine.add(
            MoveToPrePlacePoseWithFullHand.__name__,
            MoveToPrePlacePoseWithFullHand(),
            transitions={
                'Successful': Place.__name__
            }
        )
        smach.StateMachine.add(
            Place.__name__,
            Place(),
            transitions={
                'Successful': MoveToPrePlacePoseWithEmptyHand.__name__
            }
        )
        smach.StateMachine.add(
            MoveToPrePlacePoseWithEmptyHand.__name__,
            MoveToPrePlacePoseWithEmptyHand(),
            transitions={
                'Successful': MoveToHomePose.__name__
            }
        )
    return sm

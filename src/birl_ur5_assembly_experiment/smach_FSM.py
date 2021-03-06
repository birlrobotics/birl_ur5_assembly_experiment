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
from linemod_pose_estimation.srv import linemod_pose,linemod_poseRequest
from birl_ur5_assembly_experiment.srv import ur_gripper, ur_gripperRequest,ur_gripperResponse
from geometry_msgs.msg import Pose

SIM_MODE = True
pick_hover_height = 0.05
place_hover_height = 0.05

class MoveToHomePose(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['Successful'])
        self.state_no = 0 # Skill tag
        self.depend_on_prev_state = False # Set this flag accordingly

    def get_joint_state_goal(self):
        return copy.deepcopy(hardcoded_data.natural_jointAngle)

    def determine_successor(self): # Determine next state
        return 'Successful'


class DeterminePickPose(smach.State):
    pick_pose = None
    already_pick_count = 0
    def __init__(self):
        smach.State.__init__(self, outcomes=['GotOneFromVision', 'VisionSaysNone'])
        self.state_no = 0 # Skill tag
        self.depend_on_prev_state = False # Set this flag accordingly
        self.visited = False

    def get_joint_state_goal(self):
        return copy.deepcopy(hardcoded_data.camera_detection_jointAngle)

    # def determine_successor(self): # Determine next state
    #     if not SIM_MODE:
    #         rospy.wait_for_service('linemod_object_pose')
    #         try:
    #             req = linemod_poseRequest()
    #             req.object_id = 0
    #             client = rospy.ServiceProxy('linemod_object_pose', linemod_pose)
    #             resp = client(req)
    #             tmp = Pose()
    #             tmp.position = resp.transition
    #             tmp.orientation = resp.rotation
    #             DeterminePickPose.pick_pose = tmp

    #         # raise Exception("TODO: get pose from Shili's vision system")
    #     else:
    #         if self.visited:
    #             return "VisionSaysNone"            
    #         DeterminePickPose.pick_pose = copy.deepcopy(hardcoded_data.ram_fixed_pick_pose)
    #         self.visited = True
    #     return 'GotOneFromVision'
    def determine_successor(self): # Determine next state
        return 'GotOneFromVision'

class MoveToPrePickPoseWithEmptyHand(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['Successful'])
        self.state_no = 3 # Skill tag
        self.depend_on_prev_state = True # Set this flag accordingly


    def get_joint_state_goal(self):
        return copy.deepcopy(hardcoded_data.prepick_jointAngle)

    
    def determine_successor(self): # Determine next state
        return 'Successful'

class Pick(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['Successful'])
        self.state_no = 4 # Skill tag
        self.depend_on_prev_state = True # Set this flag accordingly

    def before_motion(self):
        # rospy.wait_for_service('ur_gripper_switch',timeout=3)
        # try:
        #     req = ur_gripperRequest()
        #     req.state = "open"
        #     client = rospy.ServiceProxy('ur_gripper_switch', ur_gripper)
        #     res = client(req)
        # except rospy.ServiceException, e:
        #     rospy.loginfo("Service call failed: %s"%e)
        pass
    def after_motion(self):
        # try:
        #     req = ur_gripperRequest()
        #     req.state = "close"
        #     client = rospy.ServiceProxy('ur_gripper_switch', ur_gripper)
        #     res = client(req)
        # except rospy.ServiceException, e:
        #     rospy.loginfo("Service call failed: %s"%e)
        pass

    def get_joint_state_goal(self):
        return copy.deepcopy(hardcoded_data.pick_jointAngle)

    def determine_successor(self): # Determine next state
        return 'Successful'

class MoveToPrePickPoseWithFullHand(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['Successful'])
        self.state_no = 5 # Skill tag
        self.depend_on_prev_state = True # Set this flag accordingly


    def get_joint_state_goal(self):
        return copy.deepcopy(hardcoded_data.prepick_jointAngle)

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
        # DeterminePlacePose.place_pose = copy.deepcopy(hardcoded_data.ram_fixed_place_pose)
        return 'Successful'

class MoveToPrePlacePoseWithFullHand(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['Successful'])
        self.state_no = 7 # Skill tag
        self.depend_on_prev_state = True # Set this flag accordingly

    def get_joint_state_goal(self):
        return copy.deepcopy(hardcoded_data.preplace_jointAngle)

    def determine_successor(self): # Determine next state
        return 'Successful'

class Place(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['Successful'])
        self.state_no = 8 # Skill tag
        self.depend_on_prev_state = True # Set this flag accordingly

    def after_motion(self):
        # try:
        #     req = ur_gripperRequest()
        #     req.state = "close"
        #     client = rospy.ServiceProxy('ur_gripper_switch', ur_gripper)
        #     res = client(req)
        # except rospy.ServiceException, e:
        #     rospy.loginfo("Service call failed: %s"%e)
        pass


    def get_joint_state_goal(self):
        return copy.deepcopy(hardcoded_data.place_jointAngle)

    def determine_successor(self): # Determine next state
        DeterminePlacePose.already_plac_count += 1
        return 'Successful'

class MoveToPrePlacePoseWithEmptyHand(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['Successful'])
        self.state_no = 9 # Skill tag
        self.depend_on_prev_state = True # Set this flag accordingly

    def get_joint_state_goal(self):
        return copy.deepcopy(hardcoded_data.preplace_jointAngle)

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
                'Successful': "TaskSuccessful"
            }
        )
        
    return sm

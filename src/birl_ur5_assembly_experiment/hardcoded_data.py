from geometry_msgs.msg import Pose, Point, Quaternion
from math import pi


camera_detection_jointAngle = {'elbow_joint': 1.4735589027404785, 'shoulder_pan_joint': 1.986021637916565, 'wrist_3_joint': -1.2961767355548304, 
'wrist_1_joint': -0.7861869970904749, 'shoulder_lift_joint': -3.154273335133688, 'wrist_2_joint': -1.7274764219867151}

natural_jointAngle={'elbow_joint': 1.401339054107666, 'shoulder_pan_joint': 1.9879260063171387, 'wrist_3_joint': -1.2952893416034144, 
'wrist_1_joint': -1.147008244191305, 'shoulder_lift_joint': -2.194500748311178, 'wrist_2_joint': -1.7298420111285608}

prepick_jointAngle ={'elbow_joint': 1.2553682327270508, 'shoulder_pan_joint': 1.358418345451355, 'wrist_3_joint': -1.9963386694537562, 
'wrist_1_joint': -1.4977968374835413, 'shoulder_lift_joint': -1.4115403334247034, 'wrist_2_joint': -1.5743301550494593}

pick_jointAngle = {'elbow_joint': 1.8152494430541992, 'shoulder_pan_joint': 1.3587898015975952, 'wrist_3_joint': -1.9990957419024866, 
'wrist_1_joint': -2.1557844320880335, 'shoulder_lift_joint': -1.3135893980609339, 'wrist_2_joint': -1.5732248465167444}

preplace_jointAngle = {'elbow_joint': 1.2688817977905273, 'shoulder_pan_joint': 2.579735279083252, 'wrist_3_joint': -1.996518913899557, 
'wrist_1_joint': -1.5229499975787562, 'shoulder_lift_joint': -1.4303253332721155, 'wrist_2_joint': -1.5743182341205042}    

place_jointAngle =  {'elbow_joint': 1.811680793762207, 'shoulder_pan_joint': 2.5800344944000244, 'wrist_3_joint': -1.9991076628314417, 'wrist_1_joint': 
-2.14612847963442, 'shoulder_lift_joint': -1.3499401251422327, 'wrist_2_joint': -1.5731647650348108}


joint_constraints_in_degrees = {
    'shoulder_pan_joint': [-34, 75],
    'shoulder_lift_joint': [-180, 0],
    'wrist_1_joint': [-170, 30],
    'wrist_2_joint': [-170, 30],
    'wrist_3_joint': [-170, 30],
}

right_wall_poses = [
    Pose(position=Point(x= 0.261466174855,y= -0.352523708217,z= 0.705580090699), orientation=Quaternion(x= -0.468208155841,y= 0.581463598906,z= -0.253221279465,w= 0.615272451502)),
    Pose(position=Point(x= 0.248320374588,y= -0.32307574581,z= 0.179985276188), orientation=Quaternion(x= -0.163624397477,y= 0.746900729607,z= 0.156404685627,w= 0.625223104961)),
    Pose(position=Point(x= -0.161260947705,y= -0.273250990411,z= 0.373660272948), orientation=Quaternion(x= 0.132117547513,y= 0.751514168005,z= -0.426908028184,w= 0.485305001416))
]

left_wall_poses = [
    Pose(position=Point(x= -0.0988705763476,y= 0.441884948257,z= 0.603585248101), orientation=Quaternion(x= -0.693678772302,y= -0.292968972292,z= 0.576449733663,w= 0.317308440939)),
    Pose(position=Point(x= -0.163826175967,y= 0.391609718364,z= 0.189631264426), orientation=Quaternion(x= 0.760179978253,y= 0.0883535819475,z= -0.64132964895,w= 0.0549210942937)),
    Pose(position=Point(x= -0.388096786355,y= -0.047544683807,z= 0.41309866761), orientation=Quaternion(x= 0.428966635257,y= 0.630761219358,z= -0.592143774984,w= 0.259795419007))
]

opposite_wall_poses = [
    Pose(position=Point(x= 0.568168299346,y= 0.0872185385521,z= 0.198386013786), orientation=Quaternion(x= -0.581156107492,y= 0.404107407163,z= 0.376752910086,w= 0.597504834242)),
    Pose(position=Point(x= 0.393995670991,y= 0.27672218165,z= 0.234357276234), orientation=Quaternion(x= -0.684419435769,y= 0.177711164359,z= 0.417256640218,w= 0.570863971712)),
    Pose(position=Point(x= 0.26104379437,y= 0.380654784911,z= 0.112153163096), orientation=Quaternion(x= -0.704658072095,y= 0.0590960947465,z= 0.511240137914,w= 0.488465120969)),
]

reverting_statistics = {
    'MoveToPrePickPoseWithEmptyHand': {
        "human_collision":{'MoveToPrePickPoseWithEmptyHand':25},
                                      },
    'Pick': {
        "tool_collision": {
            'MoveToPrePickPoseWithEmptyHand': 25,

        },
       "human_collision": {
            'Pick': 25,
        },
    },
    'MoveToPrePickPoseWithFullHand': {
       "human_collision": {
            'MoveToPrePickPoseWithFullHand': 25,
        },
       "object_slip": {
            'Pick': 20,
            "MoveToPrePickPoseWithEmptyHand":5,
        },
       "no_object": {
            'Pick': 24,
            'MoveToPrePickPoseWithEmptyHand': 1,
        },
    },
    'MoveToPrePlacePoseWithFullHand': {
        "object_slip": {
            'MoveToPrePickPoseWithEmptyHand': 25,                  
        },
        "human_collision":{
            'MoveToPrePlacePoseWithFullHand':25,
        },
    },
    'Place': {
        "human_collision": {
           'Place': 25,
        },
    },
}

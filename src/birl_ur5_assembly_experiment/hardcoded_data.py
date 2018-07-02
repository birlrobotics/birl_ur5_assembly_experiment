from geometry_msgs.msg import Pose, Point, Quaternion
from math import pi

home_pose = Pose(position=Point(x= 0.347374056271,y= 0.0670839656857,z= 0.575880001466), orientation=Quaternion(x= -0.662637229064,y= 0.381435720055,z= 0.221088127146,w= 0.605424424813))

ram_fixed_pick_pose = Pose(position=Point(x= 0.619046842606,y= -0.0205555205994,z= 0.240680352798), orientation=Quaternion(x= -0.34275951009,y= 0.642476859947,z= 0.538301547718,w= 0.424229709473))

ram_fixed_place_pose = Pose(position=Point(x= 0.483291959469,y= 0.446571937473,z= 0.222983235428), orientation=Quaternion(x= -0.588390371948,y= 0.253616641848,z= 0.72821750823,w= 0.243258360357))


joint_constraints = {
    'shoulder_pan_joint': [-0.351181623229599, 1.0153117727366767],
    'shoulder_lift_joint': [-0.577527257376092, -1.3108943839533242],
    'elbow_joint': [0.09208634954657935, 1.5860923139572094],
    'wrist_1_joint': [-2.8567755644687973, -0.7243984587961108],
    'wrist_2_joint': [-pi/2, -pi/2],
    'wrist_3_joint': [-pi/2, -pi/2],
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

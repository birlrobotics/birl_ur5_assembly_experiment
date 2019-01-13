from geometry_msgs.msg import Pose, Point, Quaternion
from math import pi

up = {'elbow_joint': -4.2617535722655475e-07, 'shoulder_pan_joint': -0.00010364929556594404, 'wrist_3_joint': 2.7088180305057108e-05, 'wrist_1_joint': -1.570700020101965, 'shoulder_lift_joint': -1.5707001159590872, 'wrist_2_joint': 4.447031563525883e-05}
home_joint_angles = {'elbow_joint': -0.7103890179035215, 'shoulder_pan_joint': 2.5046971609102187, 'wrist_3_joint': -1.2904286064346557, 'wrist_1_joint': -0.3825551937260574, 'shoulder_lift_joint': -2.230709533847964, 'wrist_2_joint': 1.7475283280977791}

get_vision_joint_angles = {'elbow_joint': 1.5563100940033436, 'shoulder_pan_joint': 1.599943325303202, 'wrist_3_joint': 4.760734600664932, 'wrist_1_joint': -0.9086184085882479, 'shoulder_lift_joint': -3.30565360327726, 'wrist_2_joint': -1.6620770466742}

ram_fix_prepick_joint_angles = {'elbow_joint': 0.15501022338867188, 'shoulder_pan_joint': 1.6229989528656006, 'wrist_3_joint': -1.9266837278949183, 'wrist_1_joint': -1.0626185576068323, 'shoulder_lift_joint': -0.7709811369525355, 'wrist_2_joint': -1.5327757040606897}

ram_fix_place_joint_angles = {'elbow_joint': 1.206188678741455, 'shoulder_pan_joint': 2.406372547149658, 'wrist_3_joint': -2.029276672993795, 'wrist_1_joint': -1.7258947531329554, 'shoulder_lift_joint': -0.9697883764850062, 'wrist_2_joint': -1.561734978352682}

# ram_fix_preplace_joint_angles = {'elbow_joint': 0.6660176425610361, 'shoulder_pan_joint': 2.423040600543728, 'wrist_3_joint': 4.326671215693943, 'wrist_1_joint': -1.2110839679588652, 'shoulder_lift_joint': -1.0196213490150872, 'wrist_2_joint': -1.5828390986336576}

ram_fixed_pick_pose = Pose(position=Point(x = -0.138408301693, y= 0.435841054208 , z=0.372693844976), orientation=Quaternion(x = -0.977445487723, y= -0.20332695755, z= 0.0106146586855, w= 0.0560873950606))

# ram_fixed_place_pose = Pose(position=Point(x= 0.0619293125068,y= 0.398280870516,z= 0.243341303728), orientation=Quaternion(x= -0.693673760483,y= 0.145193951023,z= 0.687426384229,w= 0.158683322592))

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

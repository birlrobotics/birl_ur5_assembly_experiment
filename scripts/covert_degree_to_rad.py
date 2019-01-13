from math import pi

ur_joint_name = ['shoulder_pan_joint', 'shoulder_lift_joint','elbow_joint', 'wrist_1_joint' ,'wrist_2_joint',  'wrist_3_joint']

get_vision_joint_angles = [91.67, -189.40, 89.17, -52.06, -95.23, 272.77]

chip_fixed_prepick_pose = [89.43, -41.49, 14.79, -59.70, -87.82, 249.61]

chip_fixed_pick_pose = [99.21, -129.02, 79.82, -77.49, -85.44, 260.29]

chip_fixed_preplace_pose = [138.83, -58.42, 38.16, -69.39, -90.69, 247.90]

chip_fixed_place_pose = [138.89,-58.47, 78.79,-109.96,-90.70,247.76]

var_list = [get_vision_joint_angles,
chip_fixed_prepick_pose,
chip_fixed_pick_pose,
chip_fixed_preplace_pose,
chip_fixed_place_pose,
]

for idx, var in enumerate(var_list):
    rad = [i/180*pi for i in var]
    # print dict(zip(ur_joint_name, rad))
    print (rad)
    print "-"*20
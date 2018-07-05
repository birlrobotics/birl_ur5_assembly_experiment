#!/usr/bin/env python
from smach_based_introspection_framework.online_part import (
    smach_runner
)
from birl_ur5_assembly_experiment.smach_FSM import (
    assembly_user_defined_sm
)

from birl_ur5_assembly_experiment.hardcoded_data import (
    reverting_statistics
)

from birl_ur5_assembly_experiment.moveit_vars_getter import get_moveit_vars

if __name__ == '__main__':
    sm = assembly_user_defined_sm()
    smach_runner.run(sm, reverting_statistics, get_moveit_vars)

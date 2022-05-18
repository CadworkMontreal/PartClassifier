# Copyright 2022 Cadwork Informatique Inc.
# All rights reserved.
# This file is part of PartClassifier,
# and is released under the "MIT License Agreement". Please see the LICENSE
# file that should have been included as part of this package.

import cadwork
import geometry_controller as gc

elements = cadwork.get_auto_attribute_elements()

for element in elements:
    actual_physical_volume = gc.get_actual_physical_volume(element)
    list_volume = gc.get_list_volume(element)
    if abs(list_volume - actual_physical_volume) < 0.0001:
        cadwork.set_auto_attribute([element], 'List')
    else:
        cadwork.set_auto_attribute([element], 'Shop Drawings')

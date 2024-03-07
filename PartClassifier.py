# Copyright 2024 Cadwork Informatique Inc.
# All rights reserved.
# This file is part of PartClassifier,
# and is released under the "MIT License Agreement". Please see the LICENSE
# file that should have been included as part of this package.

import cadwork
import geometry_controller as gc
import attribute_controller as ac

elements = cadwork.get_auto_attribute_elements()

for element in elements:
    if ac.get_production_number(element) == 0:
        continue

    actual_physical_volume = gc.get_actual_physical_volume(element)
    real_width = gc.get_width(element)
    real_height = gc.get_height(element)
    real_length = gc.get_length(element)
    real_dimensional_volume = real_width * real_height * real_length
    if abs(real_dimensional_volume - actual_physical_volume) < 1:
        cadwork.set_auto_attribute([element], 'List')
    else:
        cadwork.set_auto_attribute([element], 'Shop Drawings')

# Copyright 2022 Cadwork Informatique Inc.
# All rights reserved.
# This file is part of PartClassifier,
# and is released under the "MIT License Agreement". Please see the LICENSE
# file that should have been included as part of this package.

import cadwork
import attribute_controller as ac
import element_controller as ec
import geometry_controller as gc

###########################
#                         #
# Accurate Version (Slow) #
#                         #
###########################

elements = cadwork.get_auto_attribute_elements()
all_elements = ec.get_all_identifiable_element_ids()
conflict_elements = []

for element in all_elements:
    if ac.is_drilling(element):
        conflict_elements.append(element)
    elif ac.is_connector_axis(element):
        conflict_elements.append(element)

for element in elements:
    real_volume = gc.get_volume(element)
    list_volume = gc.get_list_volume(element)
    if abs(list_volume - real_volume) < 0.0001:
        contact_present = False
        for conflict_element in conflict_elements:
            if ec.check_if_elements_are_in_contact(element, conflict_element):
                cadwork.set_auto_attribute([element], 'Shop Drawings')
                contact_present = True
        if not contact_present:
            cadwork.set_auto_attribute([element], 'List')
    else:
        cadwork.set_auto_attribute([element], 'Shop Drawings')

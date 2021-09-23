from safety.safety import draw_safety
from leisure.leisure import draw_leisure
from outdoors.outdoors import draw_outdoors
from education.education import draw_education
from infrastructure import road, power, tree
from transportation import bus,subway

def draw_city():
    draw_safety()
    road.draw_road()
    power.draw_power_plant()
    road.draw_road()
    subway.draw_subway()
    draw_leisure()
    road.draw_road()
    draw_outdoors()
    tree.draw_tree()
    subway.draw_subway()
    road.draw_road()
    draw_education()
    bus.draw_bus()
    return

draw_city()

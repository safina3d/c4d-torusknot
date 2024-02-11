"""
    Name: Torus Knot Generator plugin
    Description: Create customized torus knots within Cinema 4D
    Author: Safina3D
    Version : 1.1.0
    Website : https://safina3d.blogspot.com
"""

import os
import c4d
from math import cos, sin, pi
from c4d import plugins, bitmaps, Vector, SplineObject

# Define the knot list
knot_list = [
    {"step": 0.1, "p": 2, "q": 1},
    {"step": 0.1, "p": 3, "q": 2},
    {"step": 0.05, "p": 4, "q": 3},
    {"step": 0.05, "p": 5, "q": 2},
    {"step": 0.05, "p": 5, "q": 3},
    {"step": 0.05, "p": 5, "q": 4},
    {"step": 0.05, "p": 6, "q": 5},
    {"step": 0.05, "p": 7, "q": 2},
    {"step": 0.05, "p": 7, "q": 3},
    {"step": 0.05, "p": 7, "q": 4},
    {"step": 0.05, "p": 7, "q": 5},
    {"step": 0.05, "p": 7, "q": 6},
    {"step": 0.05, "p": 8, "q": 3},
    {"step": 0.05, "p": 8, "q": 5},
    {"step": 0.01, "p": 9, "q": 2},
    {"step": 0.01, "p": 9, "q": 4},
    {"step": 0.01, "p": 9, "q": 5},
    {"step": 0.01, "p": 10, "q": 3},
    {"step": 0.01, "p": 11, "q": 2},
    {"step": 0.01, "p": 11, "q": 3},
    {"step": 0.01, "p": 11, "q": 4},
    {"step": 0.01, "p": 13, "q": 2},
    {"step": 0.01, "p": 13, "q": 3},
    {"step": 0.01, "p": 14, "q": 3},
    {"step": 0.01, "p": 15, "q": 2},
    {"step": 0.01, "p": 16, "q": 3},
    {"step": 0.01, "p": 17, "q": 2},
    {"step": 0.01, "p": 17, "q": 3},
    {"step": 0.01, "p": 19, "q": 2},
    {"step": 0.01, "p": 21, "q": 2},
    {"step": 0.01, "p": 23, "q": 2},
    {"step": 0.01, "p": 25, "q": 2},
    {"step": 0.01, "p": 27, "q": 2},
    {"step": 0.01, "p": 29, "q": 2},
    {"step": 0.01, "p": 31, "q": 2},
    {"step": 0.01, "p": 33, "q": 2},
    {"step": 0.01, "p": 35, "q": 2},
]


class TorusKnot(plugins.ObjectData):
    def __init__(self):
        self.SetOptimizeCache(True)

    def Init(self, node, isCloneInit=False):
        attribute_types = [int, float, float, float, float, float, float, float, bool, bool, str]
        attribute_ids = [
            c4d.KNOT_PREDEFINED_KNOT_LIST,
            c4d.KNOT_RANGE_MIN,
            c4d.KNOT_RANGE_MAX,
            c4d.KNOT_STEP,
            c4d.KNOT_PARAM_R0,
            c4d.KNOT_PARAM_R1,
            c4d.KNOT_PARAM_P,
            c4d.KNOT_PARAM_Q,
            c4d.KNOT_CUBIC_INTERPOLATION,
            c4d.KNOT_CLOSE_SPLINE,
            c4d.KNOT_POINT_COUNT
        ]

        for attribute_type, attribute_id in zip(attribute_types, attribute_ids):
            self.InitAttr(node, attribute_type, attribute_id)

        node[c4d.KNOT_PREDEFINED_KNOT_LIST] = 1003

        # Set default values
        TorusKnot._set_attributes(node, 0, 2, 0.1, 200, 100, 3, 2, True, True, 20)
        return True

    def GetVirtualObjects(self, op, hh):
        # Retrieve UI data values
        range_min = op[c4d.KNOT_RANGE_MIN] * pi
        range_max = op[c4d.KNOT_RANGE_MAX] * pi
        step = op[c4d.KNOT_STEP] * pi
        R = op[c4d.KNOT_PARAM_R0]
        r = op[c4d.KNOT_PARAM_R1]
        p = op[c4d.KNOT_PARAM_P]
        q = op[c4d.KNOT_PARAM_Q]
        is_cubic = op[c4d.KNOT_CUBIC_INTERPOLATION]

        # Calculate all points' position
        points = []
        t = range_min
        while t < range_max - 0.00001:
            x = (R + r * cos(p * t)) * cos(q * t)
            y = (R + r * cos(p * t)) * sin(q * t)
            z = r * sin(p * t)
            points.append(Vector(x, y, z))
            t += step

        # Spline initialization
        point_count = len(points)
        spline_type = c4d.SPLINETYPE_CUBIC if is_cubic else c4d.SPLINETYPE_LINEAR
        spline = SplineObject(point_count, spline_type)

        if spline is None: return

        # Update spline points
        for index, point in enumerate(points):
            spline.SetPoint(index, point)

        # Update UI point count
        op[c4d.KNOT_POINT_COUNT] = str(point_count)

        # Close the spline if needed
        spline[c4d.SPLINEOBJECT_CLOSED] = op[c4d.KNOT_CLOSE_SPLINE]

        # Send update message
        spline.Message(c4d.MSG_UPDATE)

        return spline

    def Message(self, node, type, data):
        if type == c4d.MSG_DESCRIPTION_CHECKUPDATE:
            current_id = data['descid'][0].id
            if current_id == c4d.KNOT_PREDEFINED_KNOT_LIST:
                selected_id = node[c4d.KNOT_PREDEFINED_KNOT_LIST]
                selected_index = selected_id - c4d.KNOT_PREDEFINED_KNOT_LIST - 1
                if selected_index < len(knot_list):
                    knot_data = knot_list[selected_index]
                    TorusKnot._set_attributes(node, 0, 2, knot_data["step"], 200, 100, knot_data["p"], knot_data["q"], True, True, 20)

        return True

    @staticmethod
    def _set_attributes(node, range_min, range_max, step, r0, r1, p, q, interpolation, close_spline, point_count):
        node[c4d.KNOT_RANGE_MIN] = range_min
        node[c4d.KNOT_RANGE_MAX] = range_max
        node[c4d.KNOT_STEP] = step
        node[c4d.KNOT_PARAM_R0] = r0
        node[c4d.KNOT_PARAM_R1] = r1
        node[c4d.KNOT_PARAM_P] = p
        node[c4d.KNOT_PARAM_Q] = q
        node[c4d.KNOT_CUBIC_INTERPOLATION] = interpolation
        node[c4d.KNOT_CLOSE_SPLINE] = close_spline
        node[c4d.KNOT_POINT_COUNT] = str(point_count)


if __name__ == "__main__":
    # Load the plugin icon
    icon_absolute_path = os.path.join(os.path.dirname(__file__), 'res/icons', 'knot.png')
    plugin_icon = bitmaps.BaseBitmap()
    plugin_icon.InitWith(icon_absolute_path)

    # Register the plugin
    plugins.RegisterObjectPlugin(
        id=1053564,
        str='Torus Knot 1.1',
        g=TorusKnot,
        description='Oknot',
        info=c4d.OBJECT_GENERATOR | c4d.OBJECT_ISSPLINE,
        icon=plugin_icon
    )

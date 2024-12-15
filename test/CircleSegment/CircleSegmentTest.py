import math
import random

from super_scad.boolean.Compound import Compound
from super_scad.d3.LinearExtrude import LinearExtrude
from super_scad.scad.Context import Context
from super_scad.scad.Scad import Scad
from super_scad.transformation.Paint import Paint
from super_scad.transformation.Translate2D import Translate2D
from super_scad.type import Vector3

from super_scad_circle_plus.CircleSegment import CircleSegment
from test.ScadTestCase import ScadTestCase


class CircleSegmentTest(ScadTestCase):
    """
    Unit test for circle segments.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def test_given_radius_and_central_angle(self):
        """
        Test circle segment given the radius and central angle.
        """
        segment = CircleSegment(radius=10.0, central_angle=60.0)
        self.assertAlmostEqual(segment.radius, 10.0)

        segment = CircleSegment(radius=10.0, central_angle=60.0)
        self.assertAlmostEqual(segment.diameter, 20.0)

        segment = CircleSegment(radius=10.0, central_angle=60.0)
        self.assertAlmostEqual(segment.central_angle, 60.0)

        segment = CircleSegment(radius=10.0, central_angle=60.0)
        self.assertAlmostEqual(segment.chord_length, 10.0)

        segment = CircleSegment(radius=10.0, central_angle=60.0)
        self.assertAlmostEqual(segment.arc_length, 10.47197551)

        segment = CircleSegment(radius=10.0, central_angle=60.0)
        self.assertAlmostEqual(segment.sagitta, 1.33974596)

        segment = CircleSegment(radius=10.0, central_angle=60.0)
        self.assertAlmostEqual(segment.apothem, 8.66025404)

        segment = CircleSegment(radius=10.0, central_angle=60.0)
        self.assertAlmostEqual(segment.area, 2956.69872981)

        segment = CircleSegment(radius=10.0, central_angle=60.0)
        self.assertAlmostEqual(segment.perimeter, 20.4719755)

    # ------------------------------------------------------------------------------------------------------------------
    def test_given_radius_and_chord_length(self):
        """
        Test circle segment given the radius and chord length.
        """
        segment = CircleSegment(radius=10.0, chord_length=10.0)
        self.assertAlmostEqual(segment.radius, 10.0)

        segment = CircleSegment(radius=10.0, chord_length=10.0)
        self.assertAlmostEqual(segment.diameter, 20.0)

        segment = CircleSegment(radius=10.0, chord_length=10.0)
        self.assertAlmostEqual(segment.central_angle, 60.0)

        segment = CircleSegment(radius=10.0, chord_length=10.0)
        self.assertAlmostEqual(segment.chord_length, 10.0)

        segment = CircleSegment(radius=10.0, chord_length=10.0)
        self.assertAlmostEqual(segment.arc_length, 10.47197551)

        segment = CircleSegment(radius=10.0, chord_length=10.0)
        self.assertAlmostEqual(segment.sagitta, 1.33974596)

        segment = CircleSegment(radius=10.0, chord_length=10.0)
        self.assertAlmostEqual(segment.apothem, 8.66025404)

        segment = CircleSegment(radius=10.0, chord_length=10.0)
        self.assertAlmostEqual(segment.area, 2956.69872981)

        segment = CircleSegment(radius=10.0, chord_length=10.0)
        self.assertAlmostEqual(segment.perimeter, 20.4719755)

    # ------------------------------------------------------------------------------------------------------------------
    def test_given_radius_and_arc_length(self):
        """
        Test circle segment given the radius and arc length.
        """
        segment = CircleSegment(radius=10.0, arc_length=10.471975511965976)
        self.assertAlmostEqual(segment.radius, 10.0)

        segment = CircleSegment(radius=10.0, arc_length=10.471975511965976)
        self.assertAlmostEqual(segment.diameter, 20.0)

        segment = CircleSegment(radius=10.0, arc_length=10.471975511965976)
        self.assertAlmostEqual(segment.central_angle, 60.0)

        segment = CircleSegment(radius=10.0, arc_length=10.471975511965976)
        self.assertAlmostEqual(segment.chord_length, 10.0)

        segment = CircleSegment(radius=10.0, arc_length=10.471975511965976)
        self.assertAlmostEqual(segment.arc_length, 10.47197551)

        segment = CircleSegment(radius=10.0, arc_length=10.471975511965976)
        self.assertAlmostEqual(segment.sagitta, 1.33974596)

        segment = CircleSegment(radius=10.0, arc_length=10.471975511965976)
        self.assertAlmostEqual(segment.apothem, 8.66025404)

        segment = CircleSegment(radius=10.0, arc_length=10.471975511965976)
        self.assertAlmostEqual(segment.area, 2956.69872981)

        segment = CircleSegment(radius=10.0, arc_length=10.471975511965976)
        self.assertAlmostEqual(segment.perimeter, 20.4719755)

    # ------------------------------------------------------------------------------------------------------------------
    def test_given_radius_and_sagitta(self):
        """
        Test circle segment given the radius and sagitta.
        """
        segment = CircleSegment(radius=10.0, sagitta=1.339745962155613)
        self.assertAlmostEqual(segment.radius, 10.0)

        segment = CircleSegment(radius=10.0, sagitta=1.339745962155613)
        self.assertAlmostEqual(segment.diameter, 20.0)

        segment = CircleSegment(radius=10.0, sagitta=1.339745962155613)
        self.assertAlmostEqual(segment.central_angle, 60.0)

        segment = CircleSegment(radius=10.0, sagitta=1.339745962155613)
        self.assertAlmostEqual(segment.chord_length, 10.0)

        segment = CircleSegment(radius=10.0, sagitta=1.339745962155613)
        self.assertAlmostEqual(segment.arc_length, 10.47197551)

        segment = CircleSegment(radius=10.0, sagitta=1.339745962155613)
        self.assertAlmostEqual(segment.sagitta, 1.33974596)

        segment = CircleSegment(radius=10.0, sagitta=1.339745962155613)
        self.assertAlmostEqual(segment.apothem, 8.66025404)

        segment = CircleSegment(radius=10.0, sagitta=1.339745962155613)
        self.assertAlmostEqual(segment.area, 2956.69872981)

        segment = CircleSegment(radius=10.0, sagitta=1.339745962155613)
        self.assertAlmostEqual(segment.perimeter, 20.4719755)

    # ------------------------------------------------------------------------------------------------------------------
    def test_given_radius_and_apothem(self):
        """
        Test circle segment given the radius and apothem.
        """
        segment = CircleSegment(radius=10.0, apothem=8.660254037844387)
        self.assertAlmostEqual(segment.radius, 10.0)

        segment = CircleSegment(radius=10.0, apothem=8.660254037844387)
        self.assertAlmostEqual(segment.diameter, 20.0)

        segment = CircleSegment(radius=10.0, apothem=8.660254037844387)
        self.assertAlmostEqual(segment.central_angle, 60.0)

        segment = CircleSegment(radius=10.0, apothem=8.660254037844387)
        self.assertAlmostEqual(segment.chord_length, 10.0)

        segment = CircleSegment(radius=10.0, apothem=8.660254037844387)
        self.assertAlmostEqual(segment.arc_length, 10.47197551)

        segment = CircleSegment(radius=10.0, apothem=8.660254037844387)
        self.assertAlmostEqual(segment.sagitta, 1.33974596)

        segment = CircleSegment(radius=10.0, apothem=8.660254037844387)
        self.assertAlmostEqual(segment.apothem, 8.66025404)

        segment = CircleSegment(radius=10.0, apothem=8.660254037844387)
        self.assertAlmostEqual(segment.area, 2956.69872981)

        segment = CircleSegment(radius=10.0, apothem=8.660254037844387)
        self.assertAlmostEqual(segment.perimeter, 20.4719755)

    # ------------------------------------------------------------------------------------------------------------------
    def test_radius_and_diameter(self):
        """
        Test circle segment given the radius or diameter.
        """
        segment = CircleSegment(radius=10.0, central_angle=180.0)
        self.assertAlmostEqual(segment.radius, 10.0)
        self.assertAlmostEqual(segment.diameter, 20.0)

        segment = CircleSegment(diameter=20.0, central_angle=180.0)
        self.assertAlmostEqual(segment.radius, 10.0)
        self.assertAlmostEqual(segment.diameter, 20.0)

    # ------------------------------------------------------------------------------------------------------------------
    def test_area(self):
        """
        Test the area of a minor and major circle segment.
        """
        radius = random.uniform(10.0, 20.0)
        central_angle = random.uniform(0.0, 360.0)

        segment1 = CircleSegment(radius=radius, central_angle=central_angle)
        segment2 = CircleSegment(radius=radius, central_angle=central_angle, minor_segment=False)

        self.assertAlmostEqual(segment1.area + segment2.area, math.pi * radius ** 2)

    # ------------------------------------------------------------------------------------------------------------------
    def test_perimeter(self):
        """
        Test the perimeter of a minor and major circle segment.
        """
        radius = random.uniform(10.0, 20.0)
        central_angle = random.uniform(0.0, 360.0)

        segment1 = CircleSegment(radius=radius, central_angle=central_angle)
        segment2 = CircleSegment(radius=radius, central_angle=central_angle, minor_segment=False)

        self.assertAlmostEqual(segment1.chord_length, segment2.chord_length)
        self.assertAlmostEqual(segment1.perimeter - \
                               segment1.chord_length + \
                               segment2.perimeter - \
                               segment2.chord_length, 2.0 * math.pi * radius)

    # ------------------------------------------------------------------------------------------------------------------
    def test_plain_circle_segments(self):
        """
        Test plain circle segments.
        """
        scad = Scad(context=Context(fn=60))

        segment1 = CircleSegment(radius=10.0, central_angle=135.0)
        segment2 = CircleSegment(radius=10.0, central_angle=135.0, minor_segment=False)

        segment1 = Translate2D(y=0.1, child=segment1)
        segment2 = Translate2D(y=-0.1, child=segment2)

        segments = Compound(children=[segment1, segment2])

        path_actual, path_expected = self.paths()
        scad.run_super_scad(segments, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_plain_circle_segments_no_align(self):
        """
        Test plain circle segments not aligned on the x-axis.
        """
        scad = Scad(context=Context(fn=60))

        segment1 = CircleSegment(radius=10.0, central_angle=135.0, align_on_x_axis=False)
        segment2 = CircleSegment(radius=10.0, central_angle=135.0, minor_segment=False, align_on_x_axis=False)

        segment1 = Translate2D(y=0.1, child=segment1)
        segment2 = Translate2D(y=-0.1, child=segment2)

        segments = Compound(children=[segment1, segment2])

        path_actual, path_expected = self.paths()
        scad.run_super_scad(segments, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_plain_circle_segments_180_plus(self):
        """
        Test plain circle segments with a central angle over 180 degrees.
        """
        scad = Scad(context=Context(fn=60))

        segment1 = CircleSegment(radius=10.0, central_angle=210.0)
        segment2 = CircleSegment(radius=10.0, central_angle=210.0, minor_segment=False)

        segment1 = Translate2D(y=0.1, child=segment1)
        segment2 = Translate2D(y=-0.1, child=segment2)

        segments = Compound(children=[segment1, segment2])

        path_actual, path_expected = self.paths()
        scad.run_super_scad(segments, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_plain_circle_segments_extend_by_eps_radius(self):
        """
        Test plain circle segments with radius extended by eps for a clear overlap.
        """
        scad = Scad(context=Context(fn=60, eps=1.0, vpr=Vector3.origin))
        angle = 135.0
        radius = 10.0

        segment1a = CircleSegment(radius=radius, central_angle=angle, extend_by_eps_radius=True)
        segment1a = LinearExtrude(height=1.0, child=segment1a)
        segment1a = Paint(color='red', child=segment1a)
        segment1b = CircleSegment(radius=radius, central_angle=angle)
        segment1b = LinearExtrude(height=1.0, extend_by_eps_top=True, child=segment1b)
        segment1 = Compound(children=[segment1a, segment1b])

        segment2a = CircleSegment(radius=radius, central_angle=angle, minor_segment=False, extend_by_eps_radius=True)
        segment2a = LinearExtrude(height=1.0, child=segment2a)
        segment2a = Paint(color='red', child=segment2a)
        segment2b = CircleSegment(radius=radius, central_angle=angle, minor_segment=False)
        segment2b = LinearExtrude(height=1.0, extend_by_eps_top=True, child=segment2b)
        segment2 = Compound(children=[segment2a, segment2b])

        segment1 = Translate2D(y=0.1, child=segment1)
        segment2 = Translate2D(y=-0.1, child=segment2)

        segments = Compound(children=[segment1, segment2])

        path_actual, path_expected = self.paths()
        scad.run_super_scad(segments, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_plain_circle_segments_extend_by_eps_radius_180_plus(self):
        """
        Test plain circle segments with radius extended by eps for a clear overlap and with a central angle over 180
        degrees.
        """
        scad = Scad(context=Context(fn=60, eps=1.0, vpr=Vector3.origin))
        radius = 10.0
        central_angle = 225.0

        segment1a = CircleSegment(radius=radius, central_angle=central_angle, extend_by_eps_radius=True)
        segment1a = LinearExtrude(height=1.0, child=segment1a)
        segment1a = Paint(color='red', child=segment1a)
        segment1b = CircleSegment(radius=radius, central_angle=central_angle)
        segment1b = LinearExtrude(height=1.0, extend_by_eps_top=True, child=segment1b)
        segment1 = Compound(children=[segment1a, segment1b])

        segment2a = CircleSegment(radius=radius, central_angle=central_angle, minor_segment=False,
                                  extend_by_eps_radius=True)
        segment2a = LinearExtrude(height=1.0, child=segment2a)
        segment2a = Paint(color='red', child=segment2a)
        segment2b = CircleSegment(radius=radius, central_angle=central_angle, minor_segment=False)
        segment2b = LinearExtrude(height=1.0, extend_by_eps_top=True, child=segment2b)
        segment2 = Compound(children=[segment2a, segment2b])

        segment1 = Translate2D(y=0.1, child=segment1)
        segment2 = Translate2D(y=-0.1, child=segment2)

        segments = Compound(children=[segment1, segment2])

        path_actual, path_expected = self.paths()
        scad.run_super_scad(segments, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_plain_circle_segments_extend_by_eps_cord(self):
        """
        Test plain circle segments with extended along the cord by eps for a clear overlap.
        """
        scad = Scad(context=Context(fn=60, eps=1.0, vpr=Vector3.origin))
        radius = 10.0
        angle = 100.0

        segment1a = CircleSegment(radius=radius, central_angle=angle, extend_by_eps_cord=True)
        segment1a = LinearExtrude(height=1.0, child=segment1a)
        segment1a = Paint(color='red', child=segment1a)
        segment1b = CircleSegment(radius=radius, central_angle=angle)
        segment1b = LinearExtrude(height=1.0, extend_by_eps_top=True, child=segment1b)
        segment1 = Compound(children=[segment1a, segment1b])

        segment2a = CircleSegment(radius=radius, central_angle=angle, minor_segment=False, extend_by_eps_cord=True)
        segment2a = LinearExtrude(height=1.0, child=segment2a)
        segment2a = Paint(color='red', child=segment2a)
        segment2b = CircleSegment(radius=radius, central_angle=angle, minor_segment=False)
        segment2b = LinearExtrude(height=1.0, extend_by_eps_top=True, child=segment2b)
        segment2 = Compound(children=[segment2a, segment2b])

        segment1 = Translate2D(y=1.1, child=segment1)
        segment2 = Translate2D(y=-1.1, child=segment2)

        segments = Compound(children=[segment1, segment2])

        path_actual, path_expected = self.paths()
        scad.run_super_scad(segments, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_plain_circle_segments_extend_by_eps_cord_180_plus(self):
        """
        Test plain circle segments with extended along the cord by eps for a clear overlap and with a central angle over
        180 degrees.
        """
        scad = Scad(context=Context(fn=60, eps=1.0, vpr=Vector3.origin))
        radius = 10.0
        angle = 270.0

        segment1a = CircleSegment(radius=radius, central_angle=angle, extend_by_eps_cord=True)
        segment1a = LinearExtrude(height=1.0, child=segment1a)
        segment1a = Paint(color='red', child=segment1a)
        segment1b = CircleSegment(radius=radius, central_angle=angle)
        segment1b = LinearExtrude(height=1.0, extend_by_eps_top=True, child=segment1b)
        segment1 = Compound(children=[segment1a, segment1b])

        segment2a = CircleSegment(radius=radius, central_angle=angle, minor_segment=False, extend_by_eps_cord=True)
        segment2a = LinearExtrude(height=1.0, child=segment2a)
        segment2a = Paint(color='red', child=segment2a)
        segment2b = CircleSegment(radius=radius, central_angle=angle, minor_segment=False)
        segment2b = LinearExtrude(height=1.0, extend_by_eps_top=True, child=segment2b)
        segment2 = Compound(children=[segment2a, segment2b])

        segment1 = Translate2D(y=1.1, child=segment1)
        segment2 = Translate2D(y=-1.1, child=segment2)

        segments = Compound(children=[segment1, segment2])

        path_actual, path_expected = self.paths()
        scad.run_super_scad(segments, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_plain_circle_segments_extend_by_eps_cord_and_radius(self):
        """
        Test plain circle segments with extended along the cord and radius by eps for a clear overlap.
        """
        scad = Scad(context=Context(fn=60, eps=1.0, vpr=Vector3.origin))
        radius = 10.0
        angle = 100.0

        segment1a = CircleSegment(radius=radius,
                                  central_angle=angle,
                                  extend_by_eps_radius=True,
                                  extend_by_eps_cord=True)
        segment1a = LinearExtrude(height=1.0, child=segment1a)
        segment1a = Paint(color='red', child=segment1a)
        segment1b = CircleSegment(radius=radius, central_angle=angle)
        segment1b = LinearExtrude(height=1.0, extend_by_eps_top=True, child=segment1b)
        segment1 = Compound(children=[segment1a, segment1b])

        segment2a = CircleSegment(radius=radius,
                                  central_angle=angle,
                                  minor_segment=False,
                                  extend_by_eps_radius=True,
                                  extend_by_eps_cord=True)
        segment2a = LinearExtrude(height=1.0, child=segment2a)
        segment2a = Paint(color='red', child=segment2a)
        segment2b = CircleSegment(radius=radius, central_angle=angle, minor_segment=False)
        segment2b = LinearExtrude(height=1.0, extend_by_eps_top=True, child=segment2b)
        segment2 = Compound(children=[segment2a, segment2b])

        segment1 = Translate2D(y=1.1, child=segment1)
        segment2 = Translate2D(y=-1.1, child=segment2)

        segments = Compound(children=[segment1, segment2])

        path_actual, path_expected = self.paths()
        scad.run_super_scad(segments, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_plain_circle_segments_extend_by_eps_cord_and_radius_180_plus(self):
        """
        Test plain circle segments with extended along the cord and radius by eps for a clear overlap and with a central
        angle over 180 degrees.
        """
        scad = Scad(context=Context(fn=60, eps=1.0, vpr=Vector3.origin))
        radius = 10.0
        angle = 230.0

        segment1a = CircleSegment(radius=radius,
                                  central_angle=angle,
                                  extend_by_eps_radius=True,
                                  extend_by_eps_cord=True)
        segment1a = LinearExtrude(height=1.0, child=segment1a)
        segment1a = Paint(color='red', child=segment1a)
        segment1b = CircleSegment(radius=radius, central_angle=angle)
        segment1b = LinearExtrude(height=1.0, extend_by_eps_top=True, child=segment1b)
        segment1 = Compound(children=[segment1a, segment1b])

        segment2a = CircleSegment(radius=radius,
                                  central_angle=angle,
                                  minor_segment=False,
                                  extend_by_eps_radius=True,
                                  extend_by_eps_cord=True)
        segment2a = LinearExtrude(height=1.0, child=segment2a)
        segment2a = Paint(color='red', child=segment2a)
        segment2b = CircleSegment(radius=radius, central_angle=angle, minor_segment=False)
        segment2b = LinearExtrude(height=1.0, extend_by_eps_top=True, child=segment2b)
        segment2 = Compound(children=[segment2a, segment2b])

        segment1 = Translate2D(y=1.1, child=segment1)
        segment2 = Translate2D(y=-1.1, child=segment2)

        segments = Compound(children=[segment1, segment2])

        path_actual, path_expected = self.paths()
        scad.run_super_scad(segments, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

# ----------------------------------------------------------------------------------------------------------------------

from super_scad.boolean.Difference import Difference
from super_scad.boolean.Union import Union
from super_scad.scad.Context import Context
from super_scad.scad.Scad import Scad
from super_scad.scad.Unit import Unit
from super_scad.transformation.Paint import Paint
from super_scad.type.Color import Color

from super_scad_circle_sector.CircleSector import CircleSector
from test.CircleSector.ImperialCircleSector import ImperialCircleSector
from test.ScadTestCase import ScadTestCase


class CircleSectorTest(ScadTestCase):
    """
    Test cases for CircleSector.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def test_circle_sector4n(self):
        """
        Test a circle sector based on a circle with a multiple of 4 vertices.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(context=Context(fn=360, eps=0.1))
        circle_sector = CircleSector(start_angle=10.0, end_angle=80.0, inner_radius=10.0, outer_radius=30.0, fn4n=True)

        self.assertAlmostEqual(30.0, circle_sector.radius)
        self.assertAlmostEqual(10.0, circle_sector.inner_radius)
        self.assertAlmostEqual(30.0, circle_sector.outer_radius)
        self.assertAlmostEqual(70.0, circle_sector.angle)
        self.assertAlmostEqual(10.0, circle_sector.start_angle)
        self.assertAlmostEqual(80.0, circle_sector.end_angle)
        self.assertEqual(1, circle_sector.convexity)
        self.assertIsNone(circle_sector.fn)
        self.assertTrue(circle_sector.fn4n)

        scad.run_super_scad(circle_sector, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_circle_sector_070_extend_legs_by_eps(self):
        """
        Test a circle sector that is 70 degrees and with legs extended by eps.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(context=Context(fn=360, eps=0.1))

        circle_sector1 = CircleSector(start_angle=10.0, end_angle=80.0, radius=10.0)
        circle_sector2 = CircleSector(start_angle=10.0, end_angle=80.0, radius=10.0, extend_legs_by_eps=True)

        diff = Difference(children=[Paint(color=Color('red'),
                                          child=circle_sector2),
                                    circle_sector1])
        scad.run_super_scad(diff, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_circle_sector_090_extend_legs_by_eps(self):
        """
        Test a circle sector that is 90 degrees and with legs extended by eps.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(context=Context(fn=360, eps=0.1))
        circle_sector1 = CircleSector(start_angle=10.0, end_angle=100.0, radius=10.0)
        circle_sector2 = CircleSector(start_angle=10.0, end_angle=100.0, radius=10.0, extend_legs_by_eps=True)

        diff = Difference(children=[Paint(color=Color('red'),
                                          child=circle_sector2),
                                    circle_sector1])
        scad.run_super_scad(diff, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_circle_sector_160_extend_legs_by_eps(self):
        """
        Test a circle sector that is 160 degrees and with legs extended by eps.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(context=Context(fn=360, eps=0.1))

        circle_sector1 = CircleSector(start_angle=10.0, end_angle=170.0, radius=10.0)
        circle_sector2 = CircleSector(start_angle=10.0, end_angle=170.0, radius=10.0, extend_legs_by_eps=True)

        diff = Difference(children=[Paint(color=Color('red'),
                                          child=circle_sector2),
                                    circle_sector1])
        scad.run_super_scad(diff, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_circle_sector_180_extend_legs_by_eps(self):
        """
        Test a circle sector that is 180 degrees and with legs extended by eps.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(context=Context(fn=360, eps=0.1))
        circle_sector1 = CircleSector(start_angle=10.0, end_angle=190.0, radius=10.0)
        circle_sector2 = CircleSector(start_angle=10.0, end_angle=190.0, radius=10.0, extend_legs_by_eps=True)

        diff = Difference(children=[Paint(color=Color('red'),
                                          child=circle_sector2),
                                    circle_sector1])
        scad.run_super_scad(diff, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_circle_sector_250_extend_legs_by_eps(self):
        """
        Test a circle sector that is 250 degrees and with legs extended by eps.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(context=Context(fn=360, eps=0.1))

        circle_sector1 = CircleSector(start_angle=10.0, end_angle=260.0, radius=10.0)
        circle_sector2 = CircleSector(start_angle=10.0, end_angle=260.0, radius=10.0, extend_legs_by_eps=True)

        diff = Difference(children=[Paint(color=Color('red'),
                                          child=circle_sector2),
                                    circle_sector1])
        scad.run_super_scad(diff, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_circle_sector_340_extend_legs_by_eps(self):
        """
        Test a circle sector that is 340 degrees and with legs extended by eps.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(context=Context(fn=360, eps=0.1))

        circle_sector1 = CircleSector(start_angle=5.0, end_angle=350.0, radius=10.0)
        circle_sector2 = CircleSector(start_angle=5.0, end_angle=350.0, radius=10.0, extend_legs_by_eps=True)

        diff = Difference(children=[Paint(color=Color('red'),
                                          child=circle_sector2),
                                    circle_sector1])
        scad.run_super_scad(diff, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_circle_sector_extend_start_leg_by_eps(self):
        """
        Test a circle sector that is 70 degrees and with the start leg extended by eps.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(context=Context(fn=360, eps=0.1))

        circle_sector1 = CircleSector(start_angle=10.0, end_angle=80.0, radius=10.0)
        circle_sector2 = CircleSector(start_angle=10.0, end_angle=80.0, radius=10.0, extend_legs_by_eps=(True, False))

        diff = Difference(children=[Paint(color=Color('red'),
                                          child=circle_sector2),
                                    circle_sector1])
        scad.run_super_scad(diff, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_circle_sector_extend_end_leg_by_eps(self):
        """
        Test a circle sector that is 70 degrees and with the start leg extended by eps.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(context=Context(fn=360, eps=0.1))

        circle_sector1 = CircleSector(start_angle=10.0, end_angle=80.0, radius=10.0)
        circle_sector2 = CircleSector(start_angle=10.0, end_angle=80.0, radius=10.0, extend_legs_by_eps=(False, True))

        diff = Difference(children=[Paint(color=Color('red'),
                                          child=circle_sector2),
                                    circle_sector1])
        scad.run_super_scad(diff, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_circle_sector_in_q1(self):
        """
        Test a circle sector that start lies quadrant 1.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(context=Context(fn=360, eps=0.1))
        circle_sector = CircleSector(start_angle=10.0, end_angle=80.0, inner_radius=10.0, outer_radius=30.0)

        self.assertAlmostEqual(30.0, circle_sector.radius)
        self.assertAlmostEqual(10.0, circle_sector.inner_radius)
        self.assertAlmostEqual(30.0, circle_sector.outer_radius)
        self.assertAlmostEqual(70.0, circle_sector.angle)
        self.assertAlmostEqual(10.0, circle_sector.start_angle)
        self.assertAlmostEqual(80.0, circle_sector.end_angle)
        self.assertEqual(1, circle_sector.convexity)
        self.assertIsNone(circle_sector.fn4n)

        scad.run_super_scad(circle_sector, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_circle_sector_q2(self):
        """
        Test a circle sector that start lies quadrant 2.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(context=Context(fn=360, eps=0.1))
        circle_sector = CircleSector(start_angle=100.0, end_angle=170.0, inner_radius=10.0, outer_radius=30.0)

        self.assertAlmostEqual(30.0, circle_sector.radius)
        self.assertAlmostEqual(10.0, circle_sector.inner_radius)
        self.assertAlmostEqual(30.0, circle_sector.outer_radius)
        self.assertAlmostEqual(70.0, circle_sector.angle)
        self.assertAlmostEqual(100.0, circle_sector.start_angle)
        self.assertAlmostEqual(170.0, circle_sector.end_angle)
        self.assertEqual(1, circle_sector.convexity)
        self.assertIsNone(circle_sector.fn4n)

        scad.run_super_scad(circle_sector, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_circle_sector_q3(self):
        """
        Test a circle sector that start lies quadrant 3.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(context=Context(fn=360, eps=0.1))
        circle_sector = CircleSector(start_angle=190.0, end_angle=260.0, inner_radius=10.0, outer_radius=30.0)

        self.assertAlmostEqual(30.0, circle_sector.radius)
        self.assertAlmostEqual(10.0, circle_sector.inner_radius)
        self.assertAlmostEqual(30.0, circle_sector.outer_radius)
        self.assertAlmostEqual(70.0, circle_sector.angle)
        self.assertAlmostEqual(190.0, circle_sector.start_angle)
        self.assertAlmostEqual(260.0, circle_sector.end_angle)
        self.assertEqual(1, circle_sector.convexity)
        self.assertIsNone(circle_sector.fn4n)

        scad.run_super_scad(circle_sector, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_circle_sector_q4(self):
        """
        Test a circle sector that start lies quadrant 4.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(context=Context(fn=360, eps=0.1))
        circle_sector = CircleSector(start_angle=280.0, end_angle=350.0, inner_radius=10.0, outer_radius=30.0)

        self.assertAlmostEqual(30.0, circle_sector.radius)
        self.assertAlmostEqual(10.0, circle_sector.inner_radius)
        self.assertAlmostEqual(30.0, circle_sector.outer_radius)
        self.assertAlmostEqual(70.0, circle_sector.angle)
        self.assertAlmostEqual(280.0, circle_sector.start_angle)
        self.assertAlmostEqual(350.0, circle_sector.end_angle)
        self.assertEqual(1, circle_sector.convexity)
        self.assertIsNone(circle_sector.fn4n)

        scad.run_super_scad(circle_sector, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_circle_sector_is_q1(self):
        """
        Test a circle sector that is quadrant 1.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(context=Context(fn=360, eps=0.1))
        circle_sector = CircleSector(start_angle=0.0, end_angle=90.0, radius=30.0)

        self.assertAlmostEqual(30.0, circle_sector.radius)
        self.assertAlmostEqual(0.0, circle_sector.inner_radius)
        self.assertAlmostEqual(30.0, circle_sector.outer_radius)
        self.assertAlmostEqual(90.0, circle_sector.angle)
        self.assertAlmostEqual(0.0, circle_sector.start_angle)
        self.assertAlmostEqual(90.0, circle_sector.end_angle)
        self.assertEqual(1, circle_sector.convexity)
        self.assertIsNone(circle_sector.fn4n)

        scad.run_super_scad(circle_sector, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_circle_sector_is_q2(self):
        """
        Test a circle sector that is quadrant 2.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(context=Context(fn=360, eps=0.1))
        circle_sector = CircleSector(start_angle=90.0, end_angle=180.0, radius=30.0)

        self.assertAlmostEqual(30.0, circle_sector.radius)
        self.assertAlmostEqual(0.0, circle_sector.inner_radius)
        self.assertAlmostEqual(30.0, circle_sector.outer_radius)
        self.assertAlmostEqual(90.0, circle_sector.angle)
        self.assertAlmostEqual(90.0, circle_sector.start_angle)
        self.assertAlmostEqual(180.0, circle_sector.end_angle)
        self.assertEqual(1, circle_sector.convexity)
        self.assertIsNone(circle_sector.fn4n)

        scad.run_super_scad(circle_sector, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_circle_sector_is_q3(self):
        """
        Test a circle sector that is quadrant 3.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(context=Context(fn=360, eps=0.1))
        circle_sector = CircleSector(start_angle=180.0, end_angle=270.0, radius=30.0)

        self.assertAlmostEqual(30.0, circle_sector.radius)
        self.assertAlmostEqual(0.0, circle_sector.inner_radius)
        self.assertAlmostEqual(30.0, circle_sector.outer_radius)
        self.assertAlmostEqual(90.0, circle_sector.angle)
        self.assertAlmostEqual(180.0, circle_sector.start_angle)
        self.assertAlmostEqual(270.0, circle_sector.end_angle)
        self.assertEqual(1, circle_sector.convexity)
        self.assertIsNone(circle_sector.fn4n)

        scad.run_super_scad(circle_sector, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_circle_sector_is_q4(self):
        """
        Test a circle sector that is quadrant 4.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(context=Context(fn=360, eps=0.1))
        circle_sector = CircleSector(start_angle=270.0, end_angle=360.0, radius=30.0)

        self.assertAlmostEqual(30.0, circle_sector.radius)
        self.assertAlmostEqual(0.0, circle_sector.inner_radius)
        self.assertAlmostEqual(30.0, circle_sector.outer_radius)
        self.assertAlmostEqual(90.0, circle_sector.angle)
        self.assertAlmostEqual(270.0, circle_sector.start_angle)
        self.assertAlmostEqual(0.0, circle_sector.end_angle)
        self.assertEqual(1, circle_sector.convexity)
        self.assertIsNone(circle_sector.fn4n)

        scad.run_super_scad(circle_sector, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_circle_sector_is_q1_q2(self):
        """
        Test a circle sector that is quadrant 1 & 2.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(context=Context(fn=360, eps=0.1))
        circle_sector = CircleSector(start_angle=0.0, end_angle=180.0, radius=30.0)

        self.assertAlmostEqual(30.0, circle_sector.radius)
        self.assertAlmostEqual(0.0, circle_sector.inner_radius)
        self.assertAlmostEqual(30.0, circle_sector.outer_radius)
        self.assertAlmostEqual(180.0, circle_sector.angle)
        self.assertAlmostEqual(0.0, circle_sector.start_angle)
        self.assertAlmostEqual(180.0, circle_sector.end_angle)
        self.assertEqual(2, circle_sector.convexity)
        self.assertIsNone(circle_sector.fn4n)

        scad.run_super_scad(circle_sector, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_circle_sector_is_q2_q3(self):
        """
        Test a circle sector that is quadrant 2 & 3.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(context=Context(fn=360, eps=0.1))
        circle_sector = CircleSector(start_angle=90.0, end_angle=270.0, radius=30.0)

        self.assertAlmostEqual(30.0, circle_sector.radius)
        self.assertAlmostEqual(0.0, circle_sector.inner_radius)
        self.assertAlmostEqual(30.0, circle_sector.outer_radius)
        self.assertAlmostEqual(180.0, circle_sector.angle)
        self.assertAlmostEqual(90.0, circle_sector.start_angle)
        self.assertAlmostEqual(270.0, circle_sector.end_angle)
        self.assertEqual(2, circle_sector.convexity)
        self.assertIsNone(circle_sector.fn4n)

        scad.run_super_scad(circle_sector, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_circle_sector_is_q3_q4(self):
        """
        Test a circle sector that is quadrant 3 & 4.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(context=Context(fn=360, eps=0.1))
        circle_sector = CircleSector(start_angle=180.0, end_angle=360.0, radius=30.0)

        self.assertAlmostEqual(30.0, circle_sector.radius)
        self.assertAlmostEqual(0.0, circle_sector.inner_radius)
        self.assertAlmostEqual(30.0, circle_sector.outer_radius)
        self.assertAlmostEqual(180.0, circle_sector.angle)
        self.assertAlmostEqual(180.0, circle_sector.start_angle)
        self.assertAlmostEqual(0.0, circle_sector.end_angle)
        self.assertEqual(2, circle_sector.convexity)
        self.assertIsNone(circle_sector.fn4n)

        scad.run_super_scad(circle_sector, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_circle_sector_is_q4_q1(self):
        """
        Test a circle sector that is quadrant 3 & 4.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(context=Context(fn=360, eps=0.1))
        circle_sector = CircleSector(start_angle=270.0, end_angle=90.0, radius=30.0)

        self.assertAlmostEqual(30.0, circle_sector.radius)
        self.assertAlmostEqual(0.0, circle_sector.inner_radius)
        self.assertAlmostEqual(30.0, circle_sector.outer_radius)
        self.assertAlmostEqual(180.0, circle_sector.angle)
        self.assertAlmostEqual(270.0, circle_sector.start_angle)
        self.assertAlmostEqual(90.0, circle_sector.end_angle)
        self.assertEqual(2, circle_sector.convexity)
        self.assertIsNone(circle_sector.fn4n)

        scad.run_super_scad(circle_sector, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_circle_sector_is_q1_q2_q3(self):
        """
        Test a circle sector that is quadrant 1, 2, & 3.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(context=Context(fn=360, eps=0.1))
        circle_sector = CircleSector(start_angle=0.0, end_angle=270.0, radius=30.0)

        self.assertAlmostEqual(30.0, circle_sector.radius)
        self.assertAlmostEqual(0.0, circle_sector.inner_radius)
        self.assertAlmostEqual(30.0, circle_sector.outer_radius)
        self.assertAlmostEqual(270.0, circle_sector.angle)
        self.assertAlmostEqual(0.0, circle_sector.start_angle)
        self.assertAlmostEqual(270.0, circle_sector.end_angle)
        self.assertEqual(2, circle_sector.convexity)
        self.assertIsNone(circle_sector.fn4n)

        scad.run_super_scad(circle_sector, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_circle_sector_is_q2_q3_q4(self):
        """
        Test a circle sector that is quadrant 2, 3 & 4.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(context=Context(fn=360, eps=0.1))
        circle_sector = CircleSector(start_angle=90.0, end_angle=360.0, radius=30.0)

        self.assertAlmostEqual(30.0, circle_sector.radius)
        self.assertAlmostEqual(0.0, circle_sector.inner_radius)
        self.assertAlmostEqual(30.0, circle_sector.outer_radius)
        self.assertAlmostEqual(270.0, circle_sector.angle)
        self.assertAlmostEqual(90.0, circle_sector.start_angle)
        self.assertAlmostEqual(0.0, circle_sector.end_angle)
        self.assertEqual(2, circle_sector.convexity)
        self.assertIsNone(circle_sector.fn4n)

        scad.run_super_scad(circle_sector, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_circle_sector_is_q3_q4_q1(self):
        """
        Test a circle sector that is quadrant 3, 4 & 1.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(context=Context(fn=360, eps=0.1))
        circle_sector = CircleSector(start_angle=180.0, end_angle=90.0, radius=30.0)

        self.assertAlmostEqual(30.0, circle_sector.radius)
        self.assertAlmostEqual(0.0, circle_sector.inner_radius)
        self.assertAlmostEqual(30.0, circle_sector.outer_radius)
        self.assertAlmostEqual(270.0, circle_sector.angle)
        self.assertAlmostEqual(180.0, circle_sector.start_angle)
        self.assertAlmostEqual(90.0, circle_sector.end_angle)
        self.assertEqual(2, circle_sector.convexity)
        self.assertIsNone(circle_sector.fn4n)

        scad.run_super_scad(circle_sector, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_circle_sector_is_q4_q1_q2(self):
        """
        Test a circle sector that is quadrant 4, 1 & 2.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(context=Context(fn=360, eps=0.1))
        circle_sector = CircleSector(start_angle=270.0, end_angle=180.0, radius=30.0)

        self.assertAlmostEqual(30.0, circle_sector.radius)
        self.assertAlmostEqual(0.0, circle_sector.inner_radius)
        self.assertAlmostEqual(30.0, circle_sector.outer_radius)
        self.assertAlmostEqual(270.0, circle_sector.angle)
        self.assertAlmostEqual(270.0, circle_sector.start_angle)
        self.assertAlmostEqual(180.0, circle_sector.end_angle)
        self.assertEqual(2, circle_sector.convexity)
        self.assertIsNone(circle_sector.fn4n)

        scad.run_super_scad(circle_sector, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_circle_sector_is_q1_q2_q3_q4(self):
        """
        Test a circle sector that is quadrant 1, 2, 3, & 4.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(context=Context(fn=360, eps=0.1))
        circle_sector = CircleSector(start_angle=0.0, end_angle=360.0 - 1e-8, radius=30.0)

        self.assertAlmostEqual(30.0, circle_sector.radius)
        self.assertAlmostEqual(0.0, circle_sector.inner_radius)
        self.assertAlmostEqual(30.0, circle_sector.outer_radius)
        self.assertAlmostEqual(360.0, circle_sector.angle)
        self.assertAlmostEqual(0.0, circle_sector.start_angle)
        self.assertAlmostEqual(360.0, circle_sector.end_angle)
        self.assertEqual(2, circle_sector.convexity)
        self.assertIsNone(circle_sector.fn4n)

        scad.run_super_scad(circle_sector, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_circle_sector_q1_q2(self):
        """
        Test a circle sector that starts in quadrant 1 and ends in quadrant 2.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(context=Context(fn=360, eps=0.1))
        circle_sector = CircleSector(start_angle=80.0, end_angle=100.0, inner_radius=10.0, outer_radius=30.0)

        self.assertAlmostEqual(30.0, circle_sector.radius)
        self.assertAlmostEqual(10.0, circle_sector.inner_radius)
        self.assertAlmostEqual(30.0, circle_sector.outer_radius)
        self.assertAlmostEqual(20.0, circle_sector.angle)
        self.assertAlmostEqual(80.0, circle_sector.start_angle)
        self.assertAlmostEqual(100.0, circle_sector.end_angle)
        self.assertEqual(1, circle_sector.convexity)
        self.assertIsNone(circle_sector.fn4n)

        scad.run_super_scad(circle_sector, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_circle_sector_q2_q3(self):
        """
        Test a circle sector that starts in quadrant 2 and ends in quadrant 3.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(context=Context(fn=360, eps=0.1))
        circle_sector = CircleSector(start_angle=170.0, end_angle=190.0, inner_radius=10.0, outer_radius=30.0)

        self.assertAlmostEqual(30.0, circle_sector.radius)
        self.assertAlmostEqual(10.0, circle_sector.inner_radius)
        self.assertAlmostEqual(30.0, circle_sector.outer_radius)
        self.assertAlmostEqual(20.0, circle_sector.angle)
        self.assertAlmostEqual(170.0, circle_sector.start_angle)
        self.assertAlmostEqual(190.0, circle_sector.end_angle)
        self.assertEqual(1, circle_sector.convexity)
        self.assertIsNone(circle_sector.fn4n)

        scad.run_super_scad(circle_sector, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_circle_sector_q3_q4(self):
        """
        Test a circle sector that starts in quadrant 3 and ends in quadrant 4.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(context=Context(fn=360, eps=0.1))
        circle_sector = CircleSector(start_angle=260.0, end_angle=280.0, inner_radius=10.0, outer_radius=30.0)

        self.assertAlmostEqual(30.0, circle_sector.radius)
        self.assertAlmostEqual(10.0, circle_sector.inner_radius)
        self.assertAlmostEqual(30.0, circle_sector.outer_radius)
        self.assertAlmostEqual(20.0, circle_sector.angle)
        self.assertAlmostEqual(260.0, circle_sector.start_angle)
        self.assertAlmostEqual(280.0, circle_sector.end_angle)
        self.assertEqual(1, circle_sector.convexity)
        self.assertIsNone(circle_sector.fn4n)

        scad.run_super_scad(circle_sector, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_circle_sector_q3_q1b(self):
        """
        Test a circle sector that starts in quadrant 3 and ends in quadrant 1.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(context=Context(fn=360, eps=0.1))
        circle_sector = CircleSector(start_angle=180.01, end_angle=89.99, inner_radius=10.0, outer_radius=30.0)

        self.assertAlmostEqual(30.0, circle_sector.radius)
        self.assertAlmostEqual(10.0, circle_sector.inner_radius)
        self.assertAlmostEqual(30.0, circle_sector.outer_radius)
        self.assertAlmostEqual(269.98, circle_sector.angle)
        self.assertAlmostEqual(180.01, circle_sector.start_angle)
        self.assertAlmostEqual(89.99, circle_sector.end_angle)
        self.assertEqual(2, circle_sector.convexity)
        self.assertIsNone(circle_sector.fn4n)

        scad.run_super_scad(circle_sector, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_circle_sector_q3_q1c(self):
        """
        Test a circle sector that starts in quadrant 3 and ends in quadrant 1.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(context=Context(fn=360, eps=0.1))
        circle_sector = CircleSector(start_angle=269.99, end_angle=0.01, inner_radius=10.0, outer_radius=30.0)

        self.assertAlmostEqual(30.0, circle_sector.radius)
        self.assertAlmostEqual(10.0, circle_sector.inner_radius)
        self.assertAlmostEqual(30.0, circle_sector.outer_radius)
        self.assertAlmostEqual(90.02, circle_sector.angle)
        self.assertAlmostEqual(269.99, circle_sector.start_angle)
        self.assertAlmostEqual(0.01, circle_sector.end_angle)
        self.assertEqual(1, circle_sector.convexity)
        self.assertIsNone(circle_sector.fn4n)

        scad.run_super_scad(circle_sector, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_circle_sector_q4_q1a(self):
        """
        Test a circle sector that starts in quadrant 4 and ends in quadrant 1.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(context=Context(fn=360, eps=0.1))
        circle_sector = CircleSector(start_angle=350.0, end_angle=370.0, inner_radius=10.0, outer_radius=30.0)

        self.assertAlmostEqual(30.0, circle_sector.radius)
        self.assertAlmostEqual(10.0, circle_sector.inner_radius)
        self.assertAlmostEqual(30.0, circle_sector.outer_radius)
        self.assertAlmostEqual(20.0, circle_sector.angle)
        self.assertAlmostEqual(350.0, circle_sector.start_angle)
        self.assertAlmostEqual(10.0, circle_sector.end_angle)
        self.assertEqual(1, circle_sector.convexity)
        self.assertIsNone(circle_sector.fn4n)

        scad.run_super_scad(circle_sector, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_circle_sector_q4_q1b(self):
        """
        Test a circle sector that starts in quadrant 4 and ends in quadrant 1.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(context=Context(fn=360, eps=0.1))
        circle_sector = CircleSector(start_angle=270.01, end_angle=89.99, inner_radius=10.0, outer_radius=30.0)

        self.assertAlmostEqual(30.0, circle_sector.radius)
        self.assertAlmostEqual(10.0, circle_sector.inner_radius)
        self.assertAlmostEqual(30.0, circle_sector.outer_radius)
        self.assertAlmostEqual(179.98, circle_sector.angle)
        self.assertAlmostEqual(270.01, circle_sector.start_angle)
        self.assertAlmostEqual(89.99, circle_sector.end_angle)
        self.assertEqual(1, circle_sector.convexity)
        self.assertIsNone(circle_sector.fn4n)

        scad.run_super_scad(circle_sector, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_circle_sector_q1_q3a(self):
        """
        Test a circle sector that starts in quadrant 1 and ends in quadrant 3.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(context=Context(fn=360, eps=0.1))
        circle_sector = CircleSector(start_angle=15.0, end_angle=265.0, inner_radius=10.0, outer_radius=30.0)

        self.assertAlmostEqual(30.0, circle_sector.radius)
        self.assertAlmostEqual(10.0, circle_sector.inner_radius)
        self.assertAlmostEqual(30.0, circle_sector.outer_radius)
        self.assertAlmostEqual(250.0, circle_sector.angle)
        self.assertAlmostEqual(15.0, circle_sector.start_angle)
        self.assertAlmostEqual(265.0, circle_sector.end_angle)
        self.assertEqual(2, circle_sector.convexity)
        self.assertIsNone(circle_sector.fn4n)

        scad.run_super_scad(circle_sector, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_circle_sector_q1_q3b(self):
        """
        Test a circle sector that starts in quadrant 1 and ends in quadrant 3.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(context=Context(fn=360, eps=0.1))
        circle_sector = CircleSector(start_angle=0.01, end_angle=269.99, inner_radius=10.0, outer_radius=30.0)

        self.assertAlmostEqual(30.0, circle_sector.radius)
        self.assertAlmostEqual(10.0, circle_sector.inner_radius)
        self.assertAlmostEqual(30.0, circle_sector.outer_radius)
        self.assertAlmostEqual(269.98, circle_sector.angle)
        self.assertAlmostEqual(0.01, circle_sector.start_angle)
        self.assertAlmostEqual(269.99, circle_sector.end_angle)
        self.assertEqual(2, circle_sector.convexity)
        self.assertIsNone(circle_sector.fn4n)

        scad.run_super_scad(circle_sector, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_circle_sector_q1_q3c(self):
        """
        Test a circle sector that starts in quadrant 1 and ends in quadrant 3.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(context=Context(fn=360, eps=0.1))
        circle_sector = CircleSector(start_angle=89.99, end_angle=180.01, inner_radius=10.0, outer_radius=30.0)

        self.assertAlmostEqual(30.0, circle_sector.radius)
        self.assertAlmostEqual(10.0, circle_sector.inner_radius)
        self.assertAlmostEqual(30.0, circle_sector.outer_radius)
        self.assertAlmostEqual(90.02, circle_sector.angle)
        self.assertAlmostEqual(89.99, circle_sector.start_angle)
        self.assertAlmostEqual(180.01, circle_sector.end_angle)
        self.assertEqual(1, circle_sector.convexity)
        self.assertIsNone(circle_sector.fn4n)

        scad.run_super_scad(circle_sector, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_circle_sector_q2_q4a(self):
        """
        Test a circle sector that starts in quadrant 2 and ends in quadrant 4.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(context=Context(fn=360, eps=0.1))
        circle_sector = CircleSector(start_angle=105, end_angle=355.0, inner_radius=10.0, outer_radius=30.0)

        self.assertAlmostEqual(30.0, circle_sector.radius)
        self.assertAlmostEqual(10.0, circle_sector.inner_radius)
        self.assertAlmostEqual(30.0, circle_sector.outer_radius)
        self.assertAlmostEqual(250.0, circle_sector.angle)
        self.assertAlmostEqual(105.0, circle_sector.start_angle)
        self.assertAlmostEqual(355.0, circle_sector.end_angle)
        self.assertEqual(2, circle_sector.convexity)
        self.assertIsNone(circle_sector.fn4n)

        scad.run_super_scad(circle_sector, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_circle_sector_q2_q4b(self):
        """
        Test a circle sector that starts in quadrant 2 and ends in quadrant 4.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(context=Context(fn=360, eps=0.1))
        circle_sector = CircleSector(start_angle=90.01, end_angle=-0.01, inner_radius=10.0, outer_radius=30.0)

        self.assertAlmostEqual(30.0, circle_sector.radius)
        self.assertAlmostEqual(10.0, circle_sector.inner_radius)
        self.assertAlmostEqual(30.0, circle_sector.outer_radius)
        self.assertAlmostEqual(269.98, circle_sector.angle)
        self.assertAlmostEqual(90.01, circle_sector.start_angle)
        self.assertAlmostEqual(359.99, circle_sector.end_angle)
        self.assertEqual(2, circle_sector.convexity)
        self.assertIsNone(circle_sector.fn4n)

        scad.run_super_scad(circle_sector, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_circle_sector_q2_q4c(self):
        """
        Test a circle sector that starts in quadrant 2 and ends in quadrant 4.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(context=Context(fn=360, eps=0.1))
        circle_sector = CircleSector(start_angle=179.99, end_angle=-89.99, inner_radius=10.0, outer_radius=30.0)

        self.assertAlmostEqual(30.0, circle_sector.radius)
        self.assertAlmostEqual(10.0, circle_sector.inner_radius)
        self.assertAlmostEqual(30.0, circle_sector.outer_radius)
        self.assertAlmostEqual(90.02, circle_sector.angle)
        self.assertAlmostEqual(179.99, circle_sector.start_angle)
        self.assertAlmostEqual(270.01, circle_sector.end_angle)
        self.assertEqual(1, circle_sector.convexity)
        self.assertIsNone(circle_sector.fn4n)

        scad.run_super_scad(circle_sector, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_circle_sector_negative(self):
        """
        Test a circle sector with a negative angle.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(context=Context(fn=360, eps=0.1))
        circle_sector = CircleSector(angle=-20, radius=30.0)

        self.assertAlmostEqual(30.0, circle_sector.radius)
        self.assertAlmostEqual(0.0, circle_sector.inner_radius)
        self.assertAlmostEqual(30.0, circle_sector.outer_radius)
        self.assertAlmostEqual(20.0, circle_sector.angle)
        self.assertAlmostEqual(340.0, circle_sector.start_angle)
        self.assertAlmostEqual(0.0, circle_sector.end_angle)
        self.assertEqual(1, circle_sector.convexity)
        self.assertIsNone(circle_sector.fn4n)

        scad.run_super_scad(circle_sector, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_circle_sector_positive(self):
        """
        Test a circle sector with a positive angle.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(context=Context(fn=360, eps=0.1))
        circle_sector = CircleSector(angle=20, radius=30.0)

        self.assertAlmostEqual(30.0, circle_sector.radius)
        self.assertAlmostEqual(0.0, circle_sector.inner_radius)
        self.assertAlmostEqual(30.0, circle_sector.outer_radius)
        self.assertAlmostEqual(20.0, circle_sector.angle)
        self.assertAlmostEqual(0.0, circle_sector.start_angle)
        self.assertAlmostEqual(20.0, circle_sector.end_angle)
        self.assertEqual(1, circle_sector.convexity)
        self.assertIsNone(circle_sector.fn4n)

        scad.run_super_scad(circle_sector, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_circle_sector_missing_slice_q1a(self):
        """
        Test a circle sector with a positive angle.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(context=Context(fn=360, eps=0.1))
        circle_sector = CircleSector(start_angle=25, end_angle=15, radius=30.0)

        self.assertAlmostEqual(30.0, circle_sector.radius)
        self.assertAlmostEqual(0.0, circle_sector.inner_radius)
        self.assertAlmostEqual(30.0, circle_sector.outer_radius)
        self.assertAlmostEqual(350.0, circle_sector.angle)
        self.assertAlmostEqual(25.0, circle_sector.start_angle)
        self.assertAlmostEqual(15.0, circle_sector.end_angle)
        self.assertEqual(2, circle_sector.convexity)
        self.assertIsNone(circle_sector.fn4n)

        scad.run_super_scad(circle_sector, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_circle_sector_missing_slice_q1b(self):
        """
        Test a circle sector with a positive angle.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(context=Context(fn=360, eps=0.1))
        circle_sector = CircleSector(start_angle=25, end_angle=0.0, radius=30.0)

        self.assertAlmostEqual(30.0, circle_sector.radius)
        self.assertAlmostEqual(0.0, circle_sector.inner_radius)
        self.assertAlmostEqual(30.0, circle_sector.outer_radius)
        self.assertAlmostEqual(335.0, circle_sector.angle)
        self.assertAlmostEqual(25.0, circle_sector.start_angle)
        self.assertAlmostEqual(0.0, circle_sector.end_angle)
        self.assertEqual(2, circle_sector.convexity)
        self.assertIsNone(circle_sector.fn4n)

        scad.run_super_scad(circle_sector, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_circle_sector_missing_slice_q2(self):
        """
        Test a circle sector with a positive angle.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(context=Context(fn=360, eps=0.1))
        circle_sector = CircleSector(start_angle=110, end_angle=95, radius=30.0)

        self.assertAlmostEqual(30.0, circle_sector.radius)
        self.assertAlmostEqual(0.0, circle_sector.inner_radius)
        self.assertAlmostEqual(30.0, circle_sector.outer_radius)
        self.assertAlmostEqual(345.0, circle_sector.angle)
        self.assertAlmostEqual(110.0, circle_sector.start_angle)
        self.assertAlmostEqual(95.0, circle_sector.end_angle)
        self.assertEqual(2, circle_sector.convexity)
        self.assertIsNone(circle_sector.fn4n)

        scad.run_super_scad(circle_sector, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_circle_sector_missing_slice_q3(self):
        """
        Test a circle sector with a positive angle.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(context=Context(fn=360, eps=0.1))
        circle_sector = CircleSector(start_angle=269, end_angle=181, radius=30.0)

        self.assertAlmostEqual(30.0, circle_sector.radius)
        self.assertAlmostEqual(0.0, circle_sector.inner_radius)
        self.assertAlmostEqual(30.0, circle_sector.outer_radius)
        self.assertAlmostEqual(272.0, circle_sector.angle)
        self.assertAlmostEqual(269.0, circle_sector.start_angle)
        self.assertAlmostEqual(181.0, circle_sector.end_angle)
        self.assertEqual(2, circle_sector.convexity)
        self.assertIsNone(circle_sector.fn4n)

        scad.run_super_scad(circle_sector, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_circle_sector_missing_slice_q4a(self):
        """
        Test a circle sector with a positive angle.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(context=Context(fn=360, eps=0.1))
        circle_sector = CircleSector(start_angle=-30, end_angle=-40, radius=30.0)

        self.assertAlmostEqual(30.0, circle_sector.radius)
        self.assertAlmostEqual(0.0, circle_sector.inner_radius)
        self.assertAlmostEqual(30.0, circle_sector.outer_radius)
        self.assertAlmostEqual(350.0, circle_sector.angle)
        self.assertAlmostEqual(330.0, circle_sector.start_angle)
        self.assertAlmostEqual(320.0, circle_sector.end_angle)
        self.assertEqual(2, circle_sector.convexity)
        self.assertIsNone(circle_sector.fn4n)

        scad.run_super_scad(circle_sector, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_circle_sector_missing_slice_q4b(self):
        """
        Test a circle sector with a positive angle.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(context=Context(fn=360, eps=0.1))
        circle_sector = CircleSector(start_angle=0.0, end_angle=-40, radius=30.0)

        self.assertAlmostEqual(30.0, circle_sector.radius)
        self.assertAlmostEqual(0.0, circle_sector.inner_radius)
        self.assertAlmostEqual(30.0, circle_sector.outer_radius)
        self.assertAlmostEqual(320.0, circle_sector.angle)
        self.assertAlmostEqual(0.0, circle_sector.start_angle)
        self.assertAlmostEqual(320.0, circle_sector.end_angle)
        self.assertEqual(2, circle_sector.convexity)
        self.assertIsNone(circle_sector.fn4n)

        scad.run_super_scad(circle_sector, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def xtest_imperial_metric_circle_sector(self):
        path_actual, path_expected = self.paths()

        scad = Scad(context=Context(fn=360, eps=0.1))
        circle_sector = ImperialCircleSector(start_angle=15.0,
                                             end_angle=-15.0,
                                             radius=30.0,
                                             fa=12.0,
                                             fs=2.0,
                                             fn=0)

        scad.run_super_scad(circle_sector, path_actual)

        self.assertAlmostEqual(330.0, circle_sector.imperial_circle_sector.angle)
        self.assertAlmostEqual(15.0, circle_sector.imperial_circle_sector.start_angle)
        self.assertAlmostEqual(345.0, circle_sector.imperial_circle_sector.end_angle)
        self.assertAlmostEqual(30.0 * 25.4, circle_sector.imperial_circle_sector.radius)
        self.assertAlmostEqual(0.0, circle_sector.imperial_circle_sector.inner_radius)
        self.assertAlmostEqual(30.0 * 25.4, circle_sector.imperial_circle_sector.outer_radius)
        self.assertAlmostEqual(12.0, circle_sector.imperial_circle_sector.fa)
        self.assertAlmostEqual(2.0 * 25.4, circle_sector.imperial_circle_sector.fs)
        self.assertEqual(0, circle_sector.imperial_circle_sector.fn)
        self.assertIsNone(circle_sector.imperial_circle_sector.fn4n)
        self.assertEqual(2, circle_sector.imperial_circle_sector.convexity)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def xtest_imperial_imperial_circle_sector(self):
        path_actual, path_expected = self.paths()

        scad = Scad(context=Context(unit_length_final=Unit.INCH, fn=360, eps=0.1))
        circle_sector = ImperialCircleSector(start_angle=15.0,
                                             end_angle=-15.0,
                                             radius=30.0,
                                             fa=12.0,
                                             fs=2.0,
                                             fn=0)

        scad.run_super_scad(circle_sector, path_actual)

        self.assertAlmostEqual(330.0, circle_sector.imperial_circle_sector.angle)
        self.assertAlmostEqual(15.0, circle_sector.imperial_circle_sector.start_angle)
        self.assertAlmostEqual(345.0, circle_sector.imperial_circle_sector.end_angle)
        self.assertAlmostEqual(30.0, circle_sector.imperial_circle_sector.radius)
        self.assertAlmostEqual(0.0, circle_sector.imperial_circle_sector.inner_radius)
        self.assertAlmostEqual(30.0, circle_sector.imperial_circle_sector.outer_radius)
        self.assertAlmostEqual(12.0, circle_sector.imperial_circle_sector.fa)
        self.assertAlmostEqual(2.0, circle_sector.imperial_circle_sector.fs)
        self.assertEqual(0, circle_sector.imperial_circle_sector.fn)
        self.assertIsNone(circle_sector.imperial_circle_sector.fn4n)
        self.assertEqual(2, circle_sector.imperial_circle_sector.convexity)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

# ----------------------------------------------------------------------------------------------------------------------

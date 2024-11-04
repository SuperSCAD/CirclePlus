from super_scad.scad.Context import Context
from super_scad.scad.Scad import Scad
from super_scad.scad.Unit import Unit

from super_scad_circle_sector.CircleSector import CircleSector
from test.CircleSector.ImperialCircleSector import ImperialCircleSector
from test.ScadTestCase import ScadTestCase


class CircleSectorTest(ScadTestCase):
    """
    Test cases for CircleSector.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def testCircleSector4n(self):
        """
        Test a pie slice based on a circle with a multiple of 4 vertices.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(context=Context())
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
    def testCircleSectorQ1(self):
        """
        Test a pie slice that start lies quadrant 1.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(context=Context())
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
    def testCircleSectorQ2(self):
        """
        Test a pie slice that start lies quadrant 2.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(context=Context())
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
    def testCircleSectorQ3(self):
        """
        Test a pie slice that start lies quadrant 3.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(context=Context())
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
    def testCircleSectorQ4(self):
        """
        Test a pie slice that start lies quadrant 4.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(context=Context())
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
    def testCircleSectorIsQ1(self):
        """
        Test a pie slice that is quadrant 1.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(context=Context())
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
    def testCircleSectorIsQ2(self):
        """
        Test a pie slice that is quadrant 2.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(context=Context())
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
    def testCircleSectorIsQ3(self):
        """
        Test a pie slice that is quadrant 3.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(context=Context())
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
    def testCircleSectorIsQ4(self):
        """
        Test a pie slice that is quadrant 4.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(context=Context())
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
    def testCircleSectorIsQ1Q2(self):
        """
        Test a pie slice that is quadrant 1 & 2.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(context=Context())
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
    def testCircleSectorIsQ2Q3(self):
        """
        Test a pie slice that is quadrant 2 & 3.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(context=Context())
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
    def testCircleSectorIsQ3Q4(self):
        """
        Test a pie slice that is quadrant 3 & 4.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(context=Context())
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
    def testCircleSectorIsQ4Q1(self):
        """
        Test a pie slice that is quadrant 3 & 4.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(context=Context())
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
    def testCircleSectorIsQ1Q2Q3(self):
        """
        Test a pie slice that is quadrant 1, 2, & 3.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(context=Context())
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
    def testCircleSectorIsQ2Q3Q4(self):
        """
        Test a pie slice that is quadrant 2, 3 & 4.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(context=Context())
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
    def testCircleSectorIsQ3Q4Q1(self):
        """
        Test a pie slice that is quadrant 3, 4 & 1.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(context=Context())
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
    def testCircleSectorIsQ4Q1Q2(self):
        """
        Test a pie slice that is quadrant 4, 1 & 2.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(context=Context())
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
    def testCircleSectorIsQ1Q2Q3Q4(self):
        """
        Test a pie slice that is quadrant 1, 2, 3, & 4.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(context=Context())
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
    def testCircleSectorQ1Q2(self):
        """
        Test a pie slice that start in quadrant 1 and ends in quadrant 2.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(context=Context())
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
    def testCircleSectorQ2Q3(self):
        """
        Test a pie slice that start in quadrant 2 and ends in quadrant 3.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(context=Context())
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
    def testCircleSectorQ3Q4(self):
        """
        Test a pie slice that start in quadrant 3 and ends in quadrant 4.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(context=Context())
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
    def testCircleSectorQ3Q1b(self):
        """
        Test a pie slice that start in quadrant 3 and ends in quadrant 1.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(context=Context())
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
    def testCircleSectorQ3Q1c(self):
        """
        Test a pie slice that start in quadrant 3 and ends in quadrant 1.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(context=Context())
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
    def testCircleSectorQ4Q1a(self):
        """
        Test a pie slice that start in quadrant 4 and ends in quadrant 1.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(context=Context())
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
    def testCircleSectorQ4Q1b(self):
        """
        Test a pie slice that start in quadrant 4 and ends in quadrant 1.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(context=Context())
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
    def testCircleSectorQ1Q3a(self):
        """
        Test a pie slice that start in quadrant 1 and ends in quadrant 3.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(context=Context())
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
    def testCircleSectorQ1Q3b(self):
        """
        Test a pie slice that start in quadrant 1 and ends in quadrant 3.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(context=Context())
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
    def testCircleSectorQ1Q3c(self):
        """
        Test a pie slice that start in quadrant 1 and ends in quadrant 3.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(context=Context())
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
    def testCircleSectorQ2Q4a(self):
        """
        Test a pie slice that start in quadrant 2 and ends in quadrant 4.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(context=Context())
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
    def testCircleSectorQ2Q4b(self):
        """
        Test a pie slice that start in quadrant 2 and ends in quadrant 4.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(context=Context())
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
    def testCircleSectorQ2Q4c(self):
        """
        Test a pie slice that start in quadrant 2 and ends in quadrant 4.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(context=Context())
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
    def testCircleSectorNegative(self):
        """
        Test a pie slice with a negative angle.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(context=Context())
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
    def testCircleSectorPositive(self):
        """
        Test a pie slice with a positive angle.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(context=Context())
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
    def testCircleSectorMissingSliceQ1a(self):
        """
        Test a pie slice with a positive angle.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(context=Context())
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
    def testCircleSectorMissingSliceQ1b(self):
        """
        Test a pie slice with a positive angle.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(context=Context())
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
    def testCircleSectorMissingSliceQ2(self):
        """
        Test a pie slice with a positive angle.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(context=Context())
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
    def testCircleSectorMissingSliceQ3(self):
        """
        Test a pie slice with a positive angle.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(context=Context())
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
    def testCircleSectorMissingSliceQ4a(self):
        """
        Test a pie slice with a positive angle.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(context=Context())
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
    def testCircleSectorMissingSliceQ4b(self):
        """
        Test a pie slice with a positive angle.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(context=Context())
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
    def testImperialMetricCircleSector(self):
        path_actual, path_expected = self.paths()

        scad = Scad(context=Context())
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
    def testImperialImperialCircleSector(self):
        path_actual, path_expected = self.paths()

        scad = Scad(context=Context(unit_length_final=Unit.INCH))
        scad = Scad(context=Context(unit_length_final=Unit.INCH))
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

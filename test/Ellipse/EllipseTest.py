from super_scad.scad.Context import Context
from super_scad.scad.Scad import Scad
from super_scad.scad.Unit import Unit

from super_scad_circle_plus.Ellipse import Ellipse
from test.Ellipse.ImperialUnitEllipse import ImperialUnitEllipse
from test.ScadTestCase import ScadTestCase


class EllipseTest(ScadTestCase):
    """
    Test cases for Ellipse.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def testEllipseByRadius(self):
        """
        Test a plain ellipse defend by radius.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(context=Context())
        ellipse = Ellipse(radius_x=20.0, radius_y=10.0)

        self.assertAlmostEqual(20.0, ellipse.radius_x)
        self.assertAlmostEqual(10.0, ellipse.radius_y)
        self.assertAlmostEqual(40.0, ellipse.diameter_x)
        self.assertAlmostEqual(20.0, ellipse.diameter_y)
        self.assertIsNone(ellipse.fa)
        self.assertIsNone(ellipse.fs)
        self.assertIsNone(ellipse.fn)

        scad.run_super_scad(ellipse, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testEllipseByDiameter(self):
        """
        Test a plain ellipse defend by diameter.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(context=Context())
        ellipse = Ellipse(diameter_x=40.0, diameter_y=20.0)

        self.assertAlmostEqual(20.0, ellipse.radius_x)
        self.assertAlmostEqual(10.0, ellipse.radius_y)
        self.assertAlmostEqual(40.0, ellipse.diameter_x)
        self.assertAlmostEqual(20.0, ellipse.diameter_y)
        self.assertIsNone(ellipse.fa)
        self.assertIsNone(ellipse.fs)
        self.assertIsNone(ellipse.fn)

        scad.run_super_scad(ellipse, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testEllipse4n(self):
        """
        Test a plain ellipse with a multiple of 4 vertices.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(context=Context())
        ellipse = Ellipse(radius_x=20.0, radius_y=10.0, fn4n=True)

        self.assertAlmostEqual(20.0, ellipse.radius_x)
        self.assertAlmostEqual(10.0, ellipse.radius_y)
        self.assertAlmostEqual(40.0, ellipse.diameter_x)
        self.assertAlmostEqual(20.0, ellipse.diameter_y)
        self.assertIsNone(ellipse.fa)
        self.assertIsNone(ellipse.fs)
        self.assertIsNone(ellipse.fn)
        self.assertTrue(ellipse.fn4n)

        scad.run_super_scad(ellipse, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testEllipseAuxiliaryParameter(self):
        """
        Test auxiliary parameters.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(context=Context())
        ellipse = Ellipse(diameter_x=20.0, diameter_y=20.0, fa=12.0, fs=2.0, fn=0)

        self.assertAlmostEqual(10.0, ellipse.radius_x)
        self.assertAlmostEqual(10.0, ellipse.radius_y)
        self.assertAlmostEqual(20.0, ellipse.diameter_x)
        self.assertAlmostEqual(20.0, ellipse.diameter_y)
        self.assertAlmostEqual(12.0, ellipse.fa)
        self.assertAlmostEqual(2.0, ellipse.fs)
        self.assertEqual(0, ellipse.fn)
        self.assertFalse(ellipse.fn4n)

        scad.run_super_scad(ellipse, path_actual)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def xtestImperialMetricEllipse(self):
        """
        Test for an imperial unit ellipse in metric units.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(context=Context())
        ellipse = ImperialUnitEllipse()
        scad.run_super_scad(ellipse, path_actual)

        self.assertAlmostEqual(50.8, ellipse.imperial_ellipse.radius_x)
        self.assertAlmostEqual(25.4, ellipse.imperial_ellipse.radius_y)
        self.assertAlmostEqual(101.6, ellipse.imperial_ellipse.diameter_x)
        self.assertAlmostEqual(50.8, ellipse.imperial_ellipse.diameter_y)
        self.assertIsNone(ellipse.imperial_ellipse.fa)
        self.assertIsNone(ellipse.imperial_ellipse.fs)
        self.assertIsNone(ellipse.imperial_ellipse.fn)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testImperialImperialEllipse(self):
        """
        Test for an imperial unit ellipse in imperial units.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(context=Context(unit_length_final=Unit.INCH))
        ellipse = ImperialUnitEllipse()
        scad.run_super_scad(ellipse, path_actual)

        self.assertAlmostEqual(2.0, ellipse.imperial_ellipse.radius_x)
        self.assertAlmostEqual(1.0, ellipse.imperial_ellipse.radius_y)
        self.assertAlmostEqual(4.0, ellipse.imperial_ellipse.diameter_x)
        self.assertAlmostEqual(2.0, ellipse.imperial_ellipse.diameter_y)
        self.assertIsNone(ellipse.imperial_ellipse.fa)
        self.assertIsNone(ellipse.imperial_ellipse.fs)
        self.assertIsNone(ellipse.imperial_ellipse.fn)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

# ----------------------------------------------------------------------------------------------------------------------

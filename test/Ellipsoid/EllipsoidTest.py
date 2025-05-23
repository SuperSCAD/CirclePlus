from super_scad.scad.Context import Context
from super_scad.scad.Scad import Scad
from super_scad.scad.Unit import Unit

from super_scad_circle_plus.Ellipsoid import Ellipsoid
from test.Ellipsoid.ImperialEllipsoid import ImperialEllipsoid
from test.ScadTestCase import ScadTestCase


class EllipsoidTestCase(ScadTestCase):
    """
    Testcases for Ellipsoid.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def testEllipsoidRadius(self):
        """
        Test for an ellipsoid defined by radii.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(context=Context())
        ellipsoid = Ellipsoid(radius_x=30.0, radius_y=20.0, radius_z=10.0)

        self.assertAlmostEqual(30.0, ellipsoid.radius_x)
        self.assertAlmostEqual(20.0, ellipsoid.radius_y)
        self.assertAlmostEqual(10.0, ellipsoid.radius_z)
        self.assertAlmostEqual(60.0, ellipsoid.diameter_x)
        self.assertAlmostEqual(40.0, ellipsoid.diameter_y)
        self.assertAlmostEqual(20.0, ellipsoid.diameter_z)
        self.assertIsNone(ellipsoid.fa)
        self.assertIsNone(ellipsoid.fs)
        self.assertIsNone(ellipsoid.fn)

        scad.run_super_scad(ellipsoid, path_actual)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testEllipsoidDiameter(self):
        """
        Test for an ellipsoid defined by diameters.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(context=Context())
        ellipsoid = Ellipsoid(diameter_x=30.0, diameter_y=20.0, diameter_z=10.0)

        self.assertAlmostEqual(15.0, ellipsoid.radius_x)
        self.assertAlmostEqual(10.0, ellipsoid.radius_y)
        self.assertAlmostEqual(5.0, ellipsoid.radius_z)
        self.assertAlmostEqual(30.0, ellipsoid.diameter_x)
        self.assertAlmostEqual(20.0, ellipsoid.diameter_y)
        self.assertAlmostEqual(10.0, ellipsoid.diameter_z)
        self.assertIsNone(ellipsoid.fa)
        self.assertIsNone(ellipsoid.fs)
        self.assertIsNone(ellipsoid.fn)

        scad.run_super_scad(ellipsoid, path_actual)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testEllipsoid4n(self):
        """
        Test for an ellipsoid with a multiple of 4 vertices.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(context=Context())
        ellipsoid = Ellipsoid(radius_x=30.0, radius_y=20.0, radius_z=10.0, fn4n=True)

        self.assertAlmostEqual(30.0, ellipsoid.radius_x)
        self.assertAlmostEqual(20.0, ellipsoid.radius_y)
        self.assertAlmostEqual(10.0, ellipsoid.radius_z)
        self.assertAlmostEqual(60.0, ellipsoid.diameter_x)
        self.assertAlmostEqual(40.0, ellipsoid.diameter_y)
        self.assertAlmostEqual(20.0, ellipsoid.diameter_z)
        self.assertIsNone(ellipsoid.fa)
        self.assertIsNone(ellipsoid.fs)
        self.assertIsNone(ellipsoid.fn)
        self.assertTrue(ellipsoid.fn4n)

        scad.run_super_scad(ellipsoid, path_actual)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testEllipsoidAuxiliaryParameter(self):
        """
        Test auxiliary parameters.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(context=Context())
        ellipsoid = Ellipsoid(diameter_x=30.0, diameter_y=20.0, diameter_z=10.0, fa=12.0, fs=2.0, fn=0)

        self.assertAlmostEqual(15.0, ellipsoid.radius_x)
        self.assertAlmostEqual(10.0, ellipsoid.radius_y)
        self.assertAlmostEqual(5.0, ellipsoid.radius_z)
        self.assertAlmostEqual(30.0, ellipsoid.diameter_x)
        self.assertAlmostEqual(20.0, ellipsoid.diameter_y)
        self.assertAlmostEqual(10.0, ellipsoid.diameter_z)
        self.assertAlmostEqual(12.0, ellipsoid.fa)
        self.assertAlmostEqual(2.0, ellipsoid.fs)
        self.assertEqual(0, ellipsoid.fn)
        self.assertFalse(ellipsoid.fn4n)

        scad.run_super_scad(ellipsoid, path_actual)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def xtestImperialMetricEllipsoid(self):
        """
        Test for an imperial ellipsoid in metric units.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(context=Context())
        ellipsoid = ImperialEllipsoid(radius_x=30.0, radius_y=20.0, radius_z=10.0, fa=12.0, fs=2.0, fn=0)
        scad.run_super_scad(ellipsoid, path_actual)

        self.assertAlmostEqual(762.0, ellipsoid.imperial_ellipsoid.radius_x)
        self.assertAlmostEqual(508.0, ellipsoid.imperial_ellipsoid.radius_y)
        self.assertAlmostEqual(254.0, ellipsoid.imperial_ellipsoid.radius_z)
        self.assertAlmostEqual(1524.0, ellipsoid.imperial_ellipsoid.diameter_x)
        self.assertAlmostEqual(1016.0, ellipsoid.imperial_ellipsoid.diameter_y)
        self.assertAlmostEqual(508.0, ellipsoid.imperial_ellipsoid.diameter_z)
        self.assertAlmostEqual(12.0, ellipsoid.imperial_ellipsoid.fa)
        self.assertAlmostEqual(50.8, ellipsoid.imperial_ellipsoid.fs)
        self.assertEqual(0, ellipsoid.imperial_ellipsoid.fn)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testImperialImperialEllipsoid(self):
        """
        Test for an imperial ellipsoid in imperial units.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(context=Context(unit_length_final=Unit.INCH))
        ellipsoid = ImperialEllipsoid(radius_x=30.0, radius_y=20.0, radius_z=10.0, fa=12.0, fs=2.0, fn=0)
        scad.run_super_scad(ellipsoid, path_actual)

        self.assertAlmostEqual(30.0, ellipsoid.imperial_ellipsoid.radius_x)
        self.assertAlmostEqual(20.0, ellipsoid.imperial_ellipsoid.radius_y)
        self.assertAlmostEqual(10.0, ellipsoid.imperial_ellipsoid.radius_z)
        self.assertAlmostEqual(60.0, ellipsoid.imperial_ellipsoid.diameter_x)
        self.assertAlmostEqual(40.0, ellipsoid.imperial_ellipsoid.diameter_y)
        self.assertAlmostEqual(20.0, ellipsoid.imperial_ellipsoid.diameter_z)
        self.assertAlmostEqual(12.0, ellipsoid.imperial_ellipsoid.fa)
        self.assertAlmostEqual(2.0, ellipsoid.imperial_ellipsoid.fs)
        self.assertEqual(0, ellipsoid.imperial_ellipsoid.fn)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

# ----------------------------------------------------------------------------------------------------------------------

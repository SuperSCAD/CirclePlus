from super_scad.scad.Context import Context
from super_scad.scad.ScadWidget import ScadWidget
from super_scad.scad.Unit import Unit

from super_scad_circle_sector.CircleSector import CircleSector


class ImperialCircleSector(ScadWidget):
    """
    Class for imperial circle sector.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self,
                 *,
                 angle: float | None = None,
                 start_angle: float | None = None,
                 end_angle: float | None = None,
                 radius: float | None = None,
                 inner_radius: float | None = None,
                 outer_radius: float | None = None,
                 fa: float | None = None,
                 fs: float | None = None,
                 fn: int | None = None):
        """
        Object constructor.
        """
        ScadWidget.__init__(self)
        
        self._angle = angle
        self._start_angle = start_angle
        self._end_angle = end_angle
        self._radius = radius
        self._inner_radius = inner_radius
        self._outer_radius = outer_radius
        self._fa = fa
        self._fs = fs
        self._fn = fn

        self.imperial_circle_sector: CircleSector | None = None
        """
        The imperial sphere.
        """

    # ------------------------------------------------------------------------------------------------------------------
    def build(self, context: Context) -> ScadWidget:
        """
        Builds a SuperSCAD widget.

        :param context: The build context.
        """
        Context.set_unit_length_current(Unit.INCH)

        self.imperial_circle_sector = CircleSector(angle=self._angle,
                                                   start_angle=self._start_angle,
                                                   end_angle=self._end_angle,
                                                   radius=self._radius,
                                                   inner_radius=self._inner_radius,
                                                   outer_radius=self._outer_radius,
                                                   fa=self._fa,
                                                   fs=self._fs,
                                                   fn=self._fn)

        return self.imperial_circle_sector

# ----------------------------------------------------------------------------------------------------------------------

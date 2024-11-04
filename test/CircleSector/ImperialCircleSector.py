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
        ScadWidget.__init__(self, args=locals())

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

        self.imperial_circle_sector = CircleSector(angle=self._args.get('angle'),
                                                   start_angle=self._args.get('start_angle'),
                                                   end_angle=self._args.get('end_angle'),
                                                   radius=self._args.get('radius'),
                                                   inner_radius=self._args.get('inner_radius'),
                                                   outer_radius=self._args.get('outer_radius'),
                                                   fa=self._args.get('fa'),
                                                   fs=self._args.get('fs'),
                                                   fn=self._args.get('fn'))

        return self.imperial_circle_sector

# ----------------------------------------------------------------------------------------------------------------------

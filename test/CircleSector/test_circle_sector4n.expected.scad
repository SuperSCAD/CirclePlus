// Unit of length: Unit.MM
$fn = 360;

intersection()
{
   difference()
   {
      circle(d = 60.0, $fn = 360);
      circle(d = 20.0, $fn = 360);
   }
   polygon(points = [[0.0, 0.0], [36.0668, 6.3596], [36.1376, 6.4303], [6.4303, 36.1376], [6.3596, 36.0668]], convexity = 1);
}

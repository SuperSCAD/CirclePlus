// Unit of length: Unit.MM
$fn = 360;

intersection()
{
   difference()
   {
      circle(d = 60.0);
      circle(d = 20.0);
   }
   polygon(points = [[0.0, 0.0], [6.3596, -36.0668], [6.4303, -36.1376], [36.1376, -6.4303], [36.0668, -6.3596]], convexity = 1);
}

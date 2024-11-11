// Unit of length: Unit.MM
$fn = 360;

intersection()
{
   difference()
   {
      circle(d = 60.0);
      circle(d = 20.0);
   }
   polygon(points = [[0.0, 0.0], [-30.0, 0.0052], [-30.1, 0.0052], [-30.1, -30.1], [0.0052, -30.1], [0.0052, -30.0]], convexity = 1);
}

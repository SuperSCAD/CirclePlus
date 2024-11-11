// Unit of length: Unit.MM
$fn = 360;

intersection()
{
   difference()
   {
      circle(d = 60.0);
      circle(d = 20.0);
   }
   polygon(points = [[0.0, 0.0], [-5.2898, -30.0], [-5.2898, -30.1], [5.2898, -30.1], [5.2898, -30.0]], convexity = 1);
}

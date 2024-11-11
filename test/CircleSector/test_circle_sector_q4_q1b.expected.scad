// Unit of length: Unit.MM
$fn = 360;

intersection()
{
   difference()
   {
      circle(d = 60.0);
      circle(d = 20.0);
   }
   polygon(points = [[0.0, 0.0], [0.0074, -42.419], [0.0781, -42.4897], [42.5678, 0.0], [0.0781, 42.4897], [0.0074, 42.419]], convexity = 1);
}

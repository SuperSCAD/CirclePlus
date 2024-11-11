// Unit of length: Unit.MM
$fn = 360;

intersection()
{
   difference()
   {
      circle(d = 60.0);
      circle(d = 20.0);
   }
   polygon(points = [[0.0, 0.0], [29.4248, 7.8844], [29.5244, 7.8931], [27.3621, 32.6088], [-32.6088, 27.3621], [-27.3621, -32.6088], [-2.6463, -30.4465], [-2.655, -30.3469]], convexity = 2);
}

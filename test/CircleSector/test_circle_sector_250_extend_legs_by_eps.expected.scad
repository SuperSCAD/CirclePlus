// Unit of length: Unit.MM
$fn = 360;

difference()
{
   color(c = [1.0, 0.0, 0.0, 1.0])
   {
      intersection()
      {
         circle(d = 20.0);
         polygon(points = [[0.0863, -0.0863], [10.1, 1.6794], [10.1, 10.1], [-10.1, 10.1], [-10.1, -10.1], [-1.6794, -10.1]], convexity = 2);
      }
   }
   intersection()
   {
      circle(d = 20.0);
      polygon(points = [[0.0, 0.0], [10.0, 1.7633], [10.1, 1.7633], [10.1, 10.1], [-10.1, 10.1], [-10.1, -10.1], [-1.7633, -10.1], [-1.7633, -10.0]], convexity = 2);
   }
}

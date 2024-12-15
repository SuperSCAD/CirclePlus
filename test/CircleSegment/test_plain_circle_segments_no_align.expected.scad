// Unit of length: Unit.MM
$fn = 60;

union()
{
   translate(v = [0.0, 0.1])
   {
      intersection()
      {
         circle(d = 20.0);
         polygon(points = [[-9.2388, 3.8268], [-9.2388, 10.0], [9.2388, 10.0], [9.2388, 3.8268]]);
      }
   }
   translate(v = [0.0, -0.1])
   {
      intersection()
      {
         circle(d = 20.0);
         polygon(points = [[-10.0, -10.0], [-10.0, 3.8268], [10.0, 3.8268], [10.0, -10.0]]);
      }
   }
}

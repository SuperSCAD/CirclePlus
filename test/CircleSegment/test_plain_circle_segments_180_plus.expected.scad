// Unit of length: Unit.MM
$fn = 60;

union()
{
   translate(v = [0.0, 0.1])
   {
      translate(v = [0.0, 2.5882])
      {
         intersection()
         {
            circle(d = 20.0);
            polygon(points = [[-10.0, -2.5882], [-10.0, 10.0], [10.0, 10.0], [10.0, -2.5882]]);
         }
      }
   }
   translate(v = [0.0, -0.1])
   {
      translate(v = [0.0, 2.5882])
      {
         intersection()
         {
            circle(d = 20.0);
            polygon(points = [[-9.6593, -10.0], [-9.6593, -2.5882], [9.6593, -2.5882], [9.6593, -10.0]]);
         }
      }
   }
}

// Unit of length: Unit.MM
$fn = 60;
$vpr = [0.0, 0.0, 0.0];

union()
{
   translate(v = [0.0, 0.1])
   {
      union()
      {
         color(c = [1.0, 0.0, 0.0, 1.0])
         {
            linear_extrude(height = 1.0, center = false, twist = 0.0, scale = 1.0)
            {
               translate(v = [0.0, -3.8268])
               {
                  intersection()
                  {
                     circle(d = 22.0);
                     polygon(points = [[-10.1627, 3.8268], [-10.1627, 11.0], [10.1627, 11.0], [10.1627, 3.8268]]);
                  }
               }
            }
         }
         translate(v = [0.0, 0.0, 0.0])
         {
            linear_extrude(height = 2.0, center = false, twist = 0.0, scale = 1.0)
            {
               translate(v = [0.0, -3.8268])
               {
                  intersection()
                  {
                     circle(d = 20.0);
                     polygon(points = [[-9.2388, 3.8268], [-9.2388, 10.0], [9.2388, 10.0], [9.2388, 3.8268]]);
                  }
               }
            }
         }
      }
   }
   translate(v = [0.0, -0.1])
   {
      union()
      {
         color(c = [1.0, 0.0, 0.0, 1.0])
         {
            linear_extrude(height = 1.0, center = false, twist = 0.0, scale = 1.0)
            {
               translate(v = [0.0, -3.8268])
               {
                  intersection()
                  {
                     circle(d = 22.0);
                     polygon(points = [[-11.0, -11.0], [-11.0, 3.8268], [11.0, 3.8268], [11.0, -11.0]]);
                  }
               }
            }
         }
         translate(v = [0.0, 0.0, 0.0])
         {
            linear_extrude(height = 2.0, center = false, twist = 0.0, scale = 1.0)
            {
               translate(v = [0.0, -3.8268])
               {
                  intersection()
                  {
                     circle(d = 20.0);
                     polygon(points = [[-10.0, -10.0], [-10.0, 3.8268], [10.0, 3.8268], [10.0, -10.0]]);
                  }
               }
            }
         }
      }
   }
}

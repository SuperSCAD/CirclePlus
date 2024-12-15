// Unit of length: Unit.MM
$fn = 60;
$vpr = [0.0, 0.0, 0.0];

union()
{
   translate(v = [0.0, 1.1])
   {
      union()
      {
         color(c = [1.0, 0.0, 0.0, 1.0])
         {
            linear_extrude(height = 1.0, center = false, twist = 0.0, scale = 1.0)
            {
               translate(v = [0.0, 7.0711])
               {
                  intersection()
                  {
                     circle(d = 20.0);
                     polygon(points = [[-10.0, -8.0711], [-10.0, 10.0], [10.0, 10.0], [10.0, -8.0711]]);
                  }
               }
            }
         }
         translate(v = [0.0, 0.0, 0.0])
         {
            linear_extrude(height = 2.0, center = false, twist = 0.0, scale = 1.0)
            {
               translate(v = [0.0, 7.0711])
               {
                  intersection()
                  {
                     circle(d = 20.0);
                     polygon(points = [[-10.0, -7.0711], [-10.0, 10.0], [10.0, 10.0], [10.0, -7.0711]]);
                  }
               }
            }
         }
      }
   }
   translate(v = [0.0, -1.1])
   {
      union()
      {
         color(c = [1.0, 0.0, 0.0, 1.0])
         {
            linear_extrude(height = 1.0, center = false, twist = 0.0, scale = 1.0)
            {
               translate(v = [0.0, 7.0711])
               {
                  intersection()
                  {
                     circle(d = 20.0);
                     polygon(points = [[-7.0711, -10.0], [-7.0711, -6.0711], [7.0711, -6.0711], [7.0711, -10.0]]);
                  }
               }
            }
         }
         translate(v = [0.0, 0.0, 0.0])
         {
            linear_extrude(height = 2.0, center = false, twist = 0.0, scale = 1.0)
            {
               translate(v = [0.0, 7.0711])
               {
                  intersection()
                  {
                     circle(d = 20.0);
                     polygon(points = [[-7.0711, -10.0], [-7.0711, -7.0711], [7.0711, -7.0711], [7.0711, -10.0]]);
                  }
               }
            }
         }
      }
   }
}

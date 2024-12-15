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
               translate(v = [0.0, -6.4279])
               {
                  intersection()
                  {
                     circle(d = 22.0);
                     polygon(points = [[-8.4265, 5.4279], [-8.4265, 11.0], [8.4265, 11.0], [8.4265, 5.4279]]);
                  }
               }
            }
         }
         translate(v = [0.0, 0.0, 0.0])
         {
            linear_extrude(height = 2.0, center = false, twist = 0.0, scale = 1.0)
            {
               translate(v = [0.0, -6.4279])
               {
                  intersection()
                  {
                     circle(d = 20.0);
                     polygon(points = [[-7.6604, 6.4279], [-7.6604, 10.0], [7.6604, 10.0], [7.6604, 6.4279]]);
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
               translate(v = [0.0, -6.4279])
               {
                  intersection()
                  {
                     circle(d = 22.0);
                     polygon(points = [[-11.0, -11.0], [-11.0, 7.4279], [11.0, 7.4279], [11.0, -11.0]]);
                  }
               }
            }
         }
         translate(v = [0.0, 0.0, 0.0])
         {
            linear_extrude(height = 2.0, center = false, twist = 0.0, scale = 1.0)
            {
               translate(v = [0.0, -6.4279])
               {
                  intersection()
                  {
                     circle(d = 20.0);
                     polygon(points = [[-10.0, -10.0], [-10.0, 6.4279], [10.0, 6.4279], [10.0, -10.0]]);
                  }
               }
            }
         }
      }
   }
}

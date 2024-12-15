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
               translate(v = [0.0, 4.2262])
               {
                  intersection()
                  {
                     circle(d = 22.0);
                     polygon(points = [[-11.0, -5.2262], [-11.0, 11.0], [11.0, 11.0], [11.0, -5.2262]]);
                  }
               }
            }
         }
         translate(v = [0.0, 0.0, 0.0])
         {
            linear_extrude(height = 2.0, center = false, twist = 0.0, scale = 1.0)
            {
               translate(v = [0.0, 4.2262])
               {
                  intersection()
                  {
                     circle(d = 20.0);
                     polygon(points = [[-10.0, -4.2262], [-10.0, 10.0], [10.0, 10.0], [10.0, -4.2262]]);
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
               translate(v = [0.0, 4.2262])
               {
                  intersection()
                  {
                     circle(d = 22.0);
                     polygon(points = [[-9.9694, -11.0], [-9.9694, -3.2262], [9.9694, -3.2262], [9.9694, -11.0]]);
                  }
               }
            }
         }
         translate(v = [0.0, 0.0, 0.0])
         {
            linear_extrude(height = 2.0, center = false, twist = 0.0, scale = 1.0)
            {
               translate(v = [0.0, 4.2262])
               {
                  intersection()
                  {
                     circle(d = 20.0);
                     polygon(points = [[-9.0631, -10.0], [-9.0631, -4.2262], [9.0631, -4.2262], [9.0631, -10.0]]);
                  }
               }
            }
         }
      }
   }
}

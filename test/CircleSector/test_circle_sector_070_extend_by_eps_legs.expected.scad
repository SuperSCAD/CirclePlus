// Unit of length: Unit.MM
$fn = 360;

difference()
{
   color(c = [1.0, 0.0, 0.0, 1.0])
   {
      intersection()
      {
         circle(d = 20.0);
         polygon(points = [[-0.0985, 0.0174], [-0.0707, -0.0707], [0.0174, -0.0985], [12.0396, 2.0214], [12.1177, 2.0898], [12.093, 2.1906], [2.1906, 12.093], [2.0898, 12.1177], [2.0214, 12.0396]], convexity = 1);
      }
   }
   intersection()
   {
      circle(d = 20.0);
      polygon(points = [[0.0, 0.0], [12.0223, 2.1199], [12.093, 2.1906], [2.1906, 12.093], [2.1199, 12.0223]], convexity = 1);
   }
}

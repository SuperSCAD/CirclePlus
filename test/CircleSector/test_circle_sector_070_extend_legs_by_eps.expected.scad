// Unit of length: Unit.MM
$fn = 360;

difference()
{
   color(c = [1.0, 0.0, 0.0, 1.0])
   {
      intersection()
      {
         circle(d = 20.0);
         polygon(points = [[-0.0985, 0.0174], [-0.0707, -0.0707], [0.0174, -0.0985], [12.1599, 2.0426], [12.1425, 2.1411], [2.1411, 12.1425], [2.0426, 12.1599]], convexity = 1);
      }
   }
   intersection()
   {
      circle(d = 20.0);
      polygon(points = [[0.0, 0.0], [12.1425, 2.1411], [2.1411, 12.1425]], convexity = 1);
   }
}

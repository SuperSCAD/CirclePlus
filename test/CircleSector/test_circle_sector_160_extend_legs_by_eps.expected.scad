// Unit of length: Unit.MM
$fn = 360;

difference()
{
   intersection()
   {
      circle(d = 20.0);
      polygon(points = [[0.0, -0.1], [0.0174, -0.0985], [12.1599, 2.0426], [0.0, 14.2836], [-14.2836, 0.0], [-12.1425, 2.1411], [-12.1599, 2.0426], [-0.0174, -0.0985]], convexity = 1);
   }
   intersection()
   {
      circle(d = 20.0);
      polygon(points = [[0.0, 0.0], [12.1425, 2.1411], [0.0, 14.2836], [-14.2836, 0.0], [-12.1425, 2.1411]], convexity = 1);
   }
}

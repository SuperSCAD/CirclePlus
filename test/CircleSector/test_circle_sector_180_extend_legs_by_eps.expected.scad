// Unit of length: Unit.MM
$fn = 360;

difference()
{
   intersection()
   {
      circle(d = 20.0);
      polygon(points = [[9.9639, 1.6554], [9.9466, 1.7538], [8.1927, 11.7004], [-11.7004, 8.1927], [-9.9466, -1.7538], [-9.9292, -1.8523]], convexity = 2);
   }
   intersection()
   {
      circle(d = 20.0);
      polygon(points = [[9.9466, 1.7538], [8.1927, 11.7004], [-11.7004, 8.1927], [-9.9466, -1.7538]], convexity = 2);
   }
}

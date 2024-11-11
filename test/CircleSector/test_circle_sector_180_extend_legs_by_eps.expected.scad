// Unit of length: Unit.MM
$fn = 360;

difference()
{
   color(c = [1.0, 0.0, 0.0, 1.0])
   {
      intersection()
      {
         circle(d = 20.0);
         polygon(points = [[9.9639, 1.6554], [8.1927, 11.7004], [-11.7004, 8.1927], [-9.9292, -1.8523]], convexity = 2);
      }
   }
   intersection()
   {
      circle(d = 20.0);
      polygon(points = [[9.8481, 1.7365], [8.1116, 11.5846], [8.0942, 11.683], [-11.7004, 8.1927], [-9.9466, -1.7538], [-9.8481, -1.7365]], convexity = 2);
   }
}

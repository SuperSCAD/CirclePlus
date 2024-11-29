// Unit of length: Unit.MM
$fn = 360;

difference()
{
   color(c = [1.0, 0.0, 0.0, 1.0])
   {
      intersection()
      {
         circle(d = 20.0);
         polygon(points = [[-0.0811, -0.1158], [9.9639, 1.6554], [8.1927, 11.7004], [-1.8523, 9.9292]], convexity = 1);
      }
   }
   intersection()
   {
      circle(d = 20.0);
      polygon(points = [[0.0, 0.0], [9.8481, 1.7365], [9.9466, 1.7538], [8.1927, 11.7004], [-1.7538, 9.9466], [-1.7365, 9.8481]], convexity = 1);
   }
}

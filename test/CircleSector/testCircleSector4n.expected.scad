// Unit of length: Unit.MM
intersection()
{
   difference()
   {
      circle(d = 60.0, $fn = 32);
      circle(d = 20.0, $fn = 32);
   }
   polygon(points = [[0.0, 0.0], [36.0789, 6.3617], [6.3617, 36.0789]], convexity = 1);
}

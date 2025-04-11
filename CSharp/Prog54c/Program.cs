using static System.Console;
Write("Enter radius: ");
int radius = int.Parse(ReadLine());
double pi = 3.14;
double area = pi * (radius * radius);
double circ = 2 * (pi * radius);
WriteLine("Area: " + area);
WriteLine("Circumference: " + circ);
ReadKey();
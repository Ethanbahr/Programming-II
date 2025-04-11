﻿using static System.Console;
Write("Base: ");
int base1    = int.Parse(ReadLine());
Write("Height: ");
int height   = int.Parse(ReadLine());
double area  = (base1 * height)/ 2;
double hyp   = Math.Round(Math.Sqrt((base1 * base1) + (height * height)), 2);
double perim = base1 + height + hyp;
WriteLine("Area: " + area);
WriteLine("Hypotenuse: " + hyp);
WriteLine("Perimeter: " + perim);
ReadKey();
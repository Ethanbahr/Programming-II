﻿using static System.Console;
Write("Enter package weight in kilograms: ");
double weight = double.Parse(ReadLine());
Write("Enter package length in kilograms: ");
double length = double.Parse(ReadLine());
Write("Enter package width in kilograms: ");
double width  = double.Parse(ReadLine());
Write("Enter package height in kilograms: ");
double height = double.Parse(ReadLine());
double volume = length * width * height;
if (weight > 27) WriteLine("Package is too heavy");
if (volume > 100000) WriteLine("Package is too large");
if ((weight > 27) && (volume > 100000)) WriteLine("Package is too heavy and too large");
ReadKey();
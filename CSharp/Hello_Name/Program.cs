﻿// Console.WriteLine("Hello, World!");
Console.Write("Enter your name: ");
// int, bool, string, char, double instead of float
string name = Console.ReadLine();
Console.WriteLine("Hello, " + name);

Console.Write("Enter your age: ");
// int age = Convert.ToInt32(Console.ReadLine());
int age = int.Parse (Console.ReadLine());
// age = int(input())
Console.WriteLine("Tou are " + age + " years old!");
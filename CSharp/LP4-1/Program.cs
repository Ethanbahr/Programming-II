using static System.Console;
Write("Enter # of copies to print: ");
int copies = int.Parse(ReadLine());
double price = 0;
double cost  = 0;
// && = and, || = or, ! = not
if (copies > 0 && copies <= 99) price = 0.30;
else if (copies > 99 && copies <= 499) price = 0.28;
else if (copies > 499 && copies <= 749) price = 0.27;
else if (copies > 749 && copies <= 1000) price = 0.26;
else if (copies > 1000) price = 0.25;
else WriteLine("Invalid number of copies!");
WriteLine("Price per copy is: $" + price);
WriteLine("Total cost is: $" + (price * copies));
ReadKey();
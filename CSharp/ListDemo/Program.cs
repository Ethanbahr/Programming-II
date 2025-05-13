using static System.Console;
// Lists are equivilent to Python lists
// List<TYPE> name = new List<TYPE>();
List<string> text = [];
List<string> list = new List<string>();
List<int> nums = new list<int>() { 1, 2, 3 };
nums.Add(4);
nums.Add(5);
nums.Add(6);
nums.Add(7);
nums.RemoveAt(5); // Removes '6'
nums.Remove(7); // Removes '7'
WriteLine("Length: " + nums.Count);
WriteLine(string.Join(", ", nums)); // "1, 2, 3, 4, 5"
foreach (int n in nums)
    Console.WriteLine(n);
// Look at C# deocumentation on MSDN for all list methods
nums[0] = 100;
WriteLine(nums[0]);
ReadKey();
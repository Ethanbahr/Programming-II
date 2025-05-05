using static System.Console;
// <access level> <static or not> <return type> name(<args>) {}
// In console apps, we'll make all functions "static"
// Not ststic in Forms apps; always "public" though
static int add(int x, int y) { return x + y; }
static int sub(int x, int y) { return x - y; }
static int mul(int x, int y) { return x * y; }
static int div(int x, int y) { return x / y; }

static void wait() { // void means "return nothing"
    ReadLine();
    // return;
}

Random random = new Random();
int n1        = random.Next(1,100) + 1;
int n2        = random.Next(150, 200) + 1;
Write("Choose an option: add, sub, mul, or div - ");
string op = ReadLine().ToLower();
int result = 0;
if      (op == "add") result = add(n1, n2);
else if (op == "sub") result = sub(n1, n2);
else if (op == "mul") result = mul(n1, n2);
else if (op == "div") result = div(n1, n2);
WriteLine("num1 = " + n1 + "\tnum2 = " + n2);
WriteLine("Result: " + result);
wait();
// ReadKey();
using static System.Console;
Write("Enter a string: ");
string word = ReadLine().ToLower();
int v = 0;
int c = 0;
for (int i = 0; i < word.Length; i++) {
    char let = word[i];
    if (let == 'a' || let == 'e' || let == 'i' || let == 'o' || let == 'u')
        v++;
    else if (let >= 'a' && let <= 'z') c++; // Check ASCII range
}
WriteLine("{0} coantains {1} vowels and {2} consonants", word, v, c);
ReadKey();
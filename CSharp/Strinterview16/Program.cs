using static System.Console;
static bool searchText(string text, string search)
{
    int tLen = text.Length;
    int sLen = search.Length;
    if (sLen > tLen) return false;
    for (int i = 0; i <= tLen - sLen; i++)
        // if (text[i..(i + sLen)] == search) return true;
        if (text.Substring(i, sLen) == search) return true;
    // Subrstring uses startIndex, length (not endIndex)
    return false;
}
Write("Enter a string: ");
string text = ReadLine();
Write("Enter a substring to search for: ");
string word = ReadLine();
bool result = searchText(text, word);
WriteLine("Does \"{0}\" contain \"{1}\"?: {2}", text, word, result);
ReadLine();
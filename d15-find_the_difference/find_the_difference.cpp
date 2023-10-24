#include <iostream>

using namespace std;

int countChar(string s, char c)
{
    int count = 0;

    for (char x : s) 
    {
        if (c == x) 
        {
            count++;
        }
    }

    return count;
}

char findTheDifference(string s, string t)
{
    for(char c: t) 
    {
        if(s.find(c) == string::npos)
        {
            return c;
        }
    }

    for(char c: t) 
    {
        if(countChar(s, c) != countChar(t, c))
        {
            return c;
        }
    }

    return ' ';
}

int main()
{
    cout << findTheDifference("abcd", "abcde") << endl;
    cout << findTheDifference("a", "aa") << endl;
    return 0;
}
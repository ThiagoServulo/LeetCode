#include <iostream>
#include <stack>

using namespace std;

bool isValid(string s);

int main()
{
    cout << isValid("]");
    return 0;
}

bool isValid(string s) 
{
    stack <char> symbols;
    for(char c: s)
    {
        switch(c)
        {
            case '(':
            case '[':
            case '{':
                symbols.push(c);
                break;

            case ')':
                if((symbols.size()) && (symbols.top() == '('))
                {
                    symbols.pop();
                    break;
                }
                return false;

            case ']':
                if((symbols.size()) && (symbols.top() == '['))
                {
                    symbols.pop();
                    break;
                }
                return false;

            case '}':
                if((symbols.size()) && (symbols.top() == '{'))
                {
                    symbols.pop();
                    break;
                }
                return false;
        }
    }

    return !symbols.size();
}
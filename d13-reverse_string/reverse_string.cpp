#include <iostream>
#include <vector>

using namespace std;

void printString(vector<char> s)
{
    for(char x: s)
    {
        cout << x << " ";
    }
    cout << endl;
}

void reverseString(vector<char>& s)
{
    vector<char> aux;
    for(auto x = s.rbegin(); x != s.rend(); x++)
    {
        aux.push_back(*x);
    }
    s.swap(aux);
}

int main()
{
    vector<char> s;
    s.push_back('h');
    s.push_back('e');
    s.push_back('l');
    s.push_back('l');
    s.push_back('o');

    printString(s);
    reverseString(s);
    printString(s);

    return 0;
}
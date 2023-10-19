#include <iostream>
#include <algorithm>

using namespace std;

string addBinary(string a, string b);

int main()
{
    cout << addBinary("1101", "111");
    return 0;
}

string addBinary(string a, string b) 
{
    char offset = '0';
    string result = "";
    int count = 0;

    reverse(a.begin(), a.end());
    reverse(b.begin(), b.end());

    int lenMax = (a.size() > b.size()) ? a.size() : b.size();

    for(int len = 0; len < lenMax; len++)
    {
        count = (offset == '1') ? (count + 1) : count;

        if(a.size() >= len)
        {
            count = (a[len] == '1') ? (count + 1) : count;
        }

        if(b.size() >= len)
        {
            count = (b[len] == '1') ? (count + 1) : count;
        }

        switch(count)
        {
            case 0:
                offset = '0';
                result += '0';
                break;

            case 1:
                offset = '0';
                result += '1';
                break;      

            case 2:
                offset = '1';
                result += '0';
                break;     

            case 3:
                offset = '1';
                result += '1';
                break;                                     
        }

        count = 0;
    }

    result = (offset == '1') ? (result + '1') : result;

    reverse(result.begin(), result.end());

    return result;
}
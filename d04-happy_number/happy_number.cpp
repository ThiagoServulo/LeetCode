#include <iostream>
#include <math.h>

using namespace std;

bool isHappy(int n);

int main()
{
    cout << isHappy(4);
    return 0;
}

bool isHappy(int n) 
{
    string number = to_string(n);
    int result;
    do
    {   
        result = 0;
        for(char digit: number)
        {
            result += pow((int(digit) - 48), 2);
        }
        number = to_string(result);
    } 
    while (number.size() > 1);
    return (!number.compare("1") || !number.compare("7"));
}
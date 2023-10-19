#include <iostream>

using namespace std;

int addDigits(int num);

int main()
{
    cout << addDigits(3333);
    return 0;
}

int addDigits(int num) 
{
    string number = to_string(num);
    int result;

    do
    {   
        result = 0;
        for(char digit: number)
        {
            result += (int(digit) - 48);
        }
        number = to_string(result);
    } 
    while (number.size() > 1);

    return result;
}
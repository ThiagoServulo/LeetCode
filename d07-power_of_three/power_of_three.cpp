#include <iostream>
#include <math.h>

using namespace std;

bool isPowerOfThree(int n);

int main()
{
    cout << isPowerOfThree(10);
    return 0;
}

bool isPowerOfThree(int n) 
{
    return (n != 0 && (pow(3, round(log(n) / log(3))) == n));
}
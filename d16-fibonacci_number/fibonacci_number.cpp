#include <iostream>

using namespace std;

int fib(int n)
{
    int x = 0, y = 1;

    if(n <= 0)
    {
        return 0;
    }

    for(int i = 2; i < n; i++)
    {
        int aux = y;
        y += x;
        x = aux;
    }

    return x + y;
}

int main()
{
    cout << fib(10);
    return 0;
}
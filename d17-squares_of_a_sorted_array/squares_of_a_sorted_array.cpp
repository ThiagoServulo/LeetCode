#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> sortedSquares(vector<int>& nums)
{
    vector<int> ret;

    for(int i: nums)
    {
        ret.push_back(i * i);
    }

    sort(ret.begin(), ret.end());

    return ret;
}

void printVector(vector<int> s)
{
    for(int x: s)
    {
        cout << x << " ";
    }
    cout << endl;
}

int main()
{
    vector<int> vet1 = {-2, 0, 1, 2};
    vector<int> vet2;

    vet2 = sortedSquares(vet1);

    printVector(vet2);

    return 0;
}
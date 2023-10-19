#include <iostream>
#include <vector>

using namespace std;

void printVector(vector<int> s)
{
    for(int x: s)
    {
        cout << x << " ";
    }
    cout << endl;
}

vector<int> shuffle(vector<int>& nums, int n)
{
    vector<int> ret;

    for(int i =0; i < n; i++)
    {
        ret.push_back(nums.at(i));
        ret.push_back(nums.at(i + n));
    }

    return ret;
}

int main()
{
    vector<int> s;
    s.push_back(1);
    s.push_back(2);
    s.push_back(3);
    s.push_back(4);
    s.push_back(5);
    s.push_back(6);

    vector<int> res = shuffle(s, 3);

    printVector(res);

    return 0;
}
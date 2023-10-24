#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int findDuplicate(vector<int>& nums)
{
    for(auto it = nums.begin(); it != nums.end(); it++)
    {
        if(count(it, nums.end(), *it) != 1)
        {
            return *it;
        }
    }
    return -1;
}

int main()
{
    vector<int> nums = {1, 3, 4, 2, 2};

    cout << findDuplicate(nums);

    return 0;
}
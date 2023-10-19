#include <iostream>
#include <vector>
#include <set>

using namespace std;

bool containsDuplicate(vector<int>& nums);

int main()
{
    vector<int> nums = {1, 2, 3, 4, 1};
    cout << containsDuplicate(nums);
    return 0;
}

bool containsDuplicate(vector<int>& nums) 
{
    set<int> nums_set(nums.begin(), nums.end());
    return nums_set.size() != nums.size();
}
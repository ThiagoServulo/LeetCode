#include <iostream>
#include <vector>

using namespace std;

void moveZeroes(vector<int>& nums);
void printVector(vector<int> nums);

int main()
{
    vector<int> nums{0,1,0,3,12};
    moveZeroes(nums);
    printVector(nums);
    return 0;
}

void moveZeroes(vector<int>& nums)
{
    int count = 0;
    for(int i = 0; i < nums.size();)
    {
        if(nums[i] == 0)
        {
            nums.erase(nums.begin() + i);
            count++;
        }
        else
        {
            i++;
        }
    }
    for(int i = 0; i < count; i++)
    {
        nums.push_back(0);
    }
}

void printVector(vector<int> nums)
{
    for(int i: nums)
    {
        cout << i << " ";
    }
}
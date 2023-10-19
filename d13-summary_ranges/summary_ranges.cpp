#include <iostream>
#include <vector>
#include <string>

using namespace std;

vector<string> summaryRanges(vector<int>& nums);
void printVector(vector<string> nums);

int main()
{
    vector<int> a({0,2,3,4,6,8,9});
    printVector(summaryRanges(a));
    return 0;
}

vector<string> summaryRanges(vector<int>& nums)
{
    vector<string> resp;
    int offset = 0;
    for(int i = 0; i < nums.size(); i++)
    {
        int first = nums[i];
        cout << first << endl;
        bool lastExists = false;
        for(int aux = (i + 1); aux <= nums.size(); aux++)
        {
            if(aux == nums.size())
            {
                --aux;
            }
            if(((nums[aux] - first) != 1) || (i == (nums.size() - 1)))
            {
                if(lastExists)
                {
                    resp.push_back(to_string(first) + "->" + to_string(nums[aux]));
                    offset++;
                }  
                else
                {
                    resp.push_back(to_string(first));
                }
                break;
            }
            else
            {
                lastExists = true;
                offset++;
            }
        }
        //cout << offset << endl;
        i += offset;
        offset = 0;
        lastExists = false;
    }
    return resp;
}

void printVector(vector<string> nums)
{
    for(string i: nums)
    {
        cout << i << " ";
    }
}
#include <iostream>
#include <vector>

using namespace std;

int triangularSum(vector<int>& nums);

int main()
{
    vector<int>a({2,6,6,5,5,3,3,8,6,4,3,3,5,1,0,1,3,6,9});
    cout << triangularSum(a);
    return 0;
}

int triangularSum(vector<int>& nums)
{
    vector<int> aux = nums;

    while(aux.size() != 1)
    {
        vector<int> aux2;
        for(int i = 0; i < (aux.size() - 1); i++)
        {
            aux2.push_back((aux[i] + aux[i+1]) % 10);
        }
        aux.clear();
        aux = aux2;
    }

    return aux[0];
}
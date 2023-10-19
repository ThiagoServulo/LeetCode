#include <iostream>
#include <vector>

using namespace std;

void printMatrix(vector<vector<int>>& matrix);
void rotate(vector<vector<int>>& matrix);

int main()
{
    vector<vector<int>> a{{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
    rotate(a);
    printMatrix(a);
    return 0;
}

void rotate(vector<vector<int>>& matrix)
{
    int len = matrix.size();
    vector<vector<int>> resp;
    
    for(int coluna = 0; coluna < len; coluna ++)
    {
        vector<int> r_linha;
        for(int linha = (len - 1); linha >= 0; linha--)
        {
            vector<int> m_linha = matrix[linha];
            r_linha.push_back(m_linha.at(coluna));
        }
        resp.push_back(r_linha);
    }
    matrix = resp;
}

void printMatrix(vector<vector<int>>& matrix)
{
    int len = matrix.size();

    for(int i = 0; i < len; i++)
    {
        vector<int> linha = matrix[i];
        for(int n : linha)
        {
            cout << n << " ";
        }
        cout << endl;
    }
}
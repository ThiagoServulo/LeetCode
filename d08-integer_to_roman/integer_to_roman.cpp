#include <iostream>
#include <string.h>

using namespace std;

string intToRoman(int num);

int main()
{
    cout << intToRoman(1984);
    return 0;
}

string intToRoman(int num) 
{
    int integer[7] = {1, 5, 10, 50, 100, 500, 1000};
    char roman[7] = {'I', 'V', 'X', 'L', 'C', 'D', 'M'};
    string res = "";
    int aux;

    // Loop para percorrer o array de romanos/inteiros
    for(int index = 6; index >= 0; index--)
    {
        // Verifica se o número romano precisa ser acrescido a string
        if((aux = (num / integer[index])) != 0)
        {
            // Verifica se o número é divisível por 5 / 50 / 500
            if(integer[index] == 5 || integer[index] == 50 || integer[index] == 500)
            {
                aux = (num / integer[index - 1]);
                if(aux != 9)
                {
                    res += roman[index];
                    num -= integer[index];
                }
                else
                {
                    res += roman[index - 1];
                    res += roman[index + 1];
                    num -= (aux * integer[index - 1]);
                }
                continue;
            }

            // Tratar as 4 inserções
            if(aux == 4)
            {
                res += roman[index];
                res += roman[index + 1];
            }
            else
            {
                for(int i = 0; i < aux; i ++)
                {
                    res += roman[index];
                }
            }

            // Decrementa o número base
            num -= (aux * integer[index]);
        }
    }

    return res;
}
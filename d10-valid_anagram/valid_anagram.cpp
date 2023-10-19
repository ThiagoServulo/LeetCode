#include <iostream>
#include <utility>
#include <map>

using namespace std;

bool isAnagram(string s, string t);
map<char, int> stringToMap(string s);

int main()
{
    cout << isAnagram("anagram", "nagaraxm");
    return 0;
}

bool isAnagram(string s, string t)
{
    return stringToMap(s) == stringToMap(t);
}

map<char, int> stringToMap(string s)
{
    map<char, int> s_map;
    for(char c: s)
    {
        auto it = s_map.find(c);
        if(it == s_map.end())
        {
            s_map.insert(pair<char, int>(c, 1));
        }
        else
        {
            s_map[c] += 1;
        }
    }
    return s_map;
}
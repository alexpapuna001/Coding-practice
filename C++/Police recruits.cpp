#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int available = 0;
    int crimes = 0;
    int n;
    cin >> n;
    vector<int> cops(n);
    for (int i = 0; i< n; i++)
    {
        cin >> cops[i];
    }
    for (int i = 0; i < n; i++)
    {
        if (cops[i] == -1)
        {
            available--;
            if (available < 0)
            {
                crimes ++;
                available = 0;
            }
        } else 
        {
            available += cops[i];
        }

    }
    cout << crimes;
    return 0;
}
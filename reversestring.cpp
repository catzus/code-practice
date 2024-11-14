#include <iostream>  
#include <string>
using namespace std;

int main() {
    string a,c;
    int b;
    int i;
    cin >> a;
    b = a.length();
    for (i = b-1;i >= 0;i--)
    {
        c.push_back(a[i]);
    }
    cout << c << endl;
}
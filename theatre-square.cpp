#include <iostream>

using namespace std;

int main()
{
    int n,m,a;
    cin >> n >> m >> a;
    int t =  n/a + ((n%a == 0)? 0 : 1);
    int s =  m/a + ((m%a == 0)? 0 : 1);
    cout << t*s;

    return 0;
}

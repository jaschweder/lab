#include <iostream>
#include <vector>
#include <complex>

using namespace std;

int main()
{
    // var types
    cout << "types: " << "\n";
    bool v_bool = true;
    cout << v_bool << "\n";

    char v_char = 's';
    cout << v_char << "\n";

    int v_int = 123;
    cout << v_int << "\n";

    double v_double = 123.12;
    cout << v_double << "\n";

    double v_double1 {2.3};
    cout << v_double1 << "\n";

    double v_double2 = 3.2;
    cout << v_double2 << "\n";

    //operators
    cout << "operators: " << "\n";
    cout << 3 + 3 << "\n";
    cout << +3 << "\n";
    cout << 3 - 3 << "\n";
    cout << - 3 << "\n";
    cout << 3 * 3 << "\n";
    cout << 3 / 3 << "\n";
    cout << 3 % 3 << "\n";
    cout << (3 == 3) << "\n";
    cout << (3 != 3) << "\n";
    cout << (3 < 3) << "\n";
    cout << (3 > 3) << "\n";
    cout << (3 <= 3) << "\n";
    cout << (3 >= 3) << "\n";

    //complex numbers

    //vector
    vector<int> v {1,2,3,4,5,6};
    cout << "vector: ";
    for(int n : v) {
        cout << n << ",";
    }
    cout << "\n";

    //complex
    cout << "complex: ";
    complex<double> z = {1,2};
    cout << z << "\n";

    //auto
    cout << "auto: " << "\n";
    auto a_bool = true;
    cout << a_bool << "\n";

    auto a_char = 's';
    cout << a_char << "\n";

    auto a_int = 123;
    cout << a_int << "\n";

    auto a_double = 123.12;
    cout << a_double << "\n";

    auto a_double1 {2.3};
    cout << a_double1 << "\n";

    auto a_double2 = 3.2;
    cout << a_double2 << "\n";

    //inline operators
    auto x = 1,y = 1;
    cout << x << " " << y << "\n";

    x+=y;
    cout << x << " " << y << "\n";

    ++y;
    cout << x << " " << y << "\n";

    x-=y;
    cout << x << " " << y << "\n";

    --y;
    cout << x << " " << y << "\n";

    x*=y;
    cout << x << " " << y << "\n";

    x/=y;
    cout << x << " " << y << "\n";

    x%=y;
    cout << x << " " << y << "\n";
}

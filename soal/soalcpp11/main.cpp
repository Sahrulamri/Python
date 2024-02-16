
#include <iostream>
using namespace std;

class Complex {
public:
    int real;
    int imag;
    
    Complex(int r, int i) : real(r), imag(i) {}
};

int main() {
    Complex obj(3, 4);
    Complex *ptr = &obj;
    
    cout << "Bagian real dari obj: " << obj.real << endl;
    cout << "Bagian real melalui pointer: " << ptr->real << endl;
    
    cout << "Bagian imajiner dari obj: " << obj.imag << endl;
    cout << "Bagian imajiner melalui pointer: " << ptr->imag << endl;
    
    return 0;
}

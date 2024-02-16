
#include <iostream>
using namespace std;

int* generateFibonacci(int n) {
    int* fibArray = new int[n];
    fibArray[0] = 0;
    fibArray[1] = 1;
    for (int i = 2; i < n; i++) {
        fibArray[i] = fibArray[i - 1] + fibArray[i - 2];
    }
    return fibArray;
}

int main() {
    int term = 6;

    int* fibonacciArray = generateFibonacci(term);

    cout << "Deret Fibonacci untuk " << term << " term adalah: ";
    for (int i = 0; i < term; i++) {
        cout << fibonacciArray[i] << " ";
    }

    delete[] fibonacciArray;

    return 0;
}
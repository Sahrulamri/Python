#include <iostream>
using namespace std;

double calculateAverage(int a, int b, int c);

int main() {

    double average = calculateAverage(5, 10, 15);

    cout << "Rata-rata dari 5, 10, dan 15 adalah: " << average << endl;

    return 0;
}

double calculateAverage(int a, int b, int c) {
    return (a + b + c) / 3.0;
}
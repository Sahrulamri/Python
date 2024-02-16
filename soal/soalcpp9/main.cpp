
#include <iostream>

void sorting(int arr[], int low, int high) {
    if (low < high) {
        int pivot = arr[high];
        int i = low - 1;

        for (int j = low; j <= high - 1; j++) {
            if (arr[j] < pivot) {
                i++;
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }

        int temp = arr[i + 1];
        arr[i + 1] = arr[high];
        arr[high] = temp;

        sorting(arr, low, i);
        sorting(arr, i + 2, high);
    }
}

using namespace std;
int main() {
    int arr[] = {7, 1, 3, 8, 9, 2, 5, 4, 6};
    int n = sizeof(arr)/sizeof(arr[0]);

    sorting(arr, 0, n-1);

    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }

    return 0;
}
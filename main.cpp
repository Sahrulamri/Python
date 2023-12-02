#include <iostream>

using namespace std;

// Fungsi untuk menukar dua elemen dalam array
void tukar(int &a, int &b) {
    int temp = a;
    a = b;
    b = temp;
}

// Fungsi quick_sort untuk mengurutkan array
void quick_sort(int arr[], int low, int high) {
    if (low < high) {
        // Memilih pivot (dalam contoh ini, elemen pertama)
        int pivot = arr[low];
        int left = low + 1;
        int right = high;

        while (true) {
            // Mencari elemen yang lebih besar dari pivot dari sebelah kiri
            while (left <= right && arr[left] <= pivot) {
                left++;
            }

            // Mencari elemen yang lebih kecil dari pivot dari sebelah kanan
            while (left <= right && arr[right] >= pivot) {
                right--;
            }

            // Jika left dan right masih belum bertemu, tukar elemen
            if (left < right) {
                tukar(arr[left], arr[right]);
            } else {
                break;
            }
        }

        // Tukar pivot dengan elemen di posisi right (posisi pembagian)
        tukar(arr[low], arr[right]);

        // Panggil quick_sort rekursif pada kedua sisi pivot
        quick_sort(arr, low, right - 1);
        quick_sort(arr, right + 1, high);
    }
}

int main() {
    int n;
    cout << "Masukkan jumlah elemen dalam array: ";
    cin >> n;

    int arr[n];
    cout << "Masukkan elemen-elemen array: ";
    for (int i = 0; i < n; i++) {
        cout << "Masukkan Array index ke - " << i+1 << " = ";
        cin >> arr[i];
    }

    // Panggil quick_sort untuk mengurutkan array
    quick_sort(arr, 0, n - 1);

    // Cetak hasil pengurutan
    cout << "Hasil pengurutan: ";
    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;

    return 0;
}


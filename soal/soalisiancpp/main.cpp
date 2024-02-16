// Lengkapi baris kode berikut
// Berikut terdapat program daftar gaji karyawan, lengkapi baris kode yang kosong berikut ini

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Karyawan {
public:
    string nama;
    double gaji;
    int usia;

    Karyawan(string n, double g, int u) : nama(move(n)), gaji(g), usia(u) {}

    static bool perbandinganGaji(const Karyawan& a, const Karyawan& b) {
        return a.gaji < b.gaji;
    }

    static bool perbandinganUsia(const Karyawan& a, const Karyawan& b) {
        return a.usia < b.usia;
    }
};

int main() {
    vector<Karyawan> daftarKaryawan = {
        {"Alice", 50000.0, 30},
        {"Bob", 60000.0, 25},
        {"Charlie", 45000.0, 35},
        {"David", 70000.0, 28}
    };

    int pilihan;
    cout << "Pilih kriteria pengurutan:\n";
    cout << "1. Gaji\n";
    cout << "2. Usia\n";
    cin >> pilihan;

    if (pilihan == 1) {
        sort(daftarKaryawan.begin(), daftarKaryawan.end(), Karyawan::perbandinganGaji);
    } else if (pilihan == 2) {
        sort(daftarKaryawan.begin(), daftarKaryawan.end(), Karyawan::perbandinganUsia);
    } else {
        cout << "Pilihan tidak valid.\n";
        return 1;
    }

    cout << "Daftar Karyawan setelah diurutkan:\n";
    for (const auto& karyawan : daftarKaryawan) {
        cout << karyawan.nama << ": $" << karyawan.gaji << ", Usia: " << karyawan.usia << " tahun\n";
    }

    return 0;
}

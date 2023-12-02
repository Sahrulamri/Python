// Fungsi untuk mengenkripsi teks dengan algoritma Beaufort Cipher
function enkripsiBeaufort(teks, kunci) {
    let hasil = "";
    for (let i = 0; i < teks.length; i++) {
        let teksChar = teks.charCodeAt(i);
        let kunciChar = kunci.charCodeAt(i % kunci.length);
        let enkripsiChar = (teksChar - kunciChar + 256) % 256;
        hasil += String.fromCharCode(enkripsiChar);
    }
    return hasil;
}

// Fungsi untuk mendekripsi teks yang telah dienkripsi dengan algoritma Beaufort Cipher
function dekripsiBeaufort(teks, kunci) {
    let hasil = "";
    for (let i = 0; i < teks.length; i++) {
        let teksChar = teks.charCodeAt(i);
        let kunciChar = kunci.charCodeAt(i % kunci.length);
        let dekripsiChar = (teksChar + kunciChar) % 256;
        hasil += String.fromCharCode(dekripsiChar);
    }
    return hasil;
}

const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.question("Masukkan teks (tanpa spasi) yang akan dienkripsi: ", (teksAsli) => {
    rl.question("Masukkan kunci (tanpa spasi): ", (kunci) => {
        // Enkripsi teks
        const teksTerenkripsi = enkripsiBeaufort(teksAsli, kunci);
        console.log("Teks Terenkripsi:", teksTerenkripsi);

        // Mendekripsi teks
        const teksTerdekripsi = dekripsiBeaufort(teksTerenkripsi, kunci);
        console.log("Teks Terdekripsi:", teksTerdekripsi);

        rl.close();
    });
});

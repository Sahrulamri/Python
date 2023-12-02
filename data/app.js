const crypto = require('crypto');
const readline = require('readline');

// Fungsi untuk mengenkripsi teks menggunakan AES
function enkripsiAES(teks, kunci) {
    const iv = crypto.randomBytes(16); // Vektor inisialisasi acak
    const cipher = crypto.createCipheriv('aes-256-cbc', Buffer.from(kunci), iv);
    let teksTerenkripsi = cipher.update(teks, 'utf-8', 'hex');
    teksTerenkripsi += cipher.final('hex');
    return { iv: iv.toString('hex'), teksTerenkripsi };
}

// Fungsi untuk mendekripsi teks yang telah dienkripsi dengan AES
function dekripsiAES(teksTerenkripsi, kunci, iv) {
    const decipher = crypto.createDecipheriv('aes-256-cbc', Buffer.from(kunci), Buffer.from(iv, 'hex'));
    let teksTerdekripsi = decipher.update(teksTerenkripsi, 'hex', 'utf-8');
    teksTerdekripsi += decipher.final('utf-8');
    return teksTerdekripsi;
}

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.question("Masukkan kunci (panjang harus 32 karakter): ", (kunci) => {
    rl.question("Masukkan teks yang akan dienkripsi: ", (teksAsli) => {
        // Enkripsi teks
        const hasilEnkripsi = enkripsiAES(teksAsli, kunci);
        console.log('Teks Terenkripsi:', hasilEnkripsi.teksTerenkripsi);
        console.log('IV:', hasilEnkripsi.iv);

        // Mendekripsi teks
        const teksTerdekripsi = dekripsiAES(hasilEnkripsi.teksTerenkripsi, kunci, hasilEnkripsi.iv);
        console.log('Teks Terdekripsi:', teksTerdekripsi);

        rl.close();
    });
});


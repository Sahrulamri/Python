function hitungHurufTerbanyak(string) {

    string = string.toLowerCase();
  

    const jumlahKarakter = {};
  

    [...string].forEach((char) => {

      if (char.match(/[a-z]/)) {
        if (char in jumlahKarakter) {
          jumlahKarakter[char]++;
        } else {
          jumlahKarakter[char] = 1;
        }
      }
    });
  

    let hurufTerbanyak = "";
    let kemunculanTerbanyak = 0;
  
    for (let char in jumlahKarakter) {
      if (jumlahKarakter[char] > kemunculanTerbanyak) {
        hurufTerbanyak = char;
        kemunculanTerbanyak = jumlahKarakter[char];
      }
    }
  
    return `Huruf terbanyak adalah huruf ${hurufTerbanyak.toUpperCase()} dengan jumlah kemunculan sebanyak ${kemunculanTerbanyak} kali`;
  }
  

  const string = prompt("Masukkan string: ");
  

  const hasil = hitungHurufTerbanyak(string);
  console.log("Hasil:", hasil);
  
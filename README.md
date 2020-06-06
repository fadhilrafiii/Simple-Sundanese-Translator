# Simple Sundanese Translator
Simple Sundanese to Bahasa Indonesia translator using Pattern Matching

## Latar Belakang
Pada suatu hari, ada mahasiswa bernama Riyugan yang baru pindah ke Bandung. Pada awalnya dia mengalami kesulitan untuk bersosialisai dengan lingkungan sekitar karena orang-orang di lingkungannya yang baru hanya berbicara dalam bahasa Sunda. Beruntungnya Riyugan punya teman dari kampung halamannya, yaitu Anda, untuk diminta membuat penerjemah sederhana dari Bahasa Sunda ke Bahasa Indonesia begitu pula sebaliknya untuk memudahkan dirinya bersosialisasi dengan lingkungan barunya di Bandung.

## Spesifikasi
Buatlah dalam bahasa pemrograman Python, program penerjemah sederhana yang memanfaatkan algoritma String Matching (Knuth-Morris-Pratt(KMP), Boyer-Moore(BM), dan Regex), dengan spesifikasi sebagai berikut.
1. Program mampu membaca kata atau kalimat yang akan diterjemahkan.
2. Program akan membaca file eksternal yang berisi vocabulary Bahasa Sunda - Bahasa Indonesia (file sudah disiapkan dalam repository).
3. Program akan melakukan penerjemahan secara perkata (untuk contoh akan ditampilkan di bawah).
4. Program dapat memilih mau "Bahasa Sunda ke Bahasa Indonesia" atau "Bahasa Indonesia ke Bahasa Sunda".
5. Pada saat penerjemahan "Bahasa Sunda ke Bahasa Indonesia", program mampu mengenali kata yang tidak memiliki arti (stopwords), seperti "teh" sehingga dapat diabaikan saat penerjemahan.
6. Pada saat penerjemahan "Bahasa Indonesia ke Bahasa Sunda", program mampu menambahkan kata untuk penekanan kalimat, seperti "teh".
7. Program dapat menampilkan hasil terjemahan.
8. Program dibuat secara individu.
9. Peserta akan mendapatkan nilai bonus jika mengimplementasikan dalam web (untuk bahasanya dibebaskan).
10. Dilarang meng-copy source code program yang sudah jadi, untuk source code algoritma string matching dipersilahkan menggunakan source code dari tugas yang sudah pernah dibuat (Tugas Kecil 4).
11. Batas pengerjaannya adalah 6 Juni 2020.

## Contoh Kasus Uji
```
Sunda - Indonesia
Sunda : nami abdi Riyugan
Indonesia : nama saya Riyugan
```

```
Sunda - Indonesia
Sunda : abdi teh sanes jalma Bandung
Indonesia : saya bukan orang Bandung
```

```
Sunda - Indonesia
Sunda : anjeun sumping ti mana?
Indonesia : kamu tiba dari mana?
```

```
Indonesia - Sunda
Indonesia : nama saya Riyugan
Sunda : nami abdi Riyugan
```

```
Indonesia - Sunda
Indonesia : nama adik kamu siapa?
Sunda : nami rai anjeun teh saha?
```

```
Indonesia - Sunda
Indonesia : saya tidak bisa bahasa Sunda
Sunda : abdi henteu tiasa bahasa Sunda
```

## Prerequisites
1. Python 3.6/3.7/3.8 Download https://www.python.org/downloads/
2. Flask bisa diunduh melalui terminal dengan command pip install flask
3. Web Browser
4. Internet (karena menggunakan jquery yang diambil dari googleapis.com)

### Built With
- Visual Studio Code
- Mozilla Firefox

### Authors
- Fadhil Muhammad Rafi'

### Demo Penggunaan
bit.ly/SundaneseTranslatorFadhil

### Acknowledgement
- Muhammad Hendry Prasetya

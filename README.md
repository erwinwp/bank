### Instalasi Python

#### Langkah 1: Unduh dan Instal Python

1.  Kunjungi situs web resmi Python di **[https://www.python.org/downloads/](https://www.python.org/downloads/)**.
2.  Klik tombol **"Download Python"** untuk mengunduh versi terbaru yang sesuai dengan sistem operasi Anda (Windows, macOS, atau Linux).
3.  Jalankan file installer yang sudah Anda unduh.
4.  **Sangat Penting:** Saat muncul jendela instalasi, **pastikan Anda mencentang kotak "Add Python to PATH"** di bagian bawah. Ini akan memudahkan Anda menjalankan Python dari Command Prompt atau Terminal.
5.  Klik **"Install Now"** dan ikuti proses instalasi hingga selesai.

#### Langkah 2: Verifikasi Instalasi Python

Setelah instalasi selesai, pastikan Python sudah terpasang dengan benar.

1.  Buka **Command Prompt** (untuk Windows) atau **Terminal** (untuk macOS/Linux).
2.  Ketik perintah berikut dan tekan Enter:
    ```bash
    python --version
    ```
3.  Jika instalasi berhasil, Anda akan melihat versi Python yang terpasang, contohnya: `Python 3.12.0`.

#### Langkah 3: Menyiapkan Lingkungan di Visual Studio Code (Opsional)

Jika Anda berencana menggunakan Visual Studio Code (VSC) untuk coding Python, ikuti langkah-langkah ini.

1.  Buka Visual Studio Code.
2.  Pergi ke panel **"Extensions"** (ikon kotak di sisi kiri) atau tekan `Ctrl+Shift+X`.
3.  Cari ekstensi **"Python"** yang diterbitkan oleh **Microsoft**.
4.  Klik tombol **"Install"**. Ekstensi ini akan menyediakan fitur-fitur canggih seperti *autocomplete*, *debugging*, dan format kode.

#### Langkah 4: Uji Coba Pertama Anda

Mari kita buat program "Hello, World\!" sederhana untuk memastikan semuanya berfungsi.

1.  Di VSC, buat file baru dan simpan dengan nama `hello.py`.
2.  Tulis kode berikut di dalamnya:
    ```python
    print("Hello, World!")
    ```
3.  Buka **Terminal di VSC** (`Ctrl+` \`) dan jalankan file tersebut dengan perintah:
    ```bash
    python hello.py
    ```
4.  Jika output-nya adalah **"Hello, World\!"**, selamat\! Anda sudah siap untuk mulai coding Python.
# Webcam Red Filter

Program sederhana untuk menampilkan feed webcam secara real-time dengan filter warna merah menggunakan OpenCV dan Python.

## Cara Kerja

Program membaca frame dari webcam, lalu mengubah setiap piksel sehingga hanya channel warna merah (R) yang dipertahankan, sementara channel biru (B) dan hijau (G) di-nol-kan.

## Cara Menjalankan

```bash
python main.py
```

Tekan tombol **q** untuk keluar dari program.

## Catatan

Program ini masih menggunakan loop piksel-per-piksel (`for y in range... for x in range...`) untuk proses filter, yang cukup lambat pada resolusi kamera standar. Untuk performa lebih baik, bisa diganti dengan operasi NumPy vectorized:

```python
red_frame = frame.copy()
red_frame[:, :, 0] = 0  # B
red_frame[:, :, 1] = 0  # G
```

## Lisensi

Bebas digunakan untuk keperluan belajar.

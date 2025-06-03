import random
import matplotlib.pyplot as plt

# Fungsi yang akan diminimasi
def fitness(x):
    return x**2

# Parameter PSO
batas_bawah = -10
batas_atas = 10
jumlah_partikel = 10
maks_iterasi = 50
w = 0.5
c1 = 1.5
c2 = 1.5

# Inisialisasi partikel dan kecepatan
partikel = [random.uniform(batas_bawah, batas_atas) for _ in range(jumlah_partikel)]
kecepatan = [random.uniform(-1, 1) for _ in range(jumlah_partikel)]
pbest = partikel[:]
pbest_fitness = [fitness(x) for x in pbest]
gbest = pbest[pbest_fitness.index(min(pbest_fitness))]

# Untuk menyimpan nilai terbaik tiap iterasi
nilai_terbaik_per_iterasi = []

# Iterasi utama PSO
for iterasi in range(maks_iterasi):
    for i in range(jumlah_partikel):
        r1 = random.random()
        r2 = random.random()

        # Update kecepatan
        kecepatan[i] = (
            w * kecepatan[i]
            + c1 * r1 * (pbest[i] - partikel[i])
            + c2 * r2 * (gbest - partikel[i])
        )

        # Update posisi
        partikel[i] += kecepatan[i]
        partikel[i] = max(min(partikel[i], batas_atas), batas_bawah)

        # Update pbest jika diperlukan
        current_fitness = fitness(partikel[i])
        if current_fitness < fitness(pbest[i]):
            pbest[i] = partikel[i]

    # ✅ Perbarui fitness dari pbest setelah semua partikel dievaluasi
    pbest_fitness = [fitness(x) for x in pbest]

    # Update gbest
    current_best_index = pbest_fitness.index(min(pbest_fitness))
    gbest_candidate = pbest[current_best_index]
    if fitness(gbest_candidate) < fitness(gbest):
        gbest = gbest_candidate

    # Simpan nilai terbaik iterasi ini
    nilai_terbaik_per_iterasi.append(fitness(gbest))

# Hasil akhir
print(f"Posisi x terbaik: {gbest}")
print(f"Nilai minimum f(x): {fitness(gbest)}")

# Grafik
plt.plot(nilai_terbaik_per_iterasi)
plt.title('Grafik Nilai Minimum per Iterasi')
plt.xlabel('Iterasi')
plt.ylabel('Nilai Minimum')
plt.grid(True)
plt.show()

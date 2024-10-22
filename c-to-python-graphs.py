import time
import random
import matplotlib.pyplot as plt
import pandas as pd

# Zaman ölçüm fonksiyonu
def measure_time(algorithm, input_data):
    start_time = time.time()
    algorithm(input_data)
    end_time = time.time()
    elapsed_time = end_time - start_time
    return elapsed_time

def kare_toplami(n):
    toplam = 0
    for i in range(n):
        toplam += i*i
    return toplam

def loop(n):
    toplam = 0
    for i in range(n):
        for j in range(n):
            toplam+=1
    return toplam       


def generate_random_list(length):
    random_list = [random.randint(1, 100) for _ in range(length)]
    return random_list

# Deney listeleri oluşturma
experiment_sizes = [10, 20, 50, 100, 1000, 10000, 10000]
experiment_results = []

for size in experiment_sizes:
    input_list = generate_random_list(size)
    kare_time = measure_time(kare_toplami, size)
    loop_time = measure_time(loop, size)
    experiment_results.append((size, kare_time, loop_time))


# DataFrame oluşturma
df = pd.DataFrame(experiment_results, columns=['Size', 'Kare Toplami', 'Loop'])

# 'Size' sütununu index olarak ayarlama
df.set_index('Size', inplace=True)

# DataFrame'i yazdırma
df

plt.figure(figsize=(12, 6))
plt.plot(df.index, df['Kare Toplami'], label='Kare Toplami')
plt.plot(df.index, df['Loop'], label='Loop')

plt.xlabel('Dizi Boyutu')
plt.ylabel('Çalişma Süresi (saniye)')
plt.title('Siralama Algoritmalarinin Performans Karşilaştirmasi (Python)')
plt.legend()
plt.grid(True, which="both", ls="-", alpha=0.2)

plt.tight_layout()
plt.show()
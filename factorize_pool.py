import time
from multiprocessing import Pool, cpu_count

def factorize(num):
    factors = []
    for i in range(1, num+1):
        if num % i == 0:
            factors.append(i)
    return factors

if __name__ == '__main__':
    nums = [128, 255, 99999000, 10651060]
    start_time = time.time()
    with Pool(cpu_count()) as pool:
        results = pool.map(factorize, nums)
    end_time = time.time()
    a, b, c, d = results
    print(a)
    print(b)
    print(c)
    print(d)
    print("Time taken:", end_time - start_time)
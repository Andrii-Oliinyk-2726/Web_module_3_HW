import time

def factorize(*nums):
    results = []
    for num in nums:
        factors = []
        for i in range(1, num+1):
            if num % i == 0:
                factors.append(i)
        results.append(factors)
    return results

start_time = time.time()
a, b, c, d = factorize(128, 255, 99999000, 10651060)
end_time = time.time()

print(a)
print(b)
print(c)
print(d)
print("Time taken:", end_time - start_time)



import random

def generate_sample(n):
    data = [random.randint(1, 1000000) for _ in range(n)]  # range of values from 1 to maximum allowed size of datasets
    return data


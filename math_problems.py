def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

if __name__ == "__main__":
    a, b = 0, 1
    print(f"{a} + {b} = {add(a, b)}")
    print(f"{a} - {b} = {subtract(a, b)}")
def fizzBuzz(max):
    for i in range(1, max + 1):
        print("fizz" * (i%3 == 0) + "buzz" * (i%5 == 0) or i)

if __name__ == "__main__":
    print(f'fizzBuzz : {fizzBuzz(50)}')
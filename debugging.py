divisors = lambda num: [i for i in range(1, num + 1) if num % i == 0];


def main():
  try:
    num = int(input("Input yout number please: "));
    if num < 0:
      raise ValueError("Your number is negative, but must be positive and natural number");
    print(divisors(num));
    print("End my program");
  except ValueError as error:
    print(error);


if __name__ == "__main__":
  main();


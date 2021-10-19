divisors = lambda num: [i for i in range(1, num + 1) if num % i == 0];


def main():
  num = input("Input yout number please: ");
  assert num.isnumeric() and int(num) >= 0, "Must be a number your answer and this must be a positive number";
  print(divisors(int(num)));
  print("End my program");


if __name__ == "__main__":
  main();


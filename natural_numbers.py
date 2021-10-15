def main():
  # natural_numbers_cubic = [];
  # by_three_numbers = [];

  # for natural_number in range(1, 101):
  #   natural_numbers_cubic.append(natural_number ** 2);
  #   if (natural_number % 3 != 0):
  #     by_three_numbers.append(natural_number ** 2);

  # print("natural_numbers_cubic:", natural_numbers_cubic);
  # print(""
  # "");
  # print("by_three_numbers:", by_three_numbers);
  squares = [i for i in range(1, 10001) if (i % 4 == 0) and (i % 6 == 0) and (i % 9 == 0)];

  print(squares);


def challenge():
  pass


if __name__ == "__main__":
  main();
  challenge();


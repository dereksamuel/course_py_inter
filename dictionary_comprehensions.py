from math import sqrt;

def main():
  # my_dictionary = {};

  # for index in range(1, 101):
  #   if (index % 3 != 0):
  #     my_dictionary[index] = index ** 2;
  my_dictionary = { index: sqrt(index) for index in range(1, 1001) if index % 3 != 0 };

  print(my_dictionary);


if __name__ == "__main__":
  main();


ENCODING_DEFAULT = "utf-8";


def validationLines(line):
  line_to_number = int(line);

  try:
    assert line_to_number > 0, "The number must be positive";
    return line_to_number;
  except ValueError as error:
    print(error);


def read():
  numbers = [];
  with open("./files/numbers.txt", "r", encoding=ENCODING_DEFAULT) as file:
    numbers = [validationLines(line) for line in file];
  print(numbers);


def write():
  names = ["Derek", "Pp", "Daniel", "Hector", "Milena", "Rocío 😎"];
  with open("./files/names.txt", "w", encoding=ENCODING_DEFAULT) as file:
    for name in names:
      file.write(name);
      file.write("\n");


def main():
  read();
  write();


if __name__ == "__main__":
  main();


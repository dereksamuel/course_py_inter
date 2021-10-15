def main():
  the_list = [1, "Hi", 2, 3, 5];
  the_dict = {
    "first_name": "Derek",
    "last_name": "Paul",
  };

  super_list = [
    {
      "first_name": "Derek",
      "last_name": "Paul",
    },
    {
      "first_name": "Dabiel",
      "last_name": "Paul",
    },
    {
      "first_name": "Dereka",
      "last_name": "Paula",
    },
    {
      "first_name": "Arduino",
      "last_name": "Pol",
    },
  ];

  super_dic = {
    "natural_nums": [1, 2, 3, 4, 5, 6],
    "integer_nums": [-1, -2, 0, 1, 2],
    "floating_nums": [1.1, 2.2, 3.3],
  };


  for key in super_list:
    print(key["first_name"], "-", key["last_name"]);


if __name__ == "__main__":
  main();


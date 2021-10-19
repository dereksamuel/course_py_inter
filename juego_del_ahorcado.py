import random;
from os import system, name;


def gameOver(word):
  print("""


    ============================= GAME OVER 😥😥 =============================

  """);
  print("The WORD:", word);
  restartDictionary();
  return;


def restartDictionary():
  restart = input("Do You want restart the game(y/n)? ");
  while(restart != "y" and restart != "n"):
    restart = input("Do You want restart the game(y/n)? ");
  if (restart == "y"):
    main();


def printHeader():
  print("""
    ============================= by Derek 😀 =============================


    @@@@@    @@@  @@@  @@@@@@@@  @@@@@@@@   @@@@@@@@    @@@@@    @@@@@     @@@@@@@@
  @@@   @@@  @@@  @@@  @@@  @@@  @@@  @@@   @@@       @@@   @@@  @@@  @@@  @@@  @@@
  @@@@@@@@@  @@@@@@@@  @@@  @@@  @@@@@@@    @@@       @@@@@@@@@  @@@  @@@  @@@  @@@
  @@@   @@@  @@@  @@@  @@@  @@@  @@@  @@@   @@@       @@@   @@@  @@@  @@@  @@@  @@@
  @@@   @@@  @@@  @@@  @@@@@@@@  @@@   @@@  @@@@@@@@  @@@   @@@  @@@@@     @@@@@@@@ (the game || @copyright pp)

  """);
  print("");


def listToString(s):
  str1 = "";

  for ele in s:
    str1 += ele;

  return str1;


def getWords():
  words = [];
  with open("./files/data.txt", "r", encoding="utf-8") as file:
    words = [word.split("\n")[0] for word in file];
  return words;


def clearConsole():
  if name == "nt":
    system("cls");
  else:
    system("clear");


def main():
  clearConsole();
  word = random.choice(getWords()).upper();
  intentos = len(word);
  printText = len(word) * "_";
  printHeader();
  print(printText);
  print("");
  print("intentos: (" + str(intentos) + ")");
  answer = input("Choice any letter: ").upper();

  clearConsole();
  if not (answer in word):
    intentos -= 1;

  while(answer != word and intentos > 0):
    clearConsole();
    printHeader();
    print("");
    printTextList = list(printText);
    for a in answer:
      if a in word:
        for index_w, w in enumerate(word):
          if a == w:
            printTextList[index_w] = w;
    if not (answer in word):
      intentos -= 1;
    if (intentos == 0):
      gameOver(word);
    print(listToString(printTextList));
    print("intentos: (" + str(intentos) + ")");
    answer = input("Choice any letter: ").upper();

  if (intentos == 0):
    gameOver(word);

  if (answer == word):
    print("""
                🎉🎈🎉🎉🎉🎊🎈🎊🎉🎈🎈🎈🎈🎉🎉🎉🎊🎊
      @             @                              @             @
        @         @                                  @         @
          @     @                                      @     @
            @@@                                          @@@
          @ @@@ @                                      @ @@@ @
          @ @@@ @    Thank YOU FOR PLAY THIS GAME      @ @@@ @
            @@@                                          @@@
          @     @                                      @     @
        @         @                                  @         @
      @             @                              @             @
                🎉🎈🎉🎉🎉🎊🎈🎊🎉🎈🎈🎈🎈🎉🎉🎉🎊🎊
    """);
    restartDictionary();


if __name__ == "__main__":
  main();


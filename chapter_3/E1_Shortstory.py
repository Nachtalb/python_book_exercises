import os

from colorama import init, Fore

if os.name is "nt":
    init()  # if windows call init() from colorama, to filter ANSI escape sequences out and replace them with
    # equivalent Win32 calls

print(Fore.GREEN + "##################" + Fore.RESET)
print(Fore.GREEN + "#" + Fore.RESET, "Sailent Sounds", Fore.GREEN + "#" + Fore.RESET)
print(Fore.GREEN + "##################" + Fore.RESET)
print()

gender = ""
while gender is not "m" and gender is not "f":
    gender = input("Are you male (m) or female (f)? ")

animal = ""
while animal is "":
    animal = input("What is your favorite land animal? ").lower()

gender = "Boy" if gender is "m" else "Girl"
print()

print("Back when I was young enough to invent and trust \n"
      "in my own " + Fore.GREEN + gender + Fore.RESET + " Scout knot, I tied a tape-recorder to \n"
                                                        "a " + Fore.GREEN + animal + Fore.RESET + "’s back and set it free. The first hard rain \n"
                                                                                                  "must’ve broken the flimsy thing, but I like to pretend \n"
                                                                                                  "it recorded the rain without breaking. This way, if the \n"
      + Fore.GREEN + animal + Fore.RESET + " ever returned, I could listen to the salient \n"
                                           "sounds teeter throughout the hum of low-fidelity. \n"
                                           "Maybe I’d hear my voice as a child telling it not to \n"
                                           "go too far. Or maybe I’d only hear it passing \n"
                                           "through the tall grass and slowly going too far.")
print("\n - Story by Connor Walsh")
print("   http://www.100wordstory.org/6279/salient-sounds/")

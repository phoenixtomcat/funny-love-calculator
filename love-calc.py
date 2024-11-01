print("The Love Calculator is calculating your score...")
name1 = input("What's your name: ")
name2 = input("What's their name: ")


name1 = name1.lower() #lower case the names in case there are capital letters
name2 = name2.lower()

T_count = name1.count("t") + name2.count("t") #count the number of times t occurs in the names
R_count = name1.count("r") + name2.count("r") #same as above with r
U_count = name1.count("u") + name2.count("u")#same as above with u
E_count = name1.count("e") + name2.count("e")#same as above with e

L_count = name1.count("l") + name2.count("l") #same as above with l
O_count = name1.count("o") + name2.count("o")#same as above with o
V_count = name1.count("v") + name2.count("v")#same as above with v
#e is already counted above with the word true


true_count = T_count + R_count + U_count + E_count #add all the counts spelling true
love_count = L_count + O_count + V_count + E_count #add all the counts spelling love

love_score = int(f"{true_count}" + f"{love_count}")

if love_score < 10 or love_score > 90:
  print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score >= 40 and love_score <= 50:
  print(f"Your score is {love_score}, you are alright together.")
else:
  print(f"Your score is {love_score}.")


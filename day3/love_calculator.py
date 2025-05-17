print("Welcome to love calculator!")
name1 = input("What is your name?")
name2 = input("Whats is their name?")

name1_lower = name1.lower()
name2_lower = name2.lower()

count_t = name1_lower.count("t") + name2_lower.count("t")
count_r = name1_lower.count("r") + name2_lower.count("r")
count_u = name1_lower.count("u") + name2_lower.count("u")
count_e = name1_lower.count("e") + name2_lower.count("e")

count_true = count_t + count_r + count_u + count_e

count_l = name1_lower.count("l") + name2_lower.count("l")
count_o = name1_lower.count("o") + name2_lower.count("o")
count_v = name1_lower.count("v") + name2_lower.count("v")
count_e = name1_lower.count("e") + name2_lower.count("e")

count_love = count_l + count_o + count_v + count_e 

love_score = count_true * 10 + count_love
print(love_score)

if love_score < 10 or love_score > 90:
    print(f"Your love is {love_score}, you go together like coke and mentos.")
elif love_score >= 40 and love_score <= 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")

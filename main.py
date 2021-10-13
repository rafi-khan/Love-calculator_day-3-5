print("Welcome to love calculator")
name_1 = input("What is your name?\n").lower()
name_2 = input("What is his/her name?\n").lower()
total_true = 0
total_love = 0
t = 0
r = 0
u = 0
e_1 = 0
l = 0
o = 0
v = 0
e_2 = 0

for char in (name_1, name_2):
    t += char.count("t")
    r += char.count("r")
    u += char.count("u")
    e_1 += char.count("e")
total_true += t + r + u + e_1

for char in (name_1, name_2):
    l += char.count("l")
    o += char.count("o")
    v += char.count("v")
    e_2 += char.count("e")
total_love += l + o + v + e_2

print(f"T occures {t} times\nR occures {r} times\nU occures {u} times\nE occures {e_1} times")
print(f"Total: {total_true}")

print(f"L occures {l} times\nO occures {o} times\nV occures {v} times\nE occures {e_2} times")
print(f"Total: {total_love}")

# print(f"Love score: {total_true}{total_love}")

total_score = int(f"{total_true}{total_love}")

if total_score > 90 or total_score < 10:
    print(f"Your score is {total_score}, you go together like coke and mentos")
elif  40 < total_score < 50:
    print(f"Your score is {total_score}, you alright together")
else:
    print(f"Your score is {total_score}")
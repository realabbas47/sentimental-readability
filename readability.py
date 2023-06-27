# TODO
txt = input("TEXT: ")

L, S, W = 0, 0, 0

for x in txt:
    if x.isalpha():
        L += 1
    elif x == '.' or x == '!' or x == '?':
        S += 1
    elif x == ' ':
        W += 1

gd = 0.0588 * (100 * L / (W + 1)) - 0.296 * (100 * S / (W + 1)) - 15.8

if gd < 1:
    print("Before Grade 1")
elif gd >= 16:
    print("Grade 16+")
else:
    print(f"Grade {round(gd)}")

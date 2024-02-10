S = input()

if S.len() == 1:
    if S.isupper():
        print("Yes")
else:
    if S[0].isupper and S[1:].islower():
        print("Yes")
    else:
        print("No")

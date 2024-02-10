A, B, C = map(int, input().split())

if C % 2 == 0:
    if abs(A) < abs(B):
        print("<")
    elif abs(A) == abs(B):
        print("=")
    else:
        print(">")
else:
    if 0 <= A:
        if 0 <= B:
            if abs(A) < abs(B):
                print("<")
            elif abs(A) == abs(B):
                print("=")
            else:
                print(">")
        else:
            print(">")
    else:
            if 0 <= B:
                print("<")
            else:
                if abs(A) < abs(B):
                    print(">")
                elif abs(A) == abs(B):
                    print("=")
                else:
                    print("<")

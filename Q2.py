I = int(0)
K = int(1)
X = int(input())
if(X == 0):
    print("Pertence")
else:
    while(X>=K):
        if(X==K):
            break
        else:
            J = K
            K = K + I
            I = J
    if(X==K):
        print("Pertence")
    else:
        print("Não pertence")
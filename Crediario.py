V = int(input())
P = int(input())
R = V%P
while(R>0):
    X = (V // P) + 1
    V = V - X
    P = P - 1
    print("\n", X)
    R = V % P
if(R==0):
    for i in range (P+1, P!=0, -1):
        VlrPre=V//P
        print("\n", VlrPre);
def multable(n):
    for i in range(1,n+1):
        for j in range(1,n+1):
            ij = i * j
            print("{}x{}={}".format(i,j,ij))
        print("\n")

multable(10)





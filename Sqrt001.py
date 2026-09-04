d = x = 1.000
t = 0

y = float(input("Enter a number:"))

while d>0.01 or d<-0.01 or t<51 :
    t+=1
    d = y/x-x

    if d>=-0.01 and d<=0.01 :
        print("Squre root is", x)

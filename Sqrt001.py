d = x = 1.000
t = 0

y = float(input("Enter a number:"))

while (d>0.01 or d<-0.01) and t<51 :
    t+=1
    d = y/x-x

    if d>=-0.01 and d<=0.01 :
        print("Square root: ", x)

    
    elif d>1: x+=1
    elif d>0.1: x+=0.1
    elif d>0.01: x+=0.01
    elif d<-1: x-=0.9
    elif d<-0.1: x-=0.09
    else: x-=0.009

print("Total tries: ",t)
        

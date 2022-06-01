import math
import time 
while 1>0:
    print("Hikmet Ramazanov")
    print("-")
    print("-")
    print("-")
    secim=input("Riyaziyyat=> 1 \nFizika=>2 \nKimya=>3 \nsecim: ")
    print("-")
    print("-")
    print("-")
    if secim=="1":
        print("-")
        print("-")
        print("-")
        print("-")
        print("-")
        print("-")
        print("Diskriminant=> 1    \nHeron => 2 \nKok Alti=>3 \nPifaqor =>4 \nSahe =>5 \nsecim: " )
        print("-")
        print("-")
        print("-")
        option=input("Select:")
        print("-")
        print("-")
        print("-")
        if option == "1":
            print("-")
            print("-")
            print("-")
            print("-")
            print("-")
            print("-")
            print("Diskriminanti secdin <3")
            print("-")
            print("-")
            print("-")
            a=float(input("Select A:"))
            b=float(input("Select B:"))
            c=float(input("Select C:"))
            D=(b**2)-(4*a*c)
            if D <0:
                print("kok yoxdur")
            elif D > 0:
                x1=(-b-(D**0.5))/(2*a)
                x2=(-b+(D**0.5))/(2*a)
                print("kokler=>", "x1=", x1 , "x2=", x2 )
            else:
                x12=(-b)/(2*a)
                print("1 koku var =>" , x12)
        elif option == "2":
            print("-")
            print("-")
            print("-")
            print("-")
            print("-")
            print("-")
            print("Heronu secdin <3")
            print("-")
            print("-")
            print("-")
            a=float(input("a terefi: "))
            b=float(input("b terefi: "))
            c=float(input("c terefi: "))
            p= (a+b+c)/2
            S=(p*(p-a)*(p-b)*(p-c))**0.5
            print("Sahe =>" , S)
        elif option =="3":
            a=int(input("√"))
            b=int(math.isqrt(a))
            print("√",a ,"=" , b,"^2" )
        elif option =="4":
            sc=input("hansi terefi tapirsan ? \na=>1 \nb=>2 \nc=>3 \nsecim: ")
            if sc== "1":
                b=float(input("b-ni yazin:"))
                c=float(input("c-ni yazin:"))
                b=b**2
                c=c**2
                a=c-b
                a=a**0.5
                print("a terefi =>",a)
            elif sc== "2":
                a=float(input("a-ni yazin:"))
                c=float(input("c-ni yazin:"))
                c=b**2
                a=a**2
                b=c-a
                b=b**0.5
                print("b terefi =>",b)
            elif sc == "3":
                a=float(input("a-ni yazin:"))
                b=float(input("b-ni yazin:"))
                b=b**2
                a=a**2
                c=a+b
                c=c**0.5
                print("c terefi =>",c)
        elif option == "5":
            print("Saheni secdin")
            a=input("Ucbucaq =>1 \nKvadrat =>2 \nDaire =>3 \nDuzbucaqli =>4 \nTrapesiya =>5 \nRomb =>6 \n Paraleloqram =>7 \nsecim: ") 
            if a=="1":
                us=input("Duzbucaqli =>1 beraberterefli =>2 \nsecim:")
                if us =="1":
                    print("   /|")
                    print("c / |b")
                    print(" /--|")
                    print("  a" )
                    b=float(input("b=? : "))
                    a=float(input("a=? : "))
                    s=float((a*b)/2)
                    print("sahe: " , s)
                elif us == "2":
                    a=float(input("a terefi: "))
                    b=float(input("b terefi: "))
                    c=float(input("c terefi: "))
                    p= (a+b+c)/2
                    S=(p*(p-a)*(p-b)*(p-c))**0.5
                    print("Sahe =>" , S)
            elif a=="2":
                print("   a  ")
                print(" -----")
                print("a|   |")
                print(" -----")
                a=float(input("a=? :"))
                print("Sahe =>" , a*a)
            elif a=="3":
                r=float(input("radius: "))
                print("Sahe =>" , p*r**2)
            elif a=="4":
                print("   a  ")
                print(" -----")
                print("b|   |")
                print(" |   |")
                print(" -----")
                float(input("a=? :"))
                float(input("b=? :"))
                print("Sahe =>" , a*b)
            elif a=="5":
                h=float(input("hundurluk: "))
                b=float(input("kicik oturacaq: "))
                a=float(input("boyuk oturacaq: "))
                print("Sahe => " , (a+b)*h/2)
            elif a=="6":
                d1=float(input("d1=? :"))
                d2=float(input("d2=? :"))
                S=("Sahe => " , (d1*d2)/2)
            elif a=="7":
                h=float(input("hundurluk: "))
                b=float(input("oturacaq: "))
                print("Sahe =>", h*b)


        else:
            print("-")
            print("-")
            print("-")
            print("-")
            print("-")
            print("-")
            print("zehmet olmasa duzgun emeliyyat secin")
            print("-")
            print("-")
            print("-")
    else:
        print("hele gelmeyib :D")

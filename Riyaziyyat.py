import math
import time 
import itertools
while 1>0:
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
        print("Diskriminant=> 1    \nHeron => 2 \nKok Alti=>3 \nPifaqor =>4 \nSahe =>5 \nPerimetr =>6 \nFaktorial =>7 \nab =>8 \nsecim: " )
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
                p=3.14
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
        elif option=="6":
            a=input("Ucbucaq =>1 \nKvadrat =>2 \nDaire =>3 \nDuzbucaqli =>4 \nRomb =>5 \nsecim: ") 
            if a =="1":
                a=float(input("a terefi:"))
                b=float(input("b terefi:"))
                c=float(input("c terefi:"))
                print("Perimetr: " , a+b+c)
            elif a=="2":
                a=float(input("a terefi:"))
                print("Perimetr: " , a*4)
            elif a=="3":
                r=float(input("radius:"))
                p=3.14
                print("Perimetr: " ,2*p*r)
            elif a=="4":
                a=float(input("a terefi:"))
                b=float(input("b terefi:"))
                print("Perimetr:" , (a+b)*2)
            elif a=="5":
                a=float(input("a terefi:"))
                print("Perimetr: " , 4*a)
            else:
                print("zehmet olmasa duzgun emeliyyat secin")
        elif option =="7":
            a=float(input("eded: "))
            f=math.factorial(a)
            print("Faktorial",a,"=",f)
        elif option=="8":
            a=input("1=[a,b] 2=[a,b,c] 3=[a,b,c,e] 4=[a,b,c,d,e]")
            if a=="1":
                a=int(input("a:"))
                b=int(input("b:"))
                print("-")
                print("-")
                print("-")
                stuff = [a,b]
                for L in range(0, len(stuff)+1):
                    for subset in itertools.combinations(stuff, L):
                        print(subset)
                print("-")
                print("-")
                print("-")
            elif a=="2":
                a=int(input("a:"))
                b=int(input("b:"))
                c=int(input("c:"))
                print("-")
                print("-")
                print("-")
                stuff = [a, b, c]
                for L in range(0, len(stuff)+1):
                    for subset in itertools.combinations(stuff, L):
                        print(subset)
            elif a=="3":
                a=int(input("a:"))
                b=int(input("b:"))
                c=int(input("c:"))
                d=int(input("d:"))
                print("-")
                print("-")
                print("-")
                stuff = [a, b, c , d]
                for L in range(0, len(stuff)+1):
                    for subset in itertools.combinations(stuff, L):
                        print(subset)
                print("-")
                print("-")
                print("-")
            elif a=="4":
                a=int(input("a:"))
                b=int(input("b:"))
                c=int(input("c:"))
                d=int(input("d:"))
                e=int(input("e:"))
                print("-")
                print("-")
                print("-")
                stuff = [a, b, c , d , e]
                for L in range(0, len(stuff)+1):
                    for subset in itertools.combinations(stuff, L):
                        print(subset)
                
                print("-")
                print("-")
                print("-")
            else:
                print("zehmet olmasa duzgun emeliyyat secin")
                
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
    elif secim == '3':
        e=input("En cox istifade olunan elementler :) => ")
        if e=="H" or "Hidrogen":
            print("Sira:1 Qrup:1") 
            print("Valentlik: 1 ,-1")
            print("1,00794 q/mol")
        elif e=="He" or "Helium":
            print("Sira:1 Qrup:8")
            print("Valentlik: 0")
            print("4.002 q/mol")
        elif e=="Li" or "Lityum":
            print("Sira:2 Qrup:1")
            print("Valentlik: 1")
            print("6.9 q/mol")
        elif e=="Be" or "Berillium":
            print("Sira:2 Qrup:2")
            print("Valentlik: 2")
            print("9.012 q/mol")
        elif e=="B" or "Bor":
            print("Sira:2 Qrup:3")
            print("Valentlik: 3")
            print("10.8 q/mol")
        elif e=="Ca" or "Karbon":
            print("Sira:2 Qrup:4")
            print("Valentlik: 4")
            print("12.011 q/mol")
        elif e=="N" or "Azot":
            print("Sira:2 Qrup:5")
            print("Valentlik: 3")
            print("14.00 q/mol")
        elif e=="O" or "Oksigen":
            print("Sira:1 Qrup:6")
            print("Valentlik: 2")
            print("15.99 q/mol")
        elif e=="He" or "Helium":
            print("Sira:1 Qrup:8")
            print("Valentlik: 0")
            print("4.002 q/mol")
        elif e=="He" or "Helium":
            print("Sira:1 Qrup:8")
            print("Valentlik: 0")
            print("4.002 q/mol")
        elif e=="He" or "Helium":
            print("Sira:1 Qrup:8")
            print("Valentlik: 0")
            print("4.002 q/mol")
        elif e=="He" or "Helium":
            print("Sira:1 Qrup:8")
            print("Valentlik: 0")
            print("4.002 q/mol")
        elif e=="He" or "Helium":
            print("Sira:1 Qrup:8")
            print("Valentlik: 0")
            print("4.002 q/mol")
        elif e=="He" or "Helium":
            print("Sira:1 Qrup:8")
            print("Valentlik: 0")
            print("4.002 q/mol")
        

    else:
        print("hele gelmeyib :D")

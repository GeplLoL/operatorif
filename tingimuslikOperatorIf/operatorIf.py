from math import *
#1
nimi = input("Sisestage oma nimi: ")

if nimi=="Juku" or nimi.upper()=="JUKU":
    age = int(input("Sisestage oma astat: "))
    if age<=0 or age>100:
        print("viga andmetega")
    elif age>1 and age<6:
        print("tasuta")
    elif age>7 and age<14:
        print("lastepilet")
    elif age>15 and age<65:
        print("täispilet")
    elif age>65 and age<100:
        print("sooduspilet")
else:
    print("sisestatud vale nimi")
print("")
#2
x = input("Sisestage oma nimi: ")
y = input("Sisestage oma nimi: ")
if x.isalpha() and y.isalpha():
    if (x =="Timur" and y=="Deniss") or (x=="Deniss" and y=="Timur"):
        print(f"Täna istute koos {x} ja {y}")
print("")
#3
print("ristkülikukujulise toa seinte pikkused")
try:
    a = float(input("a: "))
    b = float(input("b: "))
    S = a*b
    if a<0 or b<0:
        print("numbri viga")
    vastus = input("Kas soovite põranda remonti?(ja or ei)")
    if vastus=="ja" or vastus.upper()=="JA":
        hind = float(input("kui palju on ruutmeeter: "))
        otvet = hind*S
        print(f"remondi hind: {otvet}£")
    else:
        print("ei taha nagu tahad")
    print("")
except:
    print("error")
#4
print("kirjuta hind")
hind = float(input("hind:"))
if hind>700:
    vastus=hind-hind*0.3
    print(vastus)
else:
    print(hind)
print("")
#5
kraade = float(input("kui palju kraade: "))
if kraade>=18:
    print("saab kodus hoida")
elif kraade<18:
    print("soovitav toasoojus talvel")
#6
print("")
kasv = float(input("Kirjutage oma vanus"))
if kasv<=0 or kasv>250:
    print("sa oled looduse viga")
elif kasv<=170:
    print("see on madala tõusuga")
elif kasv>171 and kasv<185:
    print("on keskmine kõrgus")
elif kasv>186:
    print("see on pikk")
else:
    print("sa oled looduse viga")
#7
print("")
kasv = float(input("Kirjutage oma vanus: "))
sugu = input("sisestage oma sugu(mees or naine): ")
if sugu=="mees":
    if kasv<=0 or kasv>250:
        print("sa oled looduse viga")
    elif kasv<=170:
        print("see on madala tõusuga")
    elif kasv>171 and kasv<185:
        print("on keskmine kõrgus")
    elif kasv>186:
        print("see on pikk")
    else:
        print("sa oled looduse viga")
elif sugu=="naine":
    
    if kasv<=0 or kasv>250:
            print("sa oled looduse viga")
    elif kasv<=160:
            print("see on madala tõusuga")
    elif kasv>161 and kasv<175:
            print("on keskmine kõrgus")
    elif kasv>176:
            print("see on pikk")
else:
    print("sa oled looduse viga")
print("")
#8
try:
    piima = input("piima hind või mitte: ")
    saia = input("saia hind või mitte: ")
    leib = input("leiva hind või mitte: ")
    if piima=="mitte" and saia=="mitte" and leib=="mitte":
        piima=0
        saia=0
        leib=0
        print("ei ole")
    elif piima.isdigit() and saia.isdigit() and leib.isdigit():
        print(int(piima)+int(saia)+int(leib))
    elif piima=="mitte" and saia=="mitte":
        iima=0
        saia=0
        print(int(piima+int(saia)))
    elif piima=="mitte" and leib=="mitte":
        piima=0
        leib=0
        print(int(piima)+int(leib))
    elif piima=="mitte":
        piima=0
        print(int(piima)+int(saia)+int(leib))
    elif saia=="mitte" and piima=="mitte":
        saia=0
        piima=0
        print(int(saia)+int(piima)+int(leib))
    elif saia=="mitte" and leib=="mitte":
        saia=0
        leib=0
        print(int(saia)+int(leib)+int(piima))
    elif saia=="mitte":
        saia=0
        print(int(saia)+int(leib)+int(piima))
    elif leib=="mitte" and piima=="mitte":
        leib=0
        piima=0
        print(int(leib)+int(piima)+int(saia))
    elif leib=="mitte" and saia=="mitte":
        leib=0
        saia=0
        print(int(leib)+int(saia)+int(piima))
    elif leib=="mitte":
        leib=0
        print(int(leib)+int(saia)+int(piima))
except:
    print("error")
print("")
#9
a = float(input("väljaku pool a: "))
a2 = float(input("väljaku pool b: "))
if a*a2==a**2:
    print("see on ruut")
else:
    print("see ei ruut")
print("")
#10
try:
    a = float(input("a: "))
    b = float(input("b: "))
    c = input("millist toimingut soovite teha: ")
    if c=="+":
        c=a+b
        print(c)
    elif c=="-":
        c=a-b
        print(c) 
    elif c=="*":
        c=a*b
        print(c)
    elif c=="/":
        c=a/b
        print(c)
    else:
        print("error")
except:
    print("andmete sisestamise viga")
print("")
#11
try:
    user = float(input("kui vana sa oled: "))
    if user/5==int(user/5):
        print("sul on aastapäev")
    else:
        print("ok")
except:
    print("andmete sisestamise viga")
print("")
#12
hind = float(input("toote hind: "))
if hind<10:
    vastus=hind-(hind*0.1)
    print(vastus)
elif hind>10:
    vastus=hind-(hind*0.2)
    print(vastus)
else:
    print("error")
print("")
#13
try:
    sugu = input("Mis on sinu sugu?(mees or naine) ")
    if sugu=="mees":
        age = int(input("kui vana sa oled? "))
        if age>=16 and age<=18:
            print("sa sobid meile")
        else:
            print("sa pole õiges vanuses")
    elif sugu=="naine":
        print("lubatud ainult mehed")
except:
    print("andmete sisestamise viga")
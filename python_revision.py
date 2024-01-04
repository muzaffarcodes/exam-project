# Mod olish
son1 = 27
son2 = 5
natija = son1 % son2
print(natija)

#%%Darajaga ko'tarish va sep 
# ni ishlatilishi

son1 = 27
son2 = 5
natija = son1 ** son2
natija2 = son2 ** son1
print(natija,natija2,sep=(" va "))

#%% Indekslash
name = 'Muzaffar'
print(name[:]) #Boshidan oxirigacha
print(name[0:]) # 1chi elementdan oxirigacha
print(name[0:8:2]) # toq o'rinda joylashgan belgilar
print(name[1::2]) # juftlarini chiqarish uchun

#%% Type changing
"""a = 34
float(a)
print(a)
"""
a = 34
a = float(a)
print(type(a))
print(a)

b = 65.3
b = int(b)
print(type(b))
print(b)



#%%
a = 12
b = 5
c = (a**2 + b**2)**0.5
print("Output: ",c)

#%% 
# stringni listga o'tkazish
s = 'Muzaffar'
s = list(s)
print(*s)


#%%
list1 = ["aa","ab","ac","ad"]
list2 = ["bb","bc","bd","be"]
list3 = ["cc","cd","ce","cf"]
list4 = [list1,list2,list3]
#print(list4[2][5])
print(list4[1][3])

#%% TUPLE
tple = ()
print(type(tple))
print(tple)
tple1 = (1,2,3)
print(type(tple1))
print(tple1)


#%% DICTIONARY 

dict_1 = {"a":1,
          "b":2,
          "c":3,
          "d":4,
          "e":5,
          "f":6,
          "g":7}
print(dict_1)
print(dict_1.keys()) # kalitlarni chiqarish uchun (chap)
print(dict_1.values()) # qiymatlarni chiqarish uchun (o'ng)
print(dict_1.items()) # hammasini chiqaradi.

#%% ENG KATTA SIZEDAGI SON
import sys
print(sys.maxsize)

#%% Bool values/operators
# and & or
print(True and True)
print(False and True)
print(True and False)
print(False and False)

print(True or True or True)
print(True or False)
print(False or True)
print(False or False)
# not
print(not 17 == 17)
print(not "Mountstorm" == "Muzaffar")

print(not (1>2 or "Umar" == "UmaR"))

#%% OPERATORLAR > < >= <= != ==

print(ord("a")) # ascii tabledagi qiymatini chiqarish uchun

# IF ELIF ELSE
db_user = 'mountstorm'
db_passwd = 1778

inpt_user = input("Username or Gmail: ")
inpt_passwd = int(input("Password: "))

if(db_user == inpt_user and db_passwd == inpt_passwd):
    print("Welcome Home, Mountstorm")
elif(db_user == inpt_user and db_passwd != inpt_passwd):
    print("Password Xato, fake storm!")
elif(db_user != inpt_user and db_passwd == inpt_passwd):
    print("Username Xato, fake storm!")    
elif(db_user != inpt_user and db_passwd != inpt_passwd):
    print("To'g'ri yoz, fake storm!")

#%% LOOPS (FOR & WHILE)



list1 = [1,2,3,4,5,6,7,8,9,10]
summ = 0
for i in list1:
    summ += i
print(summ)










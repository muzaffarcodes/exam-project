# 1 - masalaning javobi

ism1 = input("1 - ismni kiriting: ")
ism2 = input("2 - ismni kiriting: ")
ism3 = input("3 - ismni kiriting: ")
ism4 = input("4 - ismni kiriting: ")
ism5 = input("5 - ismni kiriting: ")

list1 = [ism1,ism2,ism3,ism4,ism5]
list1.sort()
print("Ismlarni sortlangani: ",list1)


# 2 - masalaning javobi

vaqt = float(input("Vaqtni kiriting: "))
if vaqt > 00.00 and vaqt <= 12.00:
	print("Kunning Birinchi Qismi")
else:
	print("Kunning Ikkinchi Qismi")

# 3 - masalaning javobi

a = int(input("Son kiriting: "))
list1 = []
i = 1
jami = 0
while i <= a:
    try:
        son = float(input(f"{i} - son: "))
        list1.append(son)
        i += 1
        if son % 2 == 1:
        	jami += son
        else:
        	pass

    except:
        print("Faqat Son kiriting!!!")
print("Toq sonlarning yig'indisi: ",jami)
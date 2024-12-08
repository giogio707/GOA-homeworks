#1

print(20>15)    #true
print(200>105)  #true
print(30>19)    #true
print(253>211)  #true
print(22>11)    #true
print(24>12)    #true
print(27>14)    #true
print(28>17)    #true
print(29>19)    #true
print(567>156)  #true

print(30>99)    #false
print(1>2)      #false
print(300>301)  #false
print(79>97)    #false
print(60>70)    #false
print(257>258)  #false
print(10>100)   #false
print(0>1)      #false
print(400>4000) #false
print(718>999)  #false



#2

#explicity არის როდესაც ცვალდის მნიშვლობა გაწერილია პირდაპირ რაც არის მაგალითად a = 3, ხოლო implecity არის როდესაც ცვალიდს მნიშვნელობა ხელით გაწერილი არ არის მაგალითად a = b + c



#3

num1 = int(input("შეიყვანეთ პირველი რიცხვი: "))
num2 = int(input("შეიყვანეთ მეორე რიცხვი: "))

def compare_numbers():
    if num1 > num2:
        print(f"{num1} უფრო მეტია ვიდრე {num2}")
    elif num1 < num2:
        print(f"{num1} უფრო ნაკლებია ვიდრე {num2}")
    else:
        print(f"{num1} ტოლია {num2}-ს")

compare_numbers()
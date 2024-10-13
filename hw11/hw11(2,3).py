# start

## 2
str_lior: str ="lior shay yavne"
#a
print(len(str_lior))
#b
print(str_lior.upper())
#c
print(str_lior.lower())
#d
print(str_lior.startswith("lior"))
#e
print(str_lior.endswith("yavne"))
#f
print(str_lior.split(" "))
#g
str_lior.replace(" ", "*") # dosnt work, why?
print(str_lior.split("*"))
#h
print(str_lior.center(50,"="))
#i
print(str_lior[4::])
#j
print(str_lior[0:4])
#k
print(str_lior[1 :: 2])
#l
print(str_lior.title())

##3
#a
fun_day : str = " fun-day "
print(fun_day.replace(" ", ""))
#b
hello: str = "hello"
print(hello.isalpha())
#c
str_7 = 777
print(str_7.isdigit())    # it's not working on "int" , and i cant save is on "str"
#d
spaces: str = "    "
print(spaces.isspace())
#e
ninja_list: list[str] = ["N","I","N","J","A"]
# print(join(["N","I","N","J","A"]))    #i cant use 'join' i try many options
#f
print(ninja_list)
#g
letter: str ="e"
hEllo :str = "hEllo"
hEllo: str= hEllo.lower()
if letter in hEllo:
    print("True")
#h - Bonus
user_str: str ="py3thon12"

# for char in user_str:
#     if char.isalpha():
#         char.upper()  #it's dosnt work
#         list_str.append(char)
list_str: list[str] = [char.upper() for char in user_str if char.isalpha()]
print(list_str)

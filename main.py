f = open('main.txt', 'r+')

pr = f.read(100)

it = pr.replace("i", "#")
ti = it.replace("o", " ")

WR = input("Выберите режим: нажмите W чтобы начать писать изображение или R чтобы просмотреть уже написанное.\n")

if WR == 'R':
    print()
    print(ti)
if WR == 'r':
    print()
    print(ti)

opr = input("Введите сколько строк будет в вашей картинке (от 1 до 5)\n")
print("Введите вашу картинку, где o - пробел (пустота) и i - заполнение")

if opr == '1':
    one = input("Введите первую строку изображения\n")
    f.write(one)
    f.close
if opr == '2':
    one = input("Введите первую строку изображения\n")
    two = input("Введите вторую строку изображения\n")
    f.write(one)
    f.write("\n")
    f.write(two)
    f.close
if opr == '3':
    one = input("Введите первую строку изображения\n")
    two = input("Введите вторую строку изображения\n")
    three = input("Введите третью строку изображения\n")
    f.write(one)
    f.write("\n")
    f.write(two)
    f.write("\n")
    f.write(three)
    f.close
if opr == '4':
    one = input("Введите первую строку изображения\n")
    two = input("Введите вторую строку изображения\n")
    three = input("Введите третью строку изображения\n")
    four = input("Введите четвертую строку изображения\n")
    f.write(one)
    f.write("\n")
    f.write(two)
    f.write("\n")
    f.write(three)
    f.write("\n")
    f.write(four)
    f.close
if opr == '5':
    one = input("Введите первую строку изображения\n")
    two = input("Введите вторую строку изображения\n")
    three = input("Введите третью строку изображения\n")
    four = input("Введите четвертую строку изображения\n")
    five = input("Введите третью строку изображения\n")
    f.write(one)
    f.write("\n")
    f.write(two)
    f.write("\n")
    f.write(three)
    f.write("\n")
    f.write(four)
    f.write("\n")
    f.write(five)
    f.close

input("Нажмите ENTER чтобы выйти\n")
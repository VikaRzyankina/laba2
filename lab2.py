def repl(n):
    f = {0: 'ноль', 1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять', 6: 'шесть', 7: 'семь', 8: 'восемь',
         9: 'девять'}
    return f.get(n)  # замена из словаря
uwu=[]
kl=False
import re
f=open('text.txt') #открываем файл
while True:
    buff=f.readline() #читаем первый блок
    if not buff: 
        if not kl: #если файл пуст
            print('Файл пуст')
        break
    u=re.findall(r'\b(?!\d*0{5}\d*0{5}\d*0{5}\d*)\d+\b',buff)
    kl=True
    uwu+=u
if len(uwu) == 0:
    print('В файле нет подходящих под условие чисел')
    quit()
for j in uwu: #замена чисел прописью
    exp = []
    for i in j:
        if repl(int(i)) not in exp:
            exp.append(repl(int(i)))
    print(j + ' - ', *exp)

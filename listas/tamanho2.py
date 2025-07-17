count = 0
s = 'Pedro'
l = input('Digite uma letra: ')
for i in s:
    if (i == l):
        count += 1
        break
if count > 0:
    print(f'A letra "{l}" está na string "{s}".')
else:
    print(f'A letra "{l}" não está na string "{s}".')
lists = ['Bmw', 'Mercedes', 'Opel', 'Mazda']

result = len(lists)

result = lists[0]
result = lists[3]
result = lists[-1]

lists[-1] = 'Toyota'
result = lists

result = 'Mercedes' in lists

result = lists[-2]

result = lists[0:3]

lists[-2:] = ['Toyota', 'Renault']
result = lists

result = lists + ['Audi', 'Nissan']

del lists[-1]
result = lists

result = lists[::-1]

studentA = ['Yiğit', 'Bilge', 2010,[70, 60, 70]]
studentB = ['Sena', 'Turan', 1999,[80, 80, 70]]
studentC = ['Ahmet', 'Turan', 1998,[80, 70,90]]

result = studentA[0]
result = studentB[1]
result = studentC[3]

result = f" {studentA[0]} {studentA[1]} {2024 - studentA[2]} yaşında ve not ortalaması {(studentA[3][0] + studentA[3][1] + studentA[3][2]) / 3} "

print(result)

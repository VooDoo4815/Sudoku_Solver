f = open('test1.txt', 'rt')

def setLoneNum(C_List): # Может решить ряд, но только если необходимо узнать одну цифру
	if C_List.count(0)==1:
		C_List[C_List.index(0)]= 45 - sum(C_List)
		return(C_List)
	else:
		return(C_List)

def isint(value):  # Проверка, является ли значение целым числом (True/False)
	try:
		int(value)
		return(True)
	except ValueError:
		return(False)

def ListPureInt(S_list): # Очистка списка от ненужных элементов, приведение к целым числам
	for i in S_list:
		if not(isint(i)): 
			S_list.remove(i)
	S_list.pop()	# Почему-то символ перевода строки не удаляется в предыдущем цикле
	for i in S_list: 
		S_list[S_list.index(i)]=int(i)
	return S_list

def SolveTab(L): # Решает таблицу
	for i in L:
		i = setLoneNum(i)
	return(L)

def TranspTab(L): # Транспонирует "таблицу"
	C_List=[]
	for n in range(9):
		c=[]
		for i in range(9):
			c.append(L[i][n])
		C_List.append(c)		#транспонированный список
	return(C_List)

def CheckTab(L):	# Проверяет, что нет нулей
	sum0 = 0
	for i in L:
		sum0+=i.count(0)
	if sum0 == 0:
		return(True)	
	else:
		return(False)

def SolveSq(L, ru, cu):
	summ=0
	r0=0
	c0=0
	for r1 in range(ru, ru+3):
		for c1 in range(cu,cu+3):
			summ+=L[r1][c1]
			if L[r1][c1]==0: 
				r0=r1
				c0=c1
	if 45>summ>0:
		 L[r0][c0]=45-summ
	return(L)

def SolveAllSq(L):
	for r in range(0, 7, 3):
		for c in range(0, 7, 3):
			L=SolveSq(L, r, c)
	return(L)
	
T_List = []
for i in range(9):				# Выбираем и очищаем данные
	a = list(f.read(19))
	a = ListPureInt(a)
	T_List.append(a)

StrSh=''
m=0
for i in T_List:		# Собираем строку для красивого вывода на экран 
	m+=1
	c=0
	for n in i:
		StrSh+=str(n)+' '
		c+=1
		if c%3==0: StrSh+=' '
	StrSh+='\n'
	if m%3==0: StrSh+='\n'



print(StrSh)

while not(CheckTab(T_List)):	# Решаем строки и столбцы, пока не получим результат
	T_List = SolveTab(T_List)
	T_List = TranspTab(T_List)
	T_List = SolveTab(T_List)
	T_List = TranspTab(T_List)
	T_List = SolveTab(T_List)
	T_List= SolveAllSq(T_List)

StrSh=''
m=0
for i in T_List:		# Собираем строку для красивого вывода на экран 
	m+=1
	c=0
	for n in i:
		StrSh+=str(n)+' '
		c+=1
		if c%3==0: StrSh+=' '
	StrSh+='\n'
	if m%3==0: StrSh+='\n'



print(StrSh)

print(T_List[0:2][0:2])

f.close()



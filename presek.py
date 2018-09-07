import re, sys
print "----------------------------------------------------------------------------"
print "------PROGRAM DEMONSTRIRA PRESEK JEZIKA DVA AUTOMATA NAD ISTOM AZBUKOM------"
print "----------------------------------------------------------------------------"
print "\n\n"

print "-------------"
print "PRVI AUTOMAT:"
print "-------------"

print "Unesite broj stanja automata :"
br_st11 = raw_input()
while(br_st11.isdigit() == False):
	print "Niste uneli broj! Pokusajte ponovo!"
	br_st11 = raw_input()

br_st1 = int(br_st11)

print "Unesite stanja automata :"
stanja1 = []
i = 0		
while(i<br_st1):		
	st = raw_input().strip()
	if(st.isdigit() == True):
		stanja1.append(int(st))
		i = i + 1
	else:
		print "Niste uneli broj! Pokusajte ponovo!"	
		
'''
for i in stanja1:
	print i
'''		

print "Pocetno stanje je : "	
poc1 = raw_input()
t = 1
while(t):
	if(poc1.isdigit() == False):
		print "Niste uneli broj! Pokusajte ponovo!"
		poc1 = raw_input()
		t = 1
	else:
		if(int(poc1) not in stanja1):
			print "Stanje se ne nalazi medju stanjima automata. Pokusajte ponovo!"
			poc1 = raw_input()
			t = 1
		else:
			poc1 = int(poc1)
			t = 0	
		
print "Zavrsno stanje je : "
zav1 = raw_input()
t = 1
while(t):
	if(zav1.isdigit() == False):
		print "Niste uneli broj! Pokusajte ponovo!"
		zav1 = raw_input()
		t = 1
	else:
		if(int(zav1) not in stanja1):
			print "Stanje se ne nalazi medju stanjima automata. Pokusajte ponovo!"
			zav1 = raw_input()
			t = 1
		else:
			zav1 = int(zav1)
			t = 0		


print "Unesite broj elemenata azbuke automata : "
br_azb11 = raw_input()
while(br_azb11.isdigit() == False):
	print "Niste uneli broj! Pokusajte ponovo!"
	br_azb11 = raw_input()

br_azb1 = int(br_azb11)



print "Unesite azbuku automata : "
azbuka1 = []
i = 0
while(i<br_azb1):
	az = raw_input().strip()
	if(az.isalpha() == True):
		azbuka1.append(az)
		i = i + 1
	else:
		print "Niste uneli slovo! Pokusajte ponovo!"
	
'''
print "Ispis azbuke : "
for i in range(0, br_azb1):
	print azbuka1[i]	
'''

print "Unesite broj prelaza : "
br_prel11 = raw_input()

while(br_prel11.isdigit() == False):
	print "Niste uneli broj! Pokusajte ponovo!"
	br_prel11 = raw_input()
	
br_prel1 = int(br_prel11)	

prelazi1 = {}
print "Unesite prelaze u obliku (stanje slovo stanje) :"	

i = 0
while(i<br_prel1):
	pr = raw_input()
	
	if(pr[0] == '(' and pr[len(pr)-1] == ')'):
		pr = pr[1:len(pr)-1]
		
		try:		
			stanje1, slovo, stanje2 = re.split(" ", pr)
		except:
			print "Nedovoljno elemenata izmedju zagrada! Pokusajte ponovo!"
			continue
	
		if((stanje1.isdigit() == True) and (slovo.isalpha() == True) and (stanje2.isdigit() == True)):
			stanje1 = int(stanje1)
			slovo = slovo.strip()
			stanje2 = int(stanje2)
			
			if((stanje1 in stanja1) and (slovo in azbuka1) and (stanje2 in stanja1)):
				
				if(not(prelazi1.has_key((stanje1, slovo)))):
					prelazi1[(stanje1, slovo)] = stanje2	
					i = i + 1
				if(prelazi1.has_key((stanje1, slovo)) and prelazi1[(stanje1, slovo)] != stanje2):
					print "Automat nije DKA! Program se prekida!"
					sys.exit()
			else:
				print "Greska! Stanja/slova u prelazu se ne nalaze u stanjima automata/azbuci automata! Pokusajte ponovo!"
		else:
			print "Greska! Ili niste uneli brojeve za stanja, ili niste uneli slova za azbuku! Poksajte ponovo!"	
	else:			
		print "Neispravan format! Pokusajte ponovo! Ispravan format je (stanje slovo stanje) "	

'''
for i in prelazi1:
	print i,
	print prelazi1[i]
'''	

print "\n\n"
print "-------------"
print "DRUGI AUTOMAT:"
print "-------------"

print "Unesite broj stanja automata :"
br_st22 = raw_input()
while(br_st22.isdigit() == False):
	print "Niste uneli broj! Pokusajte ponovo!"
	br_st22 = raw_input()

br_st2 = int(br_st22)


print "Unesite stanja automata :"
stanja2 = []
i = 0		
while(i<br_st2):		
	st = raw_input().strip()
	if(st.isdigit() == True):
		stanja2.append(int(st))
		i = i + 1
	else:
		print "Niste uneli broj! Pokusajte ponovo!"	
		
'''
for i in stanja1:
	print i
'''		

print "Pocetno stanje je : "	
poc2 = raw_input()
t = 1
while(t):
	if(poc2.isdigit() == False):
		print "Niste uneli broj! Pokusajte ponovo!"
		poc2 = raw_input()
		t = 1
	else:
		if(int(poc2) not in stanja2):
			print "Stanje se ne nalazi medju stanjima automata. Pokusajte ponovo!"
			poc2 = raw_input()
			t = 1
		else:
			poc2 = int(poc2)
			t = 0	
		
print "Zavrsno stanje je : "
zav2 = raw_input()
t = 1
while(t):
	if(zav2.isdigit() == False):
		print "Niste uneli broj! Pokusajte ponovo!"
		zav2 = raw_input()
		t = 1
	else:
		if(int(zav2) not in stanja2):
			print "Stanje se ne nalazi medju stanjima automata. Pokusajte ponovo!"
			zav2 = raw_input()
			t = 1
		else:
			zav2 = int(zav2)
			t = 0		


print "Unesite broj elemenata azbuke automata : "
br_azb22 = raw_input()
while(br_azb22.isdigit() == False):
	print "Niste uneli broj! Pokusajte ponovo!"
	br_azb22 = raw_input()

br_azb2 = int(br_azb22)



print "Unesite azbuku automata : "
azbuka2 = []
i = 0
while(i<br_azb2):
	az = raw_input().strip()
	if(az.isalpha() == True):
		azbuka2.append(az)
		i = i + 1
	else:
		print "Niste uneli slovo! Pokusajte ponovo!"
	
'''
print "Ispis azbuke : "
for i in range(0, br_azb1):
	print azbuka1[i]	
'''

for i in azbuka1:
	if i not in azbuka2:
		print "Greska! Azbuke se ne poklapaju! Program se prekida!"
		sys.exit()


print "Unesite broj prelaza : "
br_prel22 = raw_input()

while(br_prel22.isdigit() == False):
	print "Niste uneli broj! Pokusajte ponovo!"
	br_prel22 = raw_input()
	
br_prel2 = int(br_prel22)	

prelazi2 = {}
print "Unesite prelaze u obliku (stanje slovo stanje) :"	

i = 0
while(i<br_prel2):
	pr = raw_input()
	
	if(pr[0] == '(' and pr[len(pr)-1] == ')'):
		pr = pr[1:len(pr)-1]
		
		try:		
			stanje1, slovo, stanje2 = re.split(" ", pr)
		except:
			print "Nedovoljno elemenata izmedju zagrada! Pokusajte ponovo!"
			continue
	
		if((stanje1.isdigit() == True) and (slovo.isalpha() == True) and (stanje2.isdigit() == True)):
			stanje1 = int(stanje1)
			slovo = slovo.strip()
			stanje2 = int(stanje2)
			
			if((stanje1 in stanja2) and (slovo in azbuka2) and (stanje2 in stanja2)):
				
				if(not(prelazi2.has_key((stanje1, slovo)))):
					prelazi2[(stanje1, slovo)] = stanje2	
					i = i + 1
				if(prelazi2.has_key((stanje1, slovo)) and prelazi2[(stanje1, slovo)] != stanje2):
					print "Automat nije DKA! Program se prekida!"
					sys.exit()
			else:
				print "Greska! Stanja/slova u prelazu se ne nalaze u stanjima automata/azbuci automata! Pokusajte ponovo!"
		else:
			print "Greska! Ili niste uneli brojeve za stanja, ili niste uneli slova za azbuku! Poksajte ponovo!"	
	else:			
		print "Neispravan format! Pokusajte ponovo! Ispravan format je (stanje slovo stanje) "	


'''	
for i in prelazi2:
	print i,
	print prelazi2[i]
'''		


	
print "\n"	
print "------------------------------"
print "------------PRESEK------------"
print "------------------------------"

pocetno = [poc1, poc2]
print "Pocetno stanje je : ",
print pocetno

zavrsno = [zav1, zav2]
print "Zavrsno stanje je : ",
print zavrsno


prelazi = []
print "Prelazi su:"
for i in range(0, br_st1):
	for j in range(0, br_st2):
		prelazi.append([stanja1[i], stanja2[j]])


'''
for i in prelazi:
	print i	
'''


for i in prelazi:
	for j in prelazi:
		for k in azbuka1:
			f2 = j[0]
			s2 = j[1]
			
			if(prelazi1.has_key((i[0], k)) and prelazi2.has_key((i[1], k))):
				if((prelazi1[(i[0], k)] == f2) and (prelazi2[(i[1], k)] == s2)):
					print i,
					print "->(",
					print k,
					print ")",
					print j
				else:
					continue
					
			elif((prelazi1.has_key((i[0], k))) and not(prelazi2.has_key((i[1], k)))):
				if((prelazi1[(i[0], k)] == f2)):
					print i,
					print "->(",
					print k,
					print ")",
					print j
				else:
					continue
			elif(not(prelazi1.has_key((i[0], k))) and (prelazi2.has_key((i[1], k)))):
				if((prelazi2[(i[1], k)] == s2)):				
					print i,
					print "->(",
					print k,
					print ")",
					print j
				else:
					continue
			else:
				continue					
					


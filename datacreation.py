import random 
import time
import json 

def generateName(f):
	k = [line.strip() for line in f]
	return k
	# print(k)
	# k = f.readlines()[random.randint(0,30000)]
	# print(k)
	# return k

def generateSurname(f):
	k = [line.strip() for line in f]
	return k


def generateEmail(f):
	k = [line.strip() for line in f]
	return k

def generatePhone():
	n=str(random.randint(90,99))+str(random.randint(10000000,99999999))
	return n


if __name__ == '__main__':

	n = int(input("Number of record you want to generate\n"))
	file_name = input("Enter file name\n")
	with open(file_name,"a+") as f,open('name.txt','r') as name,open('surname.txt','r') as surname,open('emails.txt','r') as email:
		Name = generateName(name)
		Sur = generateSurname(surname)
		Email = generateEmail(email)
		start = time.time()
		k = n
		while n>0:
			s={"id":"TCS"+str(random.randint(100000,999999)),
				"firstName": Name[random.randint(0,30224)].split(" ")[0],
				"lastName":Sur[random.randint(0,1799)],
				"email":Email[random.randint(0,212880)],
				"phone":int(generatePhone()),
				"age":random.randint(21,40),
				"gender":random.choice(['male','female']),
				"level":random.choice(['junior','senior']),
				"experience":random.randint(0,30),
				"salary":random.randint(500000,2000000)
			}
			jsonData=json.dumps(s)
			# print(n,"generating data.....",s)
			f.write(jsonData)
			f.write("\n")
			n-=1
		print(k," number of data generated in "+str(time.time()-start) +" second")




# l = []
# with open('emails.txt','r+') as f:
# 	k = f.readlines()[random.randint(0,212881)]
# 	print(k)
	# with open('surname.txt','w+') as w:
	# 	for i in k:
	# 		w.write(i)
	# 		w.write("\n")
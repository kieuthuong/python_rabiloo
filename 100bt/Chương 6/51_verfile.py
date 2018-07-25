#Coi ký tự trắng (space) là ký tự phân tách các từ. Lấy đầu ra của bài 50 làm đầu vào,
# trích xuất các từ trong các câu và in ra theo định dạng: 
#mỗi dòng 1 từ. In ra dòng trắng để đánh dấu kết thúc câu.
import re
import sys
import os
def get_word(str):
	string = ''
	regx = re.compile(r'([\.;:\?!])\s+([A-Z])')
	m = regx.search(str)
	last_pos = 0
	pos = m.start() if m != None else None
	
	while ( pos != None ):
		s = str[last_pos:pos+1] 
		x=re.sub(r'[\W]', ' ',s)
		arr_words=x.split()
		for i in range(len(arr_words)):
			string += arr_words[i] + "\n"

			#with open("output_ex51.txt", "w") as file:
				#file.write(arr_words[i])
		last_pos = last_pos + m.end() + 1 if m != None else None
		m = regx.search(str[last_pos:])
		pos = last_pos + m.start() if m != None else None
	return string

if __name__ == '__main__':
	os.system('cls' if os.name == 'nt' else 'clear')
	with open('nlp.txt', 'r') as f:
		f1 = open('demo_file2.txt', 'w')
		string = ''
		for line in f:
			line = line.strip()
			if line == '':
				continue
			string += get_word(line) + '\n'

		f1.write("%s" %string)

            
            

			


#Coi ký tự trắng (space) là ký tự phân tách các từ. Lấy đầu ra của bài 50 làm đầu vào,
# trích xuất các từ trong các câu và in ra theo định dạng: 
#mỗi dòng 1 từ. In ra dòng trắng để đánh dấu kết thúc câu.
import re
import sys
import os
def get_word(str):
	regx = re.compile(r'([\.;:\?!])\s+([A-Z])')
	m = regx.search(str)
	last_pos = 0
	pos = m.start() if m != None else None
    
    
    
	while ( pos != None ):
		s = str[last_pos:pos+1]
		x=re.sub(r'[\W]', '\n', s)

		# x=re.sub(r'[a-zA-Z]', '\n', s)
		#a = x.split()
		
		#print (x)
		#print("\n")
		arr_words=x.split()
		for i in range(len(arr_words)):
			print(arr_words[i])
		print("\n")
       
		last_pos = last_pos + m.end() + 1 if m != None else None
		m = regx.search(str[last_pos:])
		pos = last_pos + m.start() if m != None else None

if __name__ == '__main__':
    os.system('cls' if os.name == 'nt' else 'clear')
    with open('nlp.txt', 'r') as f:
        for line in f:
            line = line.strip()
            if line == '':
                continue
            a=get_word(line)
            


			


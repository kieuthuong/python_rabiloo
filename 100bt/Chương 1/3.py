#Tokenize câu sau: "Now I need a drink, alcoholic of course, 
#after the heavy lectures involving quantum mechanics."
#Đưa ra danh sách gồm số ký tự alphabet trong mỗi từ theo thứ tự xuất hiện của từ đó trong câu.
from nltk.tokenize import sent_tokenize, word_tokenize
s = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
s1=s.split()
print(len(s1[0]))
#Đếm số kí tự của mỗi từ
i=0
while i < len(s1):
	print('"',s1[i],'" có',len(s1[i]),'kí tự')
	i+=1
#Danh sách alphabet
s1.sort()
print(s1)
# ? ở đây chữ hoa sắp xếp trước

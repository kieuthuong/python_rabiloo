#Cho đầu vào là một câu tiếng Anh bao gồm các word ngăn cách nhau bằng ký tự space. 
#Viết chương trình thực hiện việc sau:

#Với mỗi word, giữ nguyên ký tự đầu và ký tự cuối, 
#đảo thứ tự một cách ngẫu nhiên các ký tự còn lại của
# (tất nhiên các word có ít hơn 4 ký tự thì không cần làm gì)
#Cho trước một câu tiếng Anh hợp lệ, 
#ví dụ "I couldn't believe that I could actually understand what I was reading :
# the phenomenal power of the human mind .", chạy chương trình đã viết để đưa ra kết quả.
s="I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
import random


def messup(words):
    """
        Messes up the inner spelling of words. To test this theory:
            https://en.wikipedia.org/wiki/Typoglycemia
        It's a lot harder to read than the exapmles online...
    """

    result = ''
    sub_word = ''

    for char in words + ' ' :
        if char.isalpha(): #hàm check các kí tự chữ bình thường,nếu char chứa số hay kí tự đặc biệt sẽ trả về false
            sub_word += char
        else:
            if len(sub_word) > 3:
                result += sub_word[0]
                result += ''.join(random.sample(sub_word[1:-1], len(sub_word)-2)) 
                result += sub_word[-1]
            else:
                result += sub_word
            sub_word = '' #sub_word sẵn sàng lưu từ mới tiếp theo

            result += char

    return result[:-1]



print(s)

a = messup(s)
print(a)
b = messup(s)
print(b)

#Cách dùng hàm random.sample()
names = ['Tom', 'Harry', 'Andrew', 'Robert']
print(random.sample(names, 2))


# Book08.py

# 접근 지정자 : public , private
# 접두사 __ : 접근지정을 하겠다는 의미 부여

# 접미사 __ : public
#        _  : private
#           : private
class Book :
    def __init__(self):
        self.__title__ = '무제' # public instance
        self.__author_ = "미상" # private instance
        self.__price   = 0      # private instance
    def rwAuthor(self,author):
        self.__author_ = author
        return self.__author_
#######################################################
b1 = Book()
b1.__title__ = "자바"
print(b1.__title__,b1.rwAuthor("Tom"))



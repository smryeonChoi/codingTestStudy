'''
효율성 체크 2문제 틀린 답안
def solution(book) :
    book.sort()
    for b in range(len(book)) :
        new = book[b+1:]
        for n in new :
            if book[b] == n[:len(book[b])] :
                return False
    return True
'''

def solution(book) :
    book.sort()
    for i in range(len(book)-1) :
        if book[i] == book[i+1][:len(book[i])] :
            return False
    return True

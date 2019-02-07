# 파일명 변경 금지
def cipher(word, n):
    # 아래에 코드를 작성하시오.
    # word는 모두 소문자로만 구성되어 있습니다.
    # n은 양의 정수입니다.
    # 암호화된 문자열을 반환합니다.
    result=''
    #n>=26인 경우 처리
    n = n % 26

    for char in word: #1.a
        w = ord(char) + n #w = 97 + 1
        if w>122: #ord('z') == 122
            w=w-26
        result += chr(w) #chr(98) == 'b'
    return result

    #또 다른 방법
    # result += chr((ord(c) - 97 + n) % 26 +97)

# 아래의 코드는 수정하지마세요. 
if __name__ == '__main__':
    print(cipher('apple', 1))
    print(cipher('apple', 27))
    print(cipher('zoo', 2))
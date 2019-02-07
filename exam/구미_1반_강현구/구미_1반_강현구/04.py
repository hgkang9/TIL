# 파일명 변경 금지
def cipher(word, n):
    # 아래에 코드를 작성하시오.
    # word는 모두 소문자로만 구성되어 있습니다.
    # n은 양의 정수입니다.
    # 암호화된 문자열을 반환합니다.
    result=[]
    result2=[]
    for i in word:
        a = ord(i) + n #문자열의 숫자를 n만큼 밀어낸다
        if a > 122: 
            a = a - 26 #알파벳을 순환시키기 위해 123일 때부터 97(a)로 돌아가도록 26을 빼줌
        b = chr(a) #나온 숫자 a에 대한 문자값을 b로 지정
        result.append(b)
    for i in result:
        if type(i) == str: #result의 값이 문자이면 result2로 넣어준다
            result2.append(i)
    return ''.join(result2)

# 아래의 코드는 수정하지마세요. 
if __name__ == '__main__':
    print(cipher('apple', 1))
    print(cipher('apple', 27))
    print(cipher('zoo', 2))
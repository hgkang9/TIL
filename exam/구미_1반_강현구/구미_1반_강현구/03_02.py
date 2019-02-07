# 파일명 변경 금지
def alphabet_mode(word):
    # 아래에 코드를 작성하시오.
    # word는 소문자로만 구성 되어있습니다.
    # word에서 가장 많이 발생한 알파벳 하나를 반환합니다.
    result={}
    
    count=0
    for i in word:
        if i not in result: #i가 result 안에 없으면 count에 1을 추가하고 result에 i와 count 값을 추가
            count += 1
            result.update(i[count])
        else:
            result[i] += 1 #i가 result 안에 있으면 그 i의 value값인 count에 1을 추가
    for j in result.values(): #result의 value값을 반복
        result2 = []
        result2.append(j)   #result2에 value값을 넣어준다
        a = result2[0]  #a는 result2의 첫번째 값
        b = a           #b는 a로 지정
        for k in result2:
            if k > a:   #k가 a보다 크면 b값을 k로 지정
                b = k
            else:
    return b
           




# 아래의 코드는 수정하지마세요. 
if __name__ == '__main__':
    print(alphabet_mode('hello'))
    print(alphabet_mode('internationalization'))
    print(alphabet_mode('haha'))
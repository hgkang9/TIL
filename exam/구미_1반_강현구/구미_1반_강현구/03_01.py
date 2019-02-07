# 파일명 변경 금지
def alphabet_count(word):
    # 아래에 코드를 작성하시오.
    # word는 소문자로만 구성 되어있습니다.
    # 딕셔너리를 반환합니다.
    result={}
    count=0
    for i in word:
        if i not in result: #i가 result 안에 없으면 count에 1을 추가하고 result에 i와 count 값을 추가
            count += 1
            result.update(i[count])
        else:
            result[i] += 1 #i가 result 안에 있으면 그 i의 value값인 count에 1을 추가
    return result
           




# 아래의 코드는 수정하지마세요. 
if __name__ == '__main__':
    print(alphabet_count('hello'))
    print(alphabet_count('internationalization'))
    print(alphabet_count('haha'))
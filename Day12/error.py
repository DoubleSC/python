# 3대 error
# 1. 컴파일 에러
# 프로그래밍 언어 : 동적 언어 and 정적 언어
#  동적언어 : phython, javascript
#  정적언어 : c, c++, c#, java, kotlin, ...

# 2. 런타임 에러 [예외처리 구문으로 해결]
# 실행 중에 발생하는 에러
# 정수를 입력하세요 : 커피
#  try : 에러가 발생 할 수 있는 코드 구역
 num = int(input("정수를 입력"))
 result = 10/num
 print(f"결과{result}")
except ZeroDivisionError:
 print('0으로 나누었습니다.')

except valueError:
 print('숫자를 입력하세요')

else:
print('에러 발생안함')

finally:

except Exception as e:
#
# 3. 컨텍스트 에러 (인간만 알 수 있는 에러)
#
#
#
#
#
#
#
#
#
#
#
#
#

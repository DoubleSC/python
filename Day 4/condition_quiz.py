# 비밀번호 타입체크
# 비밀번호를 입력하세요:

# 1. 특수문자가 포함이 되야합니다.
# 2. 첫번째 글자가 대문자여야 합니다.
# 3. 비밀번호의 길이가 8글자 이상이여야 합니다.

angle = int(input("각도 : "))

if 0 <= angle and angle < 90:
    print("예각")

elif angle == 90:
    print("직각")

elif 90 < angle and angle < 180:
    print("둔각")

elif 180 == angle:
    print("평각")

else:
    print("잘못된 각도")








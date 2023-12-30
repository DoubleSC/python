a = {}
b = {1,2,3,4}

news = """발생 장소로 보면 가정이 고시원 같은 다중이용시설들을 제치고 가장 큰 비중을 차지했다.

30일 질병관리청 등 정부 관계부처에 따르면 이달 18∼24일 지방자치단체 등에는 총 73건의 빈대 신고가 들어왔다.

이 가운데 실제 빈대가 발생한 것으로 확인된 건은 47건이다."""

news2 = news.split()
news2.sort()
filteredwords = list(set(news2))

print(filteredwords)

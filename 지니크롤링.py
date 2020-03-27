import requests
from bs4 import BeautifulSoup

# 타겟 URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200309',headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
# 이제 코딩을 통해 필요한 부분을 추출하면 된다.
soup = BeautifulSoup(data.text, 'html.parser')

#number,title,artist ellipsis
#############################
# (입맛에 맞게 코딩)
#############################
# #table.list-wrap>tbody>tr
ranking = soup.select('table.list-wrap > tbody > tr')
for music in ranking:

     rank= music.select_one('td.number').text
     title= music.select_one('td.info > a.title.ellipsis').text
     artist= music.select_one('td.info > a.artist.ellipsis').text

     rank = rank[0] #깔끔하게 해라 문자열 앞 두글자#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.number
     title = title.strip() #깔끔하게 해라 문자열 공백제거

     print(rank,title,artist)




# 순위 곡 제목 순서대로 나열


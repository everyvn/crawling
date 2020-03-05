import requests
from bs4 import BeautifulSoup

#BeautifulSoup으로 html 데이터 통으로 받아오기
url = 'https://tiki.vn/search?q='
query = input('찾고싶은 상품을 입력해주세요 : ')
full_url = url + query
url_data = requests.get(full_url).text
bsObj = BeautifulSoup(url_data, 'html.parser')

#받아올 값 만들기 (품명, 가격, 할인율(decompose용), 제품링크)
prod_title = bsObj.find_all(name="p", class_ = 'title') #티키에 tooltip 중 같은 class를 쓰는 div가 있음.
prod_sale = bsObj.find_all(class_ = 'final-price')
prod_rate = bsObj.find_all(class_ = 'sale-tag')
prod_link = bsObj.find_all(name="a", class_ = 'search-a-product-item')

#검색 결과 수 확인
print('검색결과는 총 ', len(prod_title), '개 입니다.')

for span in prod_rate:
    span.decompose()

for n in range(len(prod_title)):
    print(n+1,'. ',prod_title[n].text.strip(), prod_sale[n].text.strip())
    # print('구매링크 : ', prod_link[n].get('href'))
#tiki의 메인페이지는 51개의 제품이 나열되는데 코드실행시 일부 제품이 광고제품인듯한데 리스트에서빠짐.
#태그와 클래스는 같은데 왜빠지는지 모르겠음
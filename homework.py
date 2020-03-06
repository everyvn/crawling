from selenium import webdriver
import requests
from bs4 import BeautifulSoup

# 검색할 쿼리 입력받기
query = input('찾고싶은 상품을 입력해주세요 : ')

# 웹드라이버로 tiki에 접속
driver = webdriver.Chrome('./chromedriver')
driver.get('https://tiki.vn/')
driver.implicitly_wait(10)

# 페이지 전체 로딩
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

# 망할놈의 티키 알림 끄기
if driver.find_element_by_class_name('popover-button'):
    driver.find_element_by_class_name('popover-button').click()

# 쿼리로 검색진행
driver.find_element_by_class_name('FormSearch__Input-hwmlek-2').send_keys(query)
driver.find_element_by_class_name('FormSearch__Button-hwmlek-3').click()

#for문으로 사용하는 경우 전체 페이지네이션의 길이를 알 수 없음
i = 1
while True:
    
    # 페이지리스트 생성 (페이지네이션 전체 li를 리스트로 만듦)
    page_list = driver.find_elements_by_css_selector('.list-pager > ul > li')
    print(i, " 번째 페이지 입니다.")
    
    # 로딩된 페이지 다시 파싱
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    # 페이지 내용 선택자별로 정리
    prod_title = driver.find_elements_by_css_selector('p.title')
    prod_sale = driver.find_elements_by_css_selector('.final-price')
    prod_rate = driver.find_elements_by_css_selector('span.sale-tag')
    prod_link = driver.find_elements_by_css_selector('a.search-a-product-item')

    # 페이지 안에 몇개의 검색결과가 있는지 확인
    print(len(prod_title), ' 개의 검색 결과가 있습니다.')

    # 로딩된 페이지에서 전체 제품명, 가격, 할인율을 뽑아옴
    for n in range(len(prod_title)):
        print(prod_title[n].text.strip(), prod_sale[n].text.strip())
    
    page_list[-1].click() # 페에지네이션의 가장 마지막 리스트 (">")버튼을 눌러서 페이지 이동
    if i == 10:
        break
    i+=1
import requests, queue
from bs4 import BeautifulSoup

first_url = "https://docs.python.org/3/whatsnew/3.6.html"

# 작업 큐 생성
q = queue.Queue()
q.put(first_url)

# 완료 리스트 생성
success_url = []

while True:
    this_url = q.get()

    htmldata = requests.get(this_url).text

    soup = BeautifulSoup(htmldata, "html.parser")

    links = [x.get('href') for x in soup.find_all('a')]

    for each in links:
        # 제외 목록 생성
        if each[0] == "#" or not each.find("mailto:"):
            continue

        if each[0:4] == "http":
            q.put(each)

        else:
            # 상대 경로 처리 추가해야함
            q.put(each)

        print("ADD THIS URL : ", each)
    success_url.append(this_url)
    break
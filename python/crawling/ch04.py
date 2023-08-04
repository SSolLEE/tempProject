import requests
from bs4 import BeautifulSoup
import pandas as pd

com_codes = ["005930", "005490"]
com_names = ["samsung", "POSCO"]

def creadDF(result_list):
    result_df = pd.DataFrame({"title" : result_list})

    return result_df

def crawler(soup):
    # print(soup) # 여기까지 전달 잘됨
    
    div = soup.find("div", class_="today")
    result = []
    for p in div.find_all("p", class_ = "no_today"):  
        result.append(p)

    return result
    # print(div)

def main():

    # 요청 url 변수에 담긴 url의 html 문서를 출력한다. 
    custom_header = {
        'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
    }
    
    url = "https://finance.naver.com/item/main.naver?code=005930"
    req = requests.get(url, headers = custom_header)
    soup = BeautifulSoup(req.text, "html.parser")
    result = crawler(soup)
    # df = creadDF(result)
    # print(df)
    # df.to_csv("result.csv", index=False)

if __name__ == "__main__":
    main()
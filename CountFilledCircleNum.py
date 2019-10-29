from   bs4 import BeautifulSoup
from functools import reduce
import requests


def count_filled_circles(output_filename):
    with requests.Session() as session:
        headers = {"Host": "apply.dataprocessors.com.au",
                   "Connection": "keep-alive",
                   "Cache-Control": "max-age=0",
                   "Upgrade-Insecure-Requests": "1",
                   "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36",
                   "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
                   "Accept-Encoding": "gzip, deflate",
                   "Accept-Language": "en,en-GB;q=0.9,zh-CN;q=0.8,zh;q=0.7",
                   "Cookie": "PHPSESSID=7cf6a2ftqo7gill5gdtrnnh0g6; pc3o=d2r22"
                   }
        url = "http://apply.dataprocessors.com.au"
        page = session.get(url, headers=headers)

        soup = BeautifulSoup(page.content, 'html.parser')

        imgs = soup.findAll('img')

        num = reduce(lambda sum, img: sum + (1 if img['src'].split("/")[-1].upper().startswith("FILLED") else 0), imgs,
                     0)

        formdata = {'title': "submit",
                    "jobref": "PO175",
                    "valuee": str(num)
                    }
        headers = {"Host": "apply.dataprocessors.com.au",
                   "Connection": "keep-alive",
                   "Content-Length": "35",
                   "Cache-Control": "max-age=0",
                   "Origin": "http://apply.dataprocessors.com.au",
                   "Upgrade-Insecure-Requests": "1",
                   "Content-Type": "application/x-www-form-urlencoded",
                   "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36",
                   "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
                   "Referer": "http://apply.dataprocessors.com.au/",
                   "Accept-Encoding": "gzip, deflate",
                   "Accept-Language": "en,en-GB;q=0.9,zh-CN;q=0.8,zh;q=0.7",
                   "Cookie": "PHPSESSID=7cf6a2ftqo7gill5gdtrnnh0g6; pc3o=d2r22"}
        response = session.post(url=url, data=formdata, headers=headers, cookies=session.cookies.get_dict())

        with open(output_filename, "w") as file:
            file.write(response.text)


if __name__ == "__main__":
    count_filled_circles("response_file.html")

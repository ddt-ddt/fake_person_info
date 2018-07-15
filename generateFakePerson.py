from bs4 import BeautifulSoup
import requests

class generateFakePerson(object):
    def get_html(self, url):
        html = requests.get(url)
        bsObj = BeautifulSoup(html.content)

        nameList = bsObj.findAll("div",{"class": "col-md-8 col-sm-6 col-xs-12"})
        print(nameList)
        for name in nameList:
            print(name.get("p"))

        all_div = bsObj.findAll("div", {"class": "info-title"})
        for div in all_div:
            print(div)


if __name__ == '__main__':
    fp = generateFakePerson()
    fp.get_html("https://www.fakepersongenerator.com/Index/generate")

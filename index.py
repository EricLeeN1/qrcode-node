import requests
from bs4 import BeautifulSoup

def fetch_page(url):
    # 发送 HTTP GET 请求
    response = requests.get(url)

    # 检查请求是否成功
    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to fetch the page. Status code: {response.status_code}")
        return None

def parse_html(html):
    # 解析 HTML 内容
    soup = BeautifulSoup(html, 'html.parser')

    # 提取标题
    title = soup.find(class_="common-title").text
     # 提取别名
    subtitle = soup.find(class_="common-title").find('span').text

    # 提取所有链接
    links = [a['href'] for a in soup.find_all('a', href=True)]

    return title, links

def main():
    url = 'https://h5.clewm.net/?url=qr61.cn/otkFrD/qfpFfoa'

    # 获取页面内容
    html_content = fetch_page(url)
    
    if html_content:
        # 解析 HTML 内容
        title, links = parse_html(html_content)

        # 输出结果
        print(f"Title: {title}")
        print("Links:")
        for link in links:
            print(link)

if __name__ == '__main__':
    main()
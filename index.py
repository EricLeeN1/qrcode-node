from time import sleep
import requests
from bs4 import BeautifulSoup

def fetch_page(url):
    # 发送 HTTP GET 请求
    response = requests.get(url)

    sleep(5)

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
    title = soup.find(class_="title-wrapper").find(class_='common-title').get_text()
     # 提取别名
    subtitle = soup.find(class_="common-title").find('span').get_text()
    # 找到 class 为 stylelib-wrapper 所有的DOM 元素
    wrappers = soup.find_all(class_='stylelib-wrapper')
    # 选择 第二个 DOM 元素
    second_wrapper = wrappers[1] if len(wrappers) > 1 else None

    if second_wrapper:
        # 获取该 DOM 元素的子节点 section
        section = second_wrapper.find('section')
    
        if section:
            # 获取 section 子节点的所有子节点
            grandchildren = list(section.children)
        
            if len(grandchildren) >= 2:
                # 选择这些子节点中的第二个子节点
                infosText = grandchildren[1].get_text()
                print('药品信息', infosText)
            else:
                print("没有足够的子节点")
        else:
            print("父节点没有足够的子节点")
    else:
        print("未找到 class 为 stylelib-wrapper 的元素")

    # # 提取所有链接
    # links = [a['href'] for a in soup.find_all('a', href=True)]

    return title, subtitle, infosText

def main():
    url = 'https://h5.clewm.net/?url=qr61.cn/otkFrD/qfpFfoa'

    # 获取页面内容
    html_content = fetch_page(url)
    
    if html_content:

        print(html_content)
        
        # 解析 HTML 内容
        title, subtitle, infosText = parse_html(html_content)

        # 输出结果
        print("Title: {title}")
        print("subTitle: {subtitle}")
        print("infosText: {infosText}")
        # for link in links:
        #     print(link)

if __name__ == '__main__':
    main()
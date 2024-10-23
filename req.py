

import requests
from bs4 import BeautifulSoup
import pandas as pd


def fetch_page(url,route):

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
    }

    data = {
        "qrcode_route":route,
        "password":"",
        "render_default_fields":0,
        "render_component_number":0,
        "render_edit_btn":1
    }
    
    # 发送 HTTP GET 请求
    response = requests.post(url,headers=headers,data=data)


    # 检查请求是否成功
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch the page. Status code: {response.status_code}")
        return None


def parse_html(html_Infos):

    msg = html_Infos['data']['qrcode_msg']
    content_msg = msg['qrcode_compontent']

    html_title = msg['qrcode_top_component'][0]['attribute_list'][0]['content_html']['value']

    html_infos = content_msg[3]['attribute_list'][0]['content_html']['value']
    
    html_remand = content_msg[4]['attribute_list'][0]['content_html']['value']
    
    html_tips = content_msg[6]['attribute_list'][0]['content_html']['value']
    
    soup_title = BeautifulSoup(html_title, 'html.parser')
    soup_infos = BeautifulSoup(html_infos, 'html.parser')
    soup_remand = BeautifulSoup(html_remand, 'html.parser')
    soup_tips = BeautifulSoup(html_tips, 'html.parser')

    title = soup_title.get_text()
    infos = soup_infos.get_text()
    remand = soup_remand.get_text()
    tips = soup_tips.get_text()
    html = {
        'title':title,
        'infos':infos,
        'remand':remand,
        'tips':tips
    }
    return html

def main():
    url = "https://nc.cli.im/qrcoderoute/qrcodeRouteNew"

    lists =  [
    "qr61.cn/otkFrD/qfpFfoa",
    "qr61.cn/otkFrD/q25waTM",
    "qr61.cn/otkFrD/q0NlWLI",
    "qr61.cn/otkFrD/qa5GrE1",
    "qr61.cn/otkFrD/qcn4sX0",
    "qr61.cn/otkFrD/q3IP35S",
    "qr61.cn/otkFrD/qkqcBLO",
    "qr61.cn/otkFrD/qoD0YY0",
    "qr61.cn/otkFrD/qTSGCz5",
    "qr61.cn/otkFrD/qQU3wjD",
    "qr61.cn/otkFrD/qGxjRLn",
    "qr61.cn/otkFrD/qfpFfoa",
    "qr61.cn/otkFrD/q1Nur5H",
    "qr61.cn/otkFrD/qQ65MHD",
    "qr61.cn/otkFrD/qMx7o0E",
    "qr61.cn/otkFrD/q1RsYvI",
    "qr61.cn/otkFrD/qzb3BCf",
    "qr61.cn/otkFrD/qyjA8WL",
    "qr61.cn/otkFrD/qbC6QLT",
    "qr61.cn/otkFrD/qeX2joy",
    "qr61.cn/otkFrD/q7qZ1mS",
    "qr61.cn/otkFrD/q1zDyFN",
    "qr61.cn/otkFrD/qxz4GXN",
    "qr61.cn/otkFrD/qUIhKBG",
    "qr61.cn/otkFrD/qxHEuPd",
    "qr61.cn/otkFrD/qnsri6k",
    "qr61.cn/otkFrD/qcU9dpH",
    "qr61.cn/otkFrD/q0kzuUq",
    "qr61.cn/otkFrD/qX1FF7d",
    "qr61.cn/otkFrD/q7Het76"
  ]
    
    # 存储请求结果的列表
    results = []
    
    for route in lists:
        try:    
            html_Infos = fetch_page(url,route)
            data = parse_html(html_Infos)
            results.append(data)
        except requests.RequestException as e:
            print(f"请求 {url} 失败: {e}")

    # 将结果转换为 DataFrame
    df = pd.DataFrame(results)

    # 保存为 Excel 文件
    output_file = "request_results.xlsx"
    df.to_excel(output_file, index=False)

    print(f"请求结果已成功保存到 {output_file}")


if __name__ == '__main__':
    main()
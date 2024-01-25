"""
根据doi，找到文献的pdf，然后下载到本地
"""
import os
import re
import urllib.request

import pandas as pd
import requests
from fake_useragent import UserAgent

ua = UserAgent()
# headers 保持与服务器的会话连接
headers = {
    'User-Agent': ua.edge,

}

doi_files = fr"F:\Download\paper\wos\xx.xls"
save_path = fr"F:\Download\paper\papersByYear"
already_download = os.listdir(save_path)
doi_example = "http://dx.doi.org/10.1002/smll.201001109"
sci_Hub_Url = "https://sci-hub.ren/"
sci_Hub_Url2 = "https://sci-hubtw.hkvisa.net/"
dor_predix = "https://dx.doi.org/"


def getPaperPdf(url, p_no, p_year, p_name):
    pattern = '/.*?\.pdf'
    requests.packages.urllib3.disable_warnings()
    content = requests.get(url, headers=headers, stream=True, verify=False)
    download_url = re.findall(pattern, content.text)
    print(url, download_url)
    download_url[1] = "https:" + download_url[1]
    # print(download_url[1])
    if os.path.exists(save_path):
        pass
    else:
        os.makedirs(save_path)
    # 使用 urllib.request 来包装请求
    req = urllib.request.Request(download_url[1], headers=headers)
    # 使用 urllib.request 模块中的 urlopen方法获取页面
    u = urllib.request.urlopen(req, timeout=5)
    # file_name = fr"{p_year}-{p_no}-{p_name}.pdf"
    # file_name = fr"{p_year}-{p_no}.pdf"
    file_name = fr"{p_no}-{p_year}.pdf"
    f = open(save_path + '/' + file_name, 'wb')
    block_sz = 8192 * 10
    while True:
        buffer = u.read(block_sz)
        if not buffer:
            break
        f.write(buffer)
    f.close()
    print("Successful to download：" + " " + file_name)


wb = pd.read_excel(doi_files, sheet_name="savedrecs")
idx = 0
col_range = wb[['DOI Link', 'DOI'][idx]]
No_range = wb[['No.', 'Number'][idx]]
Year_range = wb[['Publication Year', "Year"][idx]]
paper_title_range = wb[['Article Title', 'Title'][idx]]
fail_list = {
    "Number": [],
    "Year": [],
    "DOI": [],
    "Title": [],
}
# cut_http = len(dor_predix)
# 加入SCI-hub网址进行下载
for doi, paper_no, paper_year, paper_name in zip(col_range, No_range, Year_range, paper_title_range):  # 打印dio列单元格中的值内容
    # try:
    #     doi = doi[cut_http:]
    # except TypeError:
    #     continue
    try:
        if f"{paper_no}-{paper_year}.pdf" in already_download:
            continue
    except TypeError:
        print(paper_no, paper_no, paper_year)
    # https://sci-hub.ren/10.1002/smll.201001109
    try:
        paper_url = sci_Hub_Url + doi
        getPaperPdf(paper_url, paper_no, paper_year, paper_name)  # 通过文献的url下载pdf
    except Exception as error1:
        print(paper_no, sci_Hub_Url, doi)
        try:
            paper_url = sci_Hub_Url2 + doi
            getPaperPdf(paper_url, paper_no, paper_year, paper_name)  # 通过文献的url下载pdf
        except Exception as error2:
            print(paper_no, sci_Hub_Url2, doi)
            print(f"error1:{error1},error2:{error2}")
            fail_list["Number"].append(paper_no)
            fail_list["Year"].append(paper_year)
            fail_list["DOI"].append(doi)
            fail_list["Title"].append(paper_name)
# 获取下载失败的doi
df = pd.DataFrame(fail_list)
# print(df)
df.to_excel(fr"F:\Download\paper\papers.xlsx", sheet_name='Fail download', index=False)

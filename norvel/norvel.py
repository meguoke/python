# encoding:utf-8
import requests
from bs4 import BeautifulSoup
import os
import sys
import time
import getopt
from concurrent import futures

reload(sys)
sys.setdefaultencoding("utf-8")
norvel_host = "https://www.xxbiquge.com"
norvel_id = '/76_76449'
norvel_url = norvel_host + norvel_id
header = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Cookie': '__cfduid=d577ccecf4016421b5e2375c5b446d74c1499765327; UM_distinctid=15d30fac6beb80-0bdcc291c89c17-9383666-13c680-15d30fac6bfa28; CNZZDATA1261736110=1277741675-1499763139-null%7C1499763139; tanwanhf_9821=1; Hm_lvt_5ee23c2731c7127c7ad800272fdd85ba=1499612614,1499672399,1499761334,1499765328; Hm_lpvt_5ee23c2731c7127c7ad800272fdd85ba=1499765328; tanwanpf_9817=1; bdshare_firstime=1499765328088',
    'Host': 'www.qu.la',
    'Proxy-Connection': 'keep-alive',
    'Referer': 'https://www.xxbiquge.com/76_76449/',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36'
}

norvel_folder = "E://python_file//norvel//"


def get_list():
    response = requests.get(norvel_url, header)
    response.encoding = "utf-8"
    html = response.text
    soup = BeautifulSoup(html, "lxml")
    title = soup.select("#wrapper .box_con #maininfo #info h1")[0].text
    norvel_save_dir = norvel_folder + title
    if not os.path.exists(norvel_save_dir):
        os.mkdir(norvel_save_dir)
    # change the dir to the current norvel folder
    os.chdir(norvel_save_dir)
    list = soup.select("#wrapper .box_con #list a")
    return list


def get_section_from_page(section_url):
    response = requests.get(section_url, header)
    response.encoding = "utf-8"
    html = response.text
    soup = BeautifulSoup(html, 'lxml')
    for ss in soup.select("script"):
        ss.decompose()
        # time.sleep(random.randint(1, 3))
    section_name = soup.select("#wrapper .content_read .box_con .bookname h1")[0].text
    section_content = soup.select("#wrapper .content_read .box_con #content")[0].text
    section_content = "\r\n".join(section_content.split())
    download_file_name = section_name + ".download"
    with open(download_file_name, "w+", 128) as f:
        f.write(section_name)
        f.write(section_content)
    # download complete
    os.rename(download_file_name, section_name + ".txt")


def download_norvel(list):
    count = 0
    try:
        for alink in list:
            section_url = alink['href']
            get_section_from_page(norvel_host + section_url)
            count = count + 1
    except Exception as e:
        print e.message
    return count


def print_done(future):
    print "============Done========={}".format(future.result())


def main():
    print 'start download, time:', time.ctime(time.time())
    start_time = time.clock()
    all_urls = get_list()
    threadNum = 50
    subListSize = len(all_urls) // threadNum
    to_do = []
    with futures.ThreadPoolExecutor(threadNum) as executor:
        for index in range(threadNum):
            future = executor.submit(download_norvel, all_urls[subListSize * index:subListSize * (index + 1)])
            future.add_done_callback(print_done)
            to_do.append(future)
    actual_count = 0
    for f in futures.as_completed(to_do):
        curr_count = f.result()
        actual_count = actual_count + curr_count
    print "expect count:{},actual count:,cost time {}".format(len(all_urls), actual_count, time.clock() - start_time)


if __name__ == '__main__':
    arguments = sys.argv[1:]
    if len(arguments)<=1:
        print 'norvel.py -t <target> -h  -s <start>'
        print 'or norvel.py --target <target> --help '
        exit(2)
    try:
        opts, args = getopt.getopt(arguments, "ht:s:", ["help", "target=", "start"])
    except getopt.GetoptError as e:
        print 'norvel.py -t <target> -h  -s <start>'
        print 'or norvel.py --target <target> --help '
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h", "help"):
            print 'Nothing'
            sys.exit(2)
        if opt in ("-t", "target"):
            print 'save target:', arg
        if opt in ("-s", "start"):
            print 'featch start url:', arg
            # main()

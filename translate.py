import requests
from bs4 import BeautifulSoup
import sys
from cprint import *
import json

def convert(word):
    try:
        url = "http://dict.youdao.com/w/eng/{}/#keyfrom=dict2.index".format(word)
        resp = requests.get(url)
        soup = BeautifulSoup(resp.text, "lxml")
        ret = ""
        for item in soup.find(class_='trans-container')('ul')[0]('li'):
            ret += item.text + '\n'
        return ret
    except:
        cprint.err("{}: Fail".format(word))
        return ""
    finally:
        cprint.info("{}: Success".format(word))
        return ret


if __name__ == '__main__':
    src = sys.argv[1]
    dst = sys.argv[2]
    cprint.ok("Convert {} to {}".format(src, dst))
    f = open(src)
    wordlist = {}
    for en in f.readlines():
        en = en.strip()
        ch = convert(en)
        wordlist[en] = ch
    f.close()
    f = open(dst, 'w')
    json.dump(wordlist, f)
    f.close()

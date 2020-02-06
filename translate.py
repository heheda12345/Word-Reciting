import requests, sys, json, os
from bs4 import BeautifulSoup
from cprint import *

voice_dir = "voice"

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
        return ""

def download_voice(word):
    if not os.path.exists(voice_dir):
        print('Voice directory {} does not exist, created'.format(voice_dir))
        os.makedirs(voice_dir)
    url = "http://dict.youdao.com/dictvoice?audio={}&type=2".format(word) # type=2 means american voice
    resp = requests.get(url)
    with open(os.path.join(voice_dir, "{}.mp3".format(word)), "wb") as f:
        f.write(resp.content)
    return True
    # try:
    #     url = "http://dict.youdao.com/dictvoice?audio={}&type=2".format(word) # type=2 means american voice
    #     resp = requests.get(url)
    #     with open(os.path.join(voice_dir, "{}.mp3".format(word)), "w") as f:
    #         f.write(resp.content)
    #     return True
    # except:
    #     return False

if __name__ == '__main__':
    src = sys.argv[1]
    dst = sys.argv[2]
    cprint.ok("Convert {} to {}".format(src, dst))
    f = open(src)
    succ = 0
    fail = 0
    wordlist = {}
    for en in f.readlines():
        en = en.strip()
        ch = convert(en)
        wordlist[en] = ch
        if ch != "":# and download_voice(en):
            cprint.info("{}: Success".format(en))
            succ += 1
        else:
            cprint.err("{}: Fail".format(en))
            fail += 1
    f.close()
    cprint.ok("Total: {} success {} fail".format(succ, fail))
    f = open(dst, 'w')
    json.dump(wordlist, f)
    f.close()

import argparse, json, random, time, os
from cprint import *

log_dir = "log"

class Reciter:
    def __init__(self, wordlist, forget_path, shuffle = True):
        self.wordlist = wordlist
        if (shuffle):
            random.shuffle(self.wordlist)
        self.forget_path = forget_path
        f = open(forget_path, "w")
        f.close()
        self.forgets = {}
    
    def forget(self, word, trans):
        self.forgets[word] = trans
        f = open(forget_path, "w")
        json.dump(self.forgets, f)
        f.close()

    def print_forget(self):
        for f in self.forgets:
            cprint.ok(f)
            cprint.info(self.forgets[f])

    def run(self):
        for w, idx in zip(self.wordlist, range(1, len(self.wordlist) + 1)):
            inp = input("{}/{} {}".format(idx, len(self.wordlist), w[0]))
            if inp == 'exit':
                break
            inp = input("{} [y/n] ? ".format(w[1]))
            if inp == 'exit':
                break    
            elif inp == 'y':
                pass
            elif inp == 'n':
                self.forget(w[0], w[1])
            else:
                self.forget(w[0], w[1])
                print("Please enter y/n, this word is marked as forgot")


class ReviewReciter(Reciter):
    def forget(self, word, trans):
        super().forget(word, trans)
        self.forget_list.append([word, trans])

    def get_forget(self):
        return [x for x in self.forget_list]
    
    def clear_forget(self):
        self.forget_list = []

    def run(self):
        todo = self.wordlist
        forget = []
        while len(todo) > 0:
            if (len(todo) > 5):
                random.shuffle(todo)
            self.clear_forget()
            for w, idx in zip(todo, range(1, len(todo) + 1)):
                inp = input("{}/{} {}".format(idx, len(todo), w[0]))
                if inp == 'exit':
                    break
                inp = input("{} [y/n] ? ".format(w[1]))
                if inp == 'exit':
                    break    
                elif inp == 'y':
                    pass
                elif inp == 'n':
                    self.forget(w[0], w[1])
                else:
                    self.forget(w[0], w[1])
                    print("Please enter y/n, this word is marked as forgot")
            todo = self.get_forget()


if __name__ == '__main__':
    parser=argparse.ArgumentParser(description='Reciting Words')
    parser.add_argument('-l', dest = 'wl', type = str, help='path to word list')
    parser.add_argument('-o', dest = 'forget', default="", type = str, help = 'path to forgot words')
    parser.add_argument('-m', dest = 'mode', type = str, default = "recite", choices = ['recite', 'test'], help = 'mode')
    parser.add_argument('-s', dest = 'start', default = 0, type = int, help = 'start id')
    parser.add_argument('-t', dest = 'end', default = -1, type = int, help = 'end id (included)')

    args = parser.parse_args()
    words = json.load(open(args.wl))
    wordlist = [[x, words[x]] for x in words]
    if args.end == -1:
        args.end = len(wordlist) - 1
    if args.start < 0 or args.end >= len(wordlist) or args.start > args.end:
        print("Invalid Range! There are {} words in the word list".format(len(wordlist)))
    wordlist = wordlist[args.start:args.end + 1]
    
    if (args.forget == ""):
        forget_path = "log/{}.{}".format(os.path.basename(args.wl), time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()))
        if not os.path.exists(log_dir):
            print('Log directory {} does not exist, created'.format(log_dir))
            os.makedirs(log_dir)
    else:
        forget_path = args.forget

    if args.mode == 'test':
        reciter = Reciter(wordlist, forget_path)
    elif args.mode == 'recite':
        reciter = ReviewReciter(wordlist, forget_path)
    reciter.run()
    reciter.print_forget()
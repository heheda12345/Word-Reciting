# Word-Reciting
背单词脚本
## 词表生成

1. 每行一个单词，写入`xxx.en`
2. `python3 translate.py xxx.en xxx.ch` 生成包括`xxx.en`内的单词的词表，存入`xxx.ch`。单词的中文释义获取自有道翻译

## 背诵

### 参数含义

* `-h` 查看帮助
* `-l path` 词表的路径
* `-o path` 忘记的单词的输出路径，如果未指定，将自动生成输出路径。输出的列表也可直接作为词表使用
* `-m mode` 背单词的模式。目前有两种
  1. `recite` 不断询问忘记的单词，直到全部记住
  2. `test` 所有单词只问一次

* `-s START -t END` 背词表第START至END的单词，编号从0开始。默认从第0个单词开始，到最后一个单词结束
例如，`python recite.py -l TOEFL/WordList-1.ch -m recite -s 1 -t 2`表示背`TOEFL/WordList-1.ch`的第1至2个单词
## 词表

将根据作者背单词进度不定期更新，目前有

* TOEFL: 绿宝书（填坑中）


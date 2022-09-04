
import jieba
jieba.add_word('孙行者')#出现大量行者不知是不是孙行者啊
jieba.add_word("卷帘大将")
jieba.add_word("斗战胜佛")
jieba.add_word("沙悟净")
jieba.add_word("大师兄")
jieba.add_word("二师兄")

def getdicofname():
    xiyouji = open("西游记.txt", "r", encoding = "UTF-8").read()
    #for hanzi in '！“”，。：；？《》、（）':#好像用中文包就没有这个问题
    words = jieba.lcut(xiyouji)
    exclude = ['一个','那里','怎么','我们','长老','不是','只见','原来','不敢','甚么','两个','妖精','国王']#,'','','']
    counts = {}
    for i in words:
        if len(i)==1:#排除单个字符最多为一些符号
            continue
        elif i == '老孙' or i == '大圣' or i == '石猴' or i == '悟空' or i == '行者' or i == '斗战胜佛' or i == '大师兄':
            rword = '孙悟空'
        elif i == '呆子' or i == '老猪' or i == '悟能' or i == '猪刚鬣' or i == '卷帘大将' or i == '二师兄':
            rword = '八戒'
        elif i == '师父' or i == '唐僧' or i == '玄奘' :#or i == '悟空' or i == '行者':
            rword = '三藏'
        elif i == '沙僧' or i == '悟净' or i == '沙悟净' or i == '老三':
            rword = '悟净'
        else:
            rword = i
        counts[rword] = counts.get(rword,0) + 1#如果单词i存在就+1不存在就归零然后再＋1
                #内部两个【】内都是i

    for j in exclude:
        del(counts[j])
    itm = list(counts.items())
    itm.sort(key = lambda x:x[1],reverse = True)
    return itm

dic = getdicofname()
for i in range(30):
    word,count = dic[i]#访问数组使用方括号
    print("{0:<10}{1:>5}".format(word,count))
            
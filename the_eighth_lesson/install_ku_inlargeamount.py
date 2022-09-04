#大量安装python 库
import os#os 调用控制台
libs = {'matplotbib','pillow','sklearn','requests','jieba',\
    'beautifulsoup4','wheel','networkx','sympy','pyinstaller','django','flask','werobot',\
        'PyQt5','pandas','pyopengl','pypdf2','docopt','pygame','numpy'}

for lib in libs:
    try:
        os.system('pip install '+lib)
        print(lib+'successful')
    except:
        print(lib+'fail')


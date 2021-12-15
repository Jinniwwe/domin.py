Python domin main.py
echo "# domin.py" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/Jinniwwe/domin.py.git
git push -u origin main

[MAIN]
#配置文件版本，当版本改变时重新读取配置
VERSION=101
#列数(横)
COL_COUNT=5
#行数（竖）
ROW_COUNT=3
#物件个数
ITEM_COUNT=17
#当前配置的奖励倍率(物件倍率/全盘倍率;实际奖励要除以该值)
PRIZE_RATE=1

#规则连线信息(123,456,789,101112,131415)
#对应物件是否可以用百搭替换(1是可替代，0是不可替代)
USE_WILDS=0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1
#物件最少连线个数（最少3连线才可中奖）
BASE_NUMS=0,0,0,0,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3
#各物件对应的连线数的奖励(1连线，2连线，3连线，4连线，5连线)
ITEM_PRIZES_0=0,0,0,0,0
ITEM_PRIZES_1=0,0,0,0,0
ITEM_PRIZES_2=0,0,0,0,0
ITEM_PRIZES_3=0,0,0,0,0
ITEM_PRIZES_4=0,0,1000000,2000000,10000000
ITEM_PRIZES_5=0,0,500000,1000000,5000000
ITEM_PRIZES_6=0,0,400000,800000,4000000
ITEM_PRIZES_7=0,0,250000,500000,2500000
ITEM_PRIZES_8=0,0,100000,200000,1000000
ITEM_PRIZES_9=0,0,50000,100000,500000
ITEM_PRIZES_10=0,0,50000,100000,500000
ITEM_PRIZES_11=0,0,50000,100000,500000
ITEM_PRIZES_12=0,0,50000,100000,500000
ITEM_PRIZES_13=0,0,50000,100000,500000
ITEM_PRIZES_14=0,0,50000,100000,500000
ITEM_PRIZES_15=0,0,50000,100000,500000
ITEM_PRIZES_16=0,0,50000,100000,500000
ITEM_PRIZES_17=0,0,0,0,0
#连线类型(1.左边连列)
LINE_MODE=1
#scatter类型
#1、按列开始找在列上出现的scatter(243条线，全线)
SCATTER_MODE=1
#scatterId号
SCATTER_ID=0
#查找scatter包含的列(判断在哪一列出现)
SCATTER_COLS=1,1,1,1,1
#是否连续的
SCATTER_SERIAL=0
#scatter出现个数对应的次数
SCATTER_MULTIPLES=0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
#scatter出现个数对应的额外奖励(*总押注)
SCATTER_PRIZES=0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
#格子是否无效(0有效 1无效)
GRID_DISABLES=0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
GRID_DISABLES_FREE=0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
fi
Python domin main.py

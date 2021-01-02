try:
    rs=int(input())
    if rs>2:
        g=[]
        print("接下来需要输入",rs,"个分数")
        while rs>0:
            try:
                sr=int(input())
                if sr>=0&sr<=100:
                    g.append()
                    rs-=1
                    if rs!=0:
                        print("还有",rs,"个评分待输入")
                else:
                    break
            except:
                print("输入分数超出范围,请输入在[0,100]之内的数")
        ma=max(g)
        mi=min(g)
        eg=(sum(g)-ma-mi)/(len(g)-2)
        print("选手的最终成绩为:",eg)
    else:
        print("评委人数不够")
except ValueError:
    print("输入非数字")
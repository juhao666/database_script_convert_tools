# coding=utf-8

## 总结
## ^ 匹配字符串的开始。
## $ 匹配字符串的结尾。
## \b 匹配一个单词的边界。
## \d 匹配任意数字。
## \D 匹配任意非数字字符。
## x? 匹配一个可选的 x 字符 (换言之，它匹配 1 次或者 0 次 x 字符)。
## x* 匹配0次或者多次 x 字符。
## x+ 匹配1次或者多次 x 字符。
## x{n,m} 匹配 x 字符，至少 n 次，至多 m 次。
## (a|b|c) 要么匹配 a，要么匹配 b，要么匹配 c。
## (x) 一般情况下表示一个记忆组 (remembered group)。你可以利用 re.search 函数返回对象的 groups() 函数获取它的值。
## <a href="https://www.baidu.com/s?wd=%E6%AD%A3%E5%88%99%E8%A1%A8%E8%BE%BE%E5%BC%8F&tn=44039180_cpr&fenlei=mv6quAkxTZn0IZRqIHckPjm4nH00T1Y4mHTdnv7hPW-BnHDvmyDz0ZwV5Hcvrjm3rH6sPfKWUMw85HfYnjn4nH6sgvPsT6KdThsqpZwYTjCEQLGCpyw9Uz4Bmy-bIi4WUvYETgN-TLwGUv3EPjn1PWnkn1TLP1f1PWDzPjfY" target="_blank" class="baidu-highlight">正则表达式</a>中的点号通常意味着 “匹配任意单字符”



import re


f = "dbo.AgentApplication.PK_AgentApplication.pkey.sql"
r = re.search(r'pkey',f)
if r is not None:
    print("it's pk")
    pattern = re.compile(r"(?<=dbo.).+?(?=.PK_)")  # 取两个字符串中间的字符
    table_name = pattern.findall(f)
    print(table_name)



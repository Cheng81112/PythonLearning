'''
编写程序，从键盘输入一段文字，
如果其中包括“密”字（可能出现0次、1次或者多次），
则输出时过滤掉该字，其他内容原样输出

'''

sentence = input("请输入一段文字：")
for word in sentence:
    if word =="密":
        continue
    print(word,end='')
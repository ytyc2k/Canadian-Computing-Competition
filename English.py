def is_chinese(uchar):
    if uchar >= u'\u4e00' and uchar <= u'\u9fa5':
        return True
    else:
        return False

with open('ESL6.txt',encoding='utf-8') as f:
    for line in f:
        NextLine=f.readline()
        if NextLine[0]=='英':
            print(line[:-1])
            print(NextLine[:-1])
            for i in range(5):
                kk=f.readline()[:-1]
                if not kk:
                    break
                if is_chinese(kk[-1]) or kk[-1]=='）':
                    print(kk)
                    print(f.readline()[:-1])
                else:
                    break




# print(chr(65))
# print(2**32)
# s1='英'
# s2='E'
# print(len(s1),len(s2))
# print(s1.isalpha(),s2.isalpha())
# print()
#
# print(is_chinese(s2))
#
# print(len('中文'.encode('utf-8')))
# print(len('中文'.encode('gbk')))
# print(len('A'.encode('utf-8')))
# print('abcde'+chr(7)+'fghijklmn')
# print(f'{0x9fa5-0x4e00}')

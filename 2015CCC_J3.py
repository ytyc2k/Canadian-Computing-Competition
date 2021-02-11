#2021-2-4 14:23
#2021-2-4 15:03
englishlist='abcdefghijklmnopqrstuvwxyz'
vowellist='aeiou'
consonantlist='bcdfghjklmnpqrstvwxyz'
ss_in='ham'
ss_out=''
def fc(x):
    return consonantlist[consonantlist.find(x)+1]
for i in ss_in:
    if i in 'bc':
        ss_out=ss_out+i+'a'+fc(i)
    elif i in 'dfg':
        ss_out=ss_out+i+'e'+fc(i)
    elif i in 'hjkl':
        ss_out=ss_out+i+'i'+fc(i)
    elif i in 'mnpqr':
        ss_out=ss_out+i+'o'+fc(i)
    elif i in 'stvwxy':
        ss_out=ss_out+i+'u'+fc(i)
    elif i=='z':
        ss_out = ss_out + i + 'z'
    elif i in vowellist:
        ss_out = ss_out + i
print(ss_out)



###########################################
# Canadian Computing Conpetition ( CCC )  #
# 2021 Junior J4                          #
# Arranging Books                         #
# Author : Tony Yang                      #
# 2021-02-17                              #
###########################################
# ss = input()
# ss = 'LMMMS'  # sample input 1  --> 0
# ss = 'LLSLM'  # sample input 2  --> 2
# ss = 'MSSLSLS'  # sample input 3  --> 3

ss = input()
# st = sorted(ss)
# lst = [ss[i] for i in range(len(ss)) if ss[i] != st[i]]
# print(lst)
# n = len(lst)
# if n % 2:
#     print((n + 1) // 2)
# else:
#     print(n // 2)

lCount = ss.count('L')
mCount = ss.count('M')
# print(lCount, mCount)

section1Ems = section1Esses = 0
for i in range(lCount):
    if ss[i] == 'M':
        section1Ems += 1
    elif ss[i] == 'S':
        section1Esses += 1

section2Els = section2Esses = 0
for i in range(lCount, lCount + mCount):
    if ss[i] == 'L':
        section2Els += 1
    elif ss[i] == 'S':
        section2Esses += 1

section3Els = section3Ems = 0
for i in range(lCount + mCount, len(ss)):
    if ss[i] == 'L':
        section3Els += 1
    elif ss[i] == 'M':
        section3Ems += 1

# print(section1Esses, section1Ems, section2Esses, section2Els, section3Els, section3Ems)


swaps = 0

if section1Esses != 0 and section3Els != 0:
    if section1Esses == section3Els:
        swaps += section3Els
        section1Esses = 0
        section3Els = 0
    elif section1Esses < section3Els:
        swaps += section1Esses
        section3Els -= section1Esses
        section1Esses = 0
    else:
        swaps += section3Els
        section1Esses -= section3Els
        section3Els = 0
# print(section1Esses, section1Ems, section2Esses, section2Els, section3Els, section3Ems)
# print(swaps)

if section1Ems != 0 and section2Els != 0:
    if section1Ems == section2Els:
        swaps += section2Els
        section1Ems = 0
        section2Els = 0
    elif section1Ems < section2Els:
        swaps += section1Ems
        section2Els -= section1Ems
        section1Ems = 0
    else:
        swaps += section2Els
        section1Ems -= section2Els
        section2Els = 0
# print(section1Esses, section1Ems, section2Esses, section2Els, section3Els, section3Ems)
# print(swaps)

if section3Ems != 0 and section2Esses != 0:
    if section3Ems == section2Esses:
        swaps += section2Esses
        section3Ems = 0
        section2Esses = 0
    elif section3Ems < section2Esses:
        swaps += section3Ems
        section2Esses -= section3Ems
        section3Ems = 0
    else:
        swaps += section2Esses
        section3Ems -= section2Esses
        section2Esses = 0
# print(section1Esses, section1Ems, section2Esses, section2Els, section3Els, section3Ems)
# print(swaps)

swaps += (section1Esses + section1Ems + section2Esses + section2Els + section3Els + section3Ems) / 3 * 2
print(int(swaps))

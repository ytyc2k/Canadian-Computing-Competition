#2021-2-4 14:05
#2021-2-4 14:12
CCC_month,CCC_Day=2,18
month=int(input())
day=int(input())
if month<CCC_month:
    print('Before')
elif month>CCC_month:
    print('After')
elif month==CCC_month:
    if day == CCC_Day:
        print('Special')
    elif day < CCC_Day:
        print('Before')
    elif day > CCC_Day:
        print('After')

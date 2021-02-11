#2021-2-4 14:12
#2021-2-4 14:22
Happy=':-)'
Sad=':-('
# ss='How are you :-) doing :-( today :-)?'
ss=input()
happy_counts=ss.count(Happy)
sad_counts=ss.count((Sad))
if happy_counts==0 and sad_counts==0:
    print('None')
elif happy_counts==sad_counts:
    print('unsure')
elif happy_counts>sad_counts:
    print('happy')
elif happy_counts<sad_counts:
    print('sad')

from builtins import frozenset

friend={'lucky':'1234','shipra':'8989'}
print(friend)#{'lucky': '1234', 'shipra': '8989'}



print(friend['lucky'])#1234


friend['bob']='7878'
print(friend)#{'lucky': '1234', 'shipra': '8989', 'bob': '7878'}


friend['bob']='1000'
print(friend)#{'lucky': '1234', 'shipra': '8989', 'bob': '1000'}


del friend['bob']
print(friend)#{'lucky': '1234', 'shipra': '8989'}




friend={'lucky':'1234',
         'shipra':'8989',
          'lucy':'8349',
          'little':'84989'}
for i in friend:
        print(i,"  " ,friend[i])
        print(len(friend))


        #####################
friend={'lucky':'1234','shipra':'8989'}
friend1={'lucky':'2121','shipra':'8989'}
print(friend==friend1)#false


friend={'lucky':'1234','shipra':'8989'}
friend1={'shipra':'8989','lucky':'1234'}
print(friend==friend1)#true


############################
friend={'lucky':'1234','shipra':'8989'}
print(friend.keys())#dict_keys(['lucky', 'shipra'])

friend={'lucky':'1234','shipra':'8989'}
print(friend.values())#dict_values(['1234', '8989'])

friend={'lucky':'1234','shipra':'8989'}
print(friend.get('lucky'))#1234

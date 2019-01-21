from difflib import SequenceMatcher

SIMILAR_SCORE = 0.40
mylist = ['python', 'tips', 'python', 'flask', 'tricks', 'resources', 'flask', 'cron', 'flask', 'tools', 'scrabble', 'code challenges', 'github', 'fork']
mydict = dict()

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

sim_list=[]
for i in range(len(mylist)):
    for j in range(len(mylist)):
        if mylist[i] != mylist[j]:
            a = mylist[i]
            b = mylist[j]
            score = similar(a, b)
            if score > SIMILAR_SCORE:
                #print("{} vergeleken met {}. Score: {}".format(a, b, score))
                tup = (a, b)
                sim_list.append(tup)

print(dict(sim_list))


#
# 
# for item in mylist:
#
# 
#     if item not in mydict:
#
# 
#         mydict[item] = 0
#
# 
#     else:
#        mydict[item] += 1

#print(mydict)

#first2pairs = {k: mydict[k] for k in list(mydict)[:3]}

#print("***")
#print(first2pairs)




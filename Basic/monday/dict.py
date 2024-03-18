d = {'k1':100, 'k2':200}
print(d)
print(d.items())


d2 = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['Hello']]}]}]}

d2['k1'][2]['k2'][1]['tough'][2]
print(d2)
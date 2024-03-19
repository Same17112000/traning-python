from collections import Counter
from collections import defaultdict 


my_list = [1,1,2,2,3,4,4,3,5,5,5,6]
print(Counter(my_list))

letters = 'aaaaaabbbccdddddddddd'
c = Counter(letters)
print(c.most_common(2)) 
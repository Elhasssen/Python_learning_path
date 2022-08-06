from algorithms import bubblesort

strs = ["flower","flow","flight"]
occ = []
strssorted = bubblesort.bubblesort(strs)

# {"flow","flower","flight"}

print(strssorted)
first = strssorted[0]

i= 0
for j in range(1,len(strssorted)):
    next = strssorted[j]
    print(next)
    if next[i] == first[i] : 
        occ.append(first[i]) 
        i = i + 1
    elif next[i] != first[i]:
        print('there is no occurence')
        break
print(occ)
# not sufficiant solution
# first = strssorted[0]
# last = strssorted[len(strssorted) - 1]

# i = 0 

# while i < len(first):
#     if first[0] != last[0] : 
#         print('No common prefix')
#     if first[i] == last[i] : 
#         occ.append(first[i])
    
#     i = i + 1 
# print(''.join(occ))

    

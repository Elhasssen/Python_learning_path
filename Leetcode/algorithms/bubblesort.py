bla = ["lower","flow","flight","caravane","cluster","rifle","testimonial"]



def bubblesort(list):
    for i in range(len(list)):
        for j in range(0, len(list) - 1 - i):
            if len(list[j]) > len(list[j + 1]):
                list[j], list[j + 1] = list[j + 1], list[j]
    return list


print(bubblesort(bla))


# i = 0      i = 1       i = 2     i = 3
# j = 0      j = 0       j = 0     j = 0
# j = 1      j = 1       j = 1
# j = 2      j = 2       
# j = 3             


import os 

os.chdir('/home/elhassen/Desktop/Python/learningpy/working_with_pdf')
######################
# # Reader objects 
# import csv 
# # we open the file 
# exampleFile = open('example.csv')
# # we read the file 
# exampleReader = csv.reader(exampleFile)
# # notice you can't pass the filename string directly to
# # the csv.reader() function
# # the most correct wat to acces the value in the reader object
# # is to pass it through a list 
# exampleData = list(exampleReader)
# print(exampleData)
# # output ; we will receive list inside a list 
# # [['4/5/2014 13:34', 'Apples', '73'], ['4/5/2014 3:41', 'Cherries', '85'], ['4/6/2014 12:46', 'Pears', '14'], ['4/8/2014 8:59', 'Oranges', '52'], ['4/10/2014 2:07', 'Apples', '152'], ['4/10/2014 18:10', 'Bananas', '23'], ['4/10/2014 2:40', 'Strawberries', '98']]
# # 4/5/2014 13:34

# print(exampleData[0][0])
# # output : 4/5/2014 13:34
# print(exampleData[0][1])
# # output : Apples

#############################
# # Reading data from reader objects in a for Loop

# import csv

# exampleFile = open('example.csv')
# exampleReader = csv.reader(exampleFile)

# for row in exampleReader: 
#     print('Row #' + str(exampleReader.line_num) + ' ' + str(row))
# # output : 
# # Row #1 ['4/5/2014 13:34', 'Apples', '73']
# # Row #2 ['4/5/2014 3:41', 'Cherries', '85']
# # Row #3 ['4/6/2014 12:46', 'Pears', '14']
# # Row #4 ['4/8/2014 8:59', 'Oranges', '52']
# # Row #5 ['4/10/2014 2:07', 'Apples', '152']
# # Row #6 ['4/10/2014 18:10', 'Bananas', '23']
# # Row #7 ['4/10/2014 2:40', 'Strawberries', '98']
##########################
# Writer Objects
# import csv
# # we open the csv file to the writing mode by adding two arguments
# outputFile = open('ouput.csv','w', newline = '' ) 
# # note : if you forget the newline argument the csv file will be double spaced
# # now we pass it to the csv writer
# outputWriter = csv.writer(outputFile)
# outputWriter.writerow(['spam','eggs','bacon','ham'])
# outputWriter.writerow(['Hello, world!','eggs','bacon','ham'])
# outputWriter.writerow([1,2,3.141592,4])
# outputFile.close()
############################################
# DictReader and DictWriter 
# import csv
# exampleFile = open('exampleWithHeader.csv')
# exampleDictReader = csv.DictReader(exampleFile)
# for row in exampleDictReader:
#     print(row['Timestamp'], row['Fruit'], row['Quantity'])
# # Output : 
# # 4/5/2015 13:34 Apples 73
# # 4/5/2015 3:41 Cherries 85
# # 4/6/2015 12:46 Pears 14
# # 4/8/2015 8:59 Oranges 52
# # 4/10/2015 2:07 Apples 152
# # 4/10/2015 18:10 Bananas 23
# # 4/10/2015 2:40 Strawberries 98
####################################






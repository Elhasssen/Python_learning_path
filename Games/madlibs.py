# string concatentantion (aka how to put strings together)
# suppose we want to create a string that says " subscribe to ______"
 


# youtuber = "Elhassen" # some string variable 


# a few ways to do this 

# print("subscribe to " + youtuber)
# print("subscribe to {}".format(youtuber))
# print(f"subscribe to {youtuber}")

adj = input("Adjective is : ")
vrb1 = input("Verb is : ")
vrb2 = input("Verb is : ")


madlib = f"Computer programing is a {adj} journey! it makes me \
very excited most of the time, i love to {vrb1}. stay focused and {vrb2}!"
print(madlib)
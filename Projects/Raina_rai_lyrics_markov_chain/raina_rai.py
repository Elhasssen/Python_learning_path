import markovify


filename = 'tyga.txt'

file = open(filename)

text = file.read()

model = markovify.NewlineText(text,state_size=2)
for i in range(4):
    print(model.make_sentence())

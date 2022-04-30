from vision import prediction
path = 'https://www.ikea.com/images/a-gladstad-bed-in-a-grey-bedroom-covered-with-lappnycklar-fl-3f6f45fbfe31064706a0c539cd0af1ce.jpg?f=s'
Part_of_home, score = prediction(path)
print(Part_of_home, score)

from vision import prediction
from details import details
path = 'image.jpg'
Part_of_home, score = prediction(path)
print(Part_of_home, score)
#if Part_of_home =='bathroom':
    #details(Part_of_home, path)

from vision import prediction
from details import details
path = 'https://st.depositphotos.com/1007549/1228/i/950/depositphotos_12289051-stock-photo-white-bathroom.jpg'
Part_of_home, score = prediction(path)
print(Part_of_home, score)
if Part_of_home =='bathroom':
    details(Part_of_home, path)

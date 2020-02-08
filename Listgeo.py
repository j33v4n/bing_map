from geopy.extra.rate_limiter import RateLimiter
import pandas as pd
from geopy import Nominatim

locator = Nominatim(user_agent='myGeocoder')

#df = pd.read_csv('C:\\Users\\anajayan\\Desktop\\Map Project\\address.csv')
w=3
i=0
df1=pd.DataFrame({'Location':[],'Latitude':[],'Longitude':[]})
y='Bangalore'
z='India'
x=[]
print('Enter the places you want to visit')
while i<w:
    x.append(input(''))
    i=i+1

i=0

while i<w :


  try:
    locations=x[i]+","+y+","+z
    locations=locations.replace(" ", "")
    print(locations)
    print(i)

    location = locator.geocode(locations,timeout=10)
    #print('Latitude = {}, Longitude = {}'.format(location.latitude, location.longitude))





    df1.loc[i,['Location']]=x[i]
    df1.loc[i,['Latitude']]=location.latitude
    df1.loc[i,['Longitude']]=location.longitude

    #df1=pd.concat([df1,df]).drop_duplicates(['Location'],keep='last')




    ##print(df1.loc[0,['Location']])
    i=i+1
  except:
    print("cant Find for Location :",x[i],"...Skipping..")
    i=i+1


print(df1.head())

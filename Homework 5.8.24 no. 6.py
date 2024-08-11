coordinates = {'x':10, 'y':20}
print(coordinates['x'])
coordinates['x'] = 15
print(coordinates['x'])
coordinates['z']=30
print(coordinates)


"""
הסוגריים המרובעים במילון מפנים למפתח בתוך הסוגריים. כלומר, בהדפסת ['x'] יודפס הערך של המפתח 'x'.
 באותו האופן ניתן לשנות את ערך המפתח או להגדיר מפתח חדש - 'z' בעל ערך 30. """
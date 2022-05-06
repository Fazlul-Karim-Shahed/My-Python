
import math

second = 86400 + 86400 + 3600 + 3600 + 3600 + 200

day = math.floor(second/86400)
hour = math.floor((second%86400)/3600)
min = math.floor(((second%86400)%3600)/60)
sec = math.floor(((second%86400)%3600)%60)

print("Day: ", day)
print("Hour: ", hour)
print("Min: ", min)
print("Sec: ", sec)

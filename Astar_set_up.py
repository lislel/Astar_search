#the following code is from Udacity
from helpers import Map, load_map
from student_code import shortest_path

map_40 = load_map('map-40.pickle')

path = shortest_path(map_40,8, 24)

print(path)
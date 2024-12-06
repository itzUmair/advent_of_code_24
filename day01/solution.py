left_array = []
right_array = []
distances = []
similarities = {}
similarity_score = []

with open("./input.txt", "r") as file:
  for line in file:
    if (line):
      line = line.split()
      left_array.append(int(line[0]))
      right_array.append(int(line[1]))

# part one
# while len(left_array) > 0:
#   min_left_array = min(left_array)  
#   index_of_min_left_array = left_array.index(min_left_array)
#   left_array.pop(index_of_min_left_array)

#   min_right_array = min(right_array)
#   index_of_min_right_array = right_array.index(min_right_array)
#   right_array.pop(index_of_min_right_array)

#   distances.append(abs(min_left_array - min_right_array))

# print(sum(distances))

# part 2
for num in left_array:
  similarities[num] = right_array.count(num)

for num, occurance in similarities.items():
  similarity_score.append(num*occurance)

print(sum(similarity_score))

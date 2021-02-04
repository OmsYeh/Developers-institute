# Exercise 7

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
even_index_colors = []
for count, i in enumerate(colors):
    if count % 2 == 0:
        even_index_colors.append(i)

print(even_index_colors)

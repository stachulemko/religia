def combinations_slippers(heights):
    slipper_combinations = []
    for i in range(1, len(heights) + 1):
        slipper_combinations.append(heights[0:i])
    return slipper_combinations

def combinations_sizes(sizes):
    size_combinations = []
    size_combinations.append([sizes[0]])
    for i in range(len(sizes) - 1):
        for j in range(i + 1, len(sizes)):
            size_combinations.append(sizes[i:j + 1])
    return size_combinations

children_heights = [5, 15, 10, 12, 1]
available_sizes = [12, 2, 1]
min_height = 14

max_children = 0

for slipper_combination in combinations_slippers(children_heights):
    children_left = children_heights.copy()
    fitted_children = 0
    indices_to_remove = []
    for i, slipper_height in enumerate(slipper_combination):
        for size_combination in combinations_sizes(available_sizes):
            if len(size_combination) >= len(slipper_combination):
                for size in size_combination:
                    if slipper_height + size < min_height:
                        indices_to_remove.append(i)
                        break
        fitted_children += 1
    for index in sorted(indices_to_remove, reverse=True):
        del children_left[index]
    max_children = max(max_children, len(children_heights) - len(children_left))

print(max_children)

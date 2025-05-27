def is_valid(region, color, assignment, neighbors):
    return all(assignment.get(n) != color for n in neighbors[region])

def backtrack(assignment, regions, colors, neighbors):
    if len(assignment) == len(regions):
        return assignment
    region = [r for r in regions if r not in assignment][0]
    for color in colors:
        if is_valid(region, color, assignment, neighbors):
            assignment[region] = color
            result = backtrack(assignment, regions, colors, neighbors)
            if result:
                return result
            del assignment[region]
    return None

regions = ['WA', 'NT', 'SA', 'Q', 'NSW', 'V', 'T']
neighbors = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'SA', 'Q'],
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
    'Q': ['NT', 'SA', 'NSW'],
    'NSW': ['Q', 'SA', 'V'],
    'V': ['SA', 'NSW'],
    'T': []
}
colors = ['Red', 'Green', 'Blue']
solution = backtrack({}, regions, colors, neighbors)
print("Color Assignment:", solution)

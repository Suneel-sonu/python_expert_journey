# motercycles = ['honda', 'yamaha', 'suzuki']
# print (motercycles)

# # motercycles[0] = 'ducati'
# # print (motercycles)

# motercycles.append('ducati')
# print (motercycles)

motercycles = []
motercycles.append('ducati')
motercycles.append('honda')
motercycles.append('yamaha')
print (f"\n{motercycles}")

motercycles.insert(0, 'suzuki')
print (f"\n{motercycles}")

# del motercycles[2]
# print (motercycles)

# popped_motercycles = motercycles.pop()
# print (f"\n {motercycles}")
# print (f"\n{popped_motercycles}")

first_owned = motercycles.pop(0)
print (f"\n{motercycles}")
print (f"\n the first motercycle was a {first_owned.title()}.")

motercycles.remove("ducati")
print (f"\n{motercycles}")
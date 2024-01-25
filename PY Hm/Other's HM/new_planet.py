# new_planet = ''
# planets = []
# while new_planet.lower() != 'done':
#     if new_planet:  # 这个if是用来判断输入的字符串是否为空字符串的
#         planets.append(new_planet)
#     new_planet = input('enter or done')
# print(planets)

new_planet = ""  # 这是你一开始定义的一个空字符串，所以你一开始运行while的时候就会加一个空字符串的
planets = []
while new_planet.lower() != "done":
    planets.append(new_planet)  # 这里就append了你的空字符串new_planet，因为你没有判断 new_planet ！= ‘’
    new_planet = input()

print(planets)

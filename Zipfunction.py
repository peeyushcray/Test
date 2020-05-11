names =("Peeyush", "Aroosh", "Priyadarshi")
comps =("Sony", "HP", "Apple")

zipped =list(zip(names, comps))
print(zipped)
zipped2 = set(zip(names,comps))
print(zipped2)
zipped3 = tuple(zip(names,comps))
print(zipped3)
zipped4 = dict(zip(names,comps))
print(zipped4)

zipped5= zip(names,comps)
for (a,b) in zipped5:
    print(a,b)
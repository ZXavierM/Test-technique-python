from cadastres.resources.data import CADASTRES

list_bourgogne = []

for i in CADASTRES:
    if i["properties"]["appellatio"] == "Bourgogne":
        list_bourgogne += [i]

print(list_bourgogne)


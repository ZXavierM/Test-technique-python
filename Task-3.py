from cadastres.resources.data import CADASTRES

list_pr = []

for i in CADASTRES:
    if "premier cru" in i["properties"]["denominati"]:
        list_pr += [i]

print(list_pr)
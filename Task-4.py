from cadastres.resources.data import CADASTRES


for i in CADASTRES:
    if "premier cru" in i["properties"]["denominati"]:
         properties = i["properties"]
         classification = {"classification": "PR"}
         properties = properties{classification}
    #     i["properties"] += i["properties"]["classification"]
    # else:
    #     i["properties"] += i["properties"]["classification"]

print(properties)

import json

with open(r"C:\Users\Сырым\Documents\pp2-22B030546\tsis4\json\data.json", "r") as read_file:
    data = json.load(read_file)

print("""Interface Status
================================================================================
DN                                                 Description           Speed    MTU  
-------------------------------------------------- --------------------  ------  ------""")

for x in data["imdata"]:
    for y in x["l1PhysIf"]:
        for f in x["l1PhysIf"][y]:
            if f == 'dn':
                DN = x["l1PhysIf"][y][f]
            if f == "speed":
                Speed = x["l1PhysIf"][y][f]
            if f == "mtu":
                MTU = x["l1PhysIf"][y][f]
            if f == "description":
                Description =  x["l1PhysIf"][y][f]
            else: 
                Description = ""
    print(f"{DN}                            {Description}  {Speed}   {MTU}")
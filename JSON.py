import json
file = open("sample-data.json")
data = json.load(file)


print("Interface Status")
print("="*80)
print("DN" + " "*49 + "Description" + " "*11 + "Speed" + " "*4 + "MTU")
print("-"*50 + " " + "-"*20 + "  " + "-"*6 + "  " + "-"*6)
for i, x in enumerate(data['imdata']):
    if i < 3:
        print(f"{x['l1PhysIf']['attributes']['dn']}  {x['l1PhysIf']['attributes']['speed']:>35}  {x['l1PhysIf']['attributes']['mtu']:>5}")
    else:
        break

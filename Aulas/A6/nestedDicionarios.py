#dicionarionest={"Keypricipal": {"Keyn": "valorn" ," Keyt": "valort"}}

users={"davif":{"nome":"David Ferreira","tel":9677339 },
       "antp":{"nome":"Anntonio Perreira","tel":9678839 }}

print(users["antp"]["nome"])

print(users.update({"joap":{"nome":"Joao Pedro","tel":9678839 }}))

for keyuser, valuedic in users.items():
    print(keyuser, f": nome =  {valuedic["nome"]}  ,Telefone =  {valuedic["tel"]} " )
import io

sea = "discovered_by = western"

f = open("definition.csv", "r")
lines = f.read().splitlines()
lines.pop(0)
for province in lines:
    prov = province.split(";")
    file = "../history/provinces/" + prov[0] + " - " + prov[4] + ".txt"
    a = io.open(file, "w", encoding="cp1252")
    if("sea" not in prov[4]):
        print("found a land")
        land = """#pronum - proname

add_core = RSI
owner = RSI
controller = RSI
culture = greek
religion = catholic
hre = no
base_tax = 1
base_production = 1
trade_goods = fish
base_manpower = 1
capital = "proname"
is_city = yes
discovered_by = western
"""
        land = land.replace("pronum", prov[0])
        land = land.replace("proname", prov[4])
        a.write(land)
    else:
        a.write(sea)
    a.close()    
f.close()

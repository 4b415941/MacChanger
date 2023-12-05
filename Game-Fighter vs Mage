import random

savascı = {
    "güc": 85,
    "can": 1500,
    "zırh": 30
}

büyücü = {
    "güc": 120,
    "can": 800,
    "zırh": 10,
    "büyü_kalkanı": False
}

def vur(vuran: dict, vurulan: dict, kritik=False):
    if vurulan.get("büyü_kalkanı", False):
        print("Büyücü kalkanını kullandı ve saldırıyı blokladı!")
        return

    if kritik:
        hasar = vuran["güc"] * 2 - vurulan["zırh"]
    else:
        hasar = vuran["güc"] - vurulan["zırh"]

    if hasar < 0:
        hasar = 0

    if vurulan["can"] < hasar:
        vurulan["can"] = 0
    else:
        vurulan["can"] -= hasar

print("Savaşçı : ", savascı)
print("Büyücü : ", büyücü)

while savascı["can"] > 0 and büyücü["can"] > 0:
    input("Vurmak için enter'a basınız!")
    kritik_vurus = random.choice([True, False])  # Kritik vuruş için rastgele seçim
    vur(savascı, büyücü, kritik_vurus)
    if kritik_vurus:
        print("""Savaşçı ⚔ Büyücüye Saldırdı ve kritik bir vuruş yaptı!
        {} güçte bir vuruş yaptı.
        Büyücünün kalan canı: {}
        """.format(savascı["güc"], büyücü["can"]))
    else:
        print("""Savaşçı ⚔ Büyücüye Saldırdı.
        {} güçte bir vuruş yaptı.
        Büyücünün kalan canı: {}
        """.format(savascı["güc"], büyücü["can"]))

    if büyücü["can"] <= 0:
        print("Büyücü öldü! Savaşçı kazandı.")
        break

    input("Vurmak için enter'a basınız!")
    büyü_kalkanı_kullansın = random.choice([True, False])  # Büyü kalkanını kullanma kararı
    büyücü["büyü_kalkanı"] = büyü_kalkanı_kullansın
    kritik_vurus = random.choice([True, False])  # Kritik vuruş için rastgele seçim
    vur(büyücü, savascı, kritik_vurus)
    if kritik_vurus:
        print("""Büyücü ⚔ Savaşçı Saldırdı ve kritik bir vuruş yaptı!
        {} güçte bir vuruş yaptı.
        Savaşçının kalan canı: {}
        """.format(büyücü["güc"], savascı["can"]))
    else:
        print("""Büyücü ⚔ Savaşçı Saldırdı.
        {} güçte bir vuruş yaptı.
        Savaşçının kalan canı: {}
        """.format(büyücü["güc"], savascı["can"]))

    if savascı["can"] <= 0:
        print("Savaşçı öldü! Büyücü kazandı.")
        break

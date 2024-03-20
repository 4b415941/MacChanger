import random

warrior = {
    "power": 85,
    "health": 1500,
    "armor": 30
}

wizard = {
    "power": 120,
    "health": 800,
    "armor": 10,
    "magic_shield": False
}

def attack(attacker: dict, target: dict, critical=False):
    if target.get("magic_shield", False):
        print("Wizard used magic shield and blocked the attack!")
        return

    if critical:
        damage = attacker["power"] * 2 - target["armor"]
    else:
        damage = attacker["power"] - target["armor"]

    if damage < 0:
        damage = 0

    if target["health"] < damage:
        target["health"] = 0
    else:
        target["health"] -= damage

print("Warrior: ", warrior)
print("Wizard: ", wizard)

while warrior["health"] > 0 and wizard["health"] > 0:
    input("Press enter to attack!")
    critical_hit = random.choice([True, False])
    attack(warrior, wizard, critical_hit)
    if critical_hit:
        print("""Warrior ⚔ Attacked Wizard and made a critical hit!
        Dealt {} power of damage.
        Wizard's remaining health: {}
        """.format(warrior["power"], wizard["health"]))
    else:
        print("""Warrior ⚔ Attacked Wizard.
        Dealt {} power of damage.
        Wizard's remaining health: {}
        """.format(warrior["power"], wizard["health"]))

    if wizard["health"] <= 0:
        print("Wizard is dead! Warrior wins.")
        break

    input("Press enter to attack!")
    use_magic_shield = random.choice([True, False])
    wizard["magic_shield"] = use_magic_shield
    critical_hit = random.choice([True, False])
    attack(wizard, warrior, critical_hit)
    if critical_hit:
        print("""Wizard ⚔ Attacked Warrior and made a critical hit!
        Dealt {} power of damage.
        Warrior's remaining health: {}
        """.format(wizard["power"], warrior["health"]))
    else:
        print("""Wizard ⚔ Attacked Warrior.
        Dealt {} power of damage.
        Warrior's remaining health: {}
        """.format(wizard["power"], warrior["health"]))

    if warrior["health"] <= 0:
        print("Warrior is dead! Wizard wins.")
        break

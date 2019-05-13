from mwf.infra.mwf_errors import DeathError
from mwf.character_util import Player, Character

import random

ATTACK_RANDOM_PARAMETER = 0.1
DEFEND_RANDOM_PARAMETER = 0.1
REST_RANDOM_PARAMETER = 0.1
EXP_PARAMETER = 3
EXP_RANDOM_PARAMETER = 0.1


def attack(attacker: Character, defender: Character):
    atkp = max(1, int(attacker.atkp * (1 + (random.random() - 0.5) * ATTACK_RANDOM_PARAMETER * 2)))
    defp = max(0, int(defender.defp * (1 + (random.random() - 0.5) * DEFEND_RANDOM_PARAMETER * 2)))
    damage = atkp - defp
    print(f"{attacker.name} hit {defender.name} with {damage} damage.")
    defender.reduce_hp(damage)
    return damage


def rest(char: Character):
    amount = max(1, int(char.max_hp * (random.random() - 0.5) * REST_RANDOM_PARAMETER * 2))
    print(f"{char.name} takes a rest and restores {amount} HP.")
    char.add_hp(amount)
    return amount


def combat(player: Player, opponent: Character):
    print("Combat start!")
    while True:
        # print status
        print(f"Player: HP={player.hp}, ATK={player.atkp}, DEF={player.defp}")
        print(f"Opponent: HP={opponent.hp}, ATK={opponent.atkp}, DEF={opponent.defp}")

        # player move
        player_move = input("Your move (attack/rest): ")
        if player_move.lower().startswith("a"):
            try:
                damage = attack(attacker=player, defender=opponent)
            except DeathError:
                # opponent dies
                exp = opponent.lv * EXP_PARAMETER * (1 + (random.random() - 0.5) * EXP_RANDOM_PARAMETER * 2)
                print(f"You win. Exp earned = {exp}")
                return exp
        elif player_move.lower().startswith("r"):
            rest(player)
        else:
            print("You did nothing.")


        # opponent move
        r = random.random()
        if r < 0.1:
            # rest
            rest(opponent)
        else:
            attack(attacker=opponent, defender=player)


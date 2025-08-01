from poke_env.battle import AbstractBattle
from poke_env.player import Player
from poke_env import SimpleHeuristicsPlayer

team = """
Koraidon @ Choice Scarf  
Ability: Orichalcum Pulse  
Tera Type: Fire  
EVs: 252 Atk / 4 SpD / 252 Spe  
Jolly Nature  
- Flare Blitz  
- Dragon Claw  
- U-turn  
- Close Combat  

Arceus-Water @ Splash Plate  
Ability: Multitype  
Tera Type: Fairy  
EVs: 248 HP / 8 SpD / 252 Spe  
Timid Nature  
- Calm Mind  
- Judgment  
- Recover  
- Earth Power  

Zacian-Crowned @ Rusted Sword  
Ability: Intrepid Sword  
Tera Type: Steel  
EVs: 252 Atk / 4 SpD / 252 Spe  
Jolly Nature  
- Behemoth Blade  
- Close Combat  
- Wild Charge  
- Swords Dance  

Ting-Lu @ Leftovers  
Ability: Vessel of Ruin  
Tera Type: Dragon  
EVs: 252 HP / 4 Def / 252 SpD  
Careful Nature  
- Spikes  
- Ruination  
- Whirlwind  
- Earthquake  

Chi-Yu @ Choice Specs  
Ability: Beads of Ruin  
Tera Type: Fire  
EVs: 252 SpA / 4 SpD / 252 Spe  
Timid Nature  
- Overheat  
- Dark Pulse  
- Psychic  
- Tera Blast  

Flutter Mane @ Focus Sash  
Ability: Protosynthesis  
Tera Type: Fairy  
EVs: 252 SpA / 4 SpD / 252 Spe  
Timid Nature  
IVs: 0 Atk  
- Shadow Ball  
- Moonblast  
- Thunderbolt  
- Taunt  
"""


# class CustomAgent(Player):
#     def __init__(self, *args, **kwargs):
#         super().__init__(team=team, *args, **kwargs)

#     def choose_move(self, battle: AbstractBattle):
#         return self.choose_random_move(battle)


# class CustomAgent(SimpleHeuristicsPlayer):
#     def __init__(self, *args, **kwargs):
#         super().__init__(team=team, *args, **kwargs)

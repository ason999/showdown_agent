from poke_env.battle import AbstractBattle
from poke_env.player import Player
from poke_env.battle.pokemon import Pokemon
from poke_env.battle.side_condition import SideCondition
from poke_env import SimpleHeuristicsPlayer


#Team for Class Competition
team = """
Koraidon @ Choice Scarf  
Ability: Orichalcum Pulse  
Tera Type: Fire  
EVs: 252 Atk / 4 Def / 252 Spe  
Jolly Nature  
- Flare Blitz  
- Close Combat  
- U-turn  
- Outrage  

Gholdengo @ Choice Specs  
Ability: Good as Gold  
Tera Type: Flying  
EVs: 252 SpA / 4 SpD / 252 Spe  
Timid Nature  
IVs: 0 Atk  
- Make It Rain  
- Shadow Ball  
- Focus Blast  
- Trick  

Ting-Lu @ Leftovers  
Ability: Vessel of Ruin  
Tera Type: Poison  
EVs: 252 HP / 4 Atk / 252 SpD  
Careful Nature  
- Spikes  
- Ruination  
- Whirlwind  
- Earthquake  

Flutter Mane @ Focus Sash  
Ability: Protosynthesis  
Tera Type: Ghost  
EVs: 252 SpA / 4 SpD / 252 Spe  
Timid Nature  
IVs: 0 Atk  
- Shadow Ball  
- Moonblast  
- Mystical Fire  
- Taunt  

Arceus-Water @ Splash Plate  
Ability: Multitype  
Tera Type: Fairy  
EVs: 248 HP / 8 Def / 252 Spe  
Timid Nature  
IVs: 0 Atk  
- Judgment  
- Calm Mind  
- Recover  
- Substitute  

Great Tusk @ Booster Energy  
Ability: Protosynthesis  
Tera Type: Steel  
EVs: 252 HP / 4 Atk / 252 Def  
Impish Nature  
- Rapid Spin  
- Knock Off  
- Earthquake  
- Ice Spinner  
"""

# # Random Team 1

# team = """
# Koraidon @ Choice Scarf  
# Ability: Orichalcum Pulse  
# Tera Type: Fire  
# EVs: 252 Atk / 4 Def / 252 Spe  
# Jolly Nature  
# - Flare Blitz  
# - Close Combat  
# - U-turn  
# - Outrage  

# Gholdengo @ Choice Specs  
# Ability: Good as Gold  
# Tera Type: Flying  
# EVs: 252 SpA / 4 SpD / 252 Spe  
# Timid Nature  
# IVs: 0 Atk  
# - Make It Rain  
# - Shadow Ball  
# - Focus Blast  
# - Trick  

# Ting-Lu @ Leftovers  
# Ability: Vessel of Ruin  
# Tera Type: Poison  
# EVs: 252 HP / 4 Atk / 252 SpD  
# Careful Nature  
# - Spikes  
# - Ruination  
# - Whirlwind  
# - Earthquake  

# Flutter Mane @ Focus Sash  
# Ability: Protosynthesis  
# Tera Type: Ghost  
# EVs: 252 SpA / 4 SpD / 252 Spe  
# Timid Nature  
# IVs: 0 Atk  
# - Shadow Ball  
# - Moonblast  
# - Mystical Fire  
# - Taunt  

# Arceus-Water @ Splash Plate  
# Ability: Multitype  
# Tera Type: Fairy  
# EVs: 248 HP / 8 Def / 252 Spe  
# Timid Nature  
# IVs: 0 Atk  
# - Judgment  
# - Calm Mind  
# - Recover  
# - Substitute  

# Great Tusk @ Booster Energy  
# Ability: Protosynthesis  
# Tera Type: Steel  
# EVs: 252 HP / 4 Atk / 252 Def  
# Impish Nature  
# - Rapid Spin  
# - Knock Off  
# - Earthquake  
# - Ice Spinner  
# """


# # Random Team 2

# team = """
# Koraidon @ Choice Scarf  
# Ability: Orichalcum Pulse  
# Tera Type: Fire  
# EVs: 252 Atk / 4 Def / 252 Spe  
# Jolly Nature  
# - Flare Blitz  
# - Close Combat  
# - U-turn  
# - Outrage  

# Gholdengo @ Choice Specs  
# Ability: Good as Gold  
# Tera Type: Flying  
# EVs: 252 SpA / 4 SpD / 252 Spe  
# Timid Nature  
# IVs: 0 Atk  
# - Make It Rain  
# - Shadow Ball  
# - Focus Blast  
# - Trick  

# Ting-Lu @ Leftovers  
# Ability: Vessel of Ruin  
# Tera Type: Poison  
# EVs: 252 HP / 4 Atk / 252 SpD  
# Careful Nature  
# - Spikes  
# - Ruination  
# - Whirlwind  
# - Earthquake  

# Flutter Mane @ Focus Sash  
# Ability: Protosynthesis  
# Tera Type: Ghost  
# EVs: 252 SpA / 4 SpD / 252 Spe  
# Timid Nature  
# IVs: 0 Atk  
# - Shadow Ball  
# - Moonblast  
# - Mystical Fire  
# - Taunt  

# Arceus-Water @ Splash Plate  
# Ability: Multitype  
# Tera Type: Fairy  
# EVs: 248 HP / 8 Def / 252 Spe  
# Timid Nature  
# IVs: 0 Atk  
# - Judgment  
# - Calm Mind  
# - Recover  
# - Substitute  

# Great Tusk @ Booster Energy  
# Ability: Protosynthesis  
# Tera Type: Steel  
# EVs: 252 HP / 4 Atk / 252 Def  
# Impish Nature  
# - Rapid Spin  
# - Knock Off  
# - Earthquake  
# - Ice Spinner  
# """


class CustomAgent(Player):
    def __init__(self, *args, **kwargs):
        super().__init__(team=team, *args, **kwargs)


    # Hazard decleration 
    ENTRY_HAZARDS = {
        "spikes": SideCondition.SPIKES,
        "stealthrock": SideCondition.STEALTH_ROCK,
        "stickyweb": SideCondition.STICKY_WEB,
        "toxicspikes": SideCondition.TOXIC_SPIKES,
    }

    ANTI_HAZARDS_MOVES = {
        "rapidspin",
        "defog"
    }

    # Hazzard logic

    # Matchup logic, used to see if the pokemon currently matched up are good agtainst eachother, checks mon type, attack, defense, HP and ability power and speed.
    def _estimate_matchup(self, mon: Pokemon, opponent: Pokemon):
        score = max([opponent.damage_multiplier(t) for t in mon.types if t is not None])
        score -= max(
            [mon.damage_multiplier(t) for t in opponent.types if t is not None]
        )
        if mon.base_stats["spe"] > opponent.base_stats["spe"]:
            score += self.SPEED_TIER_COEFICIENT
        elif opponent.base_stats["spe"] > mon.base_stats["spe"]:
            score -= self.SPEED_TIER_COEFICIENT

        score += mon.current_hp_fraction * self.HP_FRACTION_COEFICIENT
        score -= opponent.current_hp_fraction * self.HP_FRACTION_COEFICIENT

        return score
    
    #should dynamax based on if the pokemon is win condtion
    def _should_dynamax(self, battle: AbstractBattle, n_remaining_mons: int):
        return
    
    # Switch pokemon based on 
    def _should_switch_out(self, battle: AbstractBattle):
        active = battle.active_pokemon
        opponent = battle.opponent_active_pokemon
        # If there is a decent switch in...
        if [
            m
            for m in battle.available_switches
            if self._estimate_matchup(m, opponent) > 0
        ]:
            # ...and a 'good' reason to switch out
            if active.boosts["def"] <= -3 or active.boosts["spd"] <= -3:
                return True
            if (
                active.boosts["atk"] <= -3
                and active.stats["atk"] >= active.stats["spa"]
            ):
                return True
            if (
                active.boosts["spa"] <= -3
                and active.stats["atk"] <= active.stats["spa"]
            ):
                return True
            if (
                self._estimate_matchup(active, opponent)
                < self.SWITCH_OUT_MATCHUP_THRESHOLD
            ):
                return True
        return False

    def choose_move(self, battle: AbstractBattle):
        return 



    ## Plan

    # In order of importance

    # Estimate the matchup - Calculate damage ratio and special ratio of the two pokemon, health difference, 

    # Decide if i should use Entry Hazzards

    # Boost stats if match up is good

    # if matchup is shite, switch to matchup that is estimated to be the best
    # fallback to random move to not break anything 


# could possibly add:
# - switching prediction , opponent movement prediction, add hazards if opponent obviosuly switches 
# - add randomness ( eg switch to a neutral matchup to throw off opponents predicitions)
# - add to the hazards ( smarter hazards, imunities)
# - Dynamax logic, find sweep windows
# - look at switching logic, 
# - Add a risk factor? if losing then turn up the risk factor to pull of riskier but more rewarding moves
# - track opponent info? 
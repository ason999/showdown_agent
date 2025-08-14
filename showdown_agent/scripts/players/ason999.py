from poke_env.battle import AbstractBattle
from poke_env.player import Player
from poke_env.battle.move import Move
from poke_env.battle.pokemon import Pokemon
from poke_env.battle.side_condition import SideCondition

from typing import List, Optional, Tuple



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

# # # Random Team 1

# team = """
# Landorus @ Life Orb
# Ability: Sheer Force
# Tera Type: Ground
# EVs: 252 spa / 4 spd / 252 spe 
# Timid Nature
# IVs: 0 atk 
# - Earth Power
# - Focus Blast
# - Psychic
# - Nasty Plot

# Clawitzer @ Choice Specs
# Ability: Mega Launcher
# Tera Type: Dragon
# EVs: 4 def / 252 spa / 252 spe 
# Modest Nature
# IVs: 0 atk 
# - Water Pulse
# - Dragon Pulse
# - Aura Sphere
# - Dark Pulse

# Dialga @ Choice Scarf
# Ability: Pressure
# Tera Type: Dragon
# EVs: 252 spa / 4 spd / 252 spe 
# Timid Nature
# IVs: 0 atk 
# - Draco Meteor
# - Fire Blast
# - Dragon Pulse
# - Thunder

# Hydrapple @ Choice Specs
# Ability: Regenerator
# Tera Type: Steel
# EVs: 4 def / 252 spa / 252 from typing import List, Optional, Tuplespe 
# Modest Nature
# - Leaf Storm
# - Draco Meteor
# - Earth Power
# - Fickle Beam

# Appletun @ Heavy-Duty Boots
# Ability: Thick Fat
# Tera Type: Steel
# EVs: 252 hp / 4 def / 252 spd 
# Sassy Nature
# - Apple Acid
# - Dragon Pulse
# - Dragon Tail
# - Recover

# Pyroar @ Heavy-Duty Boots
# Ability: Unnerve
# Tera Type: Ghost
# EVs: 4 def / 252 spa / 252 spe 
# Timid Nature
# IVs: 0 atk 
# - Fire Blast
# - Hyper Voice
# - Taunt
# - Will-O-Wisp
# """


# # Random Team 2

# team = """
# Zacian-Crowned @ Rusted Sword
# Ability: Intrepid Sword
# Tera Type: Fighting
# EVs: 252 atk / 4 spd / 252 spe 
# Jolly Nature
# - Swords Dance
# - Behemoth Blade
# - Close Combat
# - Wild Charge

# Zekrom @ Leftovers
# Ability: Teravolt
# Tera Type: Flying
# EVs: 252 atk / 4 def / 252 spe 
# Jolly Nature
# - Dragon Dance
# - Bolt Strike
# - Dragon Claw
# - Substitute

# Arceus-Poison @ Toxic Plate
# Ability: Multitype
# Tera Type: Grass
# EVs: 252 hp / 132 def / 124 spe 
# Impish Nature
# - Poison Jab
# - Will-O-Wisp
# - Taunt
# - Recover

# Florges @ Choice Specs
# Ability: Flower Veil
# Tera Type: Ground
# EVs: 4 def / 252 spa / 252 spe 
# Modest Nature
# IVs: 0 atk 
# - Moonblast
# - Trick
# - Tera Blast
# - Psychic Noise

# Venusaur @ Heavy-Duty Boots
# Ability: Overgrow
# Tera Type: Ground
# EVs: 4 def / 252 spa / 252 spe 
# Timid Nature
# IVs: 0 atk 
# - Leaf Storm
# - Sludge Bomb
# - Earth Power
# - Synthesis

# Cinderace @ Heavy-Duty Boots
# Ability: Libero
# Tera Type: Fire
# EVs: 252 atk / 4 def / 252 spe 
# Jolly Nature
# - Pyro Ball
# - U-turn
# - Court Change
# - Sucker Punch
# """


# Coefficients
SPEED_TIER_COEFFICIENT = 0.6
HP_FRACTION_COEFFICIENT = 0.8
ATK_DEF_WEIGHT = 0.9
SPA_SPD_WEIGHT = 0.9
TYPE_WEIGHT = 1.25
HAZARD_TURN_CUTOFF = 3
SWITCH_OUT_MATCHUP_THRESHOLD = -0.75
DANGER_KO_THRESHOLD = 0.95  # if predicted best incoming hit >= 95% of our HP, bail
SWEEP_WINDOW_THRESHOLD = 1.25  # matchup score to consider "very favorable" for dmax
ENDGAME_MON_COUNT = 1  # last-mon check for dmax
MIN_SAFE_HAZARD_MATCHUP = 0.0  # only set hazards if we aren't in a losing matchup
MIN_SAFE_HAZARD_HP_FRAC = 0.6  # avoid hazards if we're too low

class CustomAgent(Player):

    # Hazards
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

    def __init__(self, *args, **kwargs):
        super().__init__(team=team, *args, **kwargs)

    ## Plan

    # In order of importance

    # Estimate the matchup - Calculate damage ratio and special ratio of the two pokemon, health difference, 

    # Decide if i should use Entry Hazzards

    # Boost stats if match up is good

    # if matchup is shite, switch to matchup that is estimated to be the best
    # fallback to random move to not break anything 


# could possibly add:
# - switching prediction , opponent movement prediction, add hazards if opponent obviosuly switches 
# - add to the hazards ( smarter hazards, imunities)
# - Dynamax logic, find sweep windows
# - look at switching logic, 
# - Add a risk factor? if losing then turn up the risk factor to pull of riskier but more rewarding moves
# - track opponent info? 


    # -----------------------
    # Core: matchup estimation
    # -----------------------
    def _coarse_stat(self, mon: Pokemon, key: str) -> int:
        # Prefer revealed stats; otherwise fall back to base_stats (poke-env provides both)
        return (mon.stats.get(key) or mon.base_stats.get(key) or 0)

    def _off_def_ratio(self, atk_mon: Pokemon, def_mon: Pokemon) -> float:
        # Compare physical and special lanes; weight them together
        atk = max(self._coarse_stat(atk_mon, "atk"), 1)
        spa = max(self._coarse_stat(atk_mon, "spa"), 1)
        dfn = max(self._coarse_stat(def_mon, "def"), 1)
        spd = max(self._coarse_stat(def_mon, "spd"), 1)
        phys = atk / dfn
        spec = spa / spd
        return ATK_DEF_WEIGHT * phys + SPA_SPD_WEIGHT * spec

    def _type_pressure(self, atk_mon: Pokemon, def_mon: Pokemon) -> float:
        # How well our types hit them vs theirs hitting us
        our_best = max([def_mon.damage_multiplier(t) for t in atk_mon.types if t], default=1.0)
        their_best = max([atk_mon.damage_multiplier(t) for t in def_mon.types if t], default=1.0)
        return TYPE_WEIGHT * (our_best - their_best)

    def _estimate_matchup(self, mon: Pokemon, opponent: Pokemon) -> float:
        """
        Positive means favorable for 'mon'. Combines: type pressure, speed tier,
        HP fractions, and coarse atk/def ratios.
        """
        score = 0.0
        score += self._type_pressure(mon, opponent)
        # speed tier bump
        if self._coarse_stat(mon, "spe") > self._coarse_stat(opponent, "spe"):
            score += SPEED_TIER_COEFFICIENT
        elif self._coarse_stat(opponent, "spe") > self._coarse_stat(mon, "spe"):
            score -= SPEED_TIER_COEFFICIENT
        # HP state
        score += (mon.current_hp_fraction - opponent.current_hp_fraction) * HP_FRACTION_COEFFICIENT
        # crude offensive/defensive slant
        score += self._off_def_ratio(mon, opponent) - self._off_def_ratio(opponent, mon)
        return score

    # ---------------------------------
    # Rough damage model for a given move
    # ---------------------------------
    def _type_multiplier_for_move(self, move: Move, defender: Pokemon) -> float:
        try:
            return defender.damage_multiplier(move)
        except Exception:
            return 1.0

    def _stab_for_move(self, move: Move, attacker: Pokemon) -> float:
        # Explicit 1.5x STAB if move type matches one of attacker's types
        try:
            return 1.5 if move.type in attacker.types else 1.0
        except Exception:
            return 1.0

    def _lane_coeff(self, move: Move, attacker: Pokemon, defender: Pokemon) -> float:
        # Physical or Special lane based on attacker & defender stats
        try:
            cat = move.category  # 'physical'|'special'|'status'
        except Exception:
            cat = "status"
        if cat == "status":
            return 0.0
        if cat == "physical":
            atk = max(self._coarse_stat(attacker, "atk"), 1)
            dfn = max(self._coarse_stat(defender, "def"), 1)
        else:  # special
            atk = max(self._coarse_stat(attacker, "spa"), 1)
            dfn = max(self._coarse_stat(defender, "spd"), 1)
        return atk / dfn

    def _estimate_move_damage_fraction(self, move: Move, attacker: Pokemon, defender: Pokemon) -> float:
        """
        Returns a coarse fraction of defender's max HP this move might deal.
        Uses: base_power * STAB * type_multiplier * lane_coeff, normalized by defender HP.
        """
        try:
            bp = float(move.base_power or 0)
        except Exception:
            bp = 0.0
        if bp <= 0:
            return 0.0
        mult = self._stab_for_move(move, attacker) * self._type_multiplier_for_move(move, defender)
        lane = self._lane_coeff(move, attacker, defender)
        raw = bp * mult * lane
        hp = max(defender.max_hp, 1)
        return (raw / 200.0) * (100.0 / (hp if hp > 100 else 100.0))

    # ------------------------------------
    # Predict opponent's next best move
    # ------------------------------------
    def _opponent_best_move_and_damage(self, battle: AbstractBattle) -> Tuple[Optional[Move], float]:
        me = battle.active_pokemon
        opp = battle.opponent_active_pokemon
        if not me or not opp:
            return None, 0.0
        best_move = None
        best_dmg = 0.0
        candidate_moves: List[Move] = list(getattr(opp, "moves", {}).values()) or []
        if not candidate_moves:
            return None, 0.25  # unknown set: assume ~25% HP potential as a soft prior
        for mv in candidate_moves:
            est = self._estimate_move_damage_fraction(mv, opp, me)
            if est > best_dmg:
                best_dmg = est
                best_move = mv
        return best_move, best_dmg

    # ------------------------------------
    # Entry hazard decision
    # ------------------------------------
    def _should_set_entry_hazard(self, battle: AbstractBattle) -> Optional[Move]:
        me = battle.active_pokemon
        opp = battle.opponent_active_pokemon
        if not me or not opp:
            return None
        if battle.turn is not None and battle.turn > HAZARD_TURN_CUTOFF:
            return None
        if me.current_hp_fraction < MIN_SAFE_HAZARD_HP_FRAC:
            return None

        matchup = self._estimate_matchup(me, opp)
        if matchup < MIN_SAFE_HAZARD_MATCHUP:
            return None  # too risky to waste a turn

        # If opponent likely to switch (they're in a bad matchup or fear a KO), hazards gain value
        _, opp_best = self._opponent_best_move_and_damage(battle)
        we_threaten_ko = self._best_offensive_pressure(battle) >= 0.9
        they_threaten_ko = opp_best >= 0.9
        likely_switch = (matchup > 0.5 and we_threaten_ko and not they_threaten_ko)

        # Only set hazards if not already present and we have the move
        our_moves = {m.id: m for m in battle.available_moves}
        for name, cond in self.ENTRY_HAZARDS.items():
            if name in our_moves:
                already_set = cond in battle.opponent_side_conditions
                if not already_set and (likely_switch or matchup >= 0.75):
                    return our_moves[name]
        return None

    def _best_offensive_pressure(self, battle: AbstractBattle) -> float:
        me = battle.active_pokemon
        opp = battle.opponent_active_pokemon
        if not me or not opp:
            return 0.0
        best = 0.0
        for mv in battle.available_moves:
            est = self._estimate_move_damage_fraction(mv, me, opp)
            if est > best:
                best = est
        return best

    # -------------------------
    # Dynamax (if the format can)
    # -------------------------
    def _should_dynamax(self, battle: AbstractBattle) -> bool:
        if not battle.can_dynamax:
            return False
        me = battle.active_pokemon
        opp = battle.opponent_active_pokemon
        if not me or not opp:
            return False

        my_remaining = len([p for p in battle.team.values() if not p.fainted])
        # Endgame: last mon standing, consider dmax to clutch
        if my_remaining <= ENDGAME_MON_COUNT:
            return True

        # Strong sweep window: we outspeed, have a great matchup, and can pressure big damage
        matchup = self._estimate_matchup(me, opp)
        outspeed = self._coarse_stat(me, "spe") >= self._coarse_stat(opp, "spe")
        pressure = self._best_offensive_pressure(battle)
        if outspeed and matchup >= SWEEP_WINDOW_THRESHOLD and pressure >= 0.6:
            return True

        return False

    # --------------------------------
    # Switch-out logic
    # --------------------------------
    def _best_switch_target(self, battle: AbstractBattle) -> Optional[Pokemon]:
        opp = battle.opponent_active_pokemon
        if not opp:
            return None
        candidates = battle.available_switches
        if not candidates:
            return None
        # Pick the switch with the highest matchup score vs the opponent
        ranked = sorted(candidates, key=lambda m: self._estimate_matchup(m, opp), reverse=True)
        return ranked[0] if ranked else None

    def _should_switch_out(self, battle: AbstractBattle) -> bool:
        me = battle.active_pokemon
        opp = battle.opponent_active_pokemon
        if not me or not opp:
            return False

        # If there's a decent switch available and our matchup is poor, consider switching
        decent_switch_exists = any(
            self._estimate_matchup(m, opp) > 0.0 for m in battle.available_switches
        )

        # Predict if we might be KO'd by their best known move
        _, opp_best = self._opponent_best_move_and_damage(battle)
        lethal_risk = opp_best >= DANGER_KO_THRESHOLD

        # Bad matchup or deep negative boosts -> get out
        bad_matchup = self._estimate_matchup(me, opp) < SWITCH_OUT_MATCHUP_THRESHOLD
        badly_debuffed = (
            me.boosts["def"] <= -3 or me.boosts["spd"] <= -3
            or (me.boosts["atk"] <= -3 and (self._coarse_stat(me, "atk") >= self._coarse_stat(me, "spa")))
            or (me.boosts["spa"] <= -3 and (self._coarse_stat(me, "spa") >= self._coarse_stat(me, "atk")))
        )

        return decent_switch_exists and (badly_debuffed or bad_matchup or lethal_risk)


    # Main decision based off of 
    def choose_move(self, battle: AbstractBattle):
        # 1) If we're forced to switch, pick the best switch
        if battle.force_switch:
            target = self._best_switch_target(battle)
            if target:
                return self.create_order(target)
            return self.choose_random_move(battle)

        me = battle.active_pokemon
        opp = battle.opponent_active_pokemon

        # 2) Emergency: if predicted KO incoming and we can switch to something better, do it
        if self._should_switch_out(battle):
            target = self._best_switch_target(battle)
            if target:
                return self.create_order(target)

        # 3) Set hazards early if sensible
        hazard_move = self._should_set_entry_hazard(battle)
        if hazard_move is not None:
            return self.create_order(hazard_move)

        # 4) Dynamax if a clear sweep window / endgame (if available in this format)
        do_dmax = self._should_dynamax(battle)

        # 5) Attack: pick the highest estimated damage move
        if me and opp and battle.available_moves:
            best_move = max(
                battle.available_moves,
                key=lambda mv: self._estimate_move_damage_fraction(mv, me, opp),
            )
            return self.create_order(best_move, dynamax=do_dmax)

        # 6) As a fallback, use poke-env random legal choice to avoid stalling the engine
        return self.choose_random_move(battle)
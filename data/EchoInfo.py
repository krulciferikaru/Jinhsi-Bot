from data.Emojis import Emojis

echoInfo = {
##---------------------------1 cost---------------------------##
    'Aero Predator': {
        'Cost': '1',
        'Class': 'Common',
        'CD': '8s',
        'SonataEffects': [f"{Emojis['SonataEffects']['Sierra Gale']}", 
                          f"{Emojis['SonataEffects']['Void Thunder']}"],
        'Description': "Summon an Aero Predator that throws a dart forward. "
                       "The dart will bounce between enemies up to three times, dealing **28.80%** Aero DMG each time it hits."
    },
    'Chirpuff': {
        'Cost': '1',
        'Class': 'Common',
        'CD': '8s',
        'SonataEffects': [f"{Emojis['SonataEffects']['Sierra Gale']}", 
                          f"{Emojis['SonataEffects']['Sun-sinking Eclipse']}"],
        'Description': "Summon a Chirpuff that self-inflates and blasts a powerful gust of wind forward **3** time(s). "
                       "Each blast inflicts **3 Aero DMG** and pushes enemies backwards."
    },
    'Clang Bang': {
        'Cost': '1',
        'Class': 'Common',
        'CD': '8s',
        'SonataEffects': [f"{Emojis['SonataEffects']['Freezing Frost']}", 
                          f"{Emojis['SonataEffects']['Sun-sinking Eclipse']}"],
        'Description': "Summon a Clang Bang that follows the enemy and eventually self-combusts, dealing **32.00%+64** Glacio DMG."
        },
    'Cruisewing': {
        'Cost': '1',
        'Class': 'Common',
        'CD': '8s',
        'SonataEffects': [f"{Emojis['SonataEffects']['Rejuvenating Glow']}", 
                          f"{Emojis['SonataEffects']['Celestial Light']}",
                          f"{Emojis['SonataEffects']['Moonlit Clouds']}"],
        'Description': "Summon a Cruisewing that restores HP for all current team characters by **1.20%** of their Max HPs plus an additional **80** points of HP, up to **4** time(s)."
        },
    'Diamond Claw': {
        'Cost': '1',
        'Class': 'Common',
        'CD': '8s',
        'SonataEffects': [f"{Emojis['SonataEffects']['Moonlit Clouds']}",
                          f"{Emojis['SonataEffects']['Lingering Tunes']}"],
        'Description': "Transform into Crystal Scorpion and enter a Parry State. "
                       "Counterattack when the Parry State is over, dealing **48.00%+96** Physical DMG."
        },
    'Dwarf Cassowary': {
        'Cost': '1',
        'Class': 'Common',
        'CD': '8s',
        'SonataEffects': [f"{Emojis['SonataEffects']['Sierra Gale']}", 
                          f"{Emojis['SonataEffects']['Rejuvenating Glow']}"],
        'Description': "Summon a Dwarf Cassowary that tracks and attacks the enemy, dealing **38.4%** Physical DMG **3** time(s)."
        },
    'Electro Predator': {
        'Cost': '1',
        'Class': 'Common',
        'CD': '8s',
        'SonataEffects': [f"{Emojis['SonataEffects']['Void Thunder']}", 
                          f"{Emojis['SonataEffects']['Molten Rift']}"],
        'Description': "Summon an Electro Predator to shoot the enemy **5** time(s). The first 4 shots deals **17.28%** Electro DMG, and the last deals **46.08%** Electro DMG."
        },
    'Excarat': {
        'Cost': '1',
        'Class': 'Common',
        'CD': '2s',
        'SonataEffects': [f"{Emojis['SonataEffects']['Freezing Frost']}", 
                          f"{Emojis['SonataEffects']['Sun-sinking Eclipse']}"],
        'Description': "Transform into an Excarat and tunnel underground to advance. In this state, you have the ability to change your direction and are immune to damage."
        },
    'Fission Junrock': {
        'Cost': '1',
        'Class': 'Common',
        'CD': '15s',
        'SonataEffects': [f"{Emojis['SonataEffects']['Void Thunder']}", 
                          f"{Emojis['SonataEffects']['Rejuvenating Glow']}"
                          f"{Emojis['SonataEffects']['Moonlit Clouds']}"],
        'Description': "Summon a Fission Junrock. Generate a Resonance Effect that restores 2% HP for friendly units each time. "
                       "If not in combat, you can pick up minerals or plants nearby."
        },
    'Fusion Dreamane Minor': {
        'Cost': '1',
        'Class': 'Common',
        'CD': '8s',
        'SonataEffects': [f"{Emojis['SonataEffects']['Molten Rift']}", 
                          f"{Emojis['SonataEffects']['Rejuvenating Glow']}"],
        'Description': "Summon a Fusion Dreadmane that fiercely strikes the enemy, dealing **32%+64** Fusion DMG."
        },
    'Fusion Prism': {
        'Cost': '1',
        'Class': 'Common',
        'CD': '8s',
        'SonataEffects': [f"{Emojis['SonataEffects']['Molten Rift']}"
                          f"{Emojis['SonataEffects']['Freezing Frost']}", 
                          f"{Emojis['SonataEffects']['Lingering Tunes']}"],
        'Description': "Summon a Fusion Prism to fire a crystal shard, dealing **32%+64** Fusion DMG."
        },
    'Fusion Warrior': {
        'Cost': '1',
        'Class': 'Common',
        'CD': '15s',
        'SonataEffects': [f"{Emojis['SonataEffects']['Molten Rift']}"
                          f"{Emojis['SonataEffects']['Void Thunder']}", 
                          f"{Emojis['SonataEffects']['Sierra Gale']}"],
        'Description': "Transform into Fusion Warrior to perform a Counterattack. "
                       "If the Counterattack is successful, the cooldown time of this skill will be reduced by **70.00%**, and **288%** Fusion DMG will be dealt."    
        },
    'Glacio Predator': {
        'Cost': '1',
        'Class': 'Common',
        'CD': '8s',
        'SonataEffects': [f"{Emojis['SonataEffects']['Freezing Frost']}"
                          f"{Emojis['SonataEffects']['Celestial Light']}"],
        'Description': "Summon a Glacio Predator that throws an ice spear, dealing **46.08%** Glacio DMG on hit. "
                       "Deal **4.61%** Glacio DMG up to **10** time(s) during the charging time, and **23.04%** Glacio DMG when the spear explodes."
        },
    'Glacio Prism': {
        'Cost': '1',
        'Class': 'Common',
        'CD': '8s',
        'SonataEffects': [f"{Emojis['SonataEffects']['Freezing Frost']}"
                          f"{Emojis['SonataEffects']['Sun-sinking Eclipse']}",
                          f"{Emojis['SonataEffects']['Moonlit Clouds']}"],
        'Description': "Summon a Glacio Prism that continuously fires three crystal shards, each dealing **38.40%** Glacio DMG."
        },
    'Gulpuff': {
        'Cost': '1',
        'Class': 'Common',
        'CD': '8s',
        'SonataEffects': [f"{Emojis['SonataEffects']['Freezing Frost']}"
                          f"{Emojis['SonataEffects']['Celestial Light']}"],
        'Description': "Summon a Gulpuff that blows bubbles **5** times, each time dealing **5** Glacio DMG."
        },
    'Havoc Prism': {
        'Cost': '1',
        'Class': 'Common',
        'CD': '8s',
        'SonataEffects': [f"{Emojis['SonataEffects']['Sun-sinking Eclipse']}"
                          f"{Emojis['SonataEffects']['Void Thunder']}",
                          f"{Emojis['SonataEffects']['Celestial Light']}"],
        'Description': "Summon a Havoc Prism to fire five crystal shards, each dealing **23.04%** Havoc DMG."
        },
    'Havoc Warrior': {
        'Cost': '1',
        'Class': 'Common',
        'CD': '15s',
        'SonataEffects': [f"{Emojis['SonataEffects']['Sun-sinking Eclipse']}",
                          f"{Emojis['SonataEffects']['Celestial Light']}"],
        'Description': "Transform into Havoc Warrior to attack up to **3** time(s), dealing **171.73%** Havoc DMG each time."
        },
    'Hoartoise': {
        'Cost': '1',
        'Class': 'Common',
        'CD': '2s',
        'SonataEffects': [f"{Emojis['SonataEffects']['Freezing Frost']}",
                          f"{Emojis['SonataEffects']['Celestial Light']}"],
        'Description': "Transform into Hoartoise and slowly restore HP. Use the Echo skill again to exit the transformation state."
        },
    'Hooscamp': {
        'Cost': '1',
        'Class': 'Common',
        'CD': '8s',
        'SonataEffects': [f"{Emojis['SonataEffects']['Sierra Gale']}",
                          f"{Emojis['SonataEffects']['Lingering Tunes']}"],
        'Description': "Transform into Hooscamp Flinger and pounce at the enemies, dealing **48.00%+96** Aero DMG."      
        },
    'Lava Larva': {
        'Cost': '1',
        'Class': 'Common',
        'CD': '8s',
        'SonataEffects': [f"{Emojis['SonataEffects']['Molten Rift']}",
                          f"{Emojis['SonataEffects']['Lingering Tunes']}"],
        'Description': "Summon a Lava Larva that continuously attacks enemies, dealing **38.4%** Fusion DMG with each hit. "
                       "The Lava Larva disappears when the summoner is switched out or moves too far away."     
        },
    'Sabyr Boar': {
        'Cost': '1',
        'Class': 'Common',
        'CD': '8s',
        'SonataEffects': [f"{Emojis['SonataEffects']['Freezing Frost']}",
                          f"{Emojis['SonataEffects']['Sierra Gale']}",
                          f"{Emojis['SonataEffects']['Moonlit Clouds']}"],
        'Description': "Summon a Sabyr Boar to headbutt the enemy into the air, dealing **32.00%+64** Physical DMG."  
        },
    'Snip Snap': {
        'Cost': '1',
        'Class': 'Common',
        'CD': '8s',
        'SonataEffects': [f"{Emojis['SonataEffects']['Molten Rift']}",
                          f"{Emojis['SonataEffects']['Rejuvenating Glow']}",
                          f"{Emojis['SonataEffects']['Lingering Tunes']}"],
        'Description': "Summon a Snip Snap that throws fireballs at the enemy, dealing **32%+64** Fusion DMG on-hit."  
        },
    'Spectro Prism': {
        'Cost': '1',
        'Class': 'Common',
        'CD': '8s',
        'SonataEffects': [f"{Emojis['SonataEffects']['Celestial Light']}",
                          f"{Emojis['SonataEffects']['Molten Rift']}",
                          f"{Emojis['SonataEffects']['Void Thunder']}"],
        'Description': "Summon a Spectro Prism to emit a laser that hits the enemy up to **8** time(s), dealing **14.40%** Spectro DMG each time."  
        },
    'Tick Tack': {
        'Cost': '1',
        'Class': 'Common',
        'CD': '15s',
        'SonataEffects': [f"{Emojis['SonataEffects']['Sun-sinking Eclipse']}",
                          f"{Emojis['SonataEffects']['Rejuvenating Glow']}",
                          f"{Emojis['SonataEffects']['Lingering Tunes']}"],
        'Description': "Summon a Tick Tack that charges and bites the enemy. "
                       "The charge from Tick Tack will deal **68.48%** Havoc DMG to the enemy, and the bite will deal **102.72%** Havoc DMG to the enemy. "
                       "Reduces enemy Vibration Strength by up to **5.00%** during **5s**."  
        },
    'Traffic Illuminator': {
        'Cost': '1',
        'Class': 'Common',
        'CD': '15s',
        'SonataEffects': [f"{Emojis['SonataEffects']['Molten Rift']}",
                          f"{Emojis['SonataEffects']['Sierra Gale']}",
                          f"{Emojis['SonataEffects']['Void Thunder']}"],
        'Description': "Summon a Traffic Illuminator, immobilizing enemies for up to **1s**. The immobilization will be lifted once the enemy is hit."  
        },
    'Vanguard Junrock': {
        'Cost': '1',
        'Class': 'Common',
        'CD': '8s',
        'SonataEffects': [f"{Emojis['SonataEffects']['Void Thunder']}",
                          f"{Emojis['SonataEffects']['Rejuvenating Glow']}",
                          f"{Emojis['SonataEffects']['Lingering Tunes']}"],
        'Description': "Summon a Vanguard Junrock that charges forward, dealing **32.00%+64** Physical DMG to enemies in its path."  
        },
    'Whiff Whaff': {
        'Cost': '1',
        'Class': 'Common',
        'CD': '15s',
        'SonataEffects': [f"{Emojis['SonataEffects']['Sierra Gale']}",
                          f"{Emojis['SonataEffects']['Rejuvenating Glow']}",
                          f"{Emojis['SonataEffects']['Moonlit Clouds']}"],
        'Description': "Summon a Whiff Whaff that triggers an air explosion, dealing **51.36%** Aero DMG and produce a Low-pressure Zone. "
                       "The Low-pressure Zone continuously pulls enemies nearby towards the center for **2s**, dealing **19.97%** Aero DMG up to **6** time(s)."  
        },
    'Young Geohide Saurian': {
        'Cost': '1',
        'Class': 'Common',
        'CD': '2s',
        'SonataEffects': [f"{Emojis['SonataEffects']['Molten Rift']}",
                          f"{Emojis['SonataEffects']['Void Thunder']}",
                          f"{Emojis['SonataEffects']['Lingering Tunes']}"],
        'Description': "Transform into Baby Viridblaze Saurian to rest in place, and slowly restore HP."  
        },
    'Young Roseshroom': {
        'Cost': '1',
        'Class': 'Common',
        'CD': '8s',
        'SonataEffects': [f"{Emojis['SonataEffects']['Sun-sinking Eclipse']}",
                          f"{Emojis['SonataEffects']['Sierra Gale']}"],
        'Description': "Summon a Baby Roseshroom that fires a laser, dealing **32%+64** Havoc DMG."  
        },
    'Zig Zag': {
        'Cost': '1',
        'Class': 'Common',
        'CD': '8s',
        'SonataEffects': [f"{Emojis['SonataEffects']['Celestial Light']}",
                          f"{Emojis['SonataEffects']['Moonlit Clouds']}",
                          f"{Emojis['SonataEffects']['Lingering Tunes']}"],
        'Description': "Summon a Zig Zag that denotates Spectro energy, dealing **48%+96** Spectro DMG and creating a Stagnation Zone that lasts **1.8s**."  
        },
##---------------------------3 cost---------------------------##
    'Autopuppet Scout': {
        'Cost': '3',
        'Class': 'Elite',
        'CD': '15s',
        'SonataEffects': [f"{Emojis['SonataEffects']['Freezing Frost']}",
                          f"{Emojis['SonataEffects']['Celestial Light']}"],
        'Description': "Transform into Autopuppet Scout, dealing **272%** Glacio DMG to the surroundings, and generate up to **3** Ice Walls to block off the enemies."
        },
    'Carapace': {
        'Cost': '3',
        'Class': 'Elite',
        'CD': '15s',
        'SonataEffects': [f"{Emojis['SonataEffects']['Sierra Gale']}",
                          f"{Emojis['SonataEffects']['Moonlit Clouds']}"],
        'Description': "Transform into Carapace to perform a spinning attack that deals **112.00%** Aero DMG, followed by a slash that deals **168.00%** Aero DMG."
        },
    'Chasm Guardian': {
        'Cost': '3',
        'Class': 'Elite',
        'CD': '15s',
        'SonataEffects': [f"{Emojis['SonataEffects']['Rejuvenating Glow']}",
                          f"{Emojis['SonataEffects']['Lingering Tunes']}"],
        'Description': "Transform into Chasm Guardian to perform a Leap Strike that deals **273.60%** Havoc DMG on hit. "
                       "Current character loses **10.00%** HP after the hit lands. "
                       "Periodically restore current character's HP after 5s for up to **10.00%** of their Max HP."
        },
    'Cyan-Feathered Heron': {
        'Cost': '3',
        'Class': 'Elite',
        'CD': '15s',
        'SonataEffects': [f"{Emojis['SonataEffects']['Sierra Gale']}",
                          f"{Emojis['SonataEffects']['Celestial Light']}"],
        'Description': "Transform into Cyan-Feathered Heron and charge at the enemies, dealing **236.8%** Aero DMG; "
                       "This Echo Skill interrupts enemy Special Skills upon dealing damage."
    },
    'Flautist': {
        'Cost': '3',
        'Class': 'Elite',
        'CD': '15s',
        'SonataEffects': [f"{Emojis['SonataEffects']['Void Thunder']}",
                          f"{Emojis['SonataEffects']['Lingering Tunes']}"],
        'Description': "Transform into Flautist, continuously emitting Electro lasers, dealing **53.2%** Electro DMG for a total of **10** time(s). "
                       "Gain **1** Concerto Energy every time a hit lands."
    },
    'Geohide Saurian': {
        'Cost': '3',
        'Class': 'Elite',
        'CD': '15s',
        'SonataEffects': [f"{Emojis['SonataEffects']['Molten Rift']}",
                          f"{Emojis['SonataEffects']['Moonlit Clouds']}"],
        'Description': "Summon a Viridblaze Saurian to continuously spit fire, dealing **17.12%** Fusion DMG **10** time(s)."
    },
    'Glacio Dreadmane': {
        'Cost': '3',
        'Class': 'Elite',
        'CD': '20s',
        'SonataEffects': [f"{Emojis['SonataEffects']['Freezing Frost']}",
                          f"{Emojis['SonataEffects']['Moonlit Clouds']}"],
        'Description': "Lacerate enemies as a Glacio Dreadmane, dealing **214.4%** Glacio DMG on each hit. Equipped with **2** charges and can be cast mid-air. "
                       "Glacio Dreadmane deals **20%** more DMG while in mid-air and generates **6** Icicles upon landing, each dealing **32%** Glacio DMG."
    },
    'Havoc Dreadmane': {
        'Cost': '3',
        'Class': 'Elite',
        'CD': '15s',
        'SonataEffects': [f"{Emojis['SonataEffects']['Molten Rift']}",
                          f"{Emojis['SonataEffects']['Sun-sinking Eclipse']}"],
        'Description': "Transform into Havoc Dreadmane to perform tail strikes up to **2** time(s). Each strike deals **116.64%** Havoc DMG. "
                       "An additional strike will be performed on hit, dealing **77.76%** Havoc DMG."
    },
    'Hoochief': {
        'Cost': '3',
        'Class': 'Elite',
        'CD': '15s',
        'SonataEffects': [f"{Emojis['SonataEffects']['Sierra Gale']}",
                          f"{Emojis['SonataEffects']['Rejuvenating Glow']}"],
        'Description': "Use the Echo skill, transform into Hoochief Cyclone and attack with a palm, causing **268.2%** Aero DMG."
    },
    'Lightcrusher': {
        'Cost': '3',
        'Class': 'Elite',
        'CD': '15s',
        'SonataEffects': [f"{Emojis['SonataEffects']['Celestial Light']}"],
        'Description': "Lunge forward as a Lightcrusher, dealing **135.36%** Spectro DMG. Generate **6** Ablucence on hit. Each Ablucence explosion deals **15.04%** Spectro DMG. "
                       "Hold the Echo Skill to stay in the Lightcrusher form, which allows you to leap up and pounce forward in the air for a short distance."
    },
    'Lumiscale Construct': {
        'Cost': '3',
        'Class': 'Elite',
        'CD': '15s',
        'SonataEffects': [f"{Emojis['SonataEffects']['Freezing Frost']}",
                          f"{Emojis['SonataEffects']['Void Thunder']}"],
        'Description': "Transform into a Lumiscale Construct and enter a Parry Stance. "
                       "If you are not attacked during the Parry Stance, slash to deal **553.6%** Glacio DMG when the stance finishes. "
                       "If attacked, counterattack instantly, dealing **830.4%** Glacio DMG. "
                       "When hit with a Special Skill attack while in the Parry Stance, break the Special Skill and counterattack, dealing **830.4%** Glacio DMG."
    },
    'Rocksteady Guardian': {
        'Cost': '3',
        'Class': 'Elite',
        'CD': '15s',
        'SonataEffects': [f"{Emojis['SonataEffects']['Celestial Light']}",
                          f"{Emojis['SonataEffects']['Rejuvenating Glow']}"],
        'Description': "Transform into Rocksteady Guardian and enter a Parry State. "
                       "Upon being attacked, deal Spectro DMG equal to **8.29%** of the current character's Max HP, "
                       "and perform a follow-up attack that deals Spectro DMG equal to **8.29%** of the current character's Max HP. "
                       "Use the Echo skill again to exit the transformation. "
                       "If the attack received is a Special Skill attack, interrupt the enemy's Special Skill and perform a two-stage follow-up attack, "
                       "each inflicting Spectro DMG equal to **5.52%** of the current character's max HP. "
                       "These follow-up attacks simultaneously launch three ground-breaking waves, each inflicting Spectro DMG equal to **4.59%** of the current character's Max HP."
    },
    'Roseshroom': {
        'Cost': '3',
        'Class': 'Elite',
        'CD': '15s',
        'SonataEffects': [f"{Emojis['SonataEffects']['Sun-sinking Eclipse']}",
                          f"{Emojis['SonataEffects']['Freezing Frost']}"],
        'Description': "Summon a Roseshroom that fires a laser, dealing **57.07%** Havoc DMG up to **3** time(s)."
    },
    'Spearback': {
        'Cost': '3',
        'Class': 'Elite',
        'CD': '15s',
        'SonataEffects': [f"{Emojis['SonataEffects']['Moonlit Clouds']}",
                          f"{Emojis['SonataEffects']['Lingering Tunes']}"],
        'Description': "Summon a Spearback to perform **5** consecutive attacks. The first **4** attacks deal **29.96%** Physical DMG, and the last deals **51.36%** Physical DMG."
    },
    'Stonewall Bracer': {
        'Cost': '3',
        'Class': 'Elite',
        'CD': '15s',
        'SonataEffects': [f"{Emojis['SonataEffects']['Rejuvenating Glow']}",
                          f"{Emojis['SonataEffects']['Lingering Tunes']}"],
        'Description': "Transform into Stonewall Bracer and charge forward, dealing **112.64%** Physical DMG on-hit, then smash to deal **168.96%** Physical DMG, "
                       "and gain a shield of **10.00%** of current character's Max HP. Use the Echo skill again to exit the transformation state."
    },
    'Tambourinist': {
        'Cost': '3',
        'Class': 'Elite',
        'CD': '15s',
        'SonataEffects': [f"{Emojis['SonataEffects']['Freezing Frost']}",
                          f"{Emojis['SonataEffects']['Sun-sinking Eclipse']}"],
        'Description': "Summon a Tambourinist that periodically emits Melodies of Annihilation. "
                       "Friendly units hit with Melodies of Annihilation deal an extra Havoc DMG of **14.40%** with their attacks, up to **10** time(s)."
    },
    'Violet-Feathered Heron': {
        'Cost': '3',
        'Class': 'Elite',
        'CD': '15s',
        'SonataEffects': [f"{Emojis['SonataEffects']['Void Thunder']}",
                          f"{Emojis['SonataEffects']['Molten Rift']}"],
        'Description': "Transform into Violet-Feathered Heron and enter a Parry Stance. Counterattack when the Parry stance is over, dealing **288%** Electro DMG. "
                       "If attacked during Parry Stance, you can counterattack in advance and additionally recover **5** Concerto Energy."
    },
##---------------------------4 cost---------------------------##
    'Bell-Borne Geochelone': {
        'Cost': '4',
        'Class': 'Calamity',
        'CD': '20s',
        'SonataEffects': [f"{Emojis['SonataEffects']['Rejuvenating Glow']}",
                          f"{Emojis['SonataEffects']['Moonlit Clouds']}"],
        'Description': "Activate the protection of Bell-Borne Geochelone. Deal Glacio DMG based on **145.92%** of the current character's DEF to nearby enemies, "
                       "and obtain a Bell-Borne Shield that lasts for **15s** The Bell-Borne Shield provides **50.00%** DMG Reduction and **10.00%** DMG Boost for the current team members, "
                       "and disappears after the current character is hit for **3** time(s)."
    },
    'Dreamless': {
        'Cost': '4',
        'Class': 'Calamity',
        'CD': '20s',
        'SonataEffects': [f"{Emojis['SonataEffects']['Sun-sinking Eclipse']}"],
        'Description': "Transform into Dreamless and perform **6** consecutive attacks. The first **5** attacks deal **54.08%** Havoc DMG each, and the last attack deal **270.40%** Havoc DMG. "
                       "The DMG of this Echo Skill is increased by **50%** during the first **5s** after Rover-Havoc casts Resonance Liberation."
    },
    'Jue': {
        'Cost': '4',
        'Class': 'Calamity',
        'CD': '20s',
        'SonataEffects': [f"{Emojis['SonataEffects']['Celestial Light']}"],
        'Description': "Summon Jué to the aid. Jué soars through the air, dealing **48.64%** Spectro DMG, and summons thunderbolts that strike nearby enemies up to **5** time(s), "
                       "each hit dealing **19.46%** Spectro DMG. Jué then spirals downward, attacking surrounding enemies twice, each hit dealing **48.64%** Spectro DMG. " 
                       "Casting this Echo Skill grants the Resonator a Blessing of Time effect that lasts **15s**, during when: \n"
                       "- The Resonator gains **16%** Resonance Skill DMG Bonus. \n"
                       "- When the Resonator's Resonance Skill hits the target, inflict **16%** Spectro DMG **1** time per second for **15s**, considered as the Resonator's Resonance Skill DMG."
    },
    'Crownless': {
        'Cost': '4',
        'Class': 'Overlord',
        'CD': '20s',
        'SonataEffects': [f"{Emojis['SonataEffects']['Sun-sinking Eclipse']}"],
        'Description': "Transform into Crownless and perform up to **4** consecutive attacks. The first **2** attacks deal **134.08%** Havoc DMG each, "
                       "the 3rd attack deals **100.56%** Havoc DMG **2** time(s), and the 4th attack deals **67.04%** Havoc DMG **3** time(s). "
                       "After the transformation, increase current character's Havoc DMG by **12.00%** and Resonance Skill DMG by **12.00%** for **15s**."
    },
    'Feilian Beringal': {
        'Cost': '4',
        'Class': 'Overlord',
        'CD': '20s',
        'SonataEffects': [f"{Emojis['SonataEffects']['Sierra Gale']}"],
        'Description': "Transform into Feilian Beringal to perform a powerful kick. If the kick lands on an enemy, immediately perform a follow-up strike. "
                       "The kick deals **231.84%** Aero DMG, and the follow-up strike deals **283.36%** Aero DMG. After the follow-up strike hits, "
                       "the current character's Aero DMG increases by **12.00%**, and the Heavy Attack DMG increases by **12.00%** for **15s**."
    },
    'Impermanence Heron': {
        'Cost': '4',
        'Class': 'Overlord',
        'CD': '20s',
        'SonataEffects': [f"{Emojis['SonataEffects']['Moonlit Clouds']}"],
        'Description': "Transform into Impermanence Heron to fly up and smack down, dealing 310.56% Havoc DMG. "
                       "Long press to stay as Impermanence Heron Heron and continuously spit flames, each attack dealing **55.73%** Havoc DMG. "
                       "Once the initial attack lands on any enemy, the current character regains **10** Resonance Energy. "
                       "If the current character uses their Outro Skill within the next **15s**, the next character's damage dealt will be boosted by **12%** for **15s**."
    },
    'Inferno Rider': {
        'Cost': '4',
        'Class': 'Overlord',
        'CD': '20s',
        'SonataEffects': [f"{Emojis['SonataEffects']['Molten Rift']}"],
        'Description': "Transform into Inferno Rider to launch up to **3** consecutive slashes in a row, each slash dealing **242.40%**, **282.80%**, and **282.80%** Fusion DMG respectively. "
                       "After the final hit, increase the current character's Fusion DMG by **12.00%** and Basic Attack DMG by **12.00%** for **15s**. "
                       "Long press the Echo Skill to transform into Inferno Rider and enter the Riding Mode. "
                       "When exiting the Riding Mode, deal **12.00%** Fusion DMG to enemies in front."
    },
    'Lampylumen Myriad': {
        'Cost': '4',
        'Class': 'Overlord',
        'CD': '20s',
        'SonataEffects': [f"{Emojis['SonataEffects']['Freezing Frost']}"],
        'Description': "Transform into Lampylumen Myriad. Perform up to **3** consecutive attacks. "
                       "Unleash a freezing shock by performing consecutive forward strikes, with the initial two strikes inflicting **200.16%** and **200.16%** Glacio DMG respectively, "
                       "and the final strike dealing **266.88%** Glacio DMG. Enemies will be frozen on hit. "
                       "Each shock increases the current character's Glacio DMG by **4.00%** and Resonance Skill DMG dealt by **4.00%** for **15s**, stacking up to **3** times."
    },
    'Mech Abomination': {
        'Cost': '4',
        'Class': 'Overlord',
        'CD': '20s',
        'SonataEffects': [f"{Emojis['SonataEffects']['Lingering Tunes']}"],
        'Description': "Strike the enemies in front, dealing **48.64%** Electro DMG. Summon Mech Waste to attack enemies. "
                       "Mech Waste deals **320%** Electro DMG on-hit and explode after a while to deal **160%** Electro DMG. "
                       "After casting this Echo Skill, increase current character's ATK by **12.00%** for **15s**. Damage dealt by Mech Waste is considered Outro Skill DMG."
    },
    'Mourning Aix': {
        'Cost': '4',
        'Class': 'Overlord',
        'CD': '20s',
        'SonataEffects': [f"{Emojis['SonataEffects']['Celestial Light']}"],
        'Description': "Transform into Mourning Aix and perform **2** consecutive claw attacks, each attack dealing **157.44%** and **236.16%** Spectro DMG respectively. "
                       "After the transformation, increase current character's Spectro DMG by **12.00%** and Resonance Liberation DMG by **12.00%** for **15s**."
    },
    'Tempest Memphis': {
        'Cost': '4',
        'Class': 'Overlord',
        'CD': '20s',
        'SonataEffects': [f"{Emojis['SonataEffects']['Void Thunder']}"],
        'Description': "Transform into Tempest Mephis to perform tail swing attacks followed by a claw attack. "
                       "The lightning strike summoned by the tail swing deals **102.48%** Electro DMG each time, while the claw attack deals **175.68%** Electro DMG. "
                       "After the claw hit, increase the current character's Electro DMG by **12.00%** and Heavy Attack DMG by **12.00%** for **15s**."
    },
    'Thundering Memphis': {
        'Cost': '4',
        'Class': 'Overlord',
        'CD': '20s',
        'SonataEffects': [f"{Emojis['SonataEffects']['Void Thunder']}"],
        'Description': "Transform into Thundering Mephis, engaging in a rapid assault of up to **6** strikes. "
                       "The first 5 strikes deal **132.61%** Electro DMG each, while the final strike inflicts **189.44%** Electro DMG, with an additional **31.57%** Electro DMG from the thunder. "
                       "After the final hit, increase the current character's Electro DMG by **12.00%** and Resonance Liberation DMG by **12.00%** for **15s**."
    }
}
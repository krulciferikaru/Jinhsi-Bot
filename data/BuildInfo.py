from data.Emojis import Emojis

buildInfo = {
    'Aalto': {
        'weapon': 'pistols',
        'element': 'aero',
        'color': 'AeroColor',
        'star': '4star',
        'options': [
            {'emoji': Emojis['SonataEffects']['Moonlit Clouds'], 'label': 'Moonlit Clouds', 'description': '[4/3/3/1/1] Sub DPS Build'},
            {'emoji': Emojis['SonataEffects']['Sierra Gale'], 'label': 'Sierra Gale', 'description': '[4/3/3/1/1] Main DPS Build'}
        ],
        'details': {
            'Moonlit Clouds': {
                'echo_set': f"{Emojis['SonataEffects']['Moonlit Clouds']} Moonlit Clouds X5",
                'main_echo': f"{Emojis['4Cost']['Impermanence Heron']} Impermanence Heron",
                'main_stats': [
                    f"{Emojis['StatIcons']['critrate']} `CRIT RATE`", 
                    f"{Emojis['StatIcons']['critdmg']} `CRIT DMG`"
                ],
                'sub_echo1': 'Any Cost 3 Echo X2',
                'sub_stats1': [
                    f"{Emojis['StatIcons']['energyregen']} `Energy Regen`",
                    f"{Emojis['StatIcons']['aerodmg']} `Aero DMG`",
                ],
                'sub_echo2': 'Any Cost 1 Echo X2',
                'sub_stats2': [
                    f"{Emojis['StatIcons']['atk']} `ATK%`"
                ],
                'sub_stats_priority': 'Energy Regen (Minimum) >= CRIT RATE = CRIT DMG > ATK% > Flat ATK'
            },
            'Sierra Gale': {
                'echo_set': f"{Emojis['SonataEffects']['Sierra Gale']} Sierra Gale X5",
                'main_echo': f"{Emojis['4Cost']['Feilian Beringal']} Feilian Beringal",
                'main_stats': [
                    f"{Emojis['StatIcons']['critrate']} `CRIT RATE`",
                    f"{Emojis['StatIcons']['critdmg']} `CRIT DMG`"
                ],
                'sub_echo1': 'Any Cost 3 Echo X2',
                'sub_stats1': [
                    f"{Emojis['StatIcons']['aerodmg']} `Aero DMG`",
                    f"{Emojis['StatIcons']['atk']} `ATK%`"
                ],
                'sub_echo2': 'Any Cost 1 Echo X2',
                'sub_stats2': [
                    f"{Emojis['StatIcons']['atk']} `ATK%`"
                ],
                'sub_stats_priority': 'Energy Regen (Minimum) >= CRIT RATE = CRIT DMG > ATK% > Flat ATK'
            }
        }
    },
    'Baizhi': {
        'weapon': 'rectifier',
        'element': 'glacio',
        'color': 'GlacioColor',
        'star': '4star',
        'options': [
            {'emoji': Emojis['SonataEffects']['Rejuvenating Glow'],'label': 'Rejuvenating Glow', 'description': '[4/3/3/1/1] Support Build'},
        ],
        'details': {
            'Rejuvenating Glow': {
                'echo_set': f"{Emojis['SonataEffects']['Rejuvenating Glow']} Rejuvenating Glow X5",
                'main_echo': f"{Emojis['4Cost']['Bell-Borne Geochelone']} Bell-Borne Geochelone",
                'main_stats': [
                    f"{Emojis['StatIcons']['healingbonus']} `Healing Bonus`",
                ],
                'sub_echo1': 'Any Cost 3 Echo X2',
                'sub_stats1': [
                    f"{Emojis['StatIcons']['energyregen']} `Energy Regen`",
                ],
                'sub_echo2': 'Any Cost 1 Echo X2',
                'sub_stats2': [
                    f"{Emojis['StatIcons']['hp']} `HP%`"
                ],
                'sub_stats_priority': 'Energy Regen (Minimum) > HP% > Flat HP'
            }
        }
    },
    'Calcharo': {
        'weapon': 'broadblade',
        'element': 'electro',
        'color': 'ElectroColor',
        'star': '5star',
        'options': [
            {'emoji': Emojis['SonataEffects']['Void Thunder'], 'label': 'Void Thunder', 'description': '[4/3/3/1/1] Best Main DPS Build'},
            {'emoji': Emojis['SonataEffects']['Void Thunder'], 'label': 'Alternative Void Thunder', 'description': '[4/4/1/1/1] Alternative Main DPS Build'},
        ],
        'details': {
            'Void Thunder': {
                'echo_set': f"{Emojis['SonataEffects']['Void Thunder']} Void Thunder X5",
                'main_echo': f"{Emojis['4Cost']['Tempest Memphis']} Tempest Memphis",
                'main_stats': [
                    f"{Emojis['StatIcons']['critrate']} `CRIT RATE`",
                    f"{Emojis['StatIcons']['critdmg']} `CRIT DMG`"
                ],
                'sub_echo1': 'Any Cost 3 Echo X2',
                'sub_stats1': [
                    f"{Emojis['StatIcons']['electrodmg']} `Electro DMG`",
                    f"{Emojis['StatIcons']['atk']} `ATK%`"
                ],
                'sub_echo2': 'Any Cost 1 Echo X2',
                'sub_stats2': [
                    f"{Emojis['StatIcons']['atk']} `ATK%`"
                ],
                'sub_stats_priority': 'Energy Regen (Minimum) >= CRIT RATE = `CRIT DMG > ATK% > Flat ATK = Liberation DMG%'
            },
            'Alternative Void Thunder': {
                'echo_set': f"{Emojis['SonataEffects']['Void Thunder']} Void Thunder X5",
                'main_echo': f"{Emojis['4Cost']['Tempest Memphis']} Tempest Memphis",
                'main_stats': [
                    f"{Emojis['StatIcons']['critrate']} `CRIT RATE`",
                ],
                'sub_echo1': [f'{Emojis['4Cost']['Thundering Memphis']} Thundering Memphis'],
                'sub_stats1': [
                    f"{Emojis['StatIcons']['critdmg']} `CRIT DMG`"
                ],
                'sub_echo2': 'Any Cost 1 Echo X3',
                'sub_stats2': [
                    f"{Emojis['StatIcons']['atk']} `ATK%`"
                ],
                'sub_stats_priority': 'Energy Regen (Minimum) >= CRIT RATE = CRIT DMG > ATK% > Flat ATK = Liberation DMG%'
            }
        }
    },
    'Changli': {
        'weapon': 'sword',
        'element': 'fusion',
        'color': 'FusionColor',
        'star': '5star',
        'options': [
            {'emoji': f'{Emojis['SonataEffects']['Molten Rift']}','label': 'Molten Rift', 'description': '[4/3/3/1/1] Main DPS Build'},
        ],
        'details': {
            'Molten Rift': {
                'echo_set': f"{Emojis['SonataEffects']['Molten Rift']} Molten Rift X5",
                'main_echo': f"{Emojis['4Cost']['Inferno Rider']} Inferno Rider",
                'main_stats': [
                    f"{Emojis['StatIcons']['critrate']} `CRIT RATE`",
                    f"{Emojis['StatIcons']['critdmg']} `CRIT DMG`"
                ],
                'sub_echo1': 'Any Cost 3 Echo X2',
                'sub_stats1': [
                    f"{Emojis['StatIcons']['fusiondmg']} `Fusion DMG`",
                    f"{Emojis['StatIcons']['atk']} `ATK%`"
                ],
                'sub_echo2': 'Any Cost 1 Echo X2',
                'sub_stats2': [
                    f"{Emojis['StatIcons']['atk']} `ATK%`"
                ],
                'sub_stats_priority': 'Energy Regen (Minimum) >= CRIT RATE = CRIT DMG > ATK% > Flat ATK = Resonance Skill DMG%'
            }
        }
    },
    'Chixia': {
        'weapon': 'pistols',
        'element': 'fusion',
        'color': 'FusionColor',
        'star': '4star',
        'options': [
            {'emoji': f'{Emojis['SonataEffects']['Molten Rift']}','label': 'Molten Rift', 'description': '[4/3/3/1/1] Main DPS Build'},
        ],
        'details': {
            'Molten Rift': {
                'echo_set': f"{Emojis['SonataEffects']['Molten Rift']} Molten Rift X5",
                'main_echo': f"{Emojis['4Cost']['Inferno Rider']} Inferno Rider",
                'main_stats': [
                    f"{Emojis['StatIcons']['critrate']} `CRIT RATE`",
                    f"{Emojis['StatIcons']['critdmg']} `CRIT DMG`"
                ],
                'sub_echo1': 'Any Cost 3 Echo X2',
                'sub_stats1': [
                    f"{Emojis['StatIcons']['fusiondmg']} `Fusion DMG`",
                    f"{Emojis['StatIcons']['atk']} `ATK%`"
                ],
                'sub_echo2': 'Any Cost 1 Echo X2',
                'sub_stats2': [
                    f"{Emojis['StatIcons']['atk']} `ATK%`"
                ],
                'sub_stats_priority': 'Energy Regen (Minimum) >= CRIT RATE = CRIT DMG > ATK% > Flat ATK'
            }
        }
    },
    'Danjin': {
        'weapon': 'sword',
        'element': 'havoc',
        'color': 'HavocColor',
        'star': '4star',
        'options': [
            {'emoji': f'{Emojis['SonataEffects']['Sun-sinking Eclipse']}','label': 'Sun-sinking Eclipse', 'description': '[4/3/3/1/1] Best Main DPS Build'},
            
            {'emoji': f'{Emojis['SonataEffects']['Sun-sinking Eclipse']}','label': 'Alternative Sun-sinking Eclipse', 'description': '[4/4/1/1/1] Alternative Main DPS Build'},
        ],
        'details': {
            'Sun-sinking Eclipse': {
                'echo_set': f"{Emojis['SonataEffects']['Sun-sinking Eclipse']} Sun-sinking Eclipse X5",
                'main_echo': f"{Emojis['4Cost']['Dreamless']} Dreamless",
                'main_stats': [
                    f"{Emojis['StatIcons']['critrate']} `CRIT RATE`",
                    f"{Emojis['StatIcons']['critdmg']} `CRIT DMG`"
                ],
                'sub_echo1': 'Any Cost 3 Echo X2',
                'sub_stats1': [
                    f"{Emojis['StatIcons']['havocdmg']} `Havoc DMG`",
                    f"{Emojis['StatIcons']['atk']} `ATK%`"
                ],
                'sub_echo2': 'Any Cost 1 Echo X2',
                'sub_stats2': [
                    f"{Emojis['StatIcons']['atk']} `ATK%`"
                ],
                'sub_stats_priority': 'CRIT RATE = CRIT DMG > ATK% > Flat ATK > Heavy DMG% > Resonance Skill DMG%'
            },
            'Alternative Sun-sinking Eclipse': {
                'echo_set': f"{Emojis['SonataEffects']['Sun-sinking Eclipse']} Sun-sinking Eclipse X5",
                'main_echo': f"{Emojis['4Cost']['Dreamless']} Dreamless",
                'main_stats': [
                    f"{Emojis['StatIcons']['critrate']} `CRIT RATE`",
                ],
                'sub_echo1': [f"{Emojis['4Cost']['Crownless']} Crownless"],
                'sub_stats1': [
                    f"{Emojis['StatIcons']['critdmg']} `CRIT DMG`"
                ],
                'sub_echo2': 'Any Cost 1 Echo X3',
                'sub_stats2': [
                    f"{Emojis['StatIcons']['atk']} `ATK%`"
                ],
                'sub_stats_priority': 'CRIT RATE = CRIT DMG > ATK% > Flat ATK > Heavy DMG% > Resonance Skill DMG%'
            }
        }

    },
    'Encore': {
        'weapon': 'rectifier',
        'element': 'fusion',
        'color': 'FusionColor',
        'star': '5star',
        'options': [
            {'emoji': f'{Emojis['SonataEffects']['Molten Rift']}','label': 'Molten Rift', 'description': '[4/3/3/1/1] Main DPS Build'},
        ],
        'details': {
            'Molten Rift': {
                'echo_set': f"{Emojis['SonataEffects']['Molten Rift']} Molten Rift X5",
                'main_echo': f"{Emojis['4Cost']['Inferno Rider']} Inferno Rider",
                'main_stats': [
                    f"{Emojis['StatIcons']['critrate']} `CRIT RATE`",
                    f"{Emojis['StatIcons']['critdmg']} `CRIT DMG`"
                ],
                'sub_echo1': 'Any Cost 3 Echo X2',
                'sub_stats1': [
                    f"{Emojis['StatIcons']['fusiondmg']} `Fusion DMG`",
                    f"{Emojis['StatIcons']['atk']} `ATK%`"
                ],
                'sub_echo2': 'Any Cost 1 Echo X2',
                'sub_stats2': [
                    f"{Emojis['StatIcons']['atk']} `ATK%`"
                ],
                'sub_stats_priority': 'Energy Regen (Minimum) >= CRIT RATE = CRIT DMG > ATK% > Flat ATK > Basic DMG%'
            }
        }
    },
    'Jianxin': {
        'weapon': 'gauntlet',
        'element': 'aero',
        'color': 'AeroColor',
        'star': '5star',
        'options': [
            {'emoji': Emojis['SonataEffects']['Moonlit Clouds'], 'label': 'Moonlit Clouds', 'description': '[4/3/3/1/1] Sub DPS Build'},
            {'emoji': Emojis['SonataEffects']['Rejuvenating Glow'], 'label': 'Rejuvenating Glow', 'description': '[4/3/3/1/1] Support Build'},
            {'emoji': Emojis['SonataEffects']['Sierra Gale'], 'label': 'Sierra Gale', 'description': '[4/3/3/1/1] Main DPS Build'}
        ],
        'details': {
            'Moonlit Clouds': {
                'echo_set': f"{Emojis['SonataEffects']['Moonlit Clouds']} Moonlit Clouds X5",
                'main_echo': f"{Emojis['4Cost']['Impermanence Heron']} Impermanence Heron",
                'main_stats': [
                    f"{Emojis['StatIcons']['critrate']} `CRIT RATE`", 
                    f"{Emojis['StatIcons']['critdmg']} `CRIT DMG`"
                ],
                'sub_echo1': 'Any Cost 3 Echo X2',
                'sub_stats1': [
                    f"{Emojis['StatIcons']['energyregen']} `Energy Regen`",
                    f"{Emojis['StatIcons']['aerodmg']} `Aero DMG`"
                ],
                'sub_echo2': 'Any Cost 1 Echo X2',
                'sub_stats2': [
                    f"{Emojis['StatIcons']['atk']} `ATK%`"
                ],
                'sub_stats_priority': 'Energy Regen (Minimum) >= CRIT RATE = CRIT DMG > ATK% > Flat ATK'
            },
            'Rejuvenating Glow': {
                'echo_set': f"{Emojis['SonataEffects']['Rejuvenating Glow']} Rejuvenating Glow X5",
                'main_echo': f"{Emojis['4Cost']['Bell-Borne Geochelone']} Bell-Borne Geochelone",
                'main_stats': [
                    f"{Emojis['StatIcons']['healingbonus']} `Healing Bonus`",
                ],
                'sub_echo1': 'Any Cost 3 Echo X2',
                'sub_stats1': [
                    f"{Emojis['StatIcons']['energyregen']} `Energy Regen`",
                ],
                'sub_echo2': 'Any Cost 1 Echo X2',
                'sub_stats2': [
                    f"{Emojis['StatIcons']['atk']} `ATK%`"
                ],
                'sub_stats_priority': 'Energy Regen (Minimum) >= CRIT RATE = CRIT DMG > ATK% > Flat ATK > Heavy DMG% > Liberation DMG%'
            },
            'Sierra Gale': {
                'echo_set': f"{Emojis['SonataEffects']['Sierra Gale']} Sierra Gale X5",
                'main_echo': f"{Emojis['4Cost']['Feilian Beringal']} Feilian Beringal",
                'main_stats': [
                    f"{Emojis['StatIcons']['critrate']} `CRIT RATE`",
                    f"{Emojis['StatIcons']['critdmg']} `CRIT DMG`"
                ],
                'sub_echo1': 'Any Cost 3 Echo X2',
                'sub_stats1': [
                    f"{Emojis['StatIcons']['aerodmg']} `Aero DMG`",
                    f"{Emojis['StatIcons']['atk']} `ATK%`"
                ],
                'sub_echo2': 'Any Cost 1 Echo X2',
                'sub_stats2': [
                    f"{Emojis['StatIcons']['atk']} `ATK%`"
                ],
                'sub_stats_priority': 'Energy Regen (Minimum) >= CRIT RATE = CRIT DMG > ATK% > Flat ATK > Heavy DMG% > Liberation DMG%'
            }
        }
    },
    'Jinhsi': {
        'weapon': 'broadblade',
        'element': 'spectro',
        'color': 'SpectroColor',
        'star': '5star',
        'options': [
            {'emoji': Emojis['SonataEffects']['Celestial Light'], 'label': 'Celestial Light', 'description': '[4/3/3/1/1] Best Main DPS Build'},
            {'emoji': Emojis['SonataEffects']['Celestial Light'], 'label': 'Alternative Celestial Light', 'description': '[4/4/1/1/1] Alternative Main DPS Build'}
        ],
        'details': {
            'Celestial Light': {
                'echo_set': f"{Emojis['SonataEffects']['Celestial Light']} Celestial Light X5",
                'main_echo': f"{Emojis['4Cost']['Jue']} Jue",
                'main_stats': [
                    f"{Emojis['StatIcons']['critrate']} `CRIT RATE`",
                    f"{Emojis['StatIcons']['critdmg']} `CRIT DMG`"
                ],
                'sub_echo1': 'Any Cost 3 Echo X2',
                'sub_stats1': [
                    f"{Emojis['StatIcons']['spectrodmg']} `Spectro DMG`",
                    f"{Emojis['StatIcons']['atk']} `ATK%`"
                ],
                'sub_echo2': 'Any Cost 1 Echo X2',
                'sub_stats2': [
                    f"{Emojis['StatIcons']['atk']} `ATK%`"
                ],
                'sub_stats_priority': 'Energy Regen (Minimum) >= CRIT RATE = CRIT DMG > ATK% > Resonance Skill DMG% > Flat ATK'
            },
            'Alternative Celestial Light': {
                'echo_set': f"{Emojis['SonataEffects']['Celestial Light']} Celestial Light X5",
                'main_echo': f"{Emojis['4Cost']['Jue']} Jue",
                'main_stats': [
                    f"{Emojis['StatIcons']['critrate']} `CRIT RATE`",
                ],
                'sub_echo1': [f"{Emojis['4Cost']['Mourning Aix']} Mourning Aix"],
                'sub_stats1': [
                    f"{Emojis['StatIcons']['critdmg']} `CRIT DMG`"
                ],
                'sub_echo2': 'Any Cost 1 Echo X3',
                'sub_stats2': [
                    f"{Emojis['StatIcons']['atk']} `ATK%`"
                ],
                'sub_stats_priority': 'Energy Regen (Minimum) >= CRIT RATE = CRIT DMG > ATK% > Resonance Skill DMG% > Flat ATK'
            }   
        }
    },
    'Jiyan': {
        'weapon': 'broadblade',
        'element': 'aero',
        'color': 'AeroColor',
        'star': '5star',
        'options': [
            {'emoji': Emojis['SonataEffects']['Sierra Gale'], 'label': 'Sierra Gale', 'description': '[4/3/3/1/1] Best Main DPS Build'},
        ],
        'details': {
                'Sierra Gale': {
                'echo_set': f"{Emojis['SonataEffects']['Sierra Gale']} Sierra Gale X5",
                'main_echo': f"{Emojis['4Cost']['Feilian Beringal']} Feilian Beringal",
                'main_stats': [
                    f"{Emojis['StatIcons']['critrate']} `CRIT RATE`",
                    f"{Emojis['StatIcons']['critdmg']} `CRIT DMG`"
                ],
                'sub_echo1': 'Any Cost 3 Echo X2',
                'sub_stats1': [
                    f"{Emojis['StatIcons']['aerodmg']} `Aero DMG`",
                    f"{Emojis['StatIcons']['energyregen']} `Energy Regen`"
                ],
                'sub_echo2': 'Any Cost 1 Echo X2',
                'sub_stats2': [
                    f"{Emojis['StatIcons']['atk']} `ATK%`"
                ],
                'sub_stats_priority': 'Energy Regen (Minimum) >= CRIT RATE = CRIT DMG > ATK% > Flat ATK > Heavy DMG%'
            }
        }
    },
    'Lingyang': {
        'weapon': 'gauntlet',
        'element': 'glacio',
        'color': 'GlacioColor',
        'star': '5star',
        'options': [
            {'emoji': Emojis['SonataEffects']['Freezing Frost'], 'label': 'Freezing Frost', 'description': '[4/3/3/1/1] Best Main DPS Build'},
        ],
        'details': {
                'Freezing Frost': {
                'echo_set': f"{Emojis['SonataEffects']['Freezing Frost']} Freezing Frost X5",
                'main_echo': f"{Emojis['4Cost']['Lampylumen Myriad']} Lampylumen Myriad",
                'main_stats': [
                    f"{Emojis['StatIcons']['critrate']} `CRIT RATE`",
                    f"{Emojis['StatIcons']['critdmg']} `CRIT DMG`"
                ],
                'sub_echo1': 'Any Cost 3 Echo X2',
                'sub_stats1': [
                    f"{Emojis['StatIcons']['glaciodmg']} `Glacio DMG`",
                    f"{Emojis['StatIcons']['atk']} `ATK%`"
                ],
                'sub_echo2': 'Any Cost 1 Echo X2',
                'sub_stats2': [
                    f"{Emojis['StatIcons']['atk']} `ATK%`"
                ],
                'sub_stats_priority': 'Energy Regen (Minimum) >= CRIT RATE = CRIT DMG > ATK% > Flat ATK'
            }
        }
    },
    'Mortefi': {
        'weapon': 'pistols',
        'element': 'fusion',
        'color': 'FusionColor',
        'star': '4star',
        'options': [
            {'emoji': Emojis['SonataEffects']['Moonlit Clouds'], 'label': 'Moonlit Clouds', 'description': '[4/3/3/1/1] Sub DPS Build'},
        ],
        'details': {
            'Moonlit Clouds': {
                'echo_set': f"{Emojis['SonataEffects']['Moonlit Clouds']} Moonlit Clouds X5",
                'main_echo': f"{Emojis['4Cost']['Impermanence Heron']} Impermanence Heron",
                'main_stats': [
                    f"{Emojis['StatIcons']['critrate']} `CRIT RATE`", 
                    f"{Emojis['StatIcons']['critdmg']} `CRIT DMG`"
                ],
                'sub_echo1': 'Any Cost 3 Echo X2',
                'sub_stats1': [
                    f"{Emojis['StatIcons']['energyregen']} `Energy Regen`",
                ],
                'sub_echo2': 'Any Cost 1 Echo X2',
                'sub_stats2': [
                    f"{Emojis['StatIcons']['atk']} `ATK%`"
                ],
                'sub_stats_priority': 'Energy Regen (Minimum) >= CRIT RATE = CRIT DMG > ATK% > Flat ATK'
            }
        } 
    },
    'Rover': {
        'weapon': 'sword',
        'star': '5star',
        'options': [
            {'emoji': Emojis['ElementType']['havoc'], 'label': 'Havoc', 'value': 'havoc'},
            {'emoji': Emojis['ElementType']['spectro'], 'label': 'Spectro', 'value': 'spectro'}
        ],
        'details': {
            'havoc': {
                'element': 'havoc',
                'color': 'HavocColor',
                'options': [
                    {'emoji': Emojis['SonataEffects']['Sun-sinking Eclipse'],'label': 'Sun-sinking Eclipse', 'description': '[4/3/3/1/1] Best Main DPS Build'},
                    {'emoji': Emojis['SonataEffects']['Sun-sinking Eclipse'],'label': 'Alternative Sun-sinking Eclipse', 'description': '[4/4/1/1/1] Alternative Main DPS Build'}
                ],
            'details': {
            'Sun-sinking Eclipse': {
                'echo_set': f"{Emojis['SonataEffects']['Sun-sinking Eclipse']} Sun-sinking Eclipse X5",
                'main_echo': f"{Emojis['4Cost']['Dreamless']} Dreamless",
                'main_stats': [
                    f"{Emojis['StatIcons']['critrate']} `CRIT RATE`",
                    f"{Emojis['StatIcons']['critdmg']} `CRIT DMG`"
                ],
                'sub_echo1': 'Any Cost 3 Echo X2',
                'sub_stats1': [
                    f"{Emojis['StatIcons']['havocdmg']} `Havoc DMG`",
                    f"{Emojis['StatIcons']['atk']} `ATK%`"
                ],
                'sub_echo2': 'Any Cost 1 Echo X2',
                'sub_stats2': [
                    f"{Emojis['StatIcons']['atk']} `ATK%`"
                ],
                'sub_stats_priority': 'Energy Regen (Minimum) >= CRIT RATE = CRIT DMG > ATK% > Flat ATK'
            },
            'Alternative Sun-sinking Eclipse': {
                'echo_set': f"{Emojis['SonataEffects']['Sun-sinking Eclipse']} Sun-sinking Eclipse X5",
                'main_echo': f"{Emojis['4Cost']['Dreamless']} Dreamless",
                'main_stats': [
                    f"{Emojis['StatIcons']['critrate']} `CRIT RATE`",
                ],
                'sub_echo1': [f"{Emojis['4Cost']['Crownless']} Crownless"],
                'sub_stats1': [
                    f"{Emojis['StatIcons']['critdmg']} `CRIT DMG`"
                ],
                'sub_echo2': 'Any Cost 1 Echo X3',
                'sub_stats2': [
                    f"{Emojis['StatIcons']['atk']} `ATK%`"
                ],
                'sub_stats_priority': 'Energy Regen (Minimum) >= CRIT RATE = CRIT DMG > ATK% > Flat ATK'
                    }
                }
            },
            'spectro': {
                'element': 'spectro',
                'color': 'SpectroColor',
                'options': [
                    {'emoji': Emojis['SonataEffects']['Celestial Light'], 'label': 'Celestial Light', 'description': '[4/3/3/1/1] Best Main DPS Build'},
                    {'emoji': Emojis['SonataEffects']['Celestial Light'], 'label': 'Alternative Celestial Light', 'description': '[4/4/1/1/1] Alternative Main DPS Build'}
                ],
                'details': {
                    'Celestial Light': {
                        'echo_set': f"{Emojis['SonataEffects']['Celestial Light']} Celestial Light X5",
                        'main_echo': f"{Emojis['4Cost']['Mourning Aix']} Mourning Aix",
                        'main_stats': [
                            f"{Emojis['StatIcons']['critrate']} `CRIT RATE`",
                            f"{Emojis['StatIcons']['critdmg']} `CRIT DMG`"
                        ],
                        'sub_echo1': 'Any Cost 3 Echo X2',
                        'sub_stats1': [
                            f"{Emojis['StatIcons']['spectrodmg']} `Spectro DMG`",
                            f"{Emojis['StatIcons']['atk']} `ATK%`"
                        ],
                        'sub_echo2': 'Any Cost 1 Echo X2',
                        'sub_stats2': [
                            f"{Emojis['StatIcons']['atk']} `ATK%`"
                        ],
                        'sub_stats_priority': 'Energy Regen (Minimum) >= CRIT RATE = CRIT DMG > ATK% > Flat ATK'
            },
                    'Alternative Celestial Light': {
                        'echo_set': f"{Emojis['SonataEffects']['Celestial Light']} Celestial Light X5",
                        'main_echo': f"{Emojis['4Cost']['Mourning Aix']} Mourning Aix",
                        'main_stats': [
                            f"{Emojis['StatIcons']['critrate']} `CRIT RATE`",
                        ],
                        'sub_echo1': [f"{Emojis['4Cost']['Jue']} Jue"],
                        'sub_stats1': [
                            f"{Emojis['StatIcons']['critdmg']} `CRIT DMG`"
                        ],
                        'sub_echo2': 'Any Cost 1 Echo X3',
                        'sub_stats2': [
                            f"{Emojis['StatIcons']['atk']} `ATK%`"
                        ],
                        'sub_stats_priority': 'Energy Regen (Minimum) >= CRIT RATE = CRIT DMG > ATK% > > Resonance Skill DMG% > Flat ATK'
                    }
                }
            }
        }
    },
    'Sanhua': {
        'weapon': 'sword',
        'element': 'glacio',
        'color': 'GlacioColor',
        'star': '4star',
        'options': [
            {'emoji': Emojis['SonataEffects']['Moonlit Clouds'], 'label': 'Moonlit Clouds', 'description': '[4/3/3/1/1] Sub DPS Build'},
        ],
        'details': {
            'Moonlit Clouds': {
                'echo_set': f"{Emojis['SonataEffects']['Moonlit Clouds']} Moonlit Clouds X5",
                'main_echo': f"{Emojis['4Cost']['Impermanence Heron']} Impermanence Heron",
                'main_stats': [
                    f"{Emojis['StatIcons']['critrate']} `CRIT RATE`", 
                    f"{Emojis['StatIcons']['critdmg']} `CRIT DMG`"
                ],
                'sub_echo1': 'Any Cost 3 Echo X2',
                'sub_stats1': [
                    f"{Emojis['StatIcons']['glaciodmg']} `Glacio DMG`",
                    f"{Emojis['StatIcons']['energyregen']} `Energy Regen`",
                ],
                'sub_echo2': 'Any Cost 1 Echo X2',
                'sub_stats2': [
                    f"{Emojis['StatIcons']['atk']} `ATK%`"
                ],
                'sub_stats_priority': 'Energy Regen (Minimum) >= CRIT RATE = CRIT DMG > ATK% > Flat ATK'
            }
        } 
    },
    'Taoqi': {
        'weapon': 'broadblade',
        'element': 'havoc',
        'color': 'HavocColor',
        'star': '4star',
        'options': [
            {'emoji': Emojis['SonataEffects']['Moonlit Clouds'], 'label': 'Moonlit Clouds', 'description': '[4/3/3/1/1] Sub DPS Build'},
            {'emoji': Emojis['SonataEffects']['Rejuvenating Glow'], 'label': 'Rejuvenating Glow', 'description': '[4/3/3/1/1] Support Build'},
        ],
        'details': {
            'Moonlit Clouds': {
                'echo_set': f"{Emojis['SonataEffects']['Moonlit Clouds']} Moonlit Clouds X5",
                'main_echo': f"{Emojis['4Cost']['Impermanence Heron']} Impermanence Heron",
                'main_stats': [
                    f"{Emojis['StatIcons']['critrate']} `CRIT RATE`", 
                    f"{Emojis['StatIcons']['critdmg']} `CRIT DMG`"
                ],
                'sub_echo1': 'Any Cost 3 Echo X2',
                'sub_stats1': [
                    f"{Emojis['StatIcons']['energyregen']} `Energy Regen`",
                    f"{Emojis['StatIcons']['def']} `DEF%`"
                ],
                'sub_echo2': 'Any Cost 1 Echo X2',
                'sub_stats2': [
                    f"{Emojis['StatIcons']['def']} `DEF%`"
                ],
                'sub_stats_priority': 'Energy Regen (Minimum) >= CRIT RATE = CRIT DMG > DEF% > Flat DEF'
            },
            'Rejuvenating Glow': {
                'echo_set': f"{Emojis['SonataEffects']['Rejuvenating Glow']} Rejuvenating Glow X5",
                'main_echo': f"{Emojis['4Cost']['Bell-Borne Geochelone']} Bell-Borne Geochelone",
                'main_stats': [
                    f"{Emojis['StatIcons']['def']} `DEF%`"
                ],
                'sub_echo1': 'Any Cost 3 Echo X2',
                'sub_stats1': [
                    f"{Emojis['StatIcons']['energyregen']} `Energy Regen`",
                    f"{Emojis['StatIcons']['def']} `DEF%`"
                ],
                'sub_echo2': 'Any Cost 1 Echo X2',
                'sub_stats2': [
                    f"{Emojis['StatIcons']['def']} `DEF%`"
                ],
                'sub_stats_priority': 'Energy Regen (Minimum) >= CRIT RATE = CRIT DMG > DEF% > Flat DEF'
            }
        }
    },
    'Verina': {
        'weapon': 'rectifier',
        'element': 'spectro',
        'color': 'SpectroColor',
        'star': '5star',
        'options': [
            {'emoji': Emojis['SonataEffects']['Rejuvenating Glow'],'label': 'Rejuvenating Glow', 'description': '[4/3/3/1/1] Support Build'},
        ],
        'details': {
            'Rejuvenating Glow': {
                'echo_set': f"{Emojis['SonataEffects']['Rejuvenating Glow']} Rejuvenating Glow X5",
                'main_echo': f"{Emojis['4Cost']['Bell-Borne Geochelone']} Bell-Borne Geochelone",
                'main_stats': [
                    f"{Emojis['StatIcons']['healingbonus']} `Healing Bonus`",
                ],
                'sub_echo1': 'Any Cost 3 Echo X2',
                'sub_stats1': [
                    f"{Emojis['StatIcons']['energyregen']} `Energy Regen`",
                ],
                'sub_echo2': 'Any Cost 1 Echo X2',
                'sub_stats2': [
                    f"{Emojis['StatIcons']['atk']} `ATK%`"
                ],
                'sub_stats_priority': 'Energy Regen (Minimum) > ATK% > Flat ATK'
            }
        }
    },
    'Xiangli Yao': {
        'weapon': 'gauntlet',
        'element': 'electro',
        'color': 'ElectroColor',
        'star': '5star',
        'options': [
            {'emoji': Emojis['SonataEffects']['Void Thunder'], 'label': 'Void Thunder', 'description': '[4/3/3/1/1] Best Main DPS Build'},
        ],
        'details': {
            'Void Thunder': {
                'echo_set': f"{Emojis['SonataEffects']['Void Thunder']} Void Thunder X5",
                'main_echo': f"{Emojis['4Cost']['Tempest Memphis']} Placeholder",
                'main_stats': [
                    f"{Emojis['StatIcons']['critrate']} Placeholder",
                    f"{Emojis['StatIcons']['critdmg']} Placeholder"
                ],
                'sub_echo1': ['Placeholder'],
                'sub_stats1': [
                    f"{Emojis['StatIcons']['electrodmg']} Placeholder",
                    f"{Emojis['StatIcons']['atk']} Placeholder"
                ],
                'sub_echo2': ['Placeholder'],
                'sub_stats2': [
                    f"{Emojis['StatIcons']['atk']} Placeholder"
                ],
                'sub_stats_priority': 'Placeholder'
            }
        }
    },     
    'Yangyang': {
        'weapon': 'sword',
        'element': 'aero',
        'color': 'AeroColor',
        'star': '4star',
        'options': [
            {'emoji': Emojis['SonataEffects']['Moonlit Clouds'], 'label': 'Moonlit Clouds', 'description': '[4/3/3/1/1] Sub DPS Build'},
            {'emoji': Emojis['SonataEffects']['Rejuvenating Glow'], 'label': 'Rejuvenating Glow', 'description': '[4/3/3/1/1] Support Build'},
        ],
        'details': {
            'Moonlit Clouds': {
                'echo_set': f"{Emojis['SonataEffects']['Moonlit Clouds']} Moonlit Clouds X5",
                'main_echo': f"{Emojis['4Cost']['Impermanence Heron']} Impermanence Heron",
                'main_stats': [
                    f"{Emojis['StatIcons']['critrate']} `CRIT RATE`", 
                    f"{Emojis['StatIcons']['critdmg']} `CRIT DMG`"
                ],
                'sub_echo1': 'Any Cost 3 Echo X2',
                'sub_stats1': [
                    f"{Emojis['StatIcons']['energyregen']} `Energy Regen`",
                    f"{Emojis['StatIcons']['aerodmg']} `Aero DMG`"
                ],
                'sub_echo2': 'Any Cost 1 Echo X2',
                'sub_stats2': [
                    f"{Emojis['StatIcons']['atk']} `ATK%`"
                ],
                'sub_stats_priority': 'Energy Regen (Minimum) >= CRIT RATE = CRIT DMG > ATK% > Flat ATK > Liberation DMG% > Basic DMG%'
            },
            'Rejuvenating Glow': {
                'echo_set': f"{Emojis['SonataEffects']['Rejuvenating Glow']} Rejuvenating Glow X5",
                'main_echo': f"{Emojis['4Cost']['Bell-Borne Geochelone']} Bell-Borne Geochelone",
                'main_stats': [
                    f"{Emojis['StatIcons']['healingbonus']} `Healing Bonus`",
                ],
                'sub_echo1': 'Any Cost 3 Echo X2',
                'sub_stats1': [
                    f"{Emojis['StatIcons']['energyregen']} `Energy Regen`",
                ],
                'sub_echo2': 'Any Cost 1 Echo X2',
                'sub_stats2': [
                    f"{Emojis['StatIcons']['atk']} `ATK%`"
                ],
                'sub_stats_priority': 'Energy Regen (Minimum) >= CRIT RATE = CRIT DMG > ATK% > Flat ATK > Liberation DMG% > Basic DMG%'
            }
        }
    },
    'Yinlin': {
        'weapon': 'rectifier',
        'element': 'electro',
        'color': 'ElectroColor',
        'star': '5star',
        'options': [
            {'emoji': Emojis['SonataEffects']['Moonlit Clouds'], 'label': 'Moonlit Clouds', 'description': '[4/3/3/1/1] Sub DPS Build'},
            {'emoji': Emojis['SonataEffects']['Void Thunder'], 'label': 'Void Thunder', 'description': '[4/3/3/1/1] Main DPS Build'},
            {'emoji': Emojis['SonataEffects']['Void Thunder'], 'label': 'Alternative Void Thunder', 'description': '[4/4/1/1/1] Alternative Main DPS Build'}
        ],
        'details': {
            'Moonlit Clouds': {
                'echo_set': f"{Emojis['SonataEffects']['Moonlit Clouds']} Moonlit Clouds X5",
                'main_echo': f"{Emojis['4Cost']['Impermanence Heron']} Impermanence Heron",
                'main_stats': [
                    f"{Emojis['StatIcons']['critrate']} `CRIT RATE`",
                    f"{Emojis['StatIcons']['critdmg']} `CRIT DMG`"
                ],
                'sub_echo1': 'Any Cost 3 Echo X2',
                'sub_stats1': [
                    f"{Emojis['StatIcons']['energyregen']} `Energy Regen`",
                ],
                'sub_echo2': 'Any Cost 1 Echo X2',
                'sub_stats2': [
                    f"{Emojis['StatIcons']['atk']} `ATK%`"
                ],
                'sub_stats_priority': 'Energy Regen (Minimum) >= CRIT RATE = CRIT DMG > ATK% > Flat ATK'
            },
            'Void Thunder': {
                'echo_set': f"{Emojis['SonataEffects']['Void Thunder']} Void Thunder X5",
                'main_echo': f"{Emojis['4Cost']['Tempest Memphis']} Tempest Memphis",
                'main_stats': [
                    f"{Emojis['StatIcons']['critrate']} `CRIT RATE`",
                    f"{Emojis['StatIcons']['critdmg']} `CRIT DMG`"
                ],
                'sub_echo1': 'Any Cost 3 Echo X2',
                'sub_stats1': [
                    f"{Emojis['StatIcons']['electrodmg']} `Electro DMG`",
                    f"{Emojis['StatIcons']['atk']} `ATK%`"
                ],
                'sub_echo2': 'Any Cost 1 Echo X2',
                'sub_stats2': [
                    f"{Emojis['StatIcons']['atk']} `ATK%`"
                ],
                'sub_stats_priority': 'Energy Regen (Minimum) >= CRIT RATE = CRIT DMG > ATK% > Flat ATK'
            },
            'Alternative Void Thunder': {
                'echo_set': f"{Emojis['SonataEffects']['Void Thunder']} Void Thunder X5",
                'main_echo': f"{Emojis['4Cost']['Tempest Memphis']} Tempest Memphis",
                'main_stats': [
                    f"{Emojis['StatIcons']['critrate']} `CRIT RATE`",
                ],
                'sub_echo1': [f'{Emojis['4Cost']['Thundering Memphis']} Thundering Memphis'],
                'sub_stats1': [
                    f"{Emojis['StatIcons']['critdmg']} `CRIT DMG`"
                ],
                'sub_echo2': 'Any Cost 1 Echo X3',
                'sub_stats2': [
                    f"{Emojis['StatIcons']['atk']} `ATK%`"
                ],
                'sub_stats_priority': 'Energy Regen (Minimum) >= CRIT RATE = CRIT DMG > ATK% > Flat ATK'
            }
        }
    },
    'Yuanwu': {
        'weapon': 'gauntlet',
        'element': 'electro',
        'color': 'ElectroColor',
        'star': '4star',
        'options': [
            {'emoji': Emojis['SonataEffects']['Moonlit Clouds'], 'label': 'Moonlit Clouds', 'description': '[4/3/3/1/1] Sub DPS Build'},
            {'emoji': Emojis['SonataEffects']['Rejuvenating Glow'], 'label': 'Rejuvenating Glow', 'description': '[4/3/3/1/1] Support Build'},
        ],
        'details': {
            'Moonlit Clouds': {
                'echo_set': f"{Emojis['SonataEffects']['Moonlit Clouds']} Moonlit Clouds X5",
                'main_echo': f"{Emojis['4Cost']['Impermanence Heron']} Impermanence Heron",
                'main_stats': [
                    f"{Emojis['StatIcons']['critrate']} `CRIT RATE`", 
                    f"{Emojis['StatIcons']['critdmg']} `CRIT DMG`"
                ],
                'sub_echo1': 'Any Cost 3 Echo X2',
                'sub_stats1': [
                    f"{Emojis['StatIcons']['energyregen']} `Energy Regen`",
                    f"{Emojis['StatIcons']['def']} `DEF%`"
                ],
                'sub_echo2': 'Any Cost 1 Echo X2',
                'sub_stats2': [
                    f"{Emojis['StatIcons']['def']} `DEF%`"
                ],
                'sub_stats_priority': 'Energy Regen (Minimum) >= CRIT RATE = CRIT DMG > DEF% > Flat DEF'
            },
            'Rejuvenating Glow': {
                'echo_set': f"{Emojis['SonataEffects']['Rejuvenating Glow']} Rejuvenating Glow X5",
                'main_echo': f"{Emojis['4Cost']['Bell-Borne Geochelone']} Bell-Borne Geochelone",
                'main_stats': [
                    f"{Emojis['StatIcons']['healingbonus']} `Healing Bonus`",
                ],
                'sub_echo1': 'Any Cost 3 Echo X2',
                'sub_stats1': [
                    f"{Emojis['StatIcons']['energyregen']} `Energy Regen`",
                    f"{Emojis['StatIcons']['def']} `DEF%`"
                ],
                'sub_echo2': 'Any Cost 1 Echo X2',
                'sub_stats2': [
                    f"{Emojis['StatIcons']['def']} `DEF%`"
                ],
                'sub_stats_priority': 'Energy Regen (Minimum) >= CRIT RATE = CRIT DMG > DEF% > Flat DEF'
            }
        }
    },
    'Zhezhi': {
        'weapon': 'rectifier',
        'element': 'glacio',
        'color': 'GlacioColor',
        'star': '5star',
        'options': [
            {'emoji': Emojis['SonataEffects']['Freezing Frost'], 'label': 'Freezing Frost', 'description': '[4/3/3/1/1] Main Build'},
            {'emoji': Emojis['SonataEffects']['Moonlit Clouds'], 'label': 'Moonlit Clouds', 'description': '[4/3/3/1/1] Sub DPS Build'},
        ],
        'details': {
            'Freezing Frost': {
                'echo_set': f"{Emojis['SonataEffects']['Freezing Frost']} Freezing Frost X5",
                'main_echo': f"{Emojis['4Cost']['Lampylumen Myriad']} Lampylumen Myriad",
                'main_stats': [
                    f"{Emojis['StatIcons']['critdmg']} `CRIT DMG`",
                    f"{Emojis['StatIcons']['critrate']} `CRIT RATE`",
                ],
                'sub_echo1': 'Any Cost 3 Echo X2',
                'sub_stats1': [
                    f"{Emojis['StatIcons']['glaciodmg']} `Glacio DMG`",
                ],
                'sub_echo2': ['Any Cost 1 Echo X2'],
                'sub_stats2': [
                    f"{Emojis['StatIcons']['atk']} `ATK%`",
                ],
                'sub_stats_priority': '`Energy Regen (Minimum) > CRIT RATE = CRIT DMG > Basic ATK DMG% = ATK% > Flat ATK`'
            },
            'Moonlit Clouds': {
                'echo_set': f"{Emojis['SonataEffects']['Moonlit Clouds']} Moonlit Clouds X5",
                'main_echo': f"{Emojis['4Cost']['Impermanence Heron']} Impermanence Heron",
                'main_stats': [
                    f"{Emojis['StatIcons']['critdmg']} `CRIT DMG`",
                    f"{Emojis['StatIcons']['critrate']} `CRIT RATE`",
                ],
                'sub_echo1': 'Any Cost 3 Echo X2',
                'sub_stats1': [
                    f"{Emojis['StatIcons']['glaciodmg']} `Glacio DMG`",
                ],
                'sub_echo2': ['Any Cost 1 Echo X2'],
                'sub_stats2': [
                    f"{Emojis['StatIcons']['atk']} `ATK%`",
                ],
                'sub_stats_priority': '`Energy Regen (Minimum) > CRIT RATE = CRIT DMG > Basic ATK DMG% = ATK% > Flat ATK`'
            }
        }
    },
}
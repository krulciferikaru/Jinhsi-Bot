from data.Emojis import Emojis

weaponInfo = {
    'Broadblade': {
        'details': {
            'Training Broadblade': {
                'star': '1★',
                'description': 'Increases ATK by **4%/5%/6%/7%/8%**.',
                'atk': {
                    'icon': Emojis['StatIcons']['atk'], 
                    'title': 'ATK',
                    'stats': '**250**',
                },
                'mainstat': {
                    'icon': Emojis['StatIcons']['atk'],
                    'title': 'ATK%',
                    'stats': '**11.4%**'
                }
            },
            'Tyro Broadblade': {
                'star': '2★',
                'description': 'Increases ATK by **5%/6.25%/7.50%/8.75%/10%**.',
                'atk': {
                    'icon': Emojis['StatIcons']['atk'], 
                    'title': 'ATK',
                    'stats': '**275**',
                },
                'mainstat': {
                    'icon': Emojis['StatIcons']['atk'],
                    'title': 'ATK%',
                    'stats': '**14.8%**'
                }
            },
            'Beguiling Melody': {
                'star': '3★',
                'description': 'When Intro Skill is cast, restores **4/5/6/7/8** Concerto Energy. '
                               'When Outro Skill is cast, restores **4/5/6/7/8** Resonance Energy.',
                'atk': {
                    'icon': Emojis['StatIcons']['atk'], 
                    'title': 'ATK',
                    'stats': '**275**',
                },
                'mainstat': {
                    'icon': Emojis['StatIcons']['atk'],
                    'title': 'ATK%',
                    'stats': '**30.4%**'
                }
            },
            'Broadblade of Night': {
                'star': '3★',
                'description': 'When Intro Skill is cast, increases ATK by **8%/10%/12%/14%/16%**, lasting for 10s.',
                'atk': {
                    'icon': Emojis['StatIcons']['atk'], 
                    'title': 'ATK',
                    'stats': '**325**',
                },
                'mainstat': {
                    'icon': Emojis['StatIcons']['atk'],
                    'title': 'ATK%',
                    'stats': '**24.3%**'
                }
            },
            'Broadblade of Voyager': {
                'star': '3★',
                'description': 'When Resonance Skill is cast, restores Resonance Energy by **8/9/10/11/12**. ' 
                               'This effect can be triggered **1** time(s) every 20s.',
                'atk': {
                    'icon': Emojis['StatIcons']['atk'], 
                    'title': 'ATK',
                    'stats': '**300**',
                },
                'mainstat': {
                    'icon': Emojis['StatIcons']['energyregen'],
                    'title': 'Energy Regen',
                    'stats': '**32.3%**'
                }
            },
            'Guardian Broadblade': {
                'star': '3★',
                'description': 'Increases Basic Attack DMG and Heavy Attack DMG by **12%/15%/18%/21%/24%**.',
                'atk': {
                    'icon': Emojis['StatIcons']['atk'], 
                    'title': 'ATK',
                    'stats': '**325**',
                },
                'mainstat': {
                    'icon': Emojis['StatIcons']['atk'],
                    'title': 'ATK%',
                    'stats': '**24.3%**'
                }
            },
            'Originite Type I': {
                'star': '3★',
                'description': 'When Resonance Skill is cast, heals the Resonator by **3%/3.75%/4.5%/5.25%/6%** of their Max HP. ' 
                               'This effect can be triggered **1** time(s) every 12s.',
                'atk': {
                    'icon': Emojis['StatIcons']['atk'], 
                    'title': 'ATK',
                    'stats': '**300**',
                },
                'mainstat': {
                    'icon': Emojis['StatIcons']['def'],
                    'title': 'DEF%',
                    'stats': '**38.4%**'
                }
            },
            'Autumntrace': {
                'star': '4★',
                'description': 'Increases ATK by **4%/6.2%/8.4%/10.6%/12.8%** upon dealing Basic Attack DMG or Heavy Attack DMG, stacking up to **5** time(s). ' 
                               'This effect lasts for 7s and can be triggered **1** time(s) every 1s.',
                'atk': {
                    'icon': Emojis['StatIcons']['atk'], 
                    'title': 'ATK',
                    'stats': '**412**',
                },
                'mainstat': {
                    'icon': Emojis['StatIcons']['critrate'],
                    'title': 'CRIT RATE',
                    'stats': '**20.2%**'
                }
            },
            'Broadblade41': {
                'star': '4★',
                'description': "When the Resonator's HP is above **80%**, increases ATK by **12%/15%/18%/21%/24%**. "
                               "When the Resonator's HP is below **40%/50%/60%/70%/80%**, restores their HP by **5%/6.25%/7.5%/8.75%/10%** for dealing Basic Attack DMG or Heavy Attack DMG. "
                               'This effect can be triggered **1** time(s) every 8s.',
                'atk': {
                    'icon': Emojis['StatIcons']['atk'], 
                    'title': 'ATK',
                    'stats': '**412**',
                },
                'mainstat': {
                    'icon': Emojis['StatIcons']['energyregen'],
                    'title': 'Energy Regen',
                    'stats': '**32.3%**'
                }
            },
            'Dauntless Evernight': {
                'star': '4★',
                'description': "When Intro Skill is cast, increases ATK by **8%/10%/12%/14%/16%** and DEF by **15%/18.75%/22.5%/26.25%/30%**.",
                'atk': {
                    'icon': Emojis['StatIcons']['atk'], 
                    'title': 'ATK',
                    'stats': '**337**',
                },
                'mainstat': {
                    'icon': Emojis['StatIcons']['def'],
                    'title': 'DEF%',
                    'stats': '**61.5%**'
                }
            },
            'Discord': {
                'star': '4★',
                'description': "When Resonance Skill is cast, restores **8/10/12/14/16** Concerto Energy. "
                               "This effect can be triggered **1** time(s) every 20s",
                'atk': {
                    'icon': Emojis['StatIcons']['atk'], 
                    'title': 'ATK',
                    'stats': '**337**',
                },
                'mainstat': {
                    'icon': Emojis['StatIcons']['energyregen'],
                    'title': 'Energy Regen',
                    'stats': '**51.8%**'
                }
            },
            'Helios Cleaver': {
                'star': '4★',
                'description': "Within 12s after Resonance Skill is cast, increases ATK by **3%/3.75%/4.5%/5.25%/6%**, stacking up to **4** time(s). "
                               "This effect can be triggered **1** time(s) every 12s. When the number of stacks reaches **4**, all stacks will be reset within 6s",
                'atk': {
                    'icon': Emojis['StatIcons']['atk'], 
                    'title': 'ATK',
                    'stats': '**413**',
                },
                'mainstat': {
                    'icon': Emojis['StatIcons']['atk'],
                    'title': 'ATK%',
                    'stats': '**30.38%**'
                }
            },
            'Ages of Harvest': {
                'star': '5★',
                'description': "Gain **12%/15%/18%/21%/24%** Attribute DMG Bonus. "
                               "Casting Intro Skill gives the equipper Ageless Marking, which grants **24%/30%/36%/42%/48%** Resonance Skill DMG Bonus for 12s. "
                               "Casting Resonance Skill gives the equipper Ethereal Endowment, which grants **24%/30%/36%/42%/48%** Resonance Skill DMG Bonus for 12s.",
                'atk': {
                    'icon': Emojis['StatIcons']['atk'], 
                    'title': 'ATK',
                    'stats': '**587**',
                },
                'mainstat': {
                    'icon': Emojis['StatIcons']['critrate'],
                    'title': 'CRIT RATE',
                    'stats': '**24.3%**'
                }
            },
            'Lustrous Razor': {
                'star': '5★',
                'description': "Increases Energy Regen **12.8%/16%/19.2%/22.4%/25.6%**. When Resonance Skill is released, "
                               "increases Resonance Liberation DMG by **7%/8.75%/10.5%/12.5%/14%**, stacking up to **3** times. This effect lasts for 12s.",
                'atk': {
                    'icon': Emojis['StatIcons']['atk'], 
                    'title': 'ATK',
                    'stats': '**587**',
                },
                'mainstat': {
                    'icon': Emojis['StatIcons']['atk'],
                    'title': 'ATK%',
                    'stats': '**36.4%**'
                }
            },
            'Verdant Summit': {
                'star': '5★',
                'description': "Increases the DMG Bonus of all Resonance Attributes by **12%/15%/18%/21%/24%**. "
                               "Every time Intro Skill or Resonance Liberation is cast, increases Heavy Attack DMG Bonus by **24%/30%/36%/42%/48%**, "
                               "stacking up to **2** time(s). This effect lasts for 14s.",
                'atk': {
                    'icon': Emojis['StatIcons']['atk'], 
                    'title': 'ATK',
                    'stats': '**587**',
                },
                'mainstat': {
                    'icon': Emojis['StatIcons']['critdmg'],
                    'title': 'CRIT DMG',
                    'stats': '**48.6%**'
                }
            },
        }
    },
    'Gauntlet': {
        'details': {
            'Training Gauntlets': {
                'star': '1★',
                'description': 'Increases ATK by **4%/5%/6%/7%/8%**.',
                'atk': {
                    'icon': Emojis['StatIcons']['atk'], 
                    'title': 'ATK',
                    'stats': '**250**',
                },
                'mainstat': {
                    'icon': Emojis['StatIcons']['atk'],
                    'title': 'ATK%',
                    'stats': '**11.4%**'
                }
            },
            'Tyro Gauntlets': {
                'star': '2★',
                'description': 'Increases ATK by **5%/6.25%/7.50%/8.75%/10%**.',
                'atk': {
                    'icon': Emojis['StatIcons']['atk'], 
                    'title': 'ATK',
                    'stats': '**275**',
                },
                'mainstat': {
                    'icon': Emojis['StatIcons']['atk'],
                    'title': 'ATK%',
                    'stats': '**14.8%**'
                }
            },
            'Gauntlets of Night': {
                'star': '3★',
                'description': 'When Intro Skill is cast, increases ATK by **8%/10%/12%/14%/16%**, lasting for 10s.',
                'atk': {
                    'icon': Emojis['StatIcons']['atk'], 
                    'title': 'ATK',
                    'stats': '**325**',
                },
                'mainstat': {
                    'icon': Emojis['StatIcons']['atk'],
                    'title': 'ATK%',
                    'stats': '**24.3%**'
                }
            },
            'Gauntlets of Voyager': {
                'star': '3★',
                'description': 'When Resonance Skill is cast, restores Resonance Energy by **8/9/10/11/12**. ' 
                               'This effect can be triggered **1** time(s) every 20s.',
                'atk': {
                    'icon': Emojis['StatIcons']['atk'], 
                    'title': 'ATK',
                    'stats': '**325**',
                },
                'mainstat': {
                    'icon': Emojis['StatIcons']['def'],
                    'title': 'DEF%',
                    'stats': '**30.7%**'
                }
            },
            'Guardian Gauntlets': {
                'star': '3★',
                'description': 'Increases Resonance Liberation DMG Bonus by **12%/15%/18%/21%/24%**.',
                'atk': {
                    'icon': Emojis['StatIcons']['atk'], 
                    'title': 'ATK',
                    'stats': '**300**',
                },
                'mainstat': {
                    'icon': Emojis['StatIcons']['def'],
                    'title': 'DEF%',
                    'stats': '**38.4%**'
                }
            },
            'Originite Type IV': {
                'star': '3★',
                'description': 'When dealing Basic Attack DMG, heals the Resonator by **0.5%/0.65%/0.8%/0.95%/1.1%** of their Max HP. ' 
                               'This effect can be triggered **1** time(s) every 3s.',
                'atk': {
                    'icon': Emojis['StatIcons']['atk'], 
                    'title': 'ATK',
                    'stats': '**300**',
                },
                'mainstat': {
                    'icon': Emojis['StatIcons']['critdmg'],
                    'title': 'CRIT DMG',
                    'stats': '**40.5%**'
                }
            },
            'Amity Accord': {
                'star': '4★',
                'description': 'When Intro Skill is cast, increases Resonance Liberation DMG Bonus by **20%/25%/30%/35%/40%**, lasting for 15s.',
                'atk': {
                    'icon': Emojis['StatIcons']['atk'], 
                    'title': 'ATK',
                    'stats': '**337**',
                },
                'mainstat': {
                    'icon': Emojis['StatIcons']['def'],
                    'title': 'DEF',
                    'stats': '**61.5%**'
                }
            },
            'Gauntlets21D': {
                'star': '4★',
                'description': 'When the Resonator dashes or dodges, increases ATK by **8%/10%/12%/14%/16%**. '
                               'Increases Dodge Counter DMG by **50%/62.5%/75%/87.5%/100%**, lasting for 8s. When Dodge Counter is performed, heals the Resonator by **5%/6.25%/7.5%/8.75%/10%** of their Max HP. ' 
                               'This effect can be triggered **1** time(s) every 3s.',
                'atk': {
                    'icon': Emojis['StatIcons']['atk'], 
                    'title': 'ATK',
                    'stats': '**387**',
                },
                'mainstat': {
                    'icon': Emojis['StatIcons']['energyregen'],
                    'title': 'Energy Regen',
                    'stats': '**38.8%**'
                }
            },
            'Hollow Mirage': {
                'star': '4★',
                'description': 'When Resonance Liberation is released, grants 3 stack(s) of Iron Armor. '
                               'Each stack increases ATK and DEF by **3%/3.5%/4%/4.5%/5%**, stacking up to 3 time(s). '
                               'When the Resonator takes damage, reduces the number of stacks by 1.',
                'atk': {
                    'icon': Emojis['StatIcons']['atk'], 
                    'title': 'ATK',
                    'stats': '**412**',
                },
                'mainstat': {
                    'icon': Emojis['StatIcons']['atk'],
                    'title': 'ATK',
                    'stats': '**30.3%**'
                }
            },
            'Marcato': {
                'star': '4★',
                'description': 'When Resonance Skill is cast, restore **8/10/12/14/16** Concerto Energy. This effect can be triggered 1 time(s) every 20s.',
                'atk': {
                    'icon': Emojis['StatIcons']['atk'], 
                    'title': 'ATK',
                    'stats': '**337**',
                },
                'mainstat': {
                    'icon': Emojis['StatIcons']['energyregen'],
                    'title': 'Energy Regen',
                    'stats': '**51.8%**'
                }
            },
            'Stonard': {
                'star': '4★',
                'description': "When Resonance Skill is cast, increases the caster's Resonance Liberation DMG Bonus by **18%/27%/36%/45%/54%**, lasting for 15s.",
                'atk': {
                    'icon': Emojis['StatIcons']['atk'], 
                    'title': 'ATK',
                    'stats': '**412**',
                },
                'mainstat': {
                    'icon': Emojis['StatIcons']['critrate'],
                    'title': 'CRIT RATE',
                    'stats': '**20.2%**'
                }
            },
            'Abyss Surges': {
                'star': '5★',
                'description': 'Increases Energy Regen by **12.8%/16%/19.2%/22.4%/25.6%**. '
                               'When hitting a target with Resonance Skill, increases Basic Attack DMG Bonus by **10%/12.5%/15%/17.5%/20%**, lasting for 8s. '
                               'When hitting a target with Basic Attacks, increases Resonance Skill DMG Bonus by **10%/12.5%/15%/17.5%/20%**, lasting for 8s.',
                'atk': {
                    'icon': Emojis['StatIcons']['atk'], 
                    'title': 'ATK',
                    'stats': '**587**',
                },
                'mainstat': {
                    'icon': Emojis['StatIcons']['atk'],
                    'title': 'ATK%',
                    'stats': '**36.4%**'
                }
            },
            'Verity\'s Handle': {
                'star': '5★',
                'description': 'Gain **12%/15%/18%/21%/24%** Attribute DMG Bonus. When using Resonance Liberation, the wielder gains **48%/60%/72%/84%/96%** Resonance Liberation DMG Bonus for 8s. This effect can be extended by 5 seconds each time Resonance Skills are cast, up to 3 times.',
                'atk': {
                    'icon': Emojis['StatIcons']['atk'], 
                    'title': 'ATK',
                    'stats': '**588**',
                },
                'mainstat': {
                    'icon': Emojis['StatIcons']['critrate'],
                    'title': 'CRIT RATE',
                    'stats': '**24.3%**'
                }
            }
        }
    },
    'Pistols': {
        'details': {
            'Training Pistols': {
                'star': '1★',
                'description': 'Increases ATK by **4%/5%/6%/7%/8%**.',
                'atk': {
                    'icon': Emojis['StatIcons']['atk'], 
                    'title': 'ATK',
                    'stats': '**250**',
                },
                'mainstat': {
                    'icon': Emojis['StatIcons']['atk'],
                    'title': 'ATK%',
                    'stats': '**11.4%**'
                }
            },
            'Tyro Pistols': {
                'star': '2★',
                'description': 'Increases ATK by **5%/6.25%/7.50%/8.75%/10%**.',
                'atk': {
                    'icon': Emojis['StatIcons']['atk'], 
                    'title': 'ATK',
                    'stats': '**275**',
                },
                'mainstat': {
                    'icon': Emojis['StatIcons']['atk'],
                    'title': 'ATK%',
                    'stats': '**14.8%**'
                }
            },
            'Guardian Pistols': {
                'star': '3★',
                'description': 'Increases Resonance Skill DMG Bonus by **12%/15%/18%/21%/24%**.',
                'atk': {
                    'icon': Emojis['StatIcons']['atk'], 
                    'title': 'ATK',
                    'stats': '**325**',
                },
                'mainstat': {
                    'icon': Emojis['StatIcons']['atk'],
                    'title': 'ATK%',
                    'stats': '**24.3%**'
                }
            },
            'Pistols of Night': {
                'star': '3★',
                'description': 'When Intro Skill is cast, increases ATK by **8%/10%/12%/14%/16%**, lasting for 10s.',
                'atk': {
                    'icon': Emojis['StatIcons']['atk'], 
                    'title': 'ATK',
                    'stats': '**325**',
                },
                'mainstat': {
                    'icon': Emojis['StatIcons']['atk'],
                    'title': 'ATK%',
                    'stats': '**24.3%**'
                }
            },
            'Pistols of Voyager': {
                'star': '3★',
                'description': 'When Resonance Skill is cast, restores Resonance Energy by **8/9/10/11/12**. ' 
                               'This effect can be triggered **1** time(s) every 20s.',
                'atk': {
                    'icon': Emojis['StatIcons']['atk'], 
                    'title': 'ATK',
                    'stats': '**300**',
                },
                'mainstat': {
                    'icon': Emojis['StatIcons']['atk'],
                    'title': 'ATK%',
                    'stats': '**30.3%**'
                }
            },
            'Originite Type III': {
                'star': '3★',
                'description': 'When Dodge Counter is cast, heals the Resonator by **1.6%/2%/2.4%/2.8%/3.2%** of their Max HP. ' 
                               'This effect can be triggered **1** time(s) every 6s.',
                'atk': {
                    'icon': Emojis['StatIcons']['atk'], 
                    'title': 'ATK',
                    'stats': '**325**',
                },
                'mainstat': {
                    'icon': Emojis['StatIcons']['atk'],
                    'title': 'ATK%',
                    'stats': '**24.3%**'
                }
            },
            'Cadenza': {
                'star': '4★',
                'description': 'When Resonance Skill is cast, restores Concerto Energy by **8/10/12/14/16**. ' 
                               'This effect can be triggered **1** time(s) every 20s.',
                'atk': {
                    'icon': Emojis['StatIcons']['atk'], 
                    'title': 'ATK',
                    'stats': '**337**',
                },
                'mainstat': {
                    'icon': Emojis['StatIcons']['energyregen'],
                    'title': 'Energy Regen',
                    'stats': '**51.8%**'
                }
            },
            'Novaburst': {
                'star': '4★',
                'description': 'When the Resonator dashes or dodges, increases ATK by **4%/5%/6%/7%/8%**, stacking up to 3 time(s). This effect lasts for 8s.',
                'atk': {
                    'icon': Emojis['StatIcons']['atk'], 
                    'title': 'ATK',
                    'stats': '**412**',
                },
                'mainstat': {
                    'icon': Emojis['StatIcons']['atk'],
                    'title': 'ATK%',
                    'stats': '**30.3%**'
                }
            },
            'Pistols26': {
                'star': '4★',
                'description': 'When the Resonator takes no damage, increases ATK by **6%/7.5%/9%/10.5%/12%** every 5s, stacking up to 2 time(s). '
                               'This effect lasts for 8s. When the Resonator takes damage, reduces the number of stacks by 1 and restores their HP by **5%/6.25%/7.5%/8.75%/10%**.',
                'atk': {
                    'icon': Emojis['StatIcons']['atk'], 
                    'title': 'ATK',
                    'stats': '**387**',
                },
                'mainstat': {
                    'icon': Emojis['StatIcons']['atk'],
                    'title': 'ATK%',
                    'stats': '**36.4%**'
                }
            },
            'Thunderbolt': {
                'star': '4★',
                'description': 'When hitting a target with Basic Attacks or Heavy Attacks, increases Resonance Skill DMG Bonus by **7%/11%/15%/19%/23%**, stacking up to 3 time(s). '
                               'This effect lasts for 10s and can be triggered **1** time(s) every 1s',
                'atk': {
                    'icon': Emojis['StatIcons']['atk'], 
                    'title': 'ATK',
                    'stats': '**387**',
                },
                'mainstat': {
                    'icon': Emojis['StatIcons']['atk'],
                    'title': 'ATK%',
                    'stats': '**36.4%**'
                }
            },
            'Undying Flame': {
                'star': '4★',
                'description': 'When Intro Skill is released, increases Resonance Skill DMG Bonus by **20%/25%/30%/35%/40%** for 15s.' ,
                'atk': {
                    'icon': Emojis['StatIcons']['atk'], 
                    'title': 'ATK',
                    'stats': '**412**',
                },
                'mainstat': {
                    'icon': Emojis['StatIcons']['atk'],
                    'title': 'ATK%',
                    'stats': '**30.3%**'
                }
            },
            'Static Mist': {
                'star': '5★',
                'description': "Increases Energy Regen by **12.8%/16%/19.2%/22.4%/25.6%**. "
                               "When Outro Skill is released, increases the switched-in Resonator's ATK by **10%/12.5%/15%/17.5%/20%**, stacking up to 1 time(s). "
                               "This effect lasts for 14s.",
                'atk': {
                    'icon': Emojis['StatIcons']['atk'], 
                    'title': 'ATK',
                    'stats': '**587**',
                },
                'mainstat': {
                    'icon': Emojis['StatIcons']['critrate'],
                    'title': 'CRIT RATE',
                    'stats': '**24.3%**'
                }
            }
        }
    },
    'Rectifier': {
        'details': {
            'Training Rectifier': {
                'star': '1★',
                'description': 'Increases ATK by **4%/5%/6%/7%/8%**.',
                'atk': {
                    'icon': Emojis['StatIcons']['atk'], 
                    'title': 'ATK',
                    'stats': '**250**',
                },
                'mainstat': {
                    'icon': Emojis['StatIcons']['atk'],
                    'title': 'ATK%',
                    'stats': '**11.4%**'
                }
            },
            'Tyro Rectifier': {
                'star': '2★',
                'description': 'Increases ATK by **5%/6.25%/7.50%/8.75%/10%**.',
                'atk': {
                    'icon': Emojis['StatIcons']['atk'], 
                    'title': 'ATK',
                    'stats': '**275**',
                },
                'mainstat': {
                    'icon': Emojis['StatIcons']['atk'],
                    'title': 'ATK%',
                    'stats': '**14.8%**'
                }
            },
            'Guardian Rectifier': {
                'star': '3★',
                'description': 'Increases Basic Attack and Heavy Attack DMG Bonus by **12%/15%/18%/21%/24%**.',
                'atk': {
                    'icon': Emojis['StatIcons']['atk'], 
                    'title': 'ATK',
                    'stats': '**325**',
                },
                'mainstat': {
                    'icon': Emojis['StatIcons']['atk'],
                    'title': 'ATK%',
                    'stats': '**24.3%**'
                }
            },
            'Originite Type V': {
                'star': '3★',
                'description': 'When Intro Skill is cast, heals the Resonator by **5%/6.25%/7.5%/8.75%/10%** of their Max HP. ' 
                               'This effect can be triggered **1** time(s) every 20s.',
                'atk': {
                    'icon': Emojis['StatIcons']['atk'], 
                    'title': 'ATK',
                    'stats': '**300**',
                },
                'mainstat': {
                    'icon': Emojis['StatIcons']['atk'],
                    'title': 'ATK%',
                    'stats': '**30.3%**'
                }
            },
            'Rectifier of Night': {
                'star': '3★',
                'description': 'When Intro Skill is cast, increases ATK by **8%/10%/12%/14%/16%**, lasting for 10s.',
                'atk': {
                    'icon': Emojis['StatIcons']['atk'], 
                    'title': 'ATK',
                    'stats': '**325**',
                },
                'mainstat': {
                    'icon': Emojis['StatIcons']['atk'],
                    'title': 'ATK%',
                    'stats': '**24.3%**'
                }
            },
            'Rectifier of Voyager': {
                'star': '3★',
                'description': 'When Resonance Skill is cast, restores Resonance Energy by **8/9/10/11/12**. ' 
                               'This effect can be triggered **1** time(s) every 20s.',
                'atk': {
                    'icon': Emojis['StatIcons']['atk'], 
                    'title': 'ATK',
                    'stats': '**300**',
                },
                'mainstat': {
                    'icon': Emojis['StatIcons']['energyregen'],
                    'title': 'Energy Regen',
                    'stats': '**32.3%**'
                }
            },
            'Augment': {
                'star': '4★',
                'description': "When Resonance Liberation is released, increases the caster's ATK by **15%/23.5%/31.5%/39.75%/48%**, lasting for 15s." ,
                'atk': {
                    'icon': Emojis['StatIcons']['atk'], 
                    'title': 'ATK',
                    'stats': '**412**',
                },
                'mainstat': {
                    'icon': Emojis['StatIcons']['critrate'],
                    'title': 'CRIT RATE',
                    'stats': '**20.2%**'
                }
            },
            'Comet Flare': {
                'star': '4★',
                'description': 'When hitting a target with Basic Attacks or Heavy Attacks, increases Healing Bonus by **3%/3.5%/4%/4.5%/5%**, stacking up to 3 time(s). '
                               'This effect lasts for 8s and can be triggered **1** time(s) every 0.6s.',
                'atk': {
                    'icon': Emojis['StatIcons']['atk'], 
                    'title': 'ATK',
                    'stats': '**412**',
                },
                'mainstat': {
                    'icon': Emojis['StatIcons']['hp'],
                    'title': 'HP%',
                    'stats': '**30.3%**'
                }
            },
            'Jinzhou Keeper': {
                'star': '4★',
                'description': "When Intro Skill is released, increases the caster's ATK by **8%/10%/12%/14%/16%** and HP by **10%/12.5%/15%/17.5%/20%**, lasting for 15s.",
                'atk': {
                    'icon': Emojis['StatIcons']['atk'], 
                    'title': 'ATK',
                    'stats': '**387**',
                },
                'mainstat': {
                    'icon': Emojis['StatIcons']['atk'],
                    'title': 'ATK%',
                    'stats': '**36.4%**'
                }
            },
            'Rectifier25': {
                'star': '4★',
                'description': "When Resonance Skill is released, if the Resonator's HP is below 60%, restores their HP by **5%/6.25%/7.5%/8.75%/10%**. "
                               "This effect can be triggered **1** time(s) every 8s; if the Resonator's HP is above 60%, increases ATK by **12%/15%/18%/21%/24%**, lasting for 10s.",
                'atk': {
                    'icon': Emojis['StatIcons']['atk'], 
                    'title': 'ATK',
                    'stats': '**387**',
                },
                'mainstat': {
                    'icon': Emojis['StatIcons']['atk'],
                    'title': 'ATK%',
                    'stats': '**36.4%**'
                }
            },
            'Variation': {
                'star': '4★',
                'description': 'When Resonance Skill is cast, restores Resonance Energy by **8/9/10/11/12**. ' 
                               'This effect can be triggered **1** time(s) every 20s.',
                'atk': {
                    'icon': Emojis['StatIcons']['atk'], 
                    'title': 'ATK',
                    'stats': '**337**',
                },
                'mainstat': {
                    'icon': Emojis['StatIcons']['energyregen'],
                    'title': 'Energy Regen',
                    'stats': '**51.8%**'
                }
            },
            'Cosmic Ripples': {
                'star': '5★',
                'description': "Increases Energy Regen by **12.8%/16%/19.2%/22.4%/25.6%**. "
                               "When hitting a target with Basic Attacks, increases Basic Attack DMG Bonus by **3.2%/4%/4.8%/5.6%/6.4%**, stacking up to 5 time(s). "
                               "This effect lasts for 8s and can be triggered **1** time(s) every 0.5s.",
                'atk': {
                    'icon': Emojis['StatIcons']['atk'], 
                    'title': 'ATK',
                    'stats': '**500**',
                },
                'mainstat': {
                    'icon': Emojis['StatIcons']['atk'],
                    'title': 'ATK',
                    'stats': '**54%**'
                }
            },
            'Stringmaster': {
                'star': '5★',
                'description': "Increases the DMG Bonus by **12%/15%/18%/21%/24%**. "
                               "When dealing Resonance Skill DMG, increases ATK by **12%/15%/18%/21%/24%**, stacking up to 2. "
                               "This effect lasts for 5s. When the equipped Resonator is not on the field, increases their ATK by an additional **12%/15%/18%/21%/24%**.",
                'atk': {
                    'icon': Emojis['StatIcons']['atk'], 
                    'title': 'ATK',
                    'stats': '**500**',
                },
                'mainstat': {
                    'icon': Emojis['StatIcons']['critrate'],
                    'title': 'CRIT RATE',
                    'stats': '**36%**'
                }
            },
            'Rime-Draped Sprouts': {
                'star': '5★',
                'description': 'Increases ATK by **12%/15%/18%/21%/24%**. Using Resonance Skill gives the equipped Resonator **12%/15%/18%/21%/24%** Basic Attack DMG Bonus for 6s, stacking up to 3 times. When casting Outro Skill with 3 stacks, consume all stacks to give **52%/65%/78%/91%/104%** Resonance DMG Bonus to the off-field Basic Attacks performed by the equipped Resonator, lasting for 27s.',
                'atk': {
                    'icon': Emojis['StatIcons']['atk'], 
                    'title': 'ATK',
                    'stats': '**500**',
                },
                'mainstat': {
                    'icon': Emojis['StatIcons']['critdmg'],
                    'title': 'CRIT DMG',
                    'stats': '**72%**'
                }
            }, 
        }
    },
    'Sword': {
        'details': {
            'Training Sword': {
                'star': '1★',
                'description': 'Increases ATK by **4%/5%/6%/7%/8%**.',
                'atk': {
                    'icon': Emojis['StatIcons']['atk'], 
                    'title': 'ATK',
                    'stats': '**250**',
                },
                'mainstat': {
                    'icon': Emojis['StatIcons']['atk'],
                    'title': 'ATK%',
                    'stats': '**11.4%**'
                }
            },
            'Tyro Sword': {
                'star': '2★',
                'description': 'Increases ATK by **5%/6.25%/7.50%/8.75%/10%**.',
                'atk': {
                    'icon': Emojis['StatIcons']['atk'], 
                    'title': 'ATK',
                    'stats': '**275**',
                },
                'mainstat': {
                    'icon': Emojis['StatIcons']['atk'],
                    'title': 'ATK%',
                    'stats': '**14.8%**'
                }
            },
            'Guardian Sword': {
                'star': '3★',
                'description': 'Increases Resonance Skill DMG Bonus by **12%/15%/18%/21%/24%**.',
                'atk': {
                    'icon': Emojis['StatIcons']['atk'], 
                    'title': 'ATK',
                    'stats': '**300**',
                },
                'mainstat': {
                    'icon': Emojis['StatIcons']['atk'],
                    'title': 'ATK%',
                    'stats': '**30.3%**'
                }
            },
            'Sword of Night': {
                'star': '3★',
                'description': 'When Intro Skill is cast, increases ATK by **8%/10%/12%/14%/16%**, lasting for 10s.',
                'atk': {
                    'icon': Emojis['StatIcons']['atk'], 
                    'title': 'ATK',
                    'stats': '**325**',
                },
                'mainstat': {
                    'icon': Emojis['StatIcons']['atk'],
                    'title': 'ATK%',
                    'stats': '**24.3%**'
                }
            },
            'Sword of Voyager': {
                'star': '3★',
                'description': 'When Resonance Skill is cast, restores Resonance Energy by **8/9/10/11/12**. ' 
                               'This effect can be triggered **1** time(s) every 20s.',
                'atk': {
                    'icon': Emojis['StatIcons']['atk'], 
                    'title': 'ATK',
                    'stats': '**300**',
                },
                'mainstat': {
                    'icon': Emojis['StatIcons']['energyregen'],
                    'title': 'Energy Regen',
                    'stats': '**32.3%**'
                }
            },
            'Originite Type II': {
                'star': '3★',
                'description': 'When Resonance Liberation is cast, heals the Resonator by **5%/6.25%/7.5%/8.75%/10%** of their Max HP. ' 
                               'This effect can be triggered **1** time(s) every 20s.',
                'atk': {
                    'icon': Emojis['StatIcons']['atk'], 
                    'title': 'ATK',
                    'stats': '**325**',
                },
                'mainstat': {
                    'icon': Emojis['StatIcons']['atk'],
                    'title': 'ATK%',
                    'stats': '**24.3%**'
                }
            },
            'Commando of Conviction': {
                'star': '4★',
                'description': 'When Intro Skill is released, increases ATK by **15%/18.75%/22.5%/26.5%/30%**, lasting for 15s.',
                'atk': {
                    'icon': Emojis['StatIcons']['atk'], 
                    'title': 'ATK',
                    'stats': '**412**',
                },
                'mainstat': {
                    'icon': Emojis['StatIcons']['atk'],
                    'title': 'ATK%',
                    'stats': '**30.3%**'
                }
            },
            'Lumingloss': {
                'star': '4★',
                'description': "When Resonance Skill is released, increases Basic Attack DMG and Heavy Attack DMG by **20%/31%/42%/53%/64%**, stacking up to 1 time(s). "
                               "This effect lasts for 10s and can be triggered **1** time(s) every 1s.",
                'atk': {
                    'icon': Emojis['StatIcons']['atk'], 
                    'title': 'ATK',
                    'stats': '**387**',
                },
                'mainstat': {
                    'icon': Emojis['StatIcons']['atk'],
                    'title': 'ATK%',
                    'stats': '**36.4%**'
                }
            },
            'Lunar Cutter': {
                'star': '4★',
                'description': "Equipped Resonator gains 6 stack(s) of Oath upon entering the battlefield. Each stack increases ATK by **2%/2.5%/3%/3.5%/4%**, up to 6 stacks. "
                               "This effect can be triggered 1 time(s) every 12s. Oath reduces by 1 stack(s) every 2s. "
                               "Equipped Resonator gains an additional **6** stack(s) of Oath upon defeating an enemy.",
                'atk': {
                    'icon': Emojis['StatIcons']['atk'], 
                    'title': 'ATK',
                    'stats': '**412**',
                },
                'mainstat': {
                    'icon': Emojis['StatIcons']['atk'],
                    'title': 'ATK%',
                    'stats': '**30.3%**'
                }
            },
            'Scale Slasher': {
                'star': '4★',
                'description': 'When Resonance Skill is released, restores Concerto Energy by 8/10/12/14/16. This effect can be triggered **1** time(s) every 20s.',
                'atk': {
                    'icon': Emojis['StatIcons']['atk'], 
                    'title': 'ATK',
                    'stats': '**337**',
                },
                'mainstat': {
                    'icon': Emojis['StatIcons']['energyregen'],
                    'title': 'Energy Regen',
                    'stats': '**51.8%**'
                }
            },
            'Sword18': {
                'star': '4★',
                'description': "When Equipped Resonator's HP drops below **40%/50%/60%/70%/80%**, "
                               "increases Heavy Attack DMG by **18%/22.5%/27%/31.5%/36%** and restores HP by **5%/6.25%/7.5%/8.75%/10%** upon dealing Heavy Attack DMG. "
                               "This effect can be triggered **1** time(s) every 8s.",
                'atk': {
                    'icon': Emojis['StatIcons']['atk'], 
                    'title': 'ATK',
                    'stats': '**387**',
                },
                'mainstat': {
                    'icon': Emojis['StatIcons']['atk'],
                    'title': 'ATK%',
                    'stats': '**36.4%**'
                }
            },
            'Blazing Brilliance': {
                'star': '5★',
                'description': "ATK increased by **12%/15%/18%/21%/24%**. The equipper gains 1 stack of Searing Feather upon dealing damage, "
                               "which can be triggered once every 0.5s, and gains 5 stacks of the same effect upon casting Resonance Skill. "
                               "Each stack of Searing Feather gives **4%/5%/6%/7%/8%** additional Resonance Skill DMG Bonus for up to 14 stacks. "
                               "All stacks will be removed within 12s after reaching the max stack.",
                'atk': {
                    'icon': Emojis['StatIcons']['atk'], 
                    'title': 'ATK',
                    'stats': '**587**',
                },
                'mainstat': {
                    'icon': Emojis['StatIcons']['critdmg'],
                    'title': 'CRIT DMG',
                    'stats': '**48.6%**'
                }
            },
            'Emerald of Genesis': {
                'star': '5★',
                'description': 'Increases Energy Regen by **12.8%/16%/19.2%/22.4%/25.6%**. When Resonance Skill is released, increases ATK by **6%/7.5%/9%/10.5%/12%**, stacking up to 2 time(s). '
                               'This effect lasts for 10s.',
                'atk': {
                    'icon': Emojis['StatIcons']['atk'], 
                    'title': 'ATK',
                    'stats': '**587**',
                },
                'mainstat': {
                    'icon': Emojis['StatIcons']['critrate'],
                    'title': 'CRIT RATE',
                    'stats': '**24.3%**'
                }
            }
        }
    }
}
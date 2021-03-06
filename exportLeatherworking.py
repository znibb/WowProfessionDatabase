#!/usr/bin/env python3.7

recipes = {
	"Barbaric Belt": {
        "ID":       4264,
        "Learn":    200,
        "Yellow":   220,
        "Green":    230,
        "Grey":     240,
        "Source":   "Drop",
        "RecipeID": 4301,
        "Reagents": {
			"Heavy Leather": 6,
			"Cured Heavy Hide": 2,
			"Coarse Gorilla Hair": 2,
			"Great Rage Potion": 1,
			"Silken Thread":  1,
			"Iron Buckle": 1
        }
    },
    "Barbaric Bracers": {
        "ID":       18948,
        "Learn":    155,
        "Yellow":   175,
        "Green":    185,
        "Grey":     195,
        "Source":   "Vendor",
        "RecipeID": 18949,
        "Reagents": {
			"Heavy Leather": 8,
			"Cured Heavy Hide": 2,
			"Small Lustrous Pearl": 4,
			"Raptor Hide": 1,
			"Large Fang": 4
        }
    },
    "Barbaric Gloves": {
        "ID":       4254,
        "Learn":    150,
        "Yellow":   170,
        "Green":    180,
        "Grey":     190,
        "Source":   "Drop",
        "RecipeID": 4297,
        "Reagents": {
			"Heavy Leather": 6,
			"Large Fang": 2,
			"Fine Thread": 1
        }
    },
    "Barbaric Harness": {
        "ID":       5739,
        "Learn":    190,
        "Yellow":   210,
        "Green":    220,
        "Grey":     230,
        "Source":   "Trainer",
        "Reagents": {
			"Heavy Leather": 14,
			"Fine Thread": 2,
			"Iron Buckle": 1
        }
    },
    "Barbaric Leggings": {
        "ID":       5963,
        "Learn":    170,
        "Yellow":   190,
        "Green":    200,
        "Grey":     210,
        "Source":   "VendorLimited",
        "RecipeID": 5973,
        "Reagents": {
			"Heavy Leather": 10,
			"Fine Thread": 2,
			"Moss Agate": 1
        }
    },
    "Barbaric Shoulders": {
        "ID":       5964,
        "Learn":    175,
        "Yellow":   195,
        "Green":    205,
        "Grey":     215,
        "Source":   "Trainer",
        "Reagents": {
			"Heavy Leather": 8,
			"Cured Heavy Hide": 1,
			"Fine Thread": 2
        }
    },
    "Big Voodoo Cloak": {
        "ID":       8216,
        "Learn":    240,
        "Yellow":   260,
        "Green":    270,
        "Grey":     280,
        "Source":   "Drop",
        "RecipeID": 8390,
        "Reagents": {
			"Thick Leather": 14,
			"Flask of Big Mojo": 4,
			"Heavy Silken Thread": 2
        }
    },
    "Big Voodoo Mask": {
        "ID":       8201,
        "Learn":    220,
        "Yellow":   240,
        "Green":    250,
        "Grey":     260,
        "Source":   "Drop",
        "RecipeID": 8387,
        "Reagents": {
			"Thick Leather": 8,
			"Flask of Mojo": 6,
			"Heavy Silken Thread": 1
        }
    },
    "Big Voodoo Pants": {
        "ID":       8202,
        "Learn":    240,
        "Yellow":   260,
        "Green":    270,
        "Grey":     280,
        "Source":   "Drop",
        "RecipeID": 8389,
        "Reagents": {
			"Thick Leather": 10,
			"Flask of Big Mojo": 6,
			"Heavy Silken Thread": 2
        }
    },
    "Big Voodoo Robe": {
        "ID":       8200,
        "Learn":    215,
        "Yellow":   235,
        "Green":    245,
        "Grey":     255,
        "Source":   "Drop",
        "RecipeID": 8386,
        "Reagents": {
			"Thick Leather": 10,
			"Flask of Mojo": 4,
			"Heavy Silken Thread": 1
        }
    },
    "Black Dragonscale Breastplate": {
        "ID":       15050,
        "Learn":    290,
        "Yellow":   310,
        "Green":    320,
        "Grey":     330,
        "Source":   "Vendor",
		"School":	"Dragonscale",
        "RecipeID": 15759,
        "Reagents": {
			"Rugged Leather": 40,
			"Black Dragonscale": 60,
			"Cured Rugged Hide": 1,
			"Rune Thread": 2
        }
    },
    "Black Whelp Cloak": {
        "ID":       7283,
        "Learn":    100,
        "Yellow":   125,
        "Green":    137,
        "Grey":     150,
        "Source":   "Vendor",
		"Faction":	"Alliance",
        "RecipeID": 7289,
        "Reagents": {
			"Black Whelp Scale": 12,
			"Medium Leather": 4,
			"Fine Thread": 1
        }
    },
    "Black Whelp Tunic": {
        "ID":       20575,
        "Learn":    100,
        "Yellow":   125,
        "Green":    137,
        "Grey":     150,
        "Source":   "VendorLimited",
		"Faction":	"Alliance",
        "RecipeID": 20576,
        "Reagents": {
			"Medium Leather": 8,
			"Black Whelp Scale": 8,
			"Cured Light Hide": 1,
			"Fine Thread": 2
        }
    },
    "Blue Dragonscale Breastplate": {
        "ID":       15048,
        "Learn":    285,
        "Yellow":   305,
        "Green":    315,
        "Grey":     325,
        "Source":   "Vendor",
        "School":   "Dragonscale",
        "RecipeID": 15751,
        "Reagents": {
			"Rugged Leather": 28,
			"Blue Dragonscale": 30,
			"Cured Rugged Hide": 1,
			"Rune Thread": 1
        }
    },
    "Blue Dragonscale Shoulders": {
        "ID":       15049,
        "Learn":    295,
        "Yellow":   315,
        "Green":    325,
        "Grey":     335,
        "Source":   "Drop",
        "RecipeID": 15763,
        "School":   "Dragonscale",
        "Reagents": {
			"Rugged Leather": 28,
			"Blue Dragonscale": 30,
			"Enchanted Leather": 2,
			"Cured Rugged Hide": 1,
			"Rune Thread": 1
        }
    },
    "Chimeric Boots": {
        "ID":       15073,
        "Learn":    275,
        "Yellow":   295,
        "Green":    305,
        "Grey":     315,
        "Source":   "Drop",
        "RecipeID": 15737,
        "School":   "Tribal",
        "Reagents": {
			"Rugged Leather": 4,
			"Chimera Leather": 8,
			"Rune Thread": 1
        }
    },
    "Chimeric Gloves": {
        "ID":       15074,
        "Learn":    265,
        "Yellow":   285,
        "Green":    295,
        "Grey":     305,
        "Source":   "Vendor",
        "School":   "Tribal",
        "RecipeID": 15729,
        "Reagents": {
			"Rugged Leather": 6,
			"Chimera Leather": 6,
			"Rune Thread": 1
        }
    },
    "Chimeric Leggings": {
        "ID":       15072,
        "Learn":    280,
        "Yellow":   300,
        "Green":    310,
        "Grey":     320,
        "Source":   "Drop",
        "RecipeID": 15746,
        "School":   "Tribal",
        "Reagents": {
			"Rugged Leather": 8,
			"Chimera Leather": 8,
			"Rune Thread": 1
        }
    },
    "Chimeric Vest": {
        "ID":       15075,
        "Learn":    290,
        "Yellow":   310,
        "Green":    320,
        "Grey":     330,
        "Source":   "Drop",
        "RecipeID": 15755,
        "School":   "Tribal",
        "Reagents": {
			"Rugged Leather": 10,
			"Chimera Leather": 10,
			"Rune Thread": 1
        }
    },
    "Comfortable Leather Hat": {
        "ID":       8174,
        "Learn":    200,
        "Yellow":   220,
        "Green":    230,
        "Grey":     240,
        "Source":   "Drop",
        "RecipeID": 8384,
        "Reagents": {
			"Heavy Leather": 12,
			"Cured Heavy Hide": 2,
			"Silken Thread": 2
        }
    },
    "Corehound Boots": {
        "ID":       16982,
        "Learn":    295,
        "Yellow":   315,
        "Green":    325,
        "Grey":     335,
        "Source":   "Reputation",
        "School":   "Tribal",
        "RecipeID": 17022,
        "Reagents": {
			"Core Leather": 20,
			"Fiery Core": 6,
			"Lava Core": 2,
			"Rune Thread": 2
        }
    },
    "Cured Heavy Hide": {
        "ID":       4236,
        "Learn":    150,
        "Yellow":   160,
        "Green":    165,
        "Grey":     170,
        "Source":   "Trainer",
        "Reagents": {
			"Heavy Hide": 1,
			"Salt": 3
        }
    },
    "Cured Light Hide": {
        "ID":       4231,
        "Learn":    35,
        "Yellow":   55,
        "Green":    65,
        "Grey":     75,
        "Source":   "Trainer",
        "Reagents": {
			"Light Hide": 1,
			"Salt": 1
        }
    },
    "Cured Medium Hide": {
        "ID":       4233,
        "Learn":    100,
        "Yellow":   115,
        "Green":    122,
        "Grey":     130,
        "Source":   "Trainer",
        "Reagents": {
			"Medium Hide": 1,
			"Salt": 1
        }
    },
    "Cured Rugged Hide": {
        "ID":       15407,
        "Learn":    250,
        "Yellow":   250,
        "Green":    255,
        "Grey":     260,
        "Source":   "Trainer",
        "Reagents": {
			"Rugged Hide": 1,
			"Refined Deeprock Salt": 1
        }
    },
    "Cured Thick Hide": {
        "ID":       8172,
        "Learn":    200,
        "Yellow":   200,
        "Green":    200,
        "Grey":     200,
        "Source":   "Trainer",
        "Reagents": {
			"Thick Hide": 1,
			"Deeprock Salt": 1
        }
    },
    "Dark Leather Belt": {
        "ID":       4249,
        "Learn":    125,
        "Yellow":   150,
        "Green":    162,
        "Grey":     175,
        "Source":   "Trainer",
        "Reagents": {
			"Fine Leather Belt": 1,
			"Cured Medium Hide": 1,
			"Fine Thread": 2,
			"Gray Dye": 1
        }
    },
    "Dark Leather Boots": {
        "ID":       2315,
        "Learn":    100,
        "Yellow":   125,
        "Green":    137,
        "Grey":     150,
        "Source":   "Trainer",
        "Reagents": {
			"Medium Leather": 4,
			"Fine Thread": 2,
			"Gray Dye": 1
        }
    },
    "Dark Leather Cloak": {
        "ID":       2316,
        "Learn":    110,
        "Yellow":   135,
        "Green":    147,
        "Grey":     160,
        "Source":   "Trainer",
        "Reagents": {
			"Medium Leather": 8,
			"Fine Thread": 1,
			"Gray Dye": 1
        }
    },
    "Dark Leather Gloves": {
        "ID":       4248,
        "Learn":    120,
        "Yellow":   155,
        "Green":    167,
        "Grey":     180,
        "Source":   "Drop",
        "RecipeID": 7360,
        "Reagents": {
			"Fine Leather Gloves": 1,
			"Cured Medium Hide": 1,
			"Fine Thread": 1,
			"Gray Dye": 1
        }
    },
    "Dark Leather Pants": {
        "ID":       5961,
        "Learn":    115,
        "Yellow":   140,
        "Green":    152,
        "Grey":     165,
        "Source":   "Trainer",
        "Reagents": {
			"Medium Leather": 12,
			"Gray Dye": 1,
			"Fine Thread": 1
        }
    },
    "Dark Leather Shoulders": {
        "ID":       4252,
        "Learn":    140,
        "Yellow":   165,
        "Green":    177,
        "Grey":     190,
        "Source":   "Drop",
        "RecipeID": 4296,
        "Reagents": {
			"Medium Leather": 12,
			"Elixir of Lesser Agility": 1,
			"Gray Dye": 1,
			"Fine Thread": 2
        }
    },
    "Dark Leather Tunic": {
        "ID":       2317,
        "Learn":    100,
        "Yellow":   125,
        "Green":    137,
        "Grey":     150,
        "Source":   "Drop",
        "RecipeID": 2409,
        "Reagents": {
			"Medium Leather": 6,
			"Fine Thread": 1,
			"Gray Dye": 1
        }
    },
    "Dawn Treaders": {
        "ID":       19052,
        "Learn":    290,
        "Yellow":   310,
        "Green":    320,
        "Grey":     330,
        "Source":   "Reputation",
        "RecipeID": 19328,
        "Reagents": {
			"Rugged Leather": 30,
			"Guardian Stone": 2,
			"Essence of Water": 4,
			"Cured Rugged Hide": 2,
			"Rune Thread": 2
        }
    },
    "Deviate Scale Belt": {
        "ID":       6468,
        "Learn":    115,
        "Yellow":   140,
        "Green":    152,
        "Grey":     165,
        "Source":   "Quest",
		"Faction":	"Any",
        "RecipeID": 6476,
        "Reagents": {
			"Perfect Deviate Scale": 10,
			"Deviate Scale": 10,
			"Fine Thread": 2
        }
    },
    "Deviate Scale Cloak": {
        "ID":       6466,
        "Learn":    90,
        "Yellow":   120,
        "Green":    135,
        "Grey":     150,
        "Source":   "Vendor",
        "RecipeID": 6474,
        "Reagents": {
			"Deviate Scale": 8,
			"Cured Light Hide": 1,
			"Fine Thread": 1
        }
    },
    "Deviate Scale Gloves": {
        "ID":       6467,
        "Learn":    105,
        "Yellow":   130,
        "Green":    142,
        "Grey":     155,
        "Source":   "Vendor",
        "RecipeID": 6475,
        "Reagents": {
			"Perfect Deviate Scale": 2,
			"Deviate Scale": 6,
			"Fine Thread": 2
        }
    },
    "Devilsaur Gauntlets": {
        "ID":       15063,
        "Learn":    290,
        "Yellow":   310,
        "Green":    320,
        "Grey":     330,
        "Source":   "Vendor",
        "School":   "Tribal",
        "RecipeID": 15758,
        "Reagents": {
			"Rugged Leather": 30,
			"Devilsaur Leather": 8,
			"Rune Thread": 1
        }
    },
    "Dragonscale Breastplate": {
        "ID":       8367,
        "Learn":    255,
        "Yellow":   275,
        "Green":    285,
        "Grey":     295,
        "Source":   "Trainer",
        "School":   "Dragonscale",
        "Reagents": {
			"Thick Leather": 40,
			"Worn Dragonscale": 30,
			"Heavy Silken Thread": 4,
			"Cured Thick Hide": 4
        }
    },
    "Dragonscale Gauntlets": {
        "ID":       8347,
        "Learn":    225,
        "Yellow":   245,
        "Green":    255,
        "Grey":     265,
        "Source":   "Trainer",
        "School":   "Dragonscale",
        "Reagents": {
			"Thick Leather": 24,
			"Worn Dragonscale": 12,
			"Heavy Silken Thread": 4,
			"Cured Thick Hide": 2
        }
    },
    "Dusky Belt": {
        "ID":       7387,
        "Learn":    195,
        "Yellow":   215,
        "Green":    225,
        "Grey":     235,
        "Source":   "Trainer",
        "Reagents": {
			"Heavy Leather": 10,
			"Bolt of Silk Cloth": 2,
			"Black Dye": 2,
			"Iron Buckle": 1
        }
    },
    "Dusky Boots": {
        "ID":       7390,
        "Learn":    200,
        "Yellow":   220,
        "Green":    230,
        "Grey":     240,
        "Source":   "Drop",
        "RecipeID": 7452,
        "Reagents": {
			"Heavy Leather": 8,
			"Shadowcat Hide": 2,
			"Shadow Oil": 1,
			"Silken Thread": 2
        }
    },
    "Dusky Bracers": {
        "ID":       7378,
        "Learn":    185,
        "Yellow":   205,
        "Green":    215,
        "Grey":     225,
        "Source":   "Trainer",
        "Reagents": {
			"Heavy Leather": 16,
			"Black Dye": 1,
			"Silken Thread": 2
        }
    },
    "Dusky Leather Armor": {
        "ID":       7374,
        "Learn":    175,
        "Yellow":   195,
        "Green":    205,
        "Grey":     215,
        "Source":   "Trainer",
        "Reagents": {
			"Heavy Leather": 10,
			"Shadow Oil": 1,
			"Fine Thread": 2
        }
    },
    "Dusky Leather Leggings": {
        "ID":       7373,
        "Learn":    165,
        "Yellow":   185,
        "Green":    195,
        "Grey":     205,
        "Source":   "Drop",
        "RecipeID": 7449,
        "Reagents": {
			"Heavy Leather": 10,
			"Black Dye": 1,
			"Fine Thread": 2
        }
    },
    "Earthen Leather Shoulders": {
        "ID":       7352,
        "Learn":    135,
        "Yellow":   160,
        "Green":    172,
        "Grey":     185,
        "Source":   "Vendor",
        "RecipeID": 7362,
        "Reagents": {
			"Medium Leather": 6,
			"Elemental Earth": 1,
			"Fine Thread": 2
        }
    },
    "Embossed Leather Boots": {
        "ID":       2309,
        "Learn":    55,
        "Yellow":   85,
        "Green":    100,
        "Grey":     115,
        "Source":   "Trainer",
        "Reagents": {
			"Light Leather": 8,
			"Coarse Thread": 5
        }
    },
    "Embossed Leather Cloak": {
        "ID":       2310,
        "Learn":    60,
        "Yellow":   90,
        "Green":    105,
        "Grey":     120,
        "Source":   "Trainer",
        "Reagents": {
			"Light Leather": 5,
			"Coarse Thread": 2
        }
    },
    "Embossed Leather Gloves": {
        "ID":       4239,
        "Learn":    55,
        "Yellow":   85,
        "Green":    100,
        "Grey":     115,
        "Source":   "Trainer",
        "Reagents": {
			"Light Leather": 3,
			"Coarse Thread": 2
        }
    },
    "Embossed Leather Pants": {
        "ID":       4242,
        "Learn":    75,
        "Yellow":   105,
        "Green":    120,
        "Grey":     135,
        "Source":   "Trainer",
        "Reagents": {
			"Cured Light Hide": 1,
			"Light Leather": 6,
			"Coarse Thread": 2
        }
    },
    "Embossed Leather Vest": {
        "ID":       2300,
        "Learn":    40,
        "Yellow":   70,
        "Green":    85,
        "Grey":     100,
        "Source":   "Trainer",
        "Reagents": {
			"Light Leather": 8,
			"Coarse Thread": 4
        }
    },
    "Feathered Breastplate": {
        "ID":       8349,
        "Learn":    250,
        "Yellow":   270,
        "Green":    280,
        "Grey":     290,
        "Source":   "Trainer",
        "School":   "Tribal",
        "Reagents": {
			"Thick Leather": 40,
			"Jet Black Feather": 40,
			"Black Pearl": 2,
			"Cured Thick Hide": 4,
			"Heavy Silken Thread": 4
        }
    },
    "Fine Leather Belt": {
        "ID":       4246,
        "Learn":    80,
        "Yellow":   110,
        "Green":    125,
        "Grey":     140,
        "Source":   "Trainer",
        "Reagents": {
			"Light Leather": 6,
			"Coarse Thread": 2
        }
    },
    "Fine Leather Boots": {
        "ID":       2307,
        "Learn":    90,
        "Yellow":   120,
        "Green":    135,
        "Grey":     150,
        "Source":   "Drop",
        "RecipeID": 2406,
        "Reagents": {
			"Light Leather": 7,
			"Coarse Thread": 2
        }
    },
    "Fine Leather Cloak": {
        "ID":       2308,
        "Learn":    85,
        "Yellow":   105,
        "Green":    120,
        "Grey":     135,
        "Source":   "Trainer",
        "Reagents": {
			"Light Leather": 10,
			"Fine Thread": 2
        }
    },
    "Fine Leather Gloves": {
        "ID":       2312,
        "Learn":    75,
        "Yellow":   105,
        "Green":    120,
        "Grey":     135,
        "Source":   "Drop",
        "RecipeID": 2408,
        "Reagents": {
			"Cured Light Hide": 1,
			"Light Leather": 4,
			"Coarse Thread": 2
        }
    },
    "Fine Leather Pants": {
        "ID":       5958,
        "Learn":    105,
        "Yellow":   130,
        "Green":    142,
        "Grey":     155,
        "Source":   "Drop",
        "RecipeID": 5972,
        "Reagents": {
			"Medium Leather": 8,
			"Bolt of Woolen Cloth": 1,
			"Fine Thread": 1
        }
    },
    "Fine Leather Tunic": {
        "ID":       4243,
        "Learn":    85,
        "Yellow":   115,
        "Green":    130,
        "Grey":     145,
        "Source":   "Trainer",
        "Reagents": {
			"Cured Light Hide": 3,
			"Light Leather": 6,
			"Coarse Thread": 4
        }
    },
    "Fletchers Gloves": {
        "ID":       7348,
        "Learn":    125,
        "Yellow":   150,
        "Green":    162,
        "Grey":     175,
        "Source":   "Trainer",
        "Reagents": {
			"Medium Leather": 8,
			"Long Tail Feather": 4,
			"Fine Thread": 2
        }
    },
    "Frost Leather Cloak": {
        "ID":       7377,
        "Learn":    180,
        "Yellow":   200,
        "Green":    210,
        "Grey":     220,
        "Source":   "Trainer",
        "Reagents": {
			"Heavy Leather": 6,
			"Elemental Earth": 2,
			"Elemental Water": 2,
			"Fine Thread": 2
        }
    },
    "Frostsaber Boots": {
        "ID":       15071,
        "Learn":    275,
        "Yellow":   295,
        "Green":    305,
        "Grey":     315,
        "Source":   "Vendor",
        "School":   "Tribal",
        "RecipeID": 15740,
        "Reagents": {
			"Rugged Leather": 4,
			"Frostsaber Leather": 6,
			"Rune Thread": 1
        }
    },
    "Frostsaber Gloves": {
        "ID":       15070,
        "Learn":    295,
        "Yellow":   315,
        "Green":    325,
        "Grey":     335,
        "Source":   "Drop",
        "RecipeID": 15761,
        "School":   "Tribal",
        "Reagents": {
			"Rugged Leather": 6,
			"Frostsaber Leather": 10,
			"Rune Thread": 1
        }
    },
    "Frostsaber Leggings": {
        "ID":       15069,
        "Learn":    285,
        "Yellow":   305,
        "Green":    315,
        "Grey":     325,
        "Source":   "Drop",
        "RecipeID": 15747,
        "School":   "Tribal",
        "Reagents": {
			"Rugged Leather": 6,
			"Frostsaber Leather": 8,
			"Rune Thread": 1
        }
    },
    "Gauntlets of the Sea": {
        "ID":       8346,
        "Learn":    230,
        "Yellow":   250,
        "Green":    260,
        "Grey":     270,
        "Source":   "Trainer",
		"Faction":	"Alliance",
        "School":   "Elemental",
        "Reagents": {
			"Thick Leather": 20,
			"Globe of Water": 8,
			"Core of Earth": 2,
			"Cured Thick Hide": 1,
			"Heavy Silken Thread": 4
        }
    },
    "Gem-studded Leather Belt": {
        "ID":       4262,
        "Learn":    185,
        "Yellow":   205,
        "Green":    215,
        "Grey":     225,
        "Source":   "VendorLimited",
        "RecipeID": 14635,
        "Reagents": {
			"Cured Heavy Hide": 4,
			"Iridescent Pearl": 2,
			"Jade": 2,
			"Citrine": 1,
			"Fine Thread": 1
        }
    },
    "Gloves of the Greatfather": {
        "ID":       17721,
        "Learn":    190,
        "Yellow":   210,
        "Green":    220,
        "Grey":     230,
        "Source":   "Seasonal",
        "RecipeID": 17722,
        "Reagents": {
			"Heavy Leather": 8,
			"Elemental Earth": 4,
			"Silken Thread": 1
        }
    },
    "Green Dragonscale Breastplate": {
        "ID":       15045,
        "Learn":    260,
        "Yellow":   280,
        "Green":    290,
        "Grey":     300,
        "Source":   "Vendor",
        "School":   "Dragonscale",
        "RecipeID": 15726,
        "Reagents": {
			"Rugged Leather": 20,
			"Green Dragonscale": 25,
			"Rune Thread": 2
        }
    },
    "Green Dragonscale Gauntlets": {
        "ID":       20296,
        "Learn":    280,
        "Yellow":   300,
        "Green":    310,
        "Grey":     320,
        "Source":   "Trainer",
        "School":   "Dragonscale",
        "Reagents": {
			"Rugged Leather": 20,
			"Green Dragonscale": 30,
			"Cured Rugged Hide": 1,
			"Rune Thread": 2
        }
    },
    "Green Dragonscale Leggings": {
        "ID":       15046,
        "Learn":    270,
        "Yellow":   290,
        "Green":    300,
        "Grey":     310,
        "Source":   "Drop",
        "RecipeID": 15733,
        "School":   "Dragonscale",
        "Reagents": {
			"Rugged Leather": 20,
			"Green Dragonscale": 25,
			"Rune Thread": 1
        }
    },
    "Green Leather Armor": {
        "ID":       4255,
        "Learn":    155,
        "Yellow":   175,
        "Green":    185,
        "Grey":     195,
        "Source":   "VendorLimited",
        "RecipeID": 7613,
        "Reagents": {
			"Heavy Leather": 9,
			"Green Dye": 2,
			"Fine Thread": 4
        }
    },
    "Green Leather Belt": {
        "ID":       4257,
        "Learn":    160,
        "Yellow":   180,
        "Green":    190,
        "Grey":     200,
        "Source":   "Trainer",
        "Reagents": {
			"Cured Heavy Hide": 1,
			"Heavy Leather": 5,
			"Fine Thread": 1,
			"Green Dye": 1,
			"Iron Buckle": 1
        }
    },
    "Green Leather Bracers": {
        "ID":       4259,
        "Learn":    180,
        "Yellow":   200,
        "Green":    210,
        "Grey":     220,
        "Source":   "Trainer",
        "Reagents": {
			"Cured Heavy Hide": 2,
			"Heavy Leather": 6,
			"Green Dye": 1,
			"Fine Thread": 1
        }
    },
    "Green Whelp Armor": {
        "ID":       7375,
        "Learn":    175,
        "Yellow":   195,
        "Green":    205,
        "Grey":     215,
        "Source":   "Drop",
        "RecipeID": 7450,
        "Reagents": {
			"Green Whelp Scale": 4,
			"Heavy Leather": 10,
			"Fine Thread": 2
        }
    },
    "Green Whelp Bracers": {
        "ID":       7386,
        "Learn":    190,
        "Yellow":   210,
        "Green":    220,
        "Grey":     230,
        "Source":   "Vendor",
        "RecipeID": 7451,
        "Reagents": {
			"Green Whelp Scale": 6,
			"Heavy Leather": 8,
			"Silken Thread": 2
        }
    },
    "Guardian Armor": {
        "ID":       4256,
        "Learn":    175,
        "Yellow":   195,
        "Green":    205,
        "Grey":     215,
        "Source":   "Drop",
        "RecipeID": 4299,
        "Reagents": {
			"Cured Heavy Hide": 2,
			"Heavy Leather": 12,
			"Shadow Oil": 1,
			"Fine Thread": 2
        }
    },
    "Guardian Belt": {
        "ID":       4258,
        "Learn":    170,
        "Yellow":   190,
        "Green":    200,
        "Grey":     210,
        "Source":   "Drop",
        "RecipeID": 4298,
        "Reagents": {
			"Cured Heavy Hide": 2,
			"Heavy Leather": 4,
			"Fine Thread": 1,
			"Iron Buckle": 1
        }
    },
    "Guardian Cloak": {
        "ID":       5965,
        "Learn":    185,
        "Yellow":   205,
        "Green":    215,
        "Grey":     225,
        "Source":   "Drop",
        "RecipeID": 5974,
        "Reagents": {
			"Heavy Leather": 14,
			"Bolt of Silk Cloth": 2,
			"Silken Thread": 2
        }
    },
    "Guardian Gloves": {
        "ID":       5966,
        "Learn":    190,
        "Yellow":   210,
        "Green":    220,
        "Grey":     230,
        "Source":   "Trainer",
        "Reagents": {
			"Heavy Leather": 4,
			"Cured Heavy Hide": 1,
			"Silken Thread": 1
        }
    },
    "Guardian Leather Bracers": {
        "ID":       4260,
        "Learn":    195,
        "Yellow":   215,
        "Green":    225,
        "Grey":     235,
        "Source":   "Drop",
        "RecipeID": 4300,
        "Reagents": {
			"Heavy Leather": 6,
			"Cured Heavy Hide": 2,
			"Silken Thread": 1
        }
    },
    "Guardian Pants": {
        "ID":       5962,
        "Learn":    160,
        "Yellow":   180,
        "Green":    190,
        "Grey":     200,
        "Source":   "Trainer",
        "Reagents": {
			"Heavy Leather": 12,
			"Bolt of Silk Cloth": 2,
			"Fine Thread": 2
        }
    },
    "Handstitched Leather Belt": {
        "ID":       4237,
        "Learn":    25,
        "Yellow":   55,
        "Green":    70,
        "Grey":     95,
        "Source":   "Trainer",
        "Reagents": {
			"Light Leather": 6,
			"Coarse Thread": 1
        }
    },
    "Handstitched Leather Boots": {
        "ID":       2302,
        "Learn":    1,
        "Yellow":   40,
        "Green":    55,
        "Grey":     70,
        "Source":   "Trainer",
        "Reagents": {
			"Light Leather": 2,
			"Coarse Thread": 1
        }
    },
    "Handstitched Leather Bracers": {
        "ID":       7277,
        "Learn":    1,
        "Yellow":   40,
        "Green":    55,
        "Grey":     70,
        "Source":   "Trainer",
        "Reagents": {
			"Light Leather": 2,
			"Coarse Thread": 3
        }
    },
    "Handstitched Leather Cloak": {
        "ID":       7276,
        "Learn":    1,
        "Yellow":   40,
        "Green":    55,
        "Grey":     70,
        "Source":   "Trainer",
        "Reagents": {
			"Light Leather": 2,
			"Coarse Thread": 1
        }
    },
    "Handstitched Leather Pants": {
        "ID":       2303,
        "Learn":    15,
        "Yellow":   40,
        "Green":    60,
        "Grey":     75,
        "Source":   "Trainer",
        "Reagents": {
			"Light Leather": 4,
			"Coarse Thread": 1
        }
    },
    "Handstitched Leather Vest": {
        "ID":       5957,
        "Learn":    1,
        "Yellow":   40,
        "Green":    55,
        "Grey":     70,
        "Source":   "Trainer",
        "Reagents": {
			"Light Leather": 3,
			"Coarse Thread": 1
        }
    },
    "Heavy Armor Kit": {
        "ID":       4265,
        "Learn":    150,
        "Yellow":   170,
        "Green":    180,
        "Grey":     190,
        "Source":   "Trainer",
        "Reagents": {
			"Heavy Leather": 5,
			"Fine Thread": 1
        }
    },
    "Heavy Earthen Gloves": {
        "ID":       7359,
        "Learn":    145,
        "Yellow":   170,
        "Green":    182,
        "Grey":     195,
        "Source":   "Drop",
        "RecipeID": 7364,
        "Reagents": {
			"Medium Leather": 12,
			"Elemental Earth": 2,
			"Bolt of Woolen Cloth": 2,
			"Fine Thread": 2
        }
    },
    "Heavy Leather": {
        "ID":       4234,
        "Learn":    150,
        "Yellow":   150,
        "Green":    155,
        "Grey":     160,
        "Source":   "Trainer",
        "Reagents": {
			"Medium Leather": 5
        }
    },
    "Heavy Leather Ammo Pouch": {
        "ID":       7372,
        "Learn":    150,
        "Yellow":   170,
        "Green":    180,
        "Grey":     190,
        "Source":   "Trainer",
        "Reagents": {
			"Heavy Leather": 8,
			"Fine Thread": 2
        }
    },
    "Heavy Leather Ball": {
        "ID":       18662,
        "Learn":    150,
        "Yellow":   150,
        "Green":    155,
        "Grey":     160,
        "Source":   "VendorLimited",
        "RecipeID": 18731,
        "Reagents": {
			"Heavy Leather": 2,
			"Fine Thread": 1
        }
    },
    "Heavy Quiver": {
        "ID":       7371,
        "Learn":    150,
        "Yellow":   170,
        "Green":    180,
        "Grey":     190,
        "Source":   "Trainer",
        "Reagents": {
			"Heavy Leather": 8,
			"Fine Thread": 2
        }
    },
    "Heavy Scorpid Belt": {
        "ID":       15082,
        "Learn":    280,
        "Yellow":   300,
        "Green":    210,
        "Grey":     320,
        "Source":   "Drop",
        "RecipeID": 15743,
        "Reagents": {
			"Rugged Leather": 6,
			"Heavy Scorpid Scale": 8,
			"Rune Thread": 1
        }
    },
    "Heavy Scorpid Bracers": {
        "ID":       15077,
        "Learn":    255,
        "Yellow":   275,
        "Green":    285,
        "Grey":     295,
        "Source":   "Vendor",
        "RecipeID": 15724,
        "Reagents": {
			"Rugged Leather": 4,
			"Heavy Scorpid Scale": 4,
			"Rune Thread": 1
        }
    },
    "Heavy Scorpid Gauntlets": {
        "ID":       15078,
        "Learn":    275,
        "Yellow":   295,
        "Green":    305,
        "Grey":     315,
        "Source":   "Drop",
        "RecipeID": 15738,
        "Reagents": {
			"Rugged Leather": 6,
			"Heavy Scorpid Scale": 8,
			"Rune Thread": 1
        }
    },
    "Heavy Scorpid Helm": {
        "ID":       15080,
        "Learn":    295,
        "Yellow":   315,
        "Green":    325,
        "Grey":     335,
        "Source":   "Vendor",
        "RecipeID": 15762,
        "Reagents": {
			"Rugged Leather": 8,
			"Heavy Scorpid Scale": 12,
			"Cured Rugged Hide": 1,
			"Rune Thread": 1
        }
    },
    "Heavy Scorpid Leggings": {
        "ID":       15079,
        "Learn":    285,
        "Yellow":   305,
        "Green":    315,
        "Grey":     325,
        "Source":   "Drop",
        "RecipeID": 15748,
        "Reagents": {
			"Rugged Leather": 8,
			"Heavy Scorpid Scale": 12,
			"Rune Thread": 1
        }
    },
    "Heavy Scorpid Vest": {
        "ID":       15076,
        "Learn":    265,
        "Yellow":   285,
        "Green":    295,
        "Grey":     305,
        "Source":   "Drop",
        "RecipeID": 15727,
        "Reagents": {
			"Rugged Leather": 6,
			"Heavy Scorpid Scale": 6,
			"Rune Thread": 1
        }
    },
    "Helm of Fire": {
        "ID":       8348,
        "Learn":    250,
        "Yellow":   270,
        "Green":    280,
        "Grey":     290,
        "Source":   "Trainer",
        "School":   "Elemental",
        "Reagents": {
			"Thick Leather": 40,
			"Heart of Fire": 8,
			"Core of Earth": 4,
			"Cured Thick Hide": 2,
			"Heavy Silken Thread": 4
        }
    },
    "Herbalists Gloves": {
        "ID":       7349,
        "Learn":    135,
        "Yellow":   160,
        "Green":    172,
        "Grey":     185,
        "Source":   "VendorLimited",
		"Faction":	"Alliance",
        "RecipeID": 7361,
        "Reagents": {
			"Medium Leather": 8,
			"Kingsblood": 4,
			"Fine Thread": 2
        }
    },
    "Hillmans Belt": {
        "ID":       4250,
        "Learn":    120,
        "Yellow":   145,
        "Green":    157,
        "Grey":     170,
        "Source":   "Drop",
        "RecipeID": 4294,
        "Reagents": {
			"Medium Leather": 8,
			"Elixir of Wisdom": 1,
			"Fine Thread": 1
        }
    },
    "Hillmans Cloak": {
        "ID":       3719,
        "Learn":    150,
        "Yellow":   170,
        "Green":    180,
        "Grey":     190,
        "Source":   "Trainer",
        "Reagents": {
			"Heavy Leather": 5,
			"Fine Thread": 2
        }
    },
    "Hillmans Leather Gloves": {
        "ID":       4247,
        "Learn":    145,
        "Yellow":   170,
        "Green":    182,
        "Grey":     195,
        "Source":   "Trainer",
        "Reagents": {
			"Medium Leather": 14,
			"Fine Thread": 4
        }
    },
    "Hillmans Leather Vest": {
        "ID":       4244,
        "Learn":    100,
        "Yellow":   125,
        "Green":    137,
        "Grey":     150,
        "Source":   "Drop",
        "RecipeID": 4293,
        "Reagents": {
			"Fine Leather Tunic": 1,
			"Cured Light Hide": 2,
			"Coarse Thread": 2
        }
    },
    "Hillmans Shoulders": {
        "ID":       4251,
        "Learn":    130,
        "Yellow":   155,
        "Green":    167,
        "Grey":     180,
        "Source":   "Trainer",
        "Reagents": {
			"Cured Medium Hide": 1,
			"Medium Leather": 4,
			"Fine Thread": 1
        }
    },
    "Ironfeather Breastplate": {
        "ID":       15066,
        "Learn":    290,
        "Yellow":   310,
        "Green":    320,
        "Grey":     330,
        "Source":   "Drop",
        "RecipeID": 15760,
        "School":   "Tribal",
        "Reagents": {
			"Rugged Leather": 40,
			"Ironfeather": 120,
			"Jade": 1,
			"Cured Rugged Hide": 1,
			"Rune Thread": 1
        }
    },
    "Ironfeather Shoulders": {
        "ID":       15067,
        "Learn":    270,
        "Yellow":   290,
        "Green":    300,
        "Grey":     310,
        "Source":   "Vendor",
        "School":   "Tribal",
        "RecipeID": 15735,
        "Reagents": {
			"Rugged Leather": 24,
			"Ironfeather": 80,
			"Jade": 2,
			"Rune Thread": 1
        }
    },
    "Kodo Hide Bag": {
        "ID":       5081,
        "Learn":    40,
        "Yellow":   70,
        "Green":    85,
        "Grey":     100,
        "Source":   "Quest",
		"Faction":	"Horde",
        "RecipeID": 5083,
        "Reagents": {
			"Thin Kodo Leather": 3,
			"Light Leather": 4,
			"Coarse Thread": 1
        }
    },
    "Light Armor Kit": {
        "ID":       2304,
        "Learn":    1,
        "Yellow":   30,
        "Green":    45,
        "Grey":     60,
        "Source":   "Trainer",
        "Reagents": {
			"Light Leather": 1
        }
    },
    "Light Leather": {
        "ID":       2318,
        "Learn":    1,
        "Yellow":   20,
        "Green":    30,
        "Grey":     40,
        "Source":   "Trainer",
        "Reagents": {
			"Ruined Leather Scraps": 3
        }
    },
    "Light Leather Bracers": {
        "ID":       7281,
        "Learn":    70,
        "Yellow":   100,
        "Green":    115,
        "Grey":     130,
        "Source":   "Trainer",
        "Reagents": {
			"Light Leather": 6,
			"Coarse Thread": 4
        }
    },
    "Light Leather Pants": {
        "ID":       7282,
        "Learn":    95,
        "Yellow":   125,
        "Green":    140,
        "Grey":     155,
        "Source":   "Trainer",
        "Reagents": {
			"Light Leather": 10,
			"Cured Light Hide": 1,
			"Fine Thread": 1
        }
    },
    "Light Leather Quiver": {
        "ID":       7278,
        "Learn":    30,
        "Yellow":   60,
        "Green":    75,
        "Grey":     90,
        "Source":   "Trainer",
        "Reagents": {
			"Light Leather": 4,
			"Coarse Thread": 2
        }
    },
    "Living Leggings": {
        "ID":       15060,
        "Learn":    285,
        "Yellow":   305,
        "Green":    315,
        "Grey":     325,
        "Source":   "Drop",
        "RecipeID": 15752,
        "School":   "Elemental",
        "Reagents": {
			"Rugged Leather": 16,
			"Living Essence": 6,
			"Cured Rugged Hide": 1,
			"Rune Thread": 1
        }
    },
    "Living Shoulders": {
        "ID":       15061,
        "Learn":    270,
        "Yellow":   290,
        "Green":    300,
        "Grey":     310,
        "Source":   "VendorLimited",
        "School":   "Elemental",
        "RecipeID": 15734,
        "Reagents": {
			"Rugged Leather": 12,
			"Living Essence": 4,
			"Rune Thread": 1
        }
    },
    "Medium Armor Kit": {
        "ID":       2313,
        "Learn":    100,
        "Yellow":   115,
        "Green":    122,
        "Grey":     130,
        "Source":   "Trainer",
        "Reagents": {
			"Medium Leather": 4,
			"Coarse Thread": 1
        }
    },
    "Medium Leather": {
        "ID":       2319,
        "Learn":    100,
        "Yellow":   100,
        "Green":    105,
        "Grey":     110,
        "Source":   "Trainer",
        "Reagents": {
			"Light Leather": 4
        }
    },
    "Might of the Timbermaw": {
        "ID":       19044,
        "Learn":    290,
        "Yellow":   310,
        "Green":    320,
        "Grey":     330,
        "Source":   "Reputation",
        "RecipeID": 19326,
        "Reagents": {
			"Rugged Leather": 30,
			"Powerful Mojo": 2,
			"Living Essence": 4,
			"Cured Rugged Hide": 2,
			"Rune Thread": 2
        }
    },
    "Moonglow Vest": {
        "ID":       6709,
        "Learn":    90,
        "Yellow":   115,
        "Green":    130,
        "Grey":     145,
        "Source":   "Quest",
		"Faction":	"Alliance",
        "RecipeID": 6710,
        "Reagents": {
			"Light Leather": 6,
			"Cured Light Hide": 1,
			"Coarse Thread": 4,
			"Small Lustrous Pearl": 1
        }
    },
    "Murloc Scale Belt": {
        "ID":       5780,
        "Learn":    90,
        "Yellow":   120,
        "Green":    135,
        "Grey":     150,
        "Source":   "VendorLimited",
        "RecipeID": 5786,
        "Reagents": {
			"Slimy Murloc Scale": 8,
			"Light Leather": 6,
			"Fine Thread": 1
        }
    },
    "Murloc Scale Bracers": {
        "ID":       5783,
        "Learn":    190,
        "Yellow":   210,
        "Green":    220,
        "Grey":     230,
        "Source":   "Vendor",
        "RecipeID": 5789,
        "Reagents": {
			"Thick Murloc Scale": 16,
			"Cured Heavy Hide": 1,
			"Heavy Leather": 14,
			"Silken Thread": 1
        }
    },
    "Murloc Scale Breastplate": {
        "ID":       5781,
        "Learn":    95,
        "Yellow":   125,
        "Green":    140,
        "Grey":     155,
        "Source":   "VendorLimited",
        "RecipeID": 5787,
        "Reagents": {
			"Slimy Murloc Scale": 12,
			"Cured Light Hide": 1,
			"Light Leather": 8,
			"Fine Thread": 1
        }
    },
    "Nightscape Boots": {
        "ID":       8197,
        "Learn":    235,
        "Yellow":   255,
        "Green":    265,
        "Grey":     275,
        "Source":   "Trainer",
        "Reagents": {
			"Thick Leather": 16,
			"Heavy Silken Thread": 2
        }
    },
    "Nightscape Headband": {
        "ID":       8176,
        "Learn":    205,
        "Yellow":   225,
        "Green":    235,
        "Grey":     245,
        "Source":   "Trainer",
        "Reagents": {
			"Thick Leather": 5,
			"Silken Thread": 2
        }
    },
    "Nightscape Pants": {
        "ID":       8193,
        "Learn":    230,
        "Yellow":   250,
        "Green":    260,
        "Grey":     270,
        "Source":   "Trainer",
        "Reagents": {
			"Thick Leather": 14,
			"Silken Thread": 4
        }
    },
    "Nightscape Shoulders": {
        "ID":       8192,
        "Learn":    210,
        "Yellow":   230,
        "Green":    240,
        "Grey":     250,
        "Source":   "Vendor",
        "RecipeID": 8409,
        "Reagents": {
			"Thick Leather": 8,
			"Mageweave Cloth": 6,
			"Silken Thread": 3
        }
    },
    "Nightscape Tunic": {
        "ID":       8175,
        "Learn":    205,
        "Yellow":   225,
        "Green":    235,
        "Grey":     245,
        "Source":   "Trainer",
        "Reagents": {
			"Thick Leather": 7,
			"Silken Thread": 2
        }
    },
    "Nimble Leather Gloves": {
        "ID":       7285,
        "Learn":    120,
        "Yellow":   145,
        "Green":    157,
        "Grey":     170,
        "Source":   "Trainer",
        "Reagents": {
			"Elixir of Minor Agility": 1,
			"Medium Leather": 6,
			"Fine Thread": 1
        }
    },
    "Pilferers Gloves": {
        "ID":       7358,
        "Learn":    140,
        "Yellow":   165,
        "Green":    177,
        "Grey":     190,
        "Source":   "Drop",
        "RecipeID": 7363,
        "Reagents": {
			"Medium Leather": 10,
			"Lucky Charm": 2,
			"Fine Thread": 2
        }
    },
    "Quickdraw Quiver": {
        "ID":       8217,
        "Learn":    225,
        "Yellow":   245,
        "Green":    255,
        "Grey":     265,
        "Source":   "Trainer",
        "Reagents": {
			"Thick Leather": 12,
			"Cured Thick Hide": 1,
			"Elixir of Agility": 1,
			"Silken Thread": 4
        }
    },
    "Raptor Hide Belt": {
        "ID":       4456,
        "Learn":    165,
        "Yellow":   185,
        "Green":    195,
        "Grey":     205,
        "Source":   "Vendor",
		"Faction":	"Alliance",
        "RecipeID": 13288,
        "Reagents": {
			"Raptor Hide": 4,
			"Heavy Leather": 4,
			"Fine Thread": 2
        }
    },
    "Raptor Hide Harness": {
        "ID":       4455,
        "Learn":    165,
        "Yellow":   185,
        "Green":    195,
        "Grey":     205,
        "Source":   "Vendor",
		"Faction":	"Horde",
        "RecipeID": 13287,
        "Reagents": {
			"Raptor Hide": 6,
			"Heavy Leather": 4,
			"Fine Thread": 2
        }
    },
    "Red Whelp Gloves": {
        "ID":       7284,
        "Learn":    120,
        "Yellow":   145,
        "Green":    157,
        "Grey":     170,
        "Source":   "VendorLimited",
		"Faction":	"Alliance",
        "RecipeID": 7290,
        "Reagents": {
			"Red Whelp Scale": 6,
			"Medium Leather": 4,
			"Fine Thread": 1
        }
    },
    "Rugged Armor Kit": {
        "ID":       15564,
        "Learn":    250,
        "Yellow":   250,
        "Green":    260,
        "Grey":     270,
        "Source":   "Trainer",
        "Reagents": {
			"Rugged Leather": 5
        }
    },
    "Rugged Leather": {
        "ID":       8170,
        "Learn":    250,
        "Yellow":   250,
        "Green":    250,
        "Grey":     250,
        "Source":   "Trainer",
        "Reagents": {
			"Thick Leather": 6
        }
    },
    "Rugged Leather Pants": {
        "ID":       7280,
        "Learn":    35,
        "Yellow":   65,
        "Green":    80,
        "Grey":     95,
        "Source":   "Drop",
        "RecipeID": 7288,
        "Reagents": {
			"Light Leather": 5,
			"Coarse Thread": 5
        }
    },
    "Runic Leather Belt": {
        "ID":       15093,
        "Learn":    280,
        "Yellow":   300,
        "Green":    310,
        "Grey":     320,
        "Source":   "Drop",
        "RecipeID": 15745,
        "Reagents": {
			"Rugged Leather": 12,
			"Runecloth": 10,
			"Rune Thread": 1
        }
    },
    "Runic Leather Bracers": {
        "ID":       15092,
        "Learn":    275,
        "Yellow":   295,
        "Green":    305,
        "Grey":     315,
        "Source":   "Drop",
        "RecipeID": 15739,
        "Reagents": {
			"Rugged Leather": 6,
			"Black Pearl": 1,
			"Runecloth": 6,
			"Rune Thread": 1
        }
    },
    "Runic Leather Gauntlets": {
        "ID":       15091,
        "Learn":    270,
        "Yellow":   290,
        "Green":    300,
        "Grey":     310,
        "Source":   "Drop",
        "RecipeID": 15731,
        "Reagents": {
			"Rugged Leather": 10,
			"Runecloth": 6,
			"Rune Thread": 1
        }
    },
    "Runic Leather Headband": {
        "ID":       15094,
        "Learn":    290,
        "Yellow":   310,
        "Green":    320,
        "Grey":     330,
        "Source":   "Vendor",
        "RecipeID": 15756,
        "Reagents": {
			"Rugged Leather": 14,
			"Runecloth": 10,
			"Rune Thread": 1
        }
    },
    "Shadowskin Gloves": {
        "ID":       18238,
        "Learn":    200,
        "Yellow":   210,
        "Green":    220,
        "Grey":     230,
        "Source":   "VendorLimited",
        "RecipeID": 18239,
        "Reagents": {
			"Thick Leather": 6,
			"Shadowcat Hide": 8,
			"Black Pearl": 2,
			"Cured Heavy Hide": 2,
			"Shadowgem": 4,
			"Heavy Silken Thread": 1
        }
    },
    "Small Leather Ammo Pouch": {
        "ID":       7279,
        "Learn":    30,
        "Yellow":   60,
        "Green":    75,
        "Grey":     90,
        "Source":   "Trainer",
        "Reagents": {
			"Light Leather": 3,
			"Coarse Thread": 4
        }
    },
    "Stormshroud Armor": {
        "ID":       15056,
        "Learn":    285,
        "Yellow":   305,
        "Green":    315,
        "Grey":     325,
        "Source":   "Drop",
        "RecipeID": 15753,
        "School":   "Elemental",
        "Reagents": {
			"Rugged Leather": 16,
			"Essence of Water": 3,
			"Essence of Air": 3,
			"Cured Rugged Hide": 1,
			"Rune Thread": 1
        }
    },
    "Stormshroud Pants": {
        "ID":       15057,
        "Learn":    275,
        "Yellow":   295,
        "Green":    305,
        "Grey":     315,
        "Source":   "VendorLimited",
        "School":   "Elemental",
        "RecipeID": 15741,
        "Reagents": {
			"Rugged Leather": 16,
			"Essence of Water": 2,
			"Essence of Air": 2,
			"Rune Thread": 1
        }
    },
    "Stormshroud Shoulders": {
        "ID":       15058,
        "Learn":    295,
        "Yellow":   315,
        "Green":    325,
        "Grey":     325,
        "Source":   "Drop",
        "RecipeID": 15764,
        "School":   "Elemental",
        "Reagents": {
			"Rugged Leather": 12,
			"Essence of Water": 3,
			"Essence of Air": 3,
			"Enchanted Leather": 2,
			"Rune Thread": 1
        }
    },
    "Swift Boots": {
        "ID":       7391,
        "Learn":    200,
        "Yellow":   220,
        "Green":    230,
        "Grey":     240,
        "Source":   "Drop",
        "RecipeID": 7453,
        "Reagents": {
			"Heavy Leather": 10,
			"Swiftness Potion": 2,
			"Thick Spiders Silk": 2,
			"Silken Thread": 1
        }
    },
    "Thick Armor Kit": {
        "ID":       8173,
        "Learn":    200,
        "Yellow":   220,
        "Green":    230,
        "Grey":     240,
        "Source":   "Trainer",
        "Reagents": {
			"Thick Leather": 5,
			"Silken Thread": 1
        }
    },
    "Thick Leather": {
        "ID":       4304,
        "Learn":    200,
        "Yellow":   200,
        "Green":    202,
        "Grey":     205,
        "Source":   "Trainer",
        "Reagents": {
			"Heavy Leather": 6
        }
    },
    "Thick Leather Ammo Pouch": {
        "ID":       8218,
        "Learn":    225,
        "Yellow":   245,
        "Green":    255,
        "Grey":     265,
        "Source":   "Trainer",
        "Reagents": {
			"Thick Leather": 10,
			"Cured Thick Hide": 1,
			"Elixir of Greater Defense": 1,
			"Silken Thread": 6
        }
    },
    "Thick Murloc Armor": {
        "ID":       5782,
        "Learn":    170,
        "Yellow":   190,
        "Green":    200,
        "Grey":     210,
        "Source":   "VendorLimited",
        "RecipeID": 5788,
        "Reagents": {
			"Thick Murloc Scale": 12,
			"Cured Heavy Hide": 1,
			"Heavy Leather": 10,
			"Fine Thread": 3
        }
    },
    "Tough Scorpid Boots": {
        "ID":       8209,
        "Learn":    235,
        "Yellow":   255,
        "Green":    265,
        "Grey":     275,
        "Source":   "Drop",
        "RecipeID": 8399,
        "Reagents": {
			"Thick Leather": 12,
			"Scorpid Scale": 12,
			"Silken Thread": 6
        }
    },
    "Tough Scorpid Bracers": {
        "ID":       8205,
        "Learn":    220,
        "Yellow":   240,
        "Green":    250,
        "Grey":     260,
        "Source":   "Drop",
        "RecipeID": 8397,
        "Reagents": {
			"Thick Leather": 10,
			"Scorpid Scale": 4,
			"Silken Thread": 2
        }
    },
    "Tough Scorpid Breastplate": {
        "ID":       8203,
        "Learn":    220,
        "Yellow":   240,
        "Green":    250,
        "Grey":     260,
        "Source":   "Drop",
        "RecipeID": 8395,
        "Reagents": {
			"Thick Leather": 12,
			"Scorpid Scale": 12,
			"Silken Thread": 4
        }
    },
    "Tough Scorpid Gloves": {
        "ID":       8204,
        "Learn":    225,
        "Yellow":   245,
        "Green":    255,
        "Grey":     265,
        "Source":   "Drop",
        "RecipeID": 8398,
        "Reagents": {
			"Thick Leather": 6,
			"Scorpid Scale": 8,
			"Silken Thread": 2
        }
    },
    "Tough Scorpid Helm": {
        "ID":       8208,
        "Learn":    250,
        "Yellow":   270,
        "Green":    280,
        "Grey":     290,
        "Source":   "Drop",
        "RecipeID": 8402,
        "Reagents": {
			"Thick Leather": 10,
			"Scorpid Scale": 20,
			"Heavy Silken Thread": 2
        }
    },
    "Tough Scorpid Leggings": {
        "ID":       8206,
        "Learn":    245,
        "Yellow":   265,
        "Green":    275,
        "Grey":     285,
        "Source":   "Drop",
        "RecipeID": 8401,
        "Reagents": {
			"Thick Leather": 14,
			"Scorpid Scale": 8,
			"Heavy Silken Thread": 2
        }
    },
    "Tough Scorpid Shoulders": {
        "ID":       8207,
        "Learn":    240,
        "Yellow":   260,
        "Green":    270,
        "Grey":     280,
        "Source":   "Drop",
        "RecipeID": 8400,
        "Reagents": {
			"Thick Leather": 12,
			"Scorpid Scale": 16,
			"Heavy Silken Thread": 2
        }
    },
    "Toughened Leather Armor": {
        "ID":       2314,
        "Learn":    120,
        "Yellow":   145,
        "Green":    157,
        "Grey":     170,
        "Source":   "Trainer",
        "Reagents": {
			"Medium Leather": 10,
			"Cured Light Hide": 2,
			"Fine Thread": 2
        }
    },
    "Toughened Leather Gloves": {
        "ID":       4253,
        "Learn":    135,
        "Yellow":   160,
        "Green":    172,
        "Grey":     185,
        "Source":   "Trainer",
        "Reagents": {
			"Medium Leather": 4,
			"Cured Medium Hide": 2,
			"Elixir of Defense": 2,
			"Spiders Silk": 2,
			"Fine Thread": 2
        }
    },
    "Turtle Scale Bracers": {
        "ID":       8198,
        "Learn":    210,
        "Yellow":   230,
        "Green":    240,
        "Grey":     250,
        "Source":   "Trainer",
        "Reagents": {
			"Thick Leather": 8,
			"Turtle Scale": 12,
			"Heavy Silken Thread": 1
        }
    },
    "Turtle Scale Breastplate": {
        "ID":       8189,
        "Learn":    210,
        "Yellow":   230,
        "Green":    240,
        "Grey":     250,
        "Source":   "Trainer",
        "Reagents": {
			"Thick Leather": 6,
			"Turtle Scale": 12,
			"Heavy Silken Thread": 1
        }
    },
    "Turtle Scale Gloves": {
        "ID":       8187,
        "Learn":    205,
        "Yellow":   225,
        "Green":    235,
        "Grey":     245,
        "Source":   "Vendor",
        "RecipeID": 8385,
        "Reagents": {
			"Thick Leather": 6,
			"Turtle Scale": 8,
			"Heavy Silken Thread": 1
        }
    },
    "Turtle Scale Helm": {
        "ID":       8191,
        "Learn":    230,
        "Yellow":   250,
        "Green":    260,
        "Grey":     270,
        "Source":   "Trainer",
        "Reagents": {
			"Thick Leather": 14,
			"Turtle Scale": 24,
			"Heavy Silken Thread": 1
        }
    },
    "Turtle Scale Leggings": {
        "ID":       8185,
        "Learn":    235,
        "Yellow":   255,
        "Green":    265,
        "Grey":     275,
        "Source":   "Trainer",
        "Reagents": {
			"Thick Leather": 14,
			"Turtle Scale": 28,
			"Heavy Silken Thread": 1
        }
    },
    "Volcanic Breastplate": {
        "ID":       15053,
        "Learn":    285,
        "Yellow":   305,
        "Green":    315,
        "Grey":     325,
        "Source":   "Drop",
        "RecipeID": 15749,
        "School":   "Elemental",
        "Reagents": {
			"Rugged Leather": 8,
			"Essence of Fire": 1,
			"Essence of Earth": 1,
			"Rune Thread": 1
        }
    },
    "Volcanic Leggings": {
        "ID":       15054,
        "Learn":    270,
        "Yellow":   290,
        "Green":    300,
        "Grey":     310,
        "Source":   "Drop",
        "RecipeID": 15732,
        "School":   "Elemental",
        "Reagents": {
			"Rugged Leather": 6,
			"Essence of Fire": 1,
			"Core of Earth": 1,
			"Rune Thread": 1
        }
    },
    "Warbear Harness": {
        "ID":       15064,
        "Learn":    275,
        "Yellow":   295,
        "Green":    305,
        "Grey":     315,
        "Source":   "Reputation",
		"School":	"Tribal",
        "RecipeID": 20253,
        "Reagents": {
			"Rugged Leather": 28,
			"Warbear Leather": 12,
			"Rune Thread": 1
        }
    },
    "Warbear Woolies": {
        "ID":       15065,
        "Learn":    285,
        "Yellow":   305,
        "Green":    315,
        "Grey":     325,
        "Source":   "Reputation",
		"School":	"Tribal",
        "RecipeID": 20254,
        "Reagents": {
			"Rugged Leather": 24,
			"Warbear Leather": 14,
			"Rune Thread": 1
        }
    },
    "White Leather Jerkin": {
        "ID":       2311,
        "Learn":    60,
        "Yellow":   90,
        "Green":    105,
        "Grey":     120,
        "Source":   "Drop",
        "RecipeID": 2407,
        "Reagents": {
			"Light Leather": 8,
			"Coarse Thread": 2,
			"Bleach": 1
        }
    },
    "Wicked Leather Bracers": {
        "ID":       15084,
        "Learn":    265,
        "Yellow":   285,
        "Green":    295,
        "Grey":     305,
        "Source":   "Drop",
        "RecipeID": 15728,
        "Reagents": {
			"Rugged Leather": 8,
			"Black Dye": 1,
			"Rune Thread": 1
        }
    },
    "Wicked Leather Gauntlets": {
        "ID":       15083,
        "Learn":    260,
        "Yellow":   280,
        "Green":    290,
        "Grey":     300,
        "Source":   "Vendor",
        "RecipeID": 15725,
        "Reagents": {
			"Rugged Leather": 8,
			"Black Dye": 1,
			"Rune Thread": 1
        }
    },
    "Wicked Leather Headband": {
        "ID":       15086,
        "Learn":    280,
        "Yellow":   300,
        "Green":    310,
        "Grey":     320,
        "Source":   "Drop",
        "RecipeID": 15744,
        "Reagents": {
			"Rugged Leather": 12,
			"Black Dye": 1,
			"Rune Thread": 1
        }
    },
    "Wicked Leather Pants": {
        "ID":       15087,
        "Learn":    290,
        "Yellow":   310,
        "Green":    320,
        "Grey":     330,
        "Source":   "Drop",
        "RecipeID": 15757,
        "Reagents": {
			"Rugged Leather": 16,
			"Cured Rugged Hide": 1,
			"Black Dye": 3,
			"Rune Thread": 1
        }
    },
    "Wild Leather Boots": {
        "ID":       8213,
        "Learn":    245,
        "Yellow":   265,
        "Green":    275,
        "Grey":     285,
        "Source":   "Quest",
		"Faction":	"Any",
        "RecipeID": 8406,
        "Reagents": {
			"Thick Leather": 14,
			"Wildvine": 4,
			"Cured Thick Hide": 2
        }
    },
    "Wild Leather Cloak": {
        "ID":       8215,
        "Learn":    250,
        "Yellow":   270,
        "Green":    280,
        "Grey":     290,
        "Source":   "Quest",
		"Faction":	"Any",
        "RecipeID": 8408,
        "Reagents": {
			"Thick Leather": 16,
			"Wildvine": 6,
			"Cured Thick Hide": 2
        }
    },
    "Wild Leather Helmet": {
        "ID":       8214,
        "Learn":    225,
        "Yellow":   245,
        "Green":    255,
        "Grey":     265,
        "Source":   "Quest",
		"Faction":	"Any",
        "RecipeID": 8405,
        "Reagents": {
			"Thick Leather": 10,
			"Wildvine": 2,
			"Cured Thick Hide": 1
        }
    },
    "Wild Leather Leggings": {
        "ID":       8212,
        "Learn":    250,
        "Yellow":   270,
        "Green":    280,
        "Grey":     290,
        "Source":   "Quest",
		"Faction":	"Any",
        "RecipeID": 8407,
        "Reagents": {
			"Thick Leather": 16,
			"Wildvine": 6,
			"Cured Thick Hide": 2
        }
    },
    "Wild Leather Shoulders": {
        "ID":       8210,
        "Learn":    220,
        "Yellow":   240,
        "Green":    250,
        "Grey":     260,
        "Source":   "Quest",
		"Faction":	"Any",
        "RecipeID": 8403,
        "Reagents": {
			"Thick Leather": 10,
			"Wildvine": 1,
			"Cured Thick Hide": 1
        }
    },
    "Wild Leather Vest": {
        "ID":       8211,
        "Learn":    225,
        "Yellow":   245,
        "Green":    255,
        "Grey":     265,
        "Source":   "Quest",
		"Faction":	"Any",
        "RecipeID": 8404,
        "Reagents": {
			"Thick Leather": 12,
			"Wildvine": 2,
			"Cured Thick Hide": 1
        }
    },
    "Wolfshead Helm": {
        "ID":       8345,
        "Learn":    225,
        "Yellow":   245,
        "Green":    255,
        "Grey":     265,
        "Source":   "Trainer",
        "School":   "Tribal",
        "Reagents": {
			"Thick Leather": 18,
			"Thick Wolfhide": 2,
			"Wicked Claw": 8,
			"Heavy Silken Thread": 4,
			"Cured Thick Hide": 2
        }
    }
}

import json
with open('leatherworking.json', 'w') as jsonFile:
    json.dump(recipes, jsonFile)
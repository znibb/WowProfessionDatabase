#!/usr/bin/env python3.7

recipes = {
    "Delicate Copper Wire": {
        "ID":       20816,
        "Learn":    1,
        "Yellow":   20,
        "Green":    35,
        "Grey":     50,
        "Source":   "Trainer",
        "Reagents": {
            "Copper Bar": 2
        }
    },
    "Rough Stone Statue": {
        "ID":       25498,
        "Learn":    1,
        "Yellow":   20,
        "Green":    35,
        "Grey":     50,
        "Source":   "Trainer",
        "Reagents": {
            "Rough Stone": 8
        }
    },
    "Braided Copper Ring": {
        "ID":       20906,
        "Learn":    1,
        "Yellow":   30,
        "Green":    45,
        "Grey":     60,
        "Source":   "Trainer",
        "Reagents": {
            "Delicate Copper Wire": 2
        }
    },
    "Woven Copper Ring": {
        "ID":       21931,
        "Learn":    1,
        "Yellow":   30,
        "Green":    45,
        "Grey":     60,
        "Source":   "Trainer",
        "Reagents": {
            "Delicate Copper Wire": 2,
			"Coper Bar": 1
        }
    },
    "Heavy Copper Ring": {
        "ID":       21932,
        "Learn":    5,
        "Yellow":   35,
        "Green":    50,
        "Grey":     65,
        "Source":   "Trainer",
        "Reagents": {
            "Copper Bar": 4,
			"Delicate Copper Wire": 2
        }
    },
    "Malachite Pendant": {
        "ID":       25438,
        "Learn":    20,
        "Yellow":   50,
        "Green":    65,
        "Grey":     80,
        "Source":   "Trainer",
        "Reagents": {
            "Malachite": 1,
			"Delicate Copper Wire": 1
        }
    },
    "Tigerseye Band": {
        "ID":       25439,
        "Learn":    20,
        "Yellow":   50,
        "Green":    65,
        "Grey":     80,
        "Source":   "Trainer",
        "Reagents": {
            "Tigerseye": 1,
			"Delicate Copper Wire": 1
        }
    },
    "Inlaid Malachite Ring": {
        "ID":       20821,
        "Learn":    30,
        "Yellow":   60,
        "Green":    75,
        "Grey":     80,
        "Source":   "Trainer",
        "Reagents": {
            "Malachite": 2,
			"Copper Bar": 2
        }
    },
    "Ornate Tigerseye Necklace": {
        "ID":       21934,
        "Learn":    30,
        "Yellow":   60,
        "Green":    75,
        "Grey":     90,
        "Source":   "Trainer",
        "Reagents": {
            "Tigerseye": 2,
			"Copper Bar": 2,
			"Delicate Copper Wire": 1
        }
    },
    "Bronze Setting": {
        "ID":       20817,
        "Learn":    50,
        "Yellow":   70,
        "Green":    80,
        "Grey":     90,
        "Source":   "Trainer",
        "Reagents": {
            "Bronze Bar": 2
        }
    },
    "Coarse Stone Statue": {
        "ID":       25880,
        "Learn":    50,
        "Yellow":   70,
        "Green":    80,
        "Grey":     90,
        "Source":   "Trainer",
        "Reagents": {
            "Coarse Stone": 8
        }
    },
    "Elegant Silver Ring": {
        "ID":       20818,
        "Learn":    50,
        "Yellow":   80,
        "Green":    95,
        "Grey":     110,
        "Source":   "Trainer",
        "Reagents": {
            "Silver Bar": 1
        }
    },
    "Solid Bronze Ring": {
        "ID":       20907,
        "Learn":    50,
        "Yellow":   80,
        "Green":    95,
        "Grey":     110,
        "Source":   "Trainer",
        "Reagents": {
            "Bronze Bar": 4
        }
    },
    "Thick Bronze Necklace": {
        "ID":       21933,
        "Learn":    50,
        "Yellow":   80,
        "Green":    95,
        "Grey":     110,
        "Source":   "Trainer",
        "Reagents": {
            "Bronze Bar": 2,
			"Shadowgem": 1,
			"Delicate Copper Wire": 1
        }
    },
    "Simple Pearl Ring": {
        "ID":       20820,
        "Learn":    60,
        "Yellow":   90,
        "Green":    105,
        "Grey":     120,
        "Source":   "Trainer",
        "Reagents": {
            "Copper Bar": 2,
			"Small Lustrous Pearl": 1,
			"Bronze Setting": 1
        }
    },
    "Bronze Band of Force": {
        "ID":       30804,
        "Learn":    65,
        "Yellow":   95,
        "Green":    110,
        "Grey":     125,
        "Source":   "Trainer",
        "Reagents": {
            "Malachite": 1,
			"Tigerseye": 3,
			"Bronze Bar": 2,
			"Shadowgem": 2,
			"Bronze Setting": 1
        }
    },
    "Gloom Band": {
        "ID":       20823,
        "Learn":    70,
        "Yellow":   100,
        "Green":    115,
        "Grey":     130,
        "Source":   "Trainer",
        "Reagents": {
            "Shadowgem": 2,
			"Delicate Copper Wire": 2,
			"Bronze Setting": 1
        }
    },
    "Brilliant Necklace": {
        "ID":       30419,
        "Learn":    75,
        "Yellow":   105,
        "Green":    120,
        "Grey":     135,
        "Source":   "Trainer",
        "Reagents": {
            "Bronze Bar": 4,
			"Bronze Setting": 1,
			"Moss Agate": 1
        }
    },
    "Bronze Torc": {
        "ID":       21154,
        "Learn":    80,
        "Yellow":   110,
        "Green":    125,
        "Grey":     140,
        "Source":   "Trainer",
        "Reagents": {
            "Bronze Bar": 6,
			"Bronze Setting": 1,
			"Lesser Moonstone": 1
        }
    },
    "Ring of Silver Might": {
        "ID":       20828,
        "Learn":    80,
        "Yellow":   110,
        "Green":    135,
        "Grey":     150,
        "Source":   "Trainer",
        "Reagents": {
            "Silver Bar": 2
        }
    },
    "Heavy Silver Ring": {
        "ID":       20826,
        "Learn":    90,
        "Yellow":   120,
        "Green":    135,
        "Grey":     150,
        "Source":   "Trainer",
        "Reagents": {
            "Silver Bar": 2,
			"Bronze Setting": 1,
			"Moss Agate": 1,
			"Lesser Moonstone": 1
        }
    },
    "Ring of Twilight Shadow": {
        "ID":       20828,
        "Learn":    100,
        "Yellow":   130,
        "Green":    145,
        "Grey":     160,
        "Source":   "Trainer",
        "Reagents": {
            "Shadowgem": 2,
			"Bronze Bar": 2
        }
    },
    "Heavy Jade Ring": {
        "ID":       30420,
        "Learn":    105,
        "Yellow":   135,
        "Green":    150,
        "Grey":     165,
        "Source":   "Trainer",
        "Reagents": {
            "Iron Bar": 2,
			"Jade": 1,
			"Bronze Setting": 1
        }
    },
    "Heavy Stone Statue": {
        "ID":       25881,
        "Learn":    110,
        "Yellow":   120,
        "Green":    130,
        "Grey":     140,
        "Source":   "Trainer",
        "Reagents": {
            "Heavy Stone": 8
        }
    },
    "Amulet of the Moon": {
        "ID":       20830,
        "Learn":    110,
        "Yellow":   140,
        "Green":    155,
        "Grey":     170,
        "Source":   "VendorLimited",
		"RecipeID": 20854,
        "Reagents": {
            "Lesser Moonstone": 2,
			"Bronze Setting": 1
        }
    },
    "Barbaric Iron Collar": {
        "ID":       20909,
        "Learn":    110,
        "Yellow":   140,
        "Green":    155,
        "Grey":     170,
        "Source":   "Trainer",
        "Reagents": {
            "Iron Bar": 8,
			"Large Fang": 2,
			"Bronze Setting": 2
        }
    },
    "Moonsoul Crown": {
        "ID":       20832,
        "Learn":    110,
        "Yellow":   150,
        "Green":    165,
        "Grey":     180,
        "Source":   "Trainer",
        "Reagents": {
            "Soul Dust": 4,
			"Silver Bar": 4,
			"Lesser Moonstone": 3,
			"Small Lustrous Pearl": 3,
			"Mana Potion": 2
        }
    },
    "Pendant of the Agate Shield": {
        "ID":       20950,
        "Learn":    120,
        "Yellow":   150,
        "Green":    165,
        "Grey":     180,
        "Source":   "VendorLimited",
		"RecipeID": 20970,
        "Reagents": {
            "Moss Agate": 1,
			"Bronze Setting": 1
        }
    },
    "Heavy Iron Knuckles": {
        "ID":       20954,
        "Learn":    125,
        "Yellow":   155,
        "Green":    170,
        "Grey":     185,
        "Source":   "VendorLimited",
		"RecipeID": 20971,
        "Reagents": {
            "Iron Bar": 8,
			"Elixir of Ogres Strength": 2
        }
    },
    "Wicked Moonstone Ring": {
        "ID":       20833,
        "Learn":    125,
        "Yellow":   155,
        "Green":    170,
        "Grey":     185,
        "Source":   "VendorLimited",
		"RecipeID": 20855,
        "Reagents": {
            "Iron Bar": 4,
			"Lesser Moonstone": 1,
			"Shadow Oil": 1
        }
    },
    "Golden Dragon Ring": {
        "ID":       20955,
        "Learn":    135,
        "Yellow":   165,
        "Green":    180,
        "Grey":     195,
        "Source":   "Trainer",
        "Reagents": {
            "Gold Bar": 2,
			"Delicate Copper Wire": 2,
			"Jade": 1
        }
    },
    "Mithril Filigree": {
        "ID":       20963,
        "Learn":    150,
        "Yellow":   170,
        "Green":    180,
        "Grey":     190,
        "Source":   "Trainer",
        "Reagents": {
            "Mithril Bar": 2
        }
    },
    "Blazing Citrine Ring": {
        "ID":       20958,
        "Learn":    150,
        "Yellow":   180,
        "Green":    195,
        "Grey":     210,
        "Source":   "VendorLimited",
		"RecipeID": 20973,
        "Reagents": {
            "Heavy Stone": 8
        }
    },
    "Heavy Golden Necklace of Battle": {
        "ID":       20931,
        "Learn":    150,
        "Yellow":   180,
        "Green":    195,
        "Grey":     210,
        "Source":   "VendorLimited",
        "Reagents": {
            "Moss Agate": 2,
			"Gold Bar": 1,
			"Elixir of Ogres Strength": 1
        }
    },
    "Jade Pendant of Blasting": {
        "ID":       20966,
        "Learn":    160,
        "Yellow":   190,
        "Green":    205,
        "Grey":     220,
        "Source":   "Drop",
		"RecipeID": 20974,
        "Reagents": {
            "Mithril Filigree": 2,
			"Jade": 1
        }
    },
    "Engraved Truesilver Ring": {
        "ID":       20960,
        "Learn":    170,
        "Yellow":   200,
        "Green":    215,
        "Grey":     230,
        "Source":   "Trainer",
        "Reagents": {
            "Mithril Filigree": 2,
			"Truesilver Bar": 1
        }
    },
    "The Jade Eye": {
        "ID":       20959,
        "Learn":    170,
        "Yellow":   200,
        "Green":    215,
        "Grey":     230,
        "Source":   "VendorLimited",
		"RecipeID": 20975,
        "Reagents": {
            "Elemental Earth ": 2,
			"Jade": 1
        }
    },
    "Solid Stone Statue": {
        "ID":       25882,
        "Learn":    175,
        "Yellow":   175,
        "Green":    185,
        "Grey":     195,
        "Source":   "Trainer",
        "Reagents": {
            "Solid Stone": 10
        }
    },
    "Golden Ring or Power": {
        "ID":       29157,
        "Learn":    180,
        "Yellow":   190,
        "Green":    200,
        "Grey":     210,
        "Source":   "Trainer",
        "Reagents": {
            "Gold Bar": 4,
			"Jade": 1,
			"Lesser Moonstone": 1,
			"Citrine": 1
        }
    },
    "Citrine Ring of Rapid Healing": {
        "ID":       20961,
        "Learn":    180,
        "Yellow":   210,
        "Green":    225,
        "Grey":     240,
        "Source":   "Trainer",
        "Reagents": {
            "Citrine": 1,
            "Elemental Water": 2,
            "Mithril Bar": 2
        }
    },
    "Citrine Pendant of Golden Healing": {
        "ID":       20967,
        "Learn":    190,
        "Yellow":   220,
        "Green":    235,
        "Grey":     250,
        "Source":   "Drop",
		"RecipeID": 20976,
        "Reagents": {
            "Elemental Water": 2,
			"Gold Bar": 2,
			"Citrine": 1,
			"Bronze Setting":  1
        }
    },
    "Amulet of Truesight": {
        "ID":       45627,
        "Learn":    200,
        "Yellow":   210,
        "Green":    220,
        "Grey":     230,
        "Source":   "Trainer",
        "Reagents": {
            "Truesilver Bar": 8
        }
    },
    "Truesilver Commanders Ring": {
        "ID":       29158,
        "Learn":    200,
        "Yellow":   210,
        "Green":    220,
        "Grey":     230,
        "Source":   "Trainer",
        "Reagents": {
            "Truesilver Bar": 3,
			"Star Ruby": 2,
			"Citrine": 2
        }
    },
    "Figurine - Golden Hare": {
        "ID":       21756,
        "Learn":    200,
        "Yellow":   225,
        "Green":    240,
        "Grey":     255,
        "Source":   "Drop",
		"RecipeID": 21940,
        "Reagents": {
            "Gold Bar": 6,
			"Citrine": 2
        }
    },
    "Figurine - Jade Owl": {
        "ID":       21748,
        "Learn":    200,
        "Yellow":   225,
        "Green":    240,
        "Grey":     255,
        "Source":   "Trainer",
        "Reagents": {
            "Jade": 4,
			"Vision Dust": 4,
			"Mithril Filigree": 4,
			"Truesilver Bar": 2
        }
    },
    "Aquamarine Signet": {
        "ID":       20964,
        "Learn":    210,
        "Yellow":   235,
        "Green":    250,
        "Grey":     265,
        "Source":   "Trainer",
        "Reagents": {
            "Flask of Mojo": 4,
			"Aquamarine": 3
        }
    },
    "Figurine - Black Pearl Panther": {
        "ID":       21758,
        "Learn":    215,
        "Yellow":   240,
        "Green":    255,
        "Grey":     270,
        "Source":   "VendorLimited",
		"RecipeID": 21941,
        "Reagents": {
            "Black Pearl": 4,
			"Flask of Mojo": 4
        }
    },
    "Aquamarine Pendant of the Warrior": {
        "ID":       21755,
        "Learn":    220,
        "Yellow":   245,
        "Green":    260,
        "Grey":     275,
        "Source":   "Trainer",
        "Reagents": {
            "Mithril Filigree": 3,
			"Aquamarine": 1
        }
    },
    "Dense Stone Statue": {
        "ID":       25883,
        "Learn":    225,
        "Yellow":   225,
        "Green":    235,
        "Grey":     250,
        "Source":   "Trainer",
        "Reagents": {
            "Dense Stone": 10
        }
    },
    "Thorium Setting": {
        "ID":       21752,
        "Learn":    225,
        "Yellow":   235,
        "Green":    250,
        "Grey":     255,
        "Source":   "Trainer",
        "Reagents": {
            "Thorium Bar": 1
        }
    },
    "Figurine - Truesilver Crab": {
        "ID":       21760,
        "Learn":    225,
        "Yellow":   250,
        "Green":    265,
        "Grey":     280,
        "Source":   "VendorLimited",
		"RecipeID": 21943,
        "Reagents": {
            "Truesilver Bar": 4,
			"Flask of Mojo": 4,
			"Core of Earth": 2,
			"Aquamarine": 2,
			"Globe of Water": 2
        }
    },
    "Ruby Crown of Restoration": {
        "ID":       20969,
        "Learn":    225,
        "Yellow":   250,
        "Green":    265,
        "Grey":     280,
        "Source":   "VendorLimited",
		"RecipeID": 21942,
        "Reagents": {
            "Greater Mana Potion": 4,
			"Truesilver Bar": 4,
			"Thorium Setting": 4,
			"Star Ruby": 2,
			"Black Pearl": 2
        }
    },
    "Red Ring of Destruction": {
        "ID":       30421,
        "Learn":    230,
        "Yellow":   255,
        "Green":    270,
        "Grey":     285,
        "Source":   "Trainer",
        "Reagents": {
            "Star Ruby": 1,
			"Thorium Bar": 1
        }
    },
    "Figurine - Truesilver Boar": {
        "ID":       21763,
        "Learn":    235,
        "Yellow":   260,
        "Green":    275,
        "Grey":     285,
        "Source":   "Drop",
		"RecipeID": 21944,
        "Reagents": {
            "Truesilver Bar": 4,
			"Flask of Mojo": 4,
			"Heart of Fire": 2,
			"Star Ruby": 2,
			"Breath of Wind": 2
        }
    },
    "Ruby Pendant of Fire": {
        "ID":       21764,
        "Learn":    235,
        "Yellow":   260,
        "Green":    275,
        "Grey":     290,
        "Source":   "Trainer",
        "Reagents": {
            "Star Ruby": 1,
			"Thorium Setting": 1
        }
    },
    "Truesilver Healing Ring": {
        "ID":       21765,
        "Learn":    240,
        "Yellow":   265,
        "Green":    280,
        "Grey":     295,
        "Source":   "Trainer",
        "Reagents": {
            "Truesilver Bar": 2,
			"Heart of the Wild": 2
        }
    },
    "The Aquamarine Ward": {
        "ID":       21754,
        "Learn":    245,
        "Yellow":   270,
        "Green":    285,
        "Grey":     300,
        "Source":   "Drop",
		"RecipeID": 21945,
        "Reagents": {
            "Aquamarine": 1,
			"Thorium Setting": 1
        }
    },
    "Gem Studded Band": {
        "ID":       21753,
        "Learn":    250,
        "Yellow":   275,
        "Green":    290,
        "Grey":     305,
        "Source":   "Drop",
		"RecipeID": 21947,
        "Reagents": {
            "Thorium Setting": 4,
			"Truesilver Bar": 2,
			"Aquamarine": 2,
			"Citrine": 2
        }
    },
    "Opal Necklace of Impact": {
        "ID":       21766,
        "Learn":    250,
        "Yellow":   275,
        "Green":    290,
        "Grey":     305,
        "Source":   "VendorLImited",
		"RecipeID": 21948,
        "Reagents": {
            "Truesilver Bar": 4,
			"Large Opal": 2,
			"Large Radiant Shard": 2,
			"Thorium Setting": 2,
			"Mithril Filigree": 2
        }
    },
    "Figurine - Ruby Serpent": {
        "ID":       21769,
        "Learn":    260,
        "Yellow":   280,
        "Green":    290,
        "Grey":     305,
        "Source":   "Drop",
		"RecipeID": 21949,
        "Reagents": {
            "Flask of Big Mojo": 4,
			"Truesilver Bar": 2,
			"Essence of Fire": 2,
			"Star Ruby": 2
        }
    },
    "Simple Opal Ring": {
        "ID":       21767,
        "Learn":    260,
        "Yellow":   280,
        "Green":    290,
        "Grey":     300,
        "Source":   "Trainer",
        "Reagents": {
            "Large Opal": 1,
			"Thorium Setting": 1
        }
    },
    "Diamond Focus Ring": {
        "ID":       30422,
        "Learn":    265,
        "Yellow":   285,
        "Green":    295,
        "Grey":     305,
        "Source":   "Trainer",
        "Reagents": {
            "Azerothian Diamond": 1,
			"Thorium Setting": 1
        }
    },
    "Emerald Crown of Destruction": {
        "ID":       21774,
        "Learn":    275,
        "Yellow":   285,
        "Green":    295,
        "Grey":     305,
        "Source":   "VendorLimited",
		"RecipeID": 21952,
        "Reagents": {
            "Huge Emerald": 2,
			"Large Opal": 2,
			"Blue Sapphire": 2,
			"Arcanite Bar": 2,
			"Thorium Bar": 2
        }
    },
    "Sapphire Signet": {
        "ID":       21768,
        "Learn":    275,
        "Yellow":   285,
        "Green":    295,
        "Grey":     305,
        "Source":   "Trainer",
        "Reagents": {
            "Truesilver Bar": 2,
			"Blue Sapphire": 4,
			"Thorium Setting": 1
        }
    },
    "Glowing Thorium Band": {
        "ID":       29159,
        "Learn":    280,
        "Yellow":   290,
        "Green":    300,
        "Grey":     310,
        "Source":   "Trainer",
        "Reagents": {
            "Azerothian Diamond": 2,
			"Thorium Setting": 1
        }
    },
    "Onslaught Ring": {
        "ID":       21775,
        "Learn":    280,
        "Yellow":   290,
        "Green":    300,
        "Grey":     310,
        "Source":   "Trainer",
        "Reagents": {
            "Powerful Mojo": 1,
			"Essence of Earth": 1,
			"Thorium Setting": 1
        }
    },
    "Sapphire Pendant of Winter Night": {
        "ID":       21790,
        "Learn":    280,
        "Yellow":   290,
        "Green":    300,
        "Grey":     310,
        "Source":   "Trainer",
        "Reagents": {
            "Essence of Undeath": 1,
			"Blue Sapphire": 1,
			"Thorium Setting": 1
        }
    },
    "Figurine - Emerald Owl": {
        "ID":       21777,
        "Learn":    285,
        "Yellow":   295,
        "Green":    305,
        "Grey":     310,
        "Source":   "Drop",
		"RecipeID": 21953,
        "Reagents": {
            "Powerful Mojo": 4,
			"Huge Emerald": 2,
			"Arcanite Bar": 2,
			"Thorium Bar": 2
        }
    },
    "Emerald Lion Ring": {
        "ID":       29160,
        "Learn":    290,
        "Yellow":   300,
        "Green":    310,
        "Grey":     315,
        "Source":   "Trainer",
        "Reagents": {
            "Huge Emerald": 2,
			"Thorium Setting": 1
        }
    },
    "Living Emerald Pendant": {
        "ID":       21791,
        "Learn":    290,
        "Yellow":   300,
        "Green":    310,
        "Grey":     320,
        "Source":   "Trainer",
        "Reagents": {
            "Powerful Mojo": 4,
			"Living Essence": 4,
			"Huge Emerald": 2
        }
    }
}

# Sort dictionary by key
recipes = {k: recipes[k] for k in sorted(recipes)}

import json
with open('jewelcrafting.json', 'w') as jsonFile:
    json.dump(recipes, jsonFile)
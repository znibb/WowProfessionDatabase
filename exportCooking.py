#!/usr/bin/env python3.7

recipes = {
    "Baked Salmon": {
        "ID":       13935,
        "Learn":    275,
        "Yellow":   315,
        "Green":    335,
        "Grey":     355,
        "Source":   "Vendor",
        "RecipeID": 13949,
        "Reagents": {
            "Raw Whitescale Salmon": 1,
            "Soothing Spices": 1
        },
        "AmountCrafted": 1,
        "Phase":    1
    },
    "Barbecued Buzzard Wing": {
        "ID":       4457,
        "Learn":    175,
        "Yellow":   215,
        "Green":    235,
        "Grey":     255,
        "Source":   "Vendor",
        "RecipeID": 4609,
        "Reagents": {
            "Buzzard Wing": 1,
            "Hot Spices": 1
        },
        "AmountCrafted": 1,
        "Phase":    1
    },
    "Bat Bites": {
        "ID":       27636,
        "Learn":    50,
        "Yellow":   90,
        "Green":    110,
        "Grey":     130,
        "Source":   "Vendor",
        "Faction":  "Horde",
        "RecipeID": 27687,
        "Reagents": {
            "Bat Flesh": 1
        },
        "AmountCrafted": 1,
        "Phase":    1
    },
    "Beer Basted Boar Ribs": {
        "ID":       2888,
        "Learn":    25,
        "Yellow":   60,
        "Green":    80,
        "Grey":     100,
        "Source":   "Quest",
        "Faction":  "Alliance",
        "RecipeID": 2889,
        "Reagents": {
            "Crag Boar Rib": 1
        },
        "AmountCrafted": 1,
        "Phase":    1
    },
    "Big Bear Steak": {
        "ID":       3726,
        "Learn":    110,
        "Yellow":   150,
        "Green":    170,
        "Grey":     190,
        "Source":   "VendorLimited",
        "RecipeID": 3734,
        "Reagents": {
            "Big Bear Meat": 1,
            "Hot Spices": 1
        },
        "AmountCrafted": 1,
        "Phase":    1
    },
    "Blackened Basilisk": {
        "ID":       27657,
        "Learn":    315,
        "Yellow":   335,
        "Green":    345,
        "Grey":     355,
        "Source":   "Vendor",
        "RecipeID": 27690,
        "Reagents": {
            "Chunk o Basilisk": 1
        },
        "AmountCrafted": 1,
        "Phase":    1
    },
    "Blackened Sporefish": {
        "ID":       27663,
        "Learn":    310,
        "Yellow":   330,
        "Green":    340,
        "Grey":     350,
        "Source":   "Vendor",
        "RecipeID": 27696,
        "Reagents": {
            "Zangarian Sporefish": 1
        },
        "AmountCrafted": 1,
        "Phase":    1
    },
    "Blackened Trout": {
        "ID":       27661,
        "Learn":    300,
        "Yellow":   320,
        "Green":    330,
        "Grey":     340,
        "Source":   "Reputation",
        "RecipeID": 27694,
        "Reagents": {
            "Chunk o Basilisk": 1
        },
        "AmountCrafted": 1,
        "Phase":    1
    },
    "Blood Sausage": {
        "ID":       3220,
        "Learn":    60,
        "Yellow":   100,
        "Green":    120,
        "Grey":     140,
        "Source":   "Vendor",
        "Faction":  "Alliance",
        "RecipeID": 3679,
        "Reagents": {
            "Bear Meat": 1,
            "Boar Intestines": 1,
            "Spider Ichor": 1
        },
        "AmountCrafted": 2,
        "Phase":    1
    },
    "Boiled Clams": {
        "ID":       5525,
        "Learn":    50,
        "Yellow":   90,
        "Green":    110,
        "Grey":     130,
        "Source":   "Trainer",
        "Reagents": {
            "Clam Meat": 1,
            "Refreshing Spring Water": 1
        },
        "AmountCrafted": 1,
        "Phase":    1
    },
    "Brilliant Smallfish": {
        "ID":       6290,
        "Learn":    1,
        "Yellow":   45,
        "Green":    65,
        "Grey":     85,
        "Source":   "Vendor",
        "RecipeID": 6325,
        "Reagents": {
            "Raw Brilliant Smallfish": 1
        },
        "AmountCrafted": 1,
        "Phase":    1
    },
    "Bristle Whisker Catfish": {
        "ID":       4593,
        "Learn":    100,
        "Yellow":   140,
        "Green":    160,
        "Grey":     180,
        "Source":   "Vendor",
        "RecipeID": 6330,
        "Reagents": {
            "Raw Bristle Whisker Catfish": 1
        },
        "AmountCrafted": 1,
        "Phase":    1
    },
    "Broiled Bloodfin": {
        "ID":       33867,
        "Learn":    300,
        "Yellow":   320,
        "Green":    330,
        "Grey":     340,
        "Source":   "Vendor",
        "RecipeID": 33869,
        "Reagents": {
            "Bloodfin Catfish": 1
        },
        "AmountCrafted": 1,
        "Phase":    1
    },
    "Buzzard Bites": {
        "ID":       27651,
        "Learn":    330,
        "Yellow":   320,
        "Green":    330,
        "Grey":     340,
        "Source":   "Quest",
        "Faction":  "Alliance",
        "RecipeID": 27684,
        "Reagents": {
            "Buzzard Meat": 1
        },
        "AmountCrafted": 1,
        "Phase":    1
    },
    "Captain Rumseys Lager": {
        "ID":       34832,
        "Learn":    100,
        "Yellow":   100,
        "Green":    105,
        "Grey":     110,
        "Source":   "Vendor",
        "RecipeID": 34834,
        "Reagents": {
            "Skin of Dwarven Stout": 1,
            "Flagon of Dwarven Honeymead": 1
        },
        "AmountCrafted": 5,
        "Phase":    1
    },
    "Carrion Surprise": {
        "ID":       12213,
        "Learn":    175,
        "Yellow":   215,
        "Green":    235,
        "Grey":     255,
        "Source":   "Vendor",
        "RecipeID": 12232,
        "Reagents": {
            "Mystery Meat": 1,
            "Hot Spices": 1
        },
        "AmountCrafted": 1,
        "Phase":    1
    },
    "Charred Bear Kabobs": {
        "ID":       35563,
        "Learn":    350,
        "Yellow":   375,
        "Green":    385,
        "Grey":     395,
        "Source":   "Vendor",
        "RecipeID": 35564,
        "Reagents": {
            "Bear Flank": 1
        },
        "AmountCrafted": 1,
        "Phase":    1
    },
    "Charred Wolf Meat": {
        "ID":       2679,
        "Learn":    1,
        "Yellow":   45,
        "Green":    65,
        "Grey":     85,
        "Source":   "Trainer",
        "Reagents": {
            "Stringy Wolf Meat": 1
        },
        "AmountCrafted": 1,
        "Phase":    1
    },
    "Clam Bar": {
        "ID":       30155,
        "Learn":    300,
        "Yellow":   320,
        "Green":    330,
        "Grey":     340,
        "Source":   "Vendor",
        "RecipeID": 30156,
        "Reagents": {
            "Jaggal Clam Meat": 2,
            "Soothing Spices": 1
        },
        "AmountCrafted": 1,
        "Phase":    1
    },
    "Clam Chowder": {
        "ID":       5526,
        "Learn":    90,
        "Yellow":   130,
        "Green":    150,
        "Grey":     170,
        "Source":   "Vendor",
        "Faction":  "Alliance",
        "RecipeID": 5528,
        "Reagents": {
            "Clam Meat": 1,
            "Ice Cold Milk": 1,
            "Mild Spices": 1,
        },
        "AmountCrafted": 1,
        "Phase":    1
    },
    "Cooked Crab Claw": {
        "ID":       2682,
        "Learn":    85,
        "Yellow":   125,
        "Green":    145,
        "Grey":     165,
        "Source":   "Drop",
        "RecipeID": 2698,
        "Reagents": {
            "Crawler Claw": 1,
            "Mild Spices": 1
        },
        "AmountCrafted": 1,
        "Phase":    1
    },
    "Cooked Glossy Mightfish": {
        "ID":       13927,
        "Learn":    225,
        "Yellow":   265,
        "Green":    285,
        "Grey":     305,
        "Source":   "Vendor",
        "RecipeID": 13940,
        "Reagents": {
            "Raw Glossy Mightfish": 1,
            "Soothing Spices": 1
        },
        "AmountCrafted": 1,
        "Phase":    1
    },
    "Coyote Steak": {
        "ID":       2684,
        "Learn":    50,
        "Yellow":   90,
        "Green":    110,
        "Grey":     130,
        "Source":   "Trainer",
        "Reagents": {
            "Coyote Meat": 1
        },
        "AmountCrafted": 1,
        "Phase":    1
    },
    "Crab Cake": {
        "ID":       2683,
        "Learn":    75,
        "Yellow":   115,
        "Green":    135,
        "Grey":     155,
        "Source":   "Trainer",
        "Reagents": {
            "Crawler Meat": 1,
            "Mild Spices": 1
        },
        "AmountCrafted": 1,
        "Phase":    1
    },
    "Crispy Bat Wing": {
        "ID":       12224,
        "Learn":    1,
        "Yellow":   45,
        "Green":    65,
        "Grey":     85,
        "Source":   "Vendor",
        "Faction":  "Horde",
        "RecipeID": 12226,
        "Reagents": {
            "Meaty Bat Wing": 1,
            "Mild Spices": 1
        },
        "AmountCrafted": 1,
        "Phase":    1
    },
    "Crispy Lizard Tail": {
        "ID":       5479,
        "Learn":    100,
        "Yellow":   140,
        "Green":    160,
        "Grey":     180,
        "Source":   "Vendor",
        "Faction":  "Horde",
        "RecipeID": 5488,
        "Reagents": {
            "Thunder Lizard Tail": 1,
            "Hot Spices": 1
        },
        "AmountCrafted": 2,
        "Phase":    1
    },
    "Crocolisk Gumbo": {
        "ID":       3664,
        "Learn":    120,
        "Yellow":   160,
        "Green":    180,
        "Grey":     200,
        "Source":   "Vendor",
        "Faction":  "Alliance",
        "RecipeID": 3681,
        "Reagents": {
            "Tender Crocolisk Meat": 1,
            "Hot Spices": 1
        },
        "AmountCrafted": 1,
        "Phase":    1
    },
    "Crocolisk Steak": {
        "ID":       3662,
        "Learn":    80,
        "Yellow":   120,
        "Green":    140,
        "Grey":     160,
        "Source":   "Vendor",
        "Faction":  "Alliance",
        "RecipeID": 3678,
        "Reagents": {
            "Crocolisk Meat": 1,
            "Mild Spices": 1
        },
        "AmountCrafted": 1,
        "Phase":    1
    },
    "Crunchy Serpent": {
        "ID":       31673,
        "Learn":    335,
        "Yellow":   355,
        "Green":    365,
        "Grey":     375,
        "Source":   "Vendor",
        "RecipeID": 31674,
        "Reagents": {
            "Serpent Flesh": 1
        },
        "AmountCrafted": 1,
        "Phase":    1
    },
    "Crunshy Spider Surprise": {
        "ID":       22645,
        "Learn":    60,
        "Yellow":   100,
        "Green":    120,
        "Grey":     140,
        "Source":   "Quest",
        "Faction":  "Horde",
        "RecipeID": 22647,
        "Reagents": {
            "Crunchy Spider Leg": 1
        },
        "AmountCrafted": 1,
        "Phase":    1
    },
    "Curiously Tasty Omelet": {
        "ID":       3665,
        "Learn":    130,
        "Yellow":   170,
        "Green":    190,
        "Grey":     210,
        "Source":   "Vendor",
        "RecipeID": 3682,
        "Reagents": {
            "Raptor Egg": 1,
            "Hot Spices": 1
        },
        "AmountCrafted": 1,
        "Phase":    1
    },
    "Delicious Chocolate Cake": {
        "ID":       33924,
        "Learn":    1,
        "Yellow":   50,
        "Green":    62,
        "Grey":     75,
        "Source":   "Quest",
        "RecipeID": 33925,
        "Reagents": {
            "Simple Flour": 8,
            "Ice Cold Milk": 4,
            "Mild Spices": 4,
            "Small Egg": 8,
            "Flask of Stormwind Tawny": 1,
            "Mageroyal": 3
        },
        "AmountCrafted": 1,
        "Phase":    1
    },
    "Dig Rat Stew": {
        "ID":       5478,
        "Learn":    90,
        "Yellow":   130,
        "Green":    150,
        "Grey":     170,
        "Source":   "Quest",
        "Faction":  "Horde",
        "RecipeID": 5487,
        "Reagents": {
            "Dig Rat": 1
        },
        "AmountCrafted": 2,
        "Phase":    1
    },
    "Dragonbreath Chili": {
        "ID":       12217,
        "Learn":    200,
        "Yellow":   240,
        "Green":    260,
        "Grey":     280,
        "Source":   "Vendor",
        "RecipeID": 12239,
        "Reagents": {
            "Mystery Meat": 1,
            "Small Flame Sac": 1,
            "Hot Spices": 1
        },
        "AmountCrafted": 1,
        "Phase":    1
    },
    "Dry Pork Ribs": {
        "ID":       2687,
        "Learn":    80,
        "Yellow":   120,
        "Green":    140,
        "Grey":     160,
        "Source":   "Trainer",
        "Reagents": {
            "Boar Ribs": 1,
            "Mild Spices": 1
        },
        "AmountCrafted": 1,
        "Phase":    1
    },
    "Egg Nog": {
        "ID":       17198,
        "Learn":    35,
        "Yellow":   75,
        "Green":    95,
        "Grey":     115,
        "Source":   "Seasonal",
        "RecipeID": 17201,
        "Reagents": {
            "Small Egg": 1,
            "Ice Cold Milk": 1,
            "Holiday Spirits": 1,
            "Holiday Spices": 1
        },
        "AmountCrafted": 1,
        "Phase":    1
    },
    "Feltail Delight": {
        "ID":       27662,
        "Learn":    300,
        "Yellow":   320,
        "Green":    330,
        "Grey":     340,
        "Source":   "Vendor",
        "RecipeID": 27695,
        "Reagents": {
            "Spotted Feltail": 1
        },
        "AmountCrafted": 1,
        "Phase":    1
    },
    "Filet of Redgill": {
        "ID":       13930,
        "Learn":    225,
        "Yellow":   265,
        "Green":    285,
        "Grey":     305,
        "Source":   "Vendor",
        "RecipeID": 13941,
        "Reagents": {
            "Raw Redgill": 1
        },
        "AmountCrafted": 1,
        "Phase":    1
    },
    "Fillet of Frenzy": {
        "ID":       5476,
        "Learn":    50,
        "Yellow":   90,
        "Green":    110,
        "Grey":     130,
        "Source":   "Vendor",
        "Faction":  "Alliance",
        "RecipeID": 5485,
        "Reagents": {
            "Soft Frenzy Fish": 1,
            "Mild Spices": 1
        },
        "AmountCrafted": 2,
        "Phase":    1
    },
    "Fishermans Feast": {
        "ID":       33052,
        "Learn":    350,
        "Yellow":   375,
        "Green":    380,
        "Grey":     385,
        "Source":   "Trainer",
        "Reagents": {
            "Huge Spotted Feltail": 1,
            "Goldenbark Apple": 5,
            "Soothing Spices": 5
        },
        "AmountCrafted": 6,
        "Phase":    1
    },
    "Giant Clam Scorcho": {
        "ID":       6038,
        "Learn":    175,
        "Yellow":   215,
        "Green":    235,
        "Grey":     255,
        "Source":   "Vendor",
        "RecipeID": 6039,
        "Reagents": {
            "Giant Clam Meat": 1,
            "Hot Spices": 1
        },
        "AmountCrafted": 1,
        "Phase":    1
    },
    "Gingerbread Cookie": {
        "ID":       17197,
        "Learn":    1,
        "Yellow":   45,
        "Green":    65,
        "Grey":     85,
        "Source":   "Seasonal",
        "RecipeID": 17200,
        "Reagents": {
            "Small Egg": 1,
            "Holiday Spices": 1
        },
        "AmountCrafted": 1,
        "Phase":    1
    },
    "Goblin Deviled Clams": {
        "ID":       5527,
        "Learn":    125,
        "Yellow":   165,
        "Green":    185,
        "Grey":     205,
        "Source":   "Trainer",
        "Reagents": {
            "Tangy Clam Meat": 1,
            "Hot Spices": 1
        },
        "AmountCrafted": 1,
        "Phase":    1
    },
    "Golden Fish Sticks": {
        "ID":       37666,
        "Learn":    325,
        "Yellow":   345,
        "Green":    355,
        "Grey":     365,
        "Source":   "Vendor",
        "RecipeID": 27699,
        "Reagents": {
            "Golden Darter": 1
        },
        "AmountCrafted": 1,
        "Phase":    1
    },
    "Goldthorn Tea": {
        "ID":       10841,
        "Learn":    175,
        "Yellow":   215,
        "Green":    235,
        "Grey":     255,
        "Source":   "Quest",
        "Faction":  "Any",
        "RecipeID": 10841,
        "Reagents": {
            "Goldthorn": 1,
            "Refreshing Spring Water": 1
        },
        "AmountCrafted": 4,
        "Phase":    1
    },
    "Gooey Spider Cake": {
        "ID":       3666,
        "Learn":    110,
        "Yellow":   150,
        "Green":    170,
        "Grey":     190,
        "Source":   "Vendor",
        "Faction":  "Alliance",
        "RecipeID": 3683,
        "Reagents": {
            "Gooey Spider Leg": 2,
            "Hot Spices": 1
        },
        "AmountCrafted": 1,
        "Phase":    1
    },
    "Goretusk Liver Pie": {
        "ID":       724,
        "Learn":    50,
        "Yellow":   90,
        "Green":    110,
        "Grey":     130,
        "Source":   "Vendor",
        "Faction":  "Alliance",
        "RecipeID": 2697,
        "Reagents": {
            "Goretusk Liver": 1,
            "Mild Spices": 1
        },
        "AmountCrafted": 1,
        "Phase":    1
    },
    "Grilled Mudfish": {
        "ID":       27664,
        "Learn":    320,
        "Yellow":   340,
        "Green":    350,
        "Grey":     360,
        "Source":   "Vendor",
        "RecipeID": 27697,
        "Reagents": {
            "Figlusters Midfish": 1
        },
        "AmountCrafted": 1,
        "Phase":    1
    },
    "Grilled Squid": {
        "ID":       13928,
        "Learn":    240,
        "Yellow":   280,
        "Green":    300,
        "Grey":     320,
        "Source":   "Vendor",
        "RecipeID": 13942,
        "Reagents": {
            "Winter Squid": 1,
            "Soothing Spices": 1
        },
        "AmountCrafted": 1,
        "Phase":    1
    },
    "Heavy Crocolisk Stew": {
        "ID":       20074,
        "Learn":    150,
        "Yellow":   160,
        "Green":    180,
        "Grey":     200,
        "Source":   "Vendor",
        "Faction":  "Horde",
        "RecipeID": 20075,
        "Reagents": {
            "Tender Crocolisk Meat": 2,
            "Soothing Spices": 1
        },
        "AmountCrafted": 1,
        "Phase":    1
    },
    "Heavy Kodo Stew": {
        "ID":       12215,
        "Learn":    200,
        "Yellow":   240,
        "Green":    260,
        "Grey":     280,
        "Source":   "Vendor",
        "RecipeID": 12240,
        "Reagents": {
            "Heavy Kodo Meat": 2,
            "Soothing Spices": 1,
            "Refreshing Spring Water": 1
        },
        "AmountCrafted": 2,
        "Phase":    1
    },
    "Herb Baked Egg": {
        "ID":       6888,
        "Learn":    1,
        "Yellow":   45,
        "Green":    65,
        "Grey":     85,
        "Source":   "Trainer",
        "Reagents": {
            "Small Egg": 1,
            "Mild Spices": 1
        },
        "AmountCrafted": 1,
        "Phase":    1
    },
    "Hot Apple Cider": {
        "ID":       34411,
        "Learn":    325,
        "Yellow":   325,
        "Green":    325,
        "Grey":     325,
        "Source":   "Seasonal",
        "RecipeID": 34413,
        "Reagents": {
            "Sparkling Apple Cider": 1,
            "Holiday Spirits": 1,
            "Holiday Spices": 1
        },
        "AmountCrafted": 2,
        "Phase":    1
    },
    "Hot Buttered Trout": {
        "ID":       33053,
        "Learn":    350,
        "Yellow":   375,
        "Green":    380,
        "Grey":     385,
        "Source":   "Trainer",
        "Reagents": {
            "Enormous Barbed Gill Trout": 1,
            "Soothing Spices": 2
        },
        "AmountCrafted": 2,
        "Phase":    1
    },
    "Hot Lion Chops": {
        "ID":       3727,
        "Learn":    125,
        "Yellow":   175,
        "Green":    195,
        "Grey":     215,
        "Source":   "Vendor",
        "RecipeID": 3735,
        "Reagents": {
            "Lion Meat": 1,
            "Hot Spices": 1
        },
        "AmountCrafted": 1,
        "Phase":    1
    },
    "Hot Smoked Bass": {
        "ID":       13929,
        "Learn":    240,
        "Yellow":   280,
        "Green":    300,
        "Grey":     320,
        "Source":   "Vendor",
        "RecipeID": 13943,
        "Reagents": {
            "Raw Summer Bass": 1,
            "Hot Spices": 2
        },
        "AmountCrafted": 1,
        "Phase":    1
    },
    "Hot Wolf Ribs": {
        "ID":       13851,
        "Learn":    175,
        "Yellow":   215,
        "Green":    235,
        "Grey":     255,
        "Source":   "Vendor",
        "RecipeID": 12229,
        "Reagents": {
            "Red Wolf Meat": 1,
            "Hot Spices": 1
        },
        "AmountCrafted": 1,
        "Phase":    1
    },
    "Juicy Bear Burger": {
        "ID":       35565,
        "Learn":    250,
        "Yellow":   275,
        "Green":    285,
        "Grey":     295,
        "Source":   "Vendor",
        "RecipeID": 35566,
        "Reagents": {
            "Bear Flank": 1
        },
        "AmountCrafted": 1,
        "Phase":    1
    },
    "Jungle Stew": {
        "ID":       12212,
        "Learn":    175,
        "Yellow":   215,
        "Green":    235,
        "Grey":     255,
        "Source":   "Vendor",
        "RecipeID": 12231,
        "Reagents": {
            "Tiger Meat": 1,
            "Refreshing Spring Water": 1,
            "Shiny Red Apple": 2
        },
        "AmountCrafted": 2,
        "Phase":    1
    },
    "Kaldorei Spider Kabob": {
        "ID":       5472,
        "Learn":    10,
        "Yellow":   50,
        "Green":    70,
        "Grey":     90,
        "Source":   "Quest",
        "Faction":  "Alliance",
        "RecipeID": 5482,
        "Reagents": {
            "Small Spider Leg": 1
        },
        "AmountCrafted": 1,
        "Phase":    1
    },
    "Kiblers Bits": {
        "ID":       33874,
        "Learn":    300,
        "Yellow":   345,
        "Green":    355,
        "Grey":     365,
        "Source":   "Quest",
        "RecipeID": 33875,
        "Reagents": {
            "Buzzard Meat": 1
        },
        "AmountCrafted": 1,
        "Phase":    1
    },
    "Lean Venison": {
        "ID":       5480,
        "Learn":    110,
        "Yellow":   150,
        "Green":    170,
        "Grey":     190,
        "Source":   "Vendor",
        "RecipeID": 5489,
        "Reagents": {
            "Stag Meat": 1,
            "Mild Spices": 4
        },
        "AmountCrafted": 2,
        "Phase":    1
    },
    "Lean Wolf Steak": {
        "ID":       12209,
        "Learn":    125,
        "Yellow":   165,
        "Green":    185,
        "Grey":     205,
        "Source":   "Vendor",
        "RecipeID": 12227,
        "Reagents": {
            "Lean Wolf Flank": 1,
            "Mild Spices": 1
        },
        "AmountCrafted": 1,
        "Phase":    1
    },
    "Lobster Stew": {
        "ID":       13933,
        "Learn":    275,
        "Yellow":   315,
        "Green":    335,
        "Grey":     355,
        "Source":   "Vendor",
        "RecipeID": 13947,
        "Reagents": {
            "Darkclaw Lobster": 1,
            "Refreshing Spring Water": 1
        },
        "AmountCrafted": 1,
        "Phase":    1
    },
    "Loch Frenzy Delight": {
        "ID":       6316,
        "Learn":    50,
        "Yellow":   90,
        "Green":    110,
        "Grey":     130,
        "Source":   "Vendor",
        "Faction":  "Alliance",
        "RecipeID": 6329,
        "Reagents": {
            "Raw Loch Frenzy": 1,
            "Mild Spices": 1
        },
        "AmountCrafted": 1,
        "Phase":    1
    },
    "Longjaw Mud Snapper": {
        "ID":       4592,
        "Learn":    50,
        "Yellow":   90,
        "Green":    110,
        "Grey":     130,
        "Source":   "Vendor",
        "RecipeID": 6328,
        "Reagents": {
            "Raw Longjaw Mud Snapper": 1
        },
        "AmountCrafted": 1,
        "Phase":    1
    },
    "Lynx Steak": {
        "ID":       27635,
        "Learn":    1,
        "Yellow":   45,
        "Green":    65,
        "Grey":     85,
        "Source":   "Vendor",
        "Faction":  "Horde",
        "RecipeID": 27685,
        "Reagents": {
            "Lynx Meat": 1
        },
        "AmountCrafted": 1,
        "Phase":    1
    },
    "Mightfish Steak": {
        "ID":       13934,
        "Learn":    275,
        "Yellow":   315,
        "Green":    335,
        "Grey":     355,
        "Source":   "Vendor",
        "RecipeID": 13948,
        "Reagents": {
            "Large Raw Mightfish": 1,
            "Hot Spices": 1,
            "Soothing Spices": 1
        },
        "AmountCrafted": 1,
        "Phase":    1
    },
    "Mithril Head Trout": {
        "ID":       8364,
        "Learn":    175,
        "Yellow":   215,
        "Green":    235,
        "Grey":     255,
        "Source":   "Vendor",
        "RecipeID": 17062,
        "Reagents": {
            "Raw Mithril Head Trout": 1
        },
        "AmountCrafted": 1,
        "Phase":    1
    },
    "Moknathal Shortribs": {
        "ID":       31672,
        "Learn":    335,
        "Yellow":   355,
        "Green":    365,
        "Grey":     375,
        "Source":   "Vendor",
        "RecipeID": 31675,
        "Reagents": {
            "Raptor Ribs": 1
        },
        "AmountCrafted": 1,
        "Phase":    1
    },
    "Monster Omelet": {
        "ID":       12218,
        "Learn":    225,
        "Yellow":   265,
        "Green":    285,
        "Grey":     305,
        "Source":   "Vendor",
        "RecipeID": 16110,
        "Reagents": {
            "Giant Egg": 1,
            "Soothing Spices": 2
        },
        "AmountCrafted": 1,
        "Phase":    1
    },
    "Murloc Fin Soup": {
        "ID":       3663,
        "Learn":    90,
        "Yellow":   130,
        "Green":    150,
        "Grey":     170,
        "Source":   "Vendor",
        "Faction":  "Alliance",
        "RecipeID": 3680,
        "Reagents": {
            "Murloc Fin": 2,
            "Hot Spices": 1
        },
        "AmountCrafted": 1,
        "Phase":    1
    },
    "Mystery Stew": {
        "ID":       12214,
        "Learn":    175,
        "Yellow":   215,
        "Green":    235,
        "Grey":     255,
        "Source":   "Vendor",
        "RecipeID": 12233,
        "Reagents": {
            "Mystery Meat": 1,
            "Skin of Dwarven Stout": 1
        },
        "AmountCrafted": 1,
        "Phase":    1
    },
    "Nightfin Soup": {
        "ID":       13931,
        "Learn":    250,
        "Yellow":   290,
        "Green":    310,
        "Grey":     30,
        "Source":   "Vendor",
        "RecipeID": 13945,
        "Reagents": {
            "Raw Nightfin Snapper": 1,
            "Refreshing Spring Water": 1
        },
        "AmountCrafted": 1,
        "Phase":    1
    },
    "Poached Bluefish": {
        "ID":       27665,
        "Learn":    320,
        "Yellow":   340,
        "Green":    350,
        "Grey":     360,
        "Source":   "Vendor",
        "RecipeID": 27698,
        "Reagents": {
            "Icefin Bluefish": 1
        },
        "AmountCrafted": 1,
        "Phase":    1
    },
    "Poached Sunscale Salmon": {
        "ID":       13932,
        "Learn":    250,
        "Yellow":   290,
        "Green":    310,
        "Grey":     330,
        "Source":   "Vendor",
        "RecipeID": 13946,
        "Reagents": {
            "Raw Sunscale Salmon": 1
        },
        "AmountCrafted": 1,
        "Phase":    1
    },
    "Rainbow Fin Albacore": {
        "ID":       5095,
        "Learn":    50,
        "Yellow":   90,
        "Green":    110,
        "Grey":     130,
        "Source":   "Vendor",
        "RecipeID": 6368,
        "Reagents": {
            "Raw Rainbow Fin Albacore": 1
        },
        "AmountCrafted": 1,
        "Phase":    1
    },
    "Ravager Dog": {
        "ID":       27655,
        "Learn":    300,
        "Yellow":   320,
        "Green":    330,
        "Grey":     340,
        "Source":   "Vendor",
        "RecipeID": 27688,
        "Reagents": {
            "Ravager Flesh": 1
        },
        "AmountCrafted": 1,
        "Phase":    1
    },
    "Redridge Goulash": {
        "ID":       1082,
        "Learn":    100,
        "Yellow":   135,
        "Green":    155,
        "Grey":     175,
        "Source":   "Vendor",
        "Faction":  "Alliance",
        "RecipeID": 2699,
        "Reagents": {
            "Crisp Spider Meat": 1,
            "Tough Condor Meat": 1
        },
        "AmountCrafted": 1,
        "Phase":    1
    },
    "Roast Raptor": {
        "ID":       12210,
        "Learn":    175,
        "Yellow":   215,
        "Green":    235,
        "Grey":     255,
        "Source":   "Vendor",
        "RecipeID": 12228,
        "Reagents": {
            "Raptor Flesh": 1,
            "Hot Spices": 1
        },
        "AmountCrafted": 1,
        "Phase":    1
    },
    "Roasted Boar Meat": {
        "ID":       2681,
        "Learn":    1,
        "Yellow":   45,
        "Green":    65,
        "Grey":     85,
        "Source":   "Trainer",
        "RecipeID": 5484,
        "Reagents": {
            "Chunk of Boar Meat": 1
        },
        "AmountCrafted": 1,
        "Phase":    1
    },
    "Roasted Clefthoof": {
        "ID":       27658,
        "Learn":    325,
        "Yellow":   345,
        "Green":    355,
        "Grey":     365,
        "Source":   "Vendor",
        "RecipeID": 27691,
        "Reagents": {
            "Clefthoof Meat": 1
        },
        "AmountCrafted": 1,
        "Phase":    1
    },
    "Roasted Kodo Meat": {
        "ID":       5474,
        "Learn":    35,
        "Yellow":   75,
        "Green":    95,
        "Grey":     115,
        "Source":   "Vendor",
        "Faction":  "Horde",
        "RecipeID": 5484,
        "Reagents": {
            "Kodo Meat": 1,
            "Mild Spices": 1
        },
        "AmountCrafted": 2,
        "Phase":    1
    },
    "Roasted Moongraze Tenderloin": {
        "ID":       24105,
        "Learn":    1,
        "Yellow":   45,
        "Green":    65,
        "Grey":     85,
        "Source":   "Quest",
        "RecipeID": 27686,
        "Reagents": {
            "Moongraze Stag Tenderloin": 1
        },
        "AmountCrafted": 1,
        "Phase":    1
    },
    "Rockscale Cod": {
        "ID":       4594,
        "Learn":    175,
        "Yellow":   190,
        "Green":    210,
        "Grey":     230,
        "Source":   "Vendor",
        "RecipeID": 6369,
        "Reagents": {
            "Raw Rockscale Cod": 1
        },
        "AmountCrafted": 1,
        "Phase":    1
    },
    "Runn Tum Tuber Surprise": {
        "ID":       18254,
        "Learn":    275,
        "Yellow":   315,
        "Green":    335,
        "Grey":     355,
        "Source":   "Quest",
        "Faction":  "Any",
        "RecipeID": 18267,
        "Reagents": {
            "Runn Tum Tuber": 1,
            "Soothing Spices": 1
        },
        "AmountCrafted": 1,
        "Phase":    1
    },
    "Sagefish Delight": {
        "ID":       21217,
        "Learn":    175,
        "Yellow":   215,
        "Green":    235,
        "Grey":     255,
        "Source":   "Vendor",
        "RecipeID": 21219,
        "Reagents": {
            "Raw Greater Sagefish": 1,
            "Hot Spices": 1
        },
        "AmountCrafted": 1,
        "Phase":    1
    },
    "Savory Deviate Delight": {
        "ID":       6657,
        "Learn":    85,
        "Yellow":   125,
        "Green":    145,
        "Grey":     165,
        "Source":   "Drop",
        "RecipeID": 6661,
        "Reagents": {
            "Deviate Fish": 1,
            "Mild Spices": 1
        },
        "AmountCrafted": 1,
        "Phase":    1
    },
    "Scorpid Surprise": {
        "ID":       5473,
        "Learn":    20,
        "Yellow":   60,
        "Green":    80,
        "Grey":     100,
        "Source":   "Vendor",
        "Faction":  "Horde",
        "RecipeID": 5483,
        "Reagents": {
            "Scorpid Stinger": 1
        },
        "AmountCrafted": 1,
        "Phase":    1
    },
    "Seasoned Wolf Kabob": {
        "ID":       1017,
        "Learn":    100,
        "Yellow":   140,
        "Green":    160,
        "Grey":     180,
        "Source":   "Vendor",
        "Faction":  "Alliance",
        "RecipeID": 2701,
        "Reagents": {
            "Lean Wolf Flank": 2,
            "Stormwind Seasoning Herbs": 1
        },
        "AmountCrafted": 3,
        "Phase":    1
    },
    "Skullfish Soup": {
        "ID":       33825,
        "Learn":    325,
        "Yellow":   335,
        "Green":    345,
        "Grey":     355,
        "Source":   "Quest",
        "RecipeID": 33870,
        "Reagents": {
            "Crescent-Tail Skullfish": 1
        },
        "AmountCrafted": 1,
        "Phase":    1
    },
    "Slitherskin Mackerel": {
        "ID":       787,
        "Learn":    1,
        "Yellow":   45,
        "Green":    65,
        "Grey":     85,
        "Source":   "Vendor",
        "RecipeID": 6326,
        "Reagents": {
            "Raw Slitherskin Mackerel": 1
        },
        "AmountCrafted": 1,
        "Phase":    1
    },
    "Smoked Bear Meat": {
        "ID":       6890,
        "Learn":    40,
        "Yellow":   80,
        "Green":    100,
        "Grey":     120,
        "Source":   "Vendor",
        "RecipeID": 6892,
        "Reagents": {
            "Bear Meat": 1
        },
        "AmountCrafted": 1,
        "Phase":    1
    },
    "Smoked Desert Dumplings": {
        "ID":       20452,
        "Learn":    285,
        "Yellow":   325,
        "Green":    345,
        "Grey":     365,
        "Source":   "Quest",
        "Faction":  "Any",
        "RecipeID": 20452,
        "Reagents": {
            "Sandworm Meat": 1,
            "Soothing Spices": 1
        },
        "AmountCrafted": 1,
        "Phase":    1
    },
    "Smoked Sagefish": {
        "ID":       21072,
        "Learn":    80,
        "Yellow":   120,
        "Green":    140,
        "Grey":     160,
        "Source":   "Vendor",
        "RecipeID": 21099,
        "Reagents": {
            "Raw Sagefish": 1,
            "Mild Spices": 1
        },
        "AmountCrafted": 1,
        "Phase":    1
    },
    "Soothing Turtle Bisque": {
        "ID":       3729,
        "Learn":    175,
        "Yellow":   215,
        "Green":    235,
        "Grey":     255,
        "Source":   "Quest",
        "Faction":  "Any",
        "RecipeID": 3737,
        "Reagents": {
            "Turtle Meat": 1,
            "Soothing Spices": 1
        },
        "AmountCrafted": 1,
        "Phase":    1
    },
    "Spice Bread": {
        "ID":       30816,
        "Learn":    1,
        "Yellow":   30,
        "Green":    35,
        "Grey":     40,
        "Source":   "Trainer",
        "Reagents": {
            "Simple Flour": 1,
            "Mild Spices": 1
        },
        "AmountCrafted": 1,
        "Phase":    1
    },
    "Spiced Chili Crab": {
        "ID":       12216,
        "Learn":    225,
        "Yellow":   265,
        "Green":    285,
        "Grey":     305,
        "Source":   "Vendor",
        "RecipeID": 16111,
        "Reagents": {
            "Tender Crab Meat": 1,
            "Hot Spices": 2
        },
        "AmountCrafted": 1,
        "Phase":    1
    },
    "Spiced Wolf Meat": {
        "ID":       2680,
        "Learn":    10,
        "Yellow":   50,
        "Green":    70,
        "Grey":     90,
        "Source":   "Trainer",
        "Reagents": {
            "Stringy Wolf Meat": 1,
            "Mild Spices": 1
        },
        "AmountCrafted": 1,
        "Phase":    1
    },
    "Spicy Crawdad": {
        "ID":       27667,
        "Learn":    350,
        "Yellow":   370,
        "Green":    380,
        "Grey":     390,
        "Source":   "Vendor",
        "RecipeID": 27700,
        "Reagents": {
            "Furious Crawdad": 1
        },
        "AmountCrafted": 1,
        "Phase":    1
    },
    "Spicy Hot Talbuk": {
        "ID":       33872,
        "Learn":    325,
        "Yellow":   335,
        "Green":    345,
        "Grey":     355,
        "Source":   "Quest",
        "RecipeID": 33873,
        "Reagents": {
            "Talbuk Venison": 1,
            "Hot Spices": 1
        },
        "AmountCrafted": 1,
        "Phase":    1
    },
    "Spider Sausage": {
        "ID":       17222,
        "Learn":    200,
        "Yellow":   240,
        "Green":    260,
        "Grey":     280,
        "Source":   "Trainer",
        "Reagents": {
            "White Spider Meat": 2
        },
        "AmountCrafted": 1,
        "Phase":    1
    },
    "Sporeling Snack": {
        "ID":       27656,
        "Learn":    310,
        "Yellow":   330,
        "Green":    340,
        "Grey":     350,
        "Source":   "Vendor",
        "RecipeID": 27689,
        "Reagents": {
            "Strange Spores": 1
        },
        "AmountCrafted": 1,
        "Phase":    1
    },
    "Spotted Yellowtail": {
        "ID":       6887,
        "Learn":    225,
        "Yellow":   265,
        "Green":    285,
        "Grey":     305,
        "Source":   "Vendor",
        "RecipeID": 13939,
        "Reagents": {
            "Raw Spotted Yellowtail": 1
        },
        "AmountCrafted": 1,
        "Phase":    1
    },
    "Stewed Trout": {
        "ID":       33048,
        "Learn":    325,
        "Yellow":   335,
        "Green":    345,
        "Grey":     355,
        "Source":   "Trainer",
        "Reagents": {
            "Barbed Gill Trout": 1,
            "Flask of Stormwind Tawny": 1,
            "Soothing Spices": 1
        },
        "AmountCrafted": 1,
        "Phase":    1
    },
    "Stormchops": {
        "ID":       33866,
        "Learn":    300,
        "Yellow":   320,
        "Green":    330,
        "Grey":     340,
        "Source":   "Quest",
        "RecipeID": 33871,
        "Reagents": {
            "Clefthoof Meat": 1,
            "Lightning Eel": 1
        },
        "AmountCrafted": 1,
        "Phase":    1
    },
    "Strider Stew": {
        "ID":       5477,
        "Learn":    50,
        "Yellow":   90,
        "Green":    110,
        "Grey":     130,
        "Source":   "Quest",
        "Faction":  "Any",
        "RecipeID": 5486,
        "Reagents": {
            "Strider Meat": 1,
            "Shiny Red Apple": 1
        },
        "AmountCrafted": 2,
        "Phase":    1
    },
    "Succulent Pork Ribs": {
        "ID":       2685,
        "Learn":    110,
        "Yellow":   130,
        "Green":    150,
        "Grey":     170,
        "Source":   "Drop",
        "RecipeID": 2700,
        "Reagents": {
            "Boar Ribs": 2,
            "Hot Spices": 1
        },
        "AmountCrafted": 1,
        "Phase":    1
    },
    "Talbuk Steak": {
        "ID":       27660,
        "Learn":    325,
        "Yellow":   345,
        "Green":    355,
        "Grey":     365,
        "Source":   "Vendor",
        "RecipeID": 27693,
        "Reagents": {
            "Talbuk Venison": 1
        },
        "AmountCrafted": 1,
        "Phase":    1
    },
    "Tasty Lion Steak": {
        "ID":       3728,
        "Learn":    150,
        "Yellow":   190,
        "Green":    210,
        "Grey":     230,
        "Source":   "Quest",
        "Faction":  "Alliance",
        "RecipeID": 3736,
        "Reagents": {
            "Lion Meat": 2,
            "Soothing Spices": 1
        },
        "AmountCrafted": 1,
        "Phase":    1
    },
    "Tender Wolf Steak": {
        "ID":       18045,
        "Learn":    225,
        "Yellow":   265,
        "Green":    285,
        "Grey":     305,
        "Source":   "Vendor",
        "RecipeID": 18046,
        "Reagents": {
            "Tender Wolf Meat": 1,
            "Soothing Spices": 1
        },
        "AmountCrafted": 1,
        "Phase":    1
    },
    "Thistle Tea": {
        "ID":       7676,
        "Learn":    60,
        "Yellow":   100,
        "Green":    120,
        "Grey":     140,
        "Source":   "Vendor",
        "RecipeID": 18160,
        "Reagents": {
            "Swiftthistle": 1,
            "Refreshing Spring Water": 1
        },
        "AmountCrafted": 1,
        "Phase":    1
    },
    "Undermine Clam Chowder": {
        "ID":       16766,
        "Learn":    225,
        "Yellow":   265,
        "Green":    285,
        "Grey":     305,
        "Source":   "Vendor",
        "RecipeID": 16767,
        "Reagents": {
            "Zesty Clam Meat": 2,
            "Hot Spices": 1,
            "Ice Cold Milk": 1
        },
        "AmountCrafted": 2,
        "Phase":    1
    },
    "Warp Burger": {
        "ID":       27659,
        "Learn":    325,
        "Yellow":   345,
        "Green":    355,
        "Grey":     365,
        "Source":   "Vendor",
        "RecipeID": 27692,
        "Reagents": {
            "Warped Flesh": 1
        },
        "AmountCrafted": 1,
        "Phase":    1
    },
    "Westfall Stew": {
        "ID":       733,
        "Learn":    75,
        "Yellow":   115,
        "Green":    135,
        "Grey":     155,
        "Source":   "Vendor",
        "Faction":  "Alliance",
        "RecipeID": 728,
        "Reagents": {
            "Stringy Vulture Meat": 1,
            "Murloc Eye": 1,
            "Goretusk Snout": 1
        },
        "AmountCrafted": 1,
        "Phase":    1
    }
}

import json
with open('cooking.json', 'w') as jsonFile:
    json.dump(recipes, jsonFile)
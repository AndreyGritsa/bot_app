from zakypki import zakyp_functions

def test_math():
    a = zakyp_functions.math('orichalcum_ingot', 10)
    assert a == {'green_wood': 73,
                 'obsidian_flux': 25,
                 'iron_ore': 75,
                 'starmetal_ore': 56,
                 'orichalcum_ore': 60
                 }

    a = zakyp_functions.math('infused_silk', 10)
    assert a == {'wireweave': 25,
                 'fibers': 100,
                 'silk_threads': 56,
                 'wirefiber': 60
                 }

    a = zakyp_functions.math('infused_leather', 10)
    assert a == {'aged_tannin': 25,
                 'rawhide': 100,
                 'thick_hide': 56,
                 'iron_hide': 60
                 }

    a = zakyp_functions.math('orichalcum_ingot1', 10)
    assert a == None

def draw_cards(*args, **kwargs):
    output = []
    cards = {
        'monster': [],
        'spell': [],
    }
    for name, type in args:
        cards[type].append(name)

    for name, type in kwargs.items():
        cards[type].append(name)

    if cards['monster']:
        output.append("Monster cards:")
        for monster in sorted(cards['monster'], reverse=True):
            output.append(f"  ***{monster}")

    if cards['spell']:
        output.append("Spell cards:")
        for monster in sorted(cards['spell']):
            output.append(f"  $$${monster}")
    return '\n'.join(output)


print(draw_cards(("cyber dragon", "monster"), freeze="spell",))

'''
output
Monster cards:
  ***cyber dragon
Spell cards:
  $$$freeze
'''

print(draw_cards(("celtic guardian", "monster"), ("earthquake", "spell"), ("fireball", "spell"), raigeki="spell", destroy="spell",))

print(draw_cards(("brave attack", "spell"), ("freeze", "spell"), lightning_bolt="spell", fireball="spell",))
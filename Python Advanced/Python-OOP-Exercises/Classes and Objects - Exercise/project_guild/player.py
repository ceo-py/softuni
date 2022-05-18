class Player:
    skills = {}
    guild = "Unaffiliated"

    def __init__(self, name, hp, mp):
        self.name = name
        self.hp = int(hp)
        self.mp = int(mp)

    def add_skill(self, skill_name, mana_cost):
        if self.name not in Player.skills:
            Player.skills[self.name] = {}
            Player.skills[self.name][skill_name] = mana_cost
            return f"Skill {skill_name} added to the collection of the player {self.name}"
        return "Skill already added"

    def player_info(self):
        text = f"Name: {self.name}\nGuild: {Player.guild}\nHP: {self.hp}\nMP: {self.mp}\n"
        for name in Player.skills:
            for key, value in Player.skills[name].items():
                text += f"==={key} - {value}"
        return text

class Player:

    def __init__(self, name: str, hp: int, mp: int):
        self.name = name
        self.hp = int(hp)
        self.mp = int(mp)
        self.skills = {}
        self.guild = "Unaffiliated"

    def add_skill(self, skill_name, mana_cost):
        if skill_name not in self.skills:
            self.skills[skill_name] = int(mana_cost)
            return f"Skill {skill_name} added to the collection of the player {self.name}"
        return "Skill already added"

    def player_info(self):
        output = [f"Name: {self.name}", f"Guild: {self.guild}", f"HP: {self.hp}", f"MP: {self.mp}"]
        for skill_name, mana_cost in self.skills.items():
            output.append(f"==={skill_name} - {mana_cost}")
        return "\n".join(output)



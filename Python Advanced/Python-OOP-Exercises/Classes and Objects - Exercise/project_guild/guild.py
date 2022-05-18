from project.player import Player


class Guild:
    players = []

    def __init__(self, name):
        self.name = name

    def assign_player(self, player):
        if player.name not in [x.name for x in Guild.players]:
            player.guild = self.name
            Guild.players.append(player)
            return f"Welcome player {player.name} to the guild {player.guild}"
        for show in Guild.players:
            if player.name == show.name and player.guild == show.guild:
                return f"Player {player.name} is in another guild."
            return f"Player {player.name} is already in the guild."

    def kick_player(self, player_name: str):
        if player_name == [x.name for x in Guild.players]:
            player_name.guild = "Unaffiliated"
            return f"Player {player_name} has been removed from the guild."
        return f"Player {player_name} is not in the guild."

    def guild_info(self):
        text = f"Guild: {self.name}\n"
        for show in Guild.players:
            if show.guild == self.name:
                text += f"Name: {show.name}\nGuild: {show.guild}\nHP: {show.hp}\nMP: {show.mp}\n"
                for name in Player.skills:
                    for key, value in Player.skills[name].items():
                        text += f"==={key} - {value}\n"
        return text

# player = Player("George", 50, 100)
# print(player.add_skill("Shield Break", 20))
# print(player.player_info())
# guild = Guild("UGT")
# print(guild.assign_player(player))
# print(guild.guild_info())

from project.song import Song


class Album:
    def __init__(self, name, *songs):
        self.name = name
        self.published = False
        self.songs = [x for x in songs]

    def add_song(self, song: Song):
        if song.single:
            return f"Cannot add {song.name}. It's a single"
        if self.published:
            return "Cannot add songs. Album is published."
        if song.name in [x.name for x in self.songs]:
            return "Song is already in the album."

        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str):
        if song_name not in [x.name for x in self.songs]:
            return "Song is not in the album."
        if self.published:
            return "Cannot remove songs. Album is published."
        for show in self.songs:
            if show.name == song_name:
                del show
                return f"Removed song {song_name} from album {self.name}."

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."
        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        text = f"Album {self.name}\n"
        for song in self.songs:
            text += f"== {song}\n"
        return text

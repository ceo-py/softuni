from project.album import Album


class Band:
    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album: Album):
        if album.name in [x.name for x in self.albums]:
            return f"Band {self.name} already has {album.name} in their library."
        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str):
        for show in self.albums:
            if show.name in [x.name for x in self.albums] and show.published:
                return "Album has been published. It cannot be removed."
        if album_name in [x.name for x in self.albums]:
            return f"Album {album_name} has been removed."
        elif album_name not in [x.name for x in self.albums]:
            return f"Album {album_name} is not found."

    def details(self):
        text = f"Band {self.name}\n"
        for x in self.albums:
            text += x.details()
        return text

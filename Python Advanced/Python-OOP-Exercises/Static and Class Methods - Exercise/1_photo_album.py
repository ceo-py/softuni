from math import ceil


class PhotoAlbum:

    def __init__(self, pages):
        self.pages = pages
        self.photos = [[] for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls(ceil(photos_count / 4))

    def add_photo(self, label: str):
        for row in range(len(self.photos)):
            if len(self.photos[row]) < 4:
                self.photos[row].append(label)
                return f"{label} photo added successfully on page {row + 1} slot {len(self.photos[row])}"
        return "No more free slots"

    def display(self):
        output = ["-----------",]
        for row in range(len(self.photos)):
            how_long = len(self.photos[row])
            if how_long > 0:
                pics = "[] " * how_long
            else:
                pics = ""
            output.append(pics.rstrip())
            output.append("-----------")
        return "\n".join(output)



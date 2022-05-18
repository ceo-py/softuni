from project_spoopify.song import Song
from project_spoopify.album import Album
from project_spoopify.band import Band

import unittest


class SongTest(unittest.TestCase):
    def test_song_init(self):
        song = Song("A", 3.15, False)
        message = song.get_info()
        expected = "A - 3.15"
        self.assertEqual(message, expected)

    def test_album_init(self):
        album = Album("The Sound of Perseverance")
        message = album.details().strip()
        expected = "Album The Sound of Perseverance"
        self.assertEqual(message, expected)

    def test_add_song_working(self):
        album = Album("The Sound of Perseverance")
        song = Song("Scavenger of Human Sorrow", 6.56, False)
        message = album.add_song(song)
        expected = "Song Scavenger of Human Sorrow has been added to the album The Sound of Perseverance."
        self.assertEqual(message, expected)

    def test_add_song_already_added(self):
        album = Album("The Sound of Perseverance")
        song = Song("Scavenger of Human Sorrow", 6.56, False)
        album.add_song(song)
        message = album.add_song(song)
        expected = "Song is already in the album."
        self.assertEqual(message, expected)

    def test_add_song_single(self):
        album = Album("The Sound of Perseverance")
        song = Song("Scavenger of Human Sorrow", 6.56, True)
        message = album.add_song(song)
        expected = "Cannot add Scavenger of Human Sorrow. It's a single"
        self.assertEqual(message, expected)

    def test_add_song_published_album(self):
        album = Album("The Sound of Perseverance")
        song = Song("Scavenger of Human Sorrow", 6.56, False)
        album.publish()
        message = album.add_song(song)
        expected = "Cannot add songs. Album is published."
        self.assertEqual(message, expected)

    def test_remove_song_working(self):
        album = Album("The Sound of Perseverance")
        song = Song("Scavenger of Human Sorrow", 6.56, False)
        album.add_song(song)
        message = album.remove_song("Scavenger of Human Sorrow")
        expected = "Removed song Scavenger of Human Sorrow from album The Sound of Perseverance."
        self.assertEqual(message, expected)

    def test_remove_song_not_in_album(self):
        album = Album("The Sound of Perseverance")
        song = Song("Scavenger of Human Sorrow", 6.56, False)
        message = album.remove_song("Scavenger of Human Sorrow")
        expected = "Song is not in the album."
        self.assertEqual(message, expected)

    def test_remove_song_album_published(self):
        album = Album("The Sound of Perseverance")
        song = Song("Scavenger of Human Sorrow", 6.56, False)
        album.add_song(song)
        album.publish()
        message = album.remove_song("Scavenger of Human Sorrow")
        expected = "Cannot remove songs. Album is published."
        self.assertEqual(message, expected)

    def test_publish(self):
        album = Album("The Sound of Perseverance")
        message = album.publish()
        expected = album.published
        self.assertTrue(expected)

    def test_publish_message(self):
        album = Album("The Sound of Perseverance")
        message = album.publish()
        expected = "Album The Sound of Perseverance has been published."
        self.assertEqual(message, expected)

    def test_details(self):
        album = Album("The Sound of Perseverance")
        song = Song("Scavenger of Human Sorrow", 6.56, False)
        album.add_song(song)
        message = album.details().strip()
        expected = "Album The Sound of Perseverance\n== Scavenger of Human Sorrow - 6.56"


    def test_init(self):
        band = Band("Death")
        message = f"{band.name} - {len(band.albums)}"
        expected = "Death - 0"
        self.assertEqual(message, expected)

    def test_add_album_working(self):
        band = Band("Death")
        album = Album("The Sound of Perseverance")
        message = band.add_album(album)
        expected = "Band Death has added their newest album The Sound of Perseverance."
        self.assertEqual(message, expected)

    def test_add_album_already_added(self):
        band = Band("Death")
        album = Album("The Sound of Perseverance")
        band.add_album(album)
        message = band.add_album(album)
        expected = "Band Death already has The Sound of Perseverance in their library."
        self.assertEqual(message, expected)

    def test_remove_album_working(self):
        band = Band("Death")
        album = Album("The Sound of Perseverance")
        band.add_album(album)
        message = band.remove_album("The Sound of Perseverance")
        expected = "Album The Sound of Perseverance has been removed."
        self.assertEqual(message, expected)

    def test_remove_album_not_found(self):
        band = Band("Death")
        album = Album("The Sound of Perseverance")
        message = band.remove_album("The Sound of Perseverance")
        expected = "Album The Sound of Perseverance is not found."
        self.assertEqual(message, expected)

    def test_remove_album_published(self):
        band = Band("Death")
        album = Album("The Sound of Perseverance")
        album.publish()
        band.add_album(album)
        message = band.remove_album("The Sound of Perseverance")
        expected = "Album has been published. It cannot be removed."
        self.assertEqual(message, expected)

    def test_details(self):
        band = Band("Death")
        message = band.details().strip()
        expected = "Band Death"
        self.assertEqual(message, expected)


if __name__ == '__main__':
    unittest.main()
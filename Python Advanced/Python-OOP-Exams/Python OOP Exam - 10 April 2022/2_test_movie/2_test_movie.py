from unittest import TestCase, main
from project.movie import Movie


class TestGunitSquad(TestCase):

    def setUp(self) -> None:
        self.movie = Movie("Interstellar", 2014, 8.6)

    def test_successful_initialization(self):
        self.assertEqual("Interstellar", self.movie.name)
        self.assertEqual(2014, self.movie.year)
        self.assertEqual(8.6, self.movie.rating)
        self.assertEqual([], self.movie.actors)

    def test_unsuccessful_name_raise_value_error_empty_string(self):
        with self.assertRaises(ValueError) as ve:
            self.movie.name = ""

        self.assertEqual("Name cannot be an empty string!", str(ve.exception))

    def test_unsuccessful_year_raise_value_error_lower_than_1887(self):
        with self.assertRaises(ValueError) as ve:
            self.movie.year = 1886

        self.assertEqual("Year is not valid!", str(ve.exception))

    def test_unsuccessful_add_actor_return_message_for_duplicity(self):
        self.movie.add_actor("Joro")
        result = self.movie.add_actor("Joro")

        self.assertEqual("Joro is already added in the list of actors!", result)
        self.assertEqual(["Joro"], self.movie.actors)

    def test_successful_add_actor_to_list_append(self):
        self.assertEqual([], self.movie.actors)
        self.movie.add_actor("Joro")
        self.movie.add_actor("Not Joro")
        self.assertEqual(["Joro", "Not Joro"], self.movie.actors)

    def test__gt__by_movie_rating_self_is_winner(self):
        other = Movie("Critters", 1986, 6.1)
        result = self.movie > other

        self.assertTrue(self.movie.rating > other.rating)
        self.assertEqual('"Interstellar" is better than "Critters"', result)

    def test__gt__by_movie_rating_other_is_winner(self):
        other = Movie("Critters", 1986, 9.1)
        result = self.movie > other

        self.assertTrue(self.movie.rating <= other.rating)
        self.assertEqual('"Critters" is better than "Interstellar"', result)

    def test__repr__(self):
        self.movie.add_actor("Joro")

        self.assertEqual("Name: Interstellar\n"
                         "Year of Release: 2014\n"
                         "Rating: 8.60\n"
                         "Cast: Joro", self.movie.__repr__())


if __name__ == "__main__":
    main()


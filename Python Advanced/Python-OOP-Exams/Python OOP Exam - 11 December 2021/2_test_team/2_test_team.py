from unittest import TestCase, main
from project.team import Team


class TestGunitSquad(TestCase):

    def setUp(self) -> None:
        self.team = Team("GUnit")

    def test_successful_initialization(self):
        self.assertEqual("GUnit", self.team.name)
        self.assertEqual({}, self.team.members)

    def test_unsuccessful_name_setter_raise_value_error_only_letters(self):
        with self.assertRaises(ValueError) as ve:
            self.team.name = "Bad Name"

        self.assertEqual("Team Name can contain only letters!", str(ve.exception))

    def test_successful_add_member_in_list_no_duplicity(self):
        self.team.add_member(Joro=21)
        result = self.team.add_member(Joro=21, Not_Joro=22, East=66)

        self.assertEqual("Successfully added: Not_Joro, East", result)
        self.assertEqual({"Joro": 21, "Not_Joro": 22, "East": 66}, self.team.members)

    def test_unsuccessful_remove_member_dont_exists_in_dict(self):
        self.team.add_member(Joro=21)
        result = self.team.remove_member("Not Joro")
        self.assertEqual("Member with name Not Joro does not exist", result)
        self.assertFalse("Not Joro" in self.team.members)

    def test_successful_remove_member_exists_in_dict(self):
        self.team.add_member(Joro=21)
        self.assertEqual({"Joro": 21}, self.team.members)

        self.team.add_member(Not_Joro=22)
        result = self.team.remove_member("Joro")

        self.assertEqual("Member Joro removed", result)
        self.assertEqual({"Not_Joro": 22}, self.team.members)

    def test__gt__by_len_of_team_members_self_return_true(self):
        self.team.add_member(Joro=21)
        self.team.add_member(Not_Joro=22)

        other = Team("Other")
        other.add_member(Joro=21)
        result = self.team > other
        self.assertEqual(True, result)
        self.assertTrue(len(self.team.members) > len(other.members))

    def test__gt__by_len_of_team_members_self_return_false(self):
        self.team.add_member(Joro=21)

        other = Team("Other")
        other.add_member(Joro=21)
        other.add_member(Not_Joro=22)

        result = self.team > other
        self.assertEqual(False, result)
        self.assertTrue(len(self.team.members) <= len(other.members))

    def test__len__members(self):
        self.team.add_member(Joro=21)
        self.team.add_member(Not_Joro=22)

        result = len(self.team)

        self.assertEqual(2, result)
        self.assertEqual({"Joro": 21, "Not_Joro": 22}, self.team.members)

    def test__add__two_teams_names_and_members_self_first(self):
        self.team.add_member(Joro=21)
        self.team.add_member(Not_Joro=22)

        other = Team("Other")
        other.add_member(Georgi=33)

        merge_team = self.team + other

        self.assertEqual("GUnitOther", merge_team.name)
        self.assertEqual({"Joro": 21, "Not_Joro": 22, "Georgi": 33}, merge_team.members)

    def test__str__(self):
        self.team.add_member(Not_Joro=21)
        self.team.add_member(Joro=21)
        self.team.add_member(Anabel=22)

        self.assertEqual("Team name: GUnit\n"
                         "Member: Anabel - 22-years old\n"
                         "Member: Joro - 21-years old\n"
                         "Member: Not_Joro - 21-years old", self.team.__str__())


if __name__ == "__main__":
    main()

import data
import hw2
import unittest

from data import Duration, Song
from hw2 import create_rectangle, shorter_duration_than, songs_shorter_than, running_time, validate_route, longest_repetition

# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_create_rectangle_one(self):
        p1 = data.Point(2, 2)
        p2 = data.Point(10, 10)
        rect = create_rectangle(p1, p2)
        self.assertEqual(rect.top_left, data.Point(2, 10))
        self.assertEqual(rect.bottom_right, data.Point(10,2))
    def test_create_rectangle_two(self):
        p1 = data.Point(5, 5)
        p2 = data.Point(15, 15)
        rect = create_rectangle(p1, p2)
        self.assertEqual(rect.top_left, data.Point(5, 15))
        self.assertEqual(rect.bottom_right,  data.Point(15, 5))
    # Part 2
    def test_shorter_duration(self):
        d1 = Duration(minutes = 30, seconds =0)
        d2 = Duration(minutes = 0, seconds =0)
        self.assertFalse(shorter_duration_than(d1, d2))

    def test_duration_equal(self):
        d1 = Duration(minutes=45, seconds=10)
        d2 = Duration(minutes=45, seconds=10)
        self.assertFalse(shorter_duration_than(d1, d2))
    # Part 3
    def test_songs_shorter_durations(self):
        d1 = Duration(minutes = 3,seconds = 30)
        d2 = Duration(minutes = 4,seconds = 0)
        d3 = Duration(minutes = 5,seconds = 0)
        song1 = Song("Lana Del Rey", "Sad Girl", d1)
        song2 = Song("The Weeknd", "AfterHours", d2)
        song3 = Song("Taylor Swift", "Cruel Summer", d3)
        max_duration = Duration(minutes=4, seconds=30)
        result = songs_shorter_than([song1, song2, song3], max_duration)
        self.assertEqual(result, [song1, song2])

    # Part 4
    def test_running_time_one(self):
        song1_duration = Duration(4, 30)
        song2_duration = Duration(3, 40)
        song3_duration = Duration(3, 29)
        song4_duration = Duration(3, 58)

        song1 = Song("Decemberists", "June Hymn", song1_duration)
        song2 = Song("Broken Bells", "October", song2_duration)
        song3 = Song("Kansas", "Dust in the Wind", song3_duration)
        song4 = Song("Local Natives", "Airplanes", song4_duration)

        playlist = [0, 2, 1, 3, 0]

        total_duration = running_time([song1, song2, song3, song4], playlist)
        self.assertEqual(total_duration.minutes, 20)
        self.assertEqual(total_duration.seconds, 7)

    def test_running_time_out_of_range_indices(self):
        song1_duration = Duration(2, 15)  # 2:15
        song2_duration = Duration(1, 45)  # 1:45
        song1 = Song("Katy Perry", "Fireworks", song1_duration)
        song2 = Song("Justin Bieber", "Baby", song2_duration)
        playlist = [0, 1, -1, 3, 5]
        total_duration = running_time([song1, song2], playlist)
        self.assertEqual(total_duration.minutes, 4)
        self.assertEqual(total_duration.seconds, 0)

    # Part 5
    city_links = [
        ['san luis obispo', 'santa margarita'],
        ['san luis obispo', 'pismo beach'],
        ['atascadero', 'santa margarita'],
        ['atascadero', 'creston']
    ]
    def test_valid_route(self):
        route = ['san luis obispo', 'santa margarita', 'atascadero']
        self.assertEqual(validate_route(self.city_links, route), True)

    def test_invalid_route(self):
        route = ['san luis obispo', 'atascadero']
        self.assertEqual(validate_route(self.city_links, route), False)
    # Part 6

    def test_longest_repetition(self):
        numbers = [1, 1, 2, 2, 1, 1, 1, 3]
        self.assertEqual(longest_repetition(numbers), 4)
    def test_no_repetition(self):
        numbers = [1, 2, 3, 4, 5]
        self.assertEqual(longest_repetition(numbers), 0)

if __name__ == '__main__':
    unittest.main()

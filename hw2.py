import data
from data import Rectangle, Song, Duration
# Write your functions for each part in the space below.


# Part 1
def create_rectangle(p1, p2):
    left_x = min(p1.x, p2.x)
    right_x = max(p1.x, p2.x)
    top_y = max(p1.x, p2.x)
    bottom_y = min(p1.x, p2.x)
    top_left = data.Point(left_x, top_y)
    bottom_right = data.Point(right_x,bottom_y)
    return Rectangle(top_left, bottom_right)

# Part 2
def shorter_duration_than(d1, d2):
    d1_total_seconds =  d1.minutes * 60 + d1.seconds
    d2_total_seconds = d2.minutes * 60 + d2.seconds
    return d1_total_seconds < d2_total_seconds

# Part 3
def songs_shorter_than(songs, max_duration):

    return [song for song in songs if shorter_duration_than(song.duration, max_duration)]

# Part 4
def running_time(songs,playlist):
    total_seconds = 0
    for index in playlist:
        if 0 <= index < len(songs):  # Check if index is valid
            song_duration = songs[index].duration
            # Convert song duration to total seconds
            total_seconds += (song_duration.minutes * 60 +
                              song_duration.seconds)
    total_minutes, seconds = divmod(total_seconds, 60)

    return Duration(minutes=total_minutes, seconds=seconds)


# Part 5
def validate_route(city_links, route):
    if len(route) <= 1:
        return True
    link_set = {tuple(sorted(link)) for link in city_links}
    for i in range(len(route) - 1):
        city_pair = tuple(sorted([route[i], route[i + 1]]))
        if city_pair not in link_set:
            return False
    return True


# Part 6
def longest_repetition(numbers: list[int]) -> int or None:
    if not numbers:
        return None
    max_length = 1
    max_index = 0
    current_length = 1
    current_index = 0
    for i in range(1, len(numbers)):
        if numbers[i] == numbers[i - 1]:
            current_length += 1
        else:
            if current_length > max_length:
                max_length = current_length
                max_index = current_index
            current_length = 1
            current_index = i
    if current_length > max_length:
        max_index = current_index
    return max_index

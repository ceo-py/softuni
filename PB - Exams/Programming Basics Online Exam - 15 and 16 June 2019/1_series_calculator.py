import math

movie_serial = input()
movie_seasons = int(input())
movie_episodes = int(input())
movie_length = float(input())

eposod_with_ads = 0.20 * movie_length
episode_full_time = eposod_with_ads + movie_length
extra_time_per_season = movie_seasons * 10

total_watch_time = ((episode_full_time * movie_episodes) * movie_seasons) + extra_time_per_season

print(f"Total time needed to watch the {movie_serial} series is {math.floor(total_watch_time)} minutes.")

# Filmography Test Scripts Breakdown
14/07/15

IMDB data lists from - ftp://ftp.fu-berlin.de/pub/misc/movies/database/

## Module Order:
- read_film_files
- line processing (* re)
- tools
- film_data_dicts (* read_film_files, line_processing, tools)
- pull_item_info (* scipy, film_data_dicts)
- film_rating_info (* scipy, film_data_dicts, pull_item_info, tools)
- top_250_test (* itertools, film_data_dict, pull_item_info)
- top_10_test (* scipy, itertools, line_processing, film_data_dicts, pull_item_info, top_250_test)

## Module Breakdowns:

### read_film_files:
- writers_file
- directors_file
- ratings_file
- read_films()
- read_ratings()
- get_writer_lines()
- get_director_lines()

### line_processing:
- format_line()
- format_lines()
- pattern
- pull_items()

### tools:
- check_in_dict
- make_reverse_dict()
- frequency_dict()
- most_popular()

### film_data_dicts:
- film_list
- ratings_list
- writer_lines
- writer_films
- director_lines
- director_films
- film_directors
- film_writers
~ make_directors_info_dict()

### pull_item_info:
- get_film_info()
- films_info_dict()
- get_ratings()

### film_rating_info
- add_ratings()
- avg_rating()
- get_director_avg_rating()
- get_writer_avg_ratings()
- get_all_avg_ratings()
- print_ratings()

### top_250_test
- top_250_films
- top_250_ratings
- get_top_250_directors() - top_250_directors
- get_top_250_writers() - top_250_writers
- get_top_250_film_info() - top_250_film_info
~ get_top_250_director_ratings
~ print_top_director_ratings()
~ get_top_writer_ratings()
~ print_top_writer_ratings

### top_10_films
- top_10_films
- top_10_films_info
- top_10_directors_ratings_dict
————— a testy mess ———




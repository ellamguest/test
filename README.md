# Filmography Test

IMDB data lists from - ftp://ftp.fu-berlin.de/pub/misc/movies/database/

## Module Order:
- read_film_files
- line processing (* re)
- film_data_dicts (* read_film_files, line_processing)
- pull_item_info (* scipy, film_data_dicts)

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

### film_data_dicts:
- film_list
- ratings_list
- writer_lines
- writer_films
- director_lines
- director_films
- make_reverse_dict()
- film_directors
- film_writers

### pull_item_info:
- get_film_info()
- films_info_dict()




movies = {'Thriller': ['bruh', 'homie', 'thrillfest'],
        'Action': ['fight', 'fest', 'kill'],
        'horror': ['frighten', 'scare', 'ghost']}

# def add_genre_and_list(genre, list):
#     movies[genre] = list
#     return movies

# print(add_genre_and_list("Drama", ["Sixth Sense", "Awake", "Taken"]))

# def add_to_dictionary(genre, movie):
#     for key, vals in movies.items():
#         if key == genre:
#             vals.append(movie)
#     return movies


# print(add_to_dictionary('Thriller', 'Secret Window'))

def define_dictionary(some_dict):
    for key, val in some_dict.items():
        print('\n')
        print(len(val), key.upper())
        for index in val:
            print(index)

define_dictionary(movies)

# -*- coding: utf-8 -*-

import media
import fresh_tomatoes


# static movie definitions.
matrix = media.Movie('Matrix',
                     'A computer hacker learns from mysterious rebels about '
                     'the true nature of his reality and his '
                     'role in the war against its controllers.',
                     'https://m.media-amazon.com/images/M'
                     '/MV5BNzQzOTk3OTAtNDQ0Zi00ZTVkLWI0MTEtMDllZjNkYzNjNTc4L2ltYWdlXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SY1000_CR0,0,665,1000_AL_.jpg',  # noqa
                     'https://www.youtube.com/watch?v=2KnZac176Hs')


the_predator = media.Movie("O Predador",
                           "A team of commandos on a mission in a Central "
                           "American jungle find themselves hunted by an "
                           "extraterrestrial warrior.",
                           "https://m.media-amazon.com/images/M/MV5BY2QwYmFmZTEtNzY2Mi00ZWMyLWEwY2YtMGIyNGZjMWExOWEyXkEyXkFqcGdeQXVyNjUwNzk3NDc@._V1_SY1000_CR0,0,671,1000_AL_.jpg",  # noqa
                           "https://www.youtube.com/watch?v=K9AT3tQGbIk")

ironman = media.Movie("Homem de Ferro",
                      "After being held captive in an Afghan cave, billionaire"
                      " engineer Tony Stark creates a unique weaponized suit "
                      "of armor to fight evil.",
                      "https://m.media-amazon.com/images/M/MV5BMTczNTI2ODUwOF5BMl5BanBnXkFtZTcwMTU0NTIzMw@@._V1_SY1000_CR0,0,674,1000_AL_.jpg",  # noqa
                      "https://www.youtube.com/watch?v=8hYlB38asDY")

black_hawk_down = media.Movie("Falcão Negro em Perigo",
                              "160 elite U.S. soldiers drop into Somalia to "
                              "capture two top lieutenants of a renegade "
                              "warlord and find themselves in a desperate "
                              "battle with a large force of heavily-armed "
                              "Somalis.",
                              "https://m.media-amazon.com/images/M/MV5BYWMwMzQxZjQtODM1YS00YmFiLTk1YjQtNzNiYWY1MDE4NTdiXkEyXkFqcGdeQXVyNDYyMDk5MTU@._V1_SY1000_SX675_AL_.jpg",  # noqa
                              "https://www.youtube.com/watch?v=2JS1bJYty7U")

fight_club = media.Movie("Clube da Luta",
                         "An insomniac office worker and a devil-may-care "
                         "soapmaker form an underground fight club that "
                         "evolves into something much, much more. ",
                         "https://m.media-amazon.com/images/M/MV5BMjJmYTNkNmItYjYyZC00MGUxLWJhNWMtZDY4Nzc1MDAwMzU5XkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_SY1000_CR0,0,676,1000_AL_.jpg",  # noqa
                         "https://www.youtube.com/watch?v=Fs0-4NLSO2Y")

eurotrip = media.Movie("Eurotrip",
                       "Dumped by his girlfriend, a high school grad decides "
                       "to embark on an overseas adventure in Europe with his "
                       "friends.",
                       "https://m.media-amazon.com/images/M/MV5BMTIxNjcxMDUxN15BMl5BanBnXkFtZTYwNjAxNTM3._V1_.jpg",  # noqa
                       "https://www.youtube.com/watch?v=-_Eu0X3B6OM")


movies = [matrix, the_predator, ironman, black_hawk_down, fight_club, eurotrip]
# call fresh_tomatoes to render html page
fresh_tomatoes.open_movies_page(movies)

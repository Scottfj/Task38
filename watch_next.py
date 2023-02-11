import spacy
nlp = spacy.load('en_core_web_md')

# Define a function that will take in the description of the last user the movie watched and recommend the best next movie to watch from a list
def watch_next(just_watched):

    # Initialise an empty dict that will contain the details of the movies
    movies = {}

    # Open the file and read the contents into the dictionary, with the title as the key
    with open("movies.txt", "r") as f:
        for line in f:
            line_split = line.split(" :")
            title = line_split[0]
            description = line_split[1]
            movies[title] = description

    # Initailise variables that will record which movie matches the best
    best_match = 0
    best_match_title = ""

    # Iterate through the movies dict and compare the descriptions to the one the user just watched
    for title, description in movies.items():
        similarity = nlp(description).similarity(nlp(just_watched))
        if similarity > best_match:
            # If a better match is found, update the variables with the value and the title of this
            best_match = similarity
            best_match_title = title

    # Print the results
    print(f"The next movie the user should watch is {best_match_title}: {movies[best_match_title]})")

# This is the input of the description the user just watched
just_watched = """Will he save
their world or destroy it? When the Hulk becomes too dangerous for the
Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a
planet where the Hulk can live in peace. Unfortunately, Hulk land on the
planet Sakaar where he is sold into slavery and trained as a gladiator."""

# Call the function with the description
watch_next(just_watched)
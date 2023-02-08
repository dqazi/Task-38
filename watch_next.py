#Import spaCy library
    
import spacy

# Load the en_core_web_md model and store as nlp
nlp = spacy.load('en_core_web_md')

# Define the movie description of Planet Hulk and process description using nlp model
planet_hulk = nlp('''Will he save their world or destroy it? When the Hulk becomes too dangerous for the
Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a
planet where the Hulk can live in peace. Unfortunately, Hulk land on the
planet Sakaar where he is sold into slavery and trained as a gladiator.''')

# Open the movies.txt file -  use readlines to make list . Store list as "movies"
with open('movies.txt', 'r') as f:
    movies = f.readlines()


# function takes the description Planet Hulk and returns the title of the most similar movie from the movies.txt file.
   
def find_similar_movies(planet_hulk):
    
    # Create a list to store the similarities between Planet Hulk and each movie in the movies.txt file
    similarities = []

    # Loop through each movie in the movies list
    for movie in movies:
        # Remove the newline character from the end of the movie string
        movie = movie.rstrip()

        # Process the movie string using the en_core_web_md model
        movie_doc = nlp(movie)

        # Calculate the similarity between Planet Hulk and the current movie
        similarity = planet_hulk.similarity(movie_doc)

        # Add the similarity score and movie title to the similarities list
        similarities.append((similarity, movie))

    # Sort the similarities list in descending order of similarity scores
    similarities.sort(reverse=True)

    # Return the title of the movie with the highest similarity score
    #The first bracket [0] accesses the first tuple in the list, and the second bracket [1] accesses the second element in the tuple, which is the title of the movie.
    return similarities[0][1]

# Call the find_similar_movies function with the Planet Hulk description
print ("The next movie to be shown is:")
print(find_similar_movies(planet_hulk))


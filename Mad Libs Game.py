
def mad_libs_game():
    print("Welcome to Judith Mad Libs Game/Successful Programmer's Tale.\n")
    print("Tell a Story.")


    story_template ="""\t Once upon a time, there was a {adjective} {noun} who {verb} with {language},
     After years of dedication, became an expertise in {language},They mastered programming language, 
     contributed to open-source projects, and mentored aspiring,programmers."""

    
    #word types to fill in the blanks
    word_types = ["adjective", "noun", "verb", "language"]

    #store the user's inputs/response in dictionary
    user_inputs = {}

    '''Ask user for each word type ["adjective", "noun", "verb", "language"]and 
    store the inputs in the dictionary'''

    for word_type in word_types:
        user_input = input(f"Enter a {word_type}: ")
        user_inputs[word_type] = user_input

    # Fill in the blanks in the story template with the user's inputs
    mad_libs_story = story_template.format(**user_inputs)

    # Display the completed Mad Libs story
    print("\nSuccessful Programmer's Tale.")
    print(mad_libs_story)
    print("\t Do you Want to become that Programmer? Start Today and Never give up.")


mad_libs_game()

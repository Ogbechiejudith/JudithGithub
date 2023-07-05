
"""JUDITH WORD COUNTING SYSTEM
FILE TEXT WORD COUNT SYSTEM"""

def count_words_characters_lines(file_path):
    word_count = 0
    character_count = 0
    line_count = 0

    with open(file_path) as file:
        for line in file:
            line_count += 1
            words = line.split()
            word_count += len(words)
            character_count += len(line)

    return word_count, character_count, line_count

def main():
    print("WELCOME TO JUDITH WORD COUNTING SYSTEM")
    
    while True:
        file_path = input("Enter the path to the text file (Enter 'exit' to quit): ")
        
        if file_path.lower() == 'exit':
            print("Exit Successfully")
            break

        try:
            word_count, character_count, line_count = count_words_characters_lines(file_path)
            print(f"Word count: {word_count}")
            print(f"Character count: {character_count}")
            print(f"Line count: {line_count}")
        except FileNotFoundError:
            print("File not found.")

if __name__ == "__main__":
    main()

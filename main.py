# main.py
# This script takes a user input sentence and modifies it using the start_scrabble function
# from the scrabble module, then prints out the modified sentence.

from scrabble import start_scrabble

def main():
    """Main function to modify and print a user-entered sentence."""
    try:
        input_string = input("Enter a sentence: ")
        if input_string:
            output_string = start_scrabble(input_string)
            print(f"Modified sentence: {output_string}")
        else:
            print("No sentence entered. Exiting...")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

# main.py
# This script takes a user input sentence and modifies it using the start_scrabble function
# from the scrabble module, then prints out the modified sentence.

from scrabble.scrabble import start_scrabble

def main():
    """Main function to modify and print a user-entered sentence."""
    try:
        input_string = input("Enter a sentence: ")
        if input_string:
            while True:
                output_string = start_scrabble(input_string)
                print(f"\nNew randomized sentence: {output_string}\n")
                user_choice = input("Are you satisfied with the result? (yes/no):\n")
                if user_choice.lower() == 'yes':
                    break
                else:
                    print("Re-randomizing the sentence...")
        else:
            print("No sentence entered. Exiting...")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

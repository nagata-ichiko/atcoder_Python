def solve(S: str) -> str:
    # Store the valid strings in a list
    valid_strings = ["ACE", "BDF", "CEG", "DFA", "EGB", "FAC", "GBD"]

    # Check if the input string is in the list of valid strings
    if S in valid_strings:
        return "Yes"
    else:
        return "No"

def main():
    # Read the input string from the standard input
    S = input().strip()

    # Pass the string to the function and print the result
    print(solve(S))

# Call the main function
if __name__ == "__main__":
    main()

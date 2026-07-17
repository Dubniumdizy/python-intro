"""Iteration, File Handling, Exception Handling, and Dictionaries.

This script contains solutions for Laboratory Assignment 3, covering basic 
algorithms (Insertion Sort), safe text-file transformations, and advanced 
text indexing using native dictionary tools.
"""

# =============================================================================
# Uppgift 1a: insert_in_sorted
# =============================================================================
def insert_in_sorted(x: int, sorted_list: list[int]) -> list[int]:
    """Inserts an element x into its correct mathematical position within a sorted list.

    Args:
        x (int): The numerical element to be inserted into the collection.
        sorted_list (list): A list of integers that is already sorted in 
          ascending order.

    Returns:
        list: The same list instance containing the newly inserted element in 
          the correct place.

    Example: insert_in_sorted(5, [1, 3, 7]) -> [1, 3, 5, 7]

    sorted_list = [1 2 3 5] elements
    new list = [] inserted
    x = 4

    element = 1
    not insterted and 4 is not less than 1
    -> new list = [1]

    ... new list = [123]

    element = 5
    not inserted and 4<5!
    new list = [1 2 3 4]
    inserted TRUE!
    new list = [1 2 3 4 5]

    """
    idx = 0
    # Iterate to find the first element greater than x
    while idx < len(sorted_list):
        if x < sorted_list[idx]:
            sorted_list.insert(idx, x)
            return sorted_list
        idx += 1
        
    # If no element was larger, append x to the very end
    sorted_list.append(x)
    return sorted_list


# =============================================================================
# Uppgift 1b: insertion_sort
# =============================================================================
def insertion_sort(my_list: list[int]) -> list[int]:
    """Sorts a list of integers using the iterative Insertion Sort algorithm.

    Args:
        my_list (list): An unsorted or arbitrary list of integers.

    Returns:
        list: A completely new list containing the identical elements sorted 
          in ascending order.

    Example: insertion_sort([3, 1, 4]) -> [1, 3, 4]

    my_list = [321]
    out = []

    for x=3
    out = func(insert element, sorted list) = func(3, out) = [3]
    
    for x=2
    out = func(2, out) = [2 3]

    for x=1
    out = func(1, out) = [1 2 3]

    (2, [])
    """
    out: list[int] = [] # Initialize an empty list to and add type hint
    for item in my_list:
        out = insert_in_sorted(item, out)
    return out


# =============================================================================
# Uppgift 2: filhantering (number_lines)
# =============================================================================
def number_lines(f: str) -> None:
    """Reads a file and creates a new version prefixed with sequential line numbers.

    Args:
        f (str): The filename string of the source file to target.

    Example: If f = "example.txt" and contains:
        Hello World
        This is a test.
    The output file "numbered_example.txt" will contain:
        0 Hello World
        1 This is a test.

    f = poem.txt
    cats are best
    no protests!

    Mjau
    _________

    outputfilename = numbered_poem.txt

    infile = opens poem.txt reads -> the full txt
    outfile = in numbered_poem.txt it can edit

    for line = 0 "cats are best"
    outfile = 0 + " " + cats are best = 0 cats are best

    for line = 1 "no preotests!"
    outfile = 1 + " " + no protests!

    for line = 2 " "
    outfile = 2 + " "
    ...

    close() both and save
    """
    # Create the output filename according to rules: "numbered_" + original name
    output_filename = "numbered_" + f
    
    # Open and process the files safely using standard contexts
    infile = open(f, "r")
    outfile = open(output_filename, "w")
    
    line_number = 0
    for line in infile:
        outfile.write(str(line_number) + " " + line) # outfile = ...
        line_number += 1
        
    infile.close()
    outfile.close()

# variable.func()

# =============================================================================
# Uppgift 3a: enkel textindexering (index_text)
# =============================================================================
def index_text(filename):
    """Builds an index dictionary tracking the specific line numbers where words occur.

    Step-by-Step Execution Workflow:
    1. Initializes an empty storage dictionary (`index_dict = {}`).
    2. Opens the target file in read-only mode (`open(filename, "r")`).
    3. Starts a line tracker variable (`line_idx`) at 0.
    4. Loops through each line of the file sequentially.
    5. Splits the line into a list of separate words using `.split()`.
    6. Iterates over each individual word in that split line list.
    7. Normalizes the word by converting it to lowercase using `.lower()`.
    8. Checks if the lowercase word is missing from the dictionary keys.
       If it is a new word, it initializes an empty list: `index_dict[word] = []`.
    9. Fetches the current list of line indices stored for that word.
    10. Enforces a duplication guard check:
        `if len(current_lines) == 0 or current_lines[len(current_lines) - 1] != line_idx:`
        This ensures that if a word shows up multiple times on the *same* line, 
        the line number is only appended once.
    11. Appends the current `line_idx` to the word's list if the guard check passes.
    12. Increments `line_idx` by 1 after fully completing a line's word loop.
    13. Closes the file object and returns the populated index dictionary.

    Trace Example Scenario:
    Given a file 'sample.txt' containing:
        Line 0: "Python is fun"
        Line 1: "Fun and simple"
        Line 2: "Python Python Python"

    Traced Iteration Changes:
    - Line 0 (line_idx = 0):
      * Words found: ["Python", "is", "fun"]
      * Lowercased to: "python", "is", "fun"
      * All three keys are initialized and append 0.
      * State: {"python": [0], "is": [0], "fun": [0]}
    
    - Line 1 (line_idx = 1):
      * Words found: ["Fun", "and", "simple"]
      * Lowercased to: "fun", "and", "simple"
      * "fun" already exists. Its last element is 0. Since 0 != 1, it appends 1.
      * "and" and "simple" are new keys; they are initialized and append 1.
      * State: {"python": [0], "is": [0], "fun": [0, 1], "and": [1], "simple": [1]}

    - Line 2 (line_idx = 2):
      * Words found: ["Python", "Python", "Python"]
      * All lowercase to "python".
      * Occurrence 1: List is [0]. Last item 0 != 2, so it appends 2 -> [0, 2].
      * Occurrence 2: List is [0, 2]. Last item is 2. Since 2 == 2, the duplication
        guard check triggers and it skips appending.
      * Occurrence 3: Last item is 2. Guard triggers and skips appending again.

    Args:
        filename (str): The string filename of the text document to process.

    Returns:
        dict[str, list[int]]: A dictionary mapping lowercase word strings to 
          sorted lists of unique line indices where they appear.

    """
    index_dict = {} 
    infile = open(filename, "r")
    
    line_idx = 0
    for line in infile:
        # Split line into words using default whitespace rules
        words = line.split()
        for word in words:
            clean_word = word.lower()
            
            # Initialize key if it doesn't exist
            if clean_word not in index_dict:
                index_dict[clean_word] = []
                
            # Get the list of line numbers currently recorded for this word
            current_lines = index_dict[clean_word]
            
            # Guard against adding the same line number twice if a word appears 
            # multiple times on this line. We only append if the list is empty 
            # or if the last recorded line is different from the current one.
            if len(current_lines) == 0 or current_lines[len(current_lines) - 1] != line_idx:
                current_lines.append(line_idx)
                
        line_idx += 1
        
    infile.close()
    return index_dict

# =============================================================================
# Uppgift 3b: important_words
# =============================================================================
def important_words(an_index: dict[str, list[int]], stop_words: list[str]) -> list[str]:
    """Extracts up to the five most frequent words in an index, ignoring stop words.

    Example:
        >>> index = {"fun": [0, 1, 2, 9], "hoarse": [0, 4, 12], "simple": [1]}
        >>> important_words(index, ["och"])
        ['fun', 'hoarse', 'simple']

    Trace Example Scenario:
        Given an initial filtered candidates list:
        candidates = ["simple", "hoarse", "fun"]

        Frequencies (list lengths from an_index):
        - simple -> length 1 (appears on 1 line)
        - hoarse -> length 3 (appears on 3 lines)
        - fun    -> length 4 (appears on 4 lines)

        - Outer Pass i = 0 (Looking for largest frequency for index 0):
          * max_idx starts at 0 ("simple", len=1)
          * Compare with j = 1 ("hoarse", len=3): 3 > 1 -> max_idx becomes 1
          * Compare with j = 2 ("fun", len=4):    4 > 3 -> max_idx becomes 2
          * Swap candidates[0] ("simple") with candidates[2] ("fun")
          * State: ["fun", "hoarse", "simple"]

        - Outer Pass i = 1 (Looking for largest remaining frequency for index 1):
          * max_idx starts at 1 ("hoarse", len=3)
          * Compare with j = 2 ("simple", len=1): 1 > 3 is False -> max_idx stays 1
          * Swap candidates[1] with candidates[1] (no change)
          * State: ["fun", "hoarse", "simple"]

        - Outer Pass i = 2 (Last element checked automatically)
          * State remains sorted.

    Args:
        an_index (dict): An index mapping lowercase word strings to the lists 
          of line indices where they appear.
        stop_words (list): A list of lowercase strings representing words that 
          should be excluded from the results.

    Returns:
        list: A collection containing up to 5 of the most frequent words, 
          sorted in descending order by appearance count.
    """
    candidates = []
    
    # Filter out any word present in the stop_words sequence
    for word in an_index:
        if word not in stop_words:
            candidates.append(word)
            
    # Sort the candidates in descending order using Selection Sort.
    # We find the word with the longest line list and bring it to the front.
    i = 0
    while i < len(candidates):
        max_idx = i 
        j = i + 1
        
        while j < len(candidates):
            # Compare frequencies by looking at the lengths of their line lists
            if len(an_index[candidates[j]]) > len(an_index[candidates[max_idx]]):
                max_idx = j
            j += 1
            
        # Swap the current element with the maximum element found
        temp = candidates[i]
        candidates[i] = candidates[max_idx]
        candidates[max_idx] = temp
        i += 1
        
    # Return a slice of up to the first 5 elements
    return candidates[:5]


# =============================================================================
# Uppgift 3c: Huvudprogram med felhantering
# =============================================================================
def main() -> None:
    """Manages the user interface workflow and executes choices continuously.

    Example:
        >>> main()
        En textfil: missing_file.txt
        Filen hittades inte. Försök igen.
        En textfil: idas.txt
        De viktigaste orden är:
        så
        där
        små
        barna
        gör

    Trace Example Scenario:
        Given an environment where 'idas.txt' exists but 'wrong.txt' does not:

        - Loop Iteration 1:
          * User inputs filename = "wrong.txt"
          * `index_text("wrong.txt")` attempts to open the file.
          * System raises a `FileNotFoundError`.
          * The `try` block execution halts immediately.
          * The `except FileNotFoundError` block catches the exception.
          * Prints: "Filen hittades inte. Försök igen."
          * The loop does not hit the `break` statement; it restarts.

        - Loop Iteration 2:
          * User inputs filename = "idas.txt"
          * `index_text("idas.txt")` opens and indexes the file successfully.
          * The `try` block completes without errors, assigning data to `text_index`.
          * Hits `break` statement -> Terminates the `while True` loop sequence.

        - Post-Loop Execution:
          * `important_words(text_index, stop_words)` filters out the specified 
            stop words and sorts the remaining words by frequency.
          * Prints the introductory line: "De viktigaste orden är:"
          * Loops through the top 5 most frequent words list and prints each sequentially.

    Args:
        None

    Returns:
        None
    """
    # Define the mandatory stop words list
    stop_words = ["och", "jag", "som", "det", "för"]
    
    # Interactive while loop with try-except validation block as required by the assignment
    while True:
        try:
            filename = input("En textfil: ")
            # Try to run the index function, will throw FileNotFoundError if missing
            text_index = index_text(filename)
            break
        except FileNotFoundError:
            print("Filen hittades inte. Försök igen.")
            
    # Process and fetch important target results
    top_words = important_words(text_index, stop_words)
    
    print("De viktigaste orden är:")
    for word in top_words:
        print(word)


# This standard block ensures main() executes only when run directly (not imported)
if __name__ == "__main__":
    main()


    '''
    open(Karolina/python-intro/HW3.py, r, uttf8)
    

    with open("geeksforgeeks.txt","r") as gfg_file:
    file_content = gfg_file.read()
    print(file_content)

    gfg_file = open(...)


    read = "I am a frog" -> 1 OBJECT
    readlines = [I am a frog...] -> 3rd word

    

    print("It is very sunny today", file=weather)

    with open(weather, "w") as edit
    edit("it is very sunny today") -> "str" / file 
    '''
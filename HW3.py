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

    Args:
        filename (str): The filename string of the text document to index.

    Returns:
        dict: A dictionary mapping lowercase word strings to lists of unique 
          line indices where they were found.

    Example: If the file contains:
        Hello 
        world
    The index_dict will contain:
        {"hello": [0], "world": [1]}

    dicttionary{key: keyword} = {{Disa: [22, fish]}, {Karolina: [19, cat]}} = dict
    dict[Disa][0] = 22
_________________________________________

    filename = zoo_animals.txt
    Hoarses are fun
    Apples are are fun for hoarses

    index_dict = {key: keywords, ...}
    infile = zoo_animals.txt info downloaded

    line_idx = 0
    for line = 0 in zoo_animals
    words created list = [hoarses, are, fun]
        for horases in words
        make all low letters
        if hoarse isnt in {} True -> add horases as a key to to the dict, syntax: index_dict[hoarses] = [] with no keywords
        current_list = horases x2 for ex two key
        if the dict repeats horses then we update the dict by deleting that extra key 
        if that is clear then add horases = 1
...
        are_2 = word
        clean_are = low letters
        if are not in {} -> dict{are = []}
        current line = dict{are = [2]}
        if are appear or if are was not the previous key (are_1)?=2 THEN add in dict the keyword line

....

Keys: keywords
Hoarses: [0, 1]
Are: [0, 1]
Fun: [0, 1]
Apples: [1]
For: [1]
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
                
            # Avoid repeating the line number if word occurs multiple times on the same line
            current_lines = index_dict[clean_word]
            # Check if the current line index is already recorded for this word by checking 
            # if it's 0 or if the last recorded line index is not equal to the current line index
            if (len(current_lines) == 0 or current_lines[len(current_lines) - 1]) != line_idx: 
                # Append the current line index to the list for this word
                current_lines.append(line_idx)
                
        line_idx += 1
        
    infile.close()
    return index_dict

# =============================================================================
# Uppgift 3b: important_words
# =============================================================================
def important_words(an_index: dict[str, list[int]], stop_words: list[str]) -> list[str]:
    """Extracts up to the five most frequent words in an index, ignoring stop words.

    Args:
        an_index (dict): An index mapping word strings to their line lists.
        stop_words (list): A list of strings containing words that should be 
          ignored.

    Returns:
        list: A collection containing up to 5 of the most frequent words, sorted 
          by appearance count.

     ehueafuaef ueafh d hadvhasfu af hoasf hoasijo 
     which one is the most frequent? but skip are, be, I
     hoarse: 79
     Fun: 22
     ...
    """
    candidates = []
    
    # Filter out any word present in the stop_words sequence
    for word in an_index:
        if word not in stop_words:
            candidates.append(word)
            
    # Sort candidates by the length of their line index lists (frequency)
    # Using Selection Sort layout since built-in sort/sorted are strictly forbidden
    # Selection sort is used like before
    '''
    hoarses : 1
    fun : 2

    max_idx for hoarses
    j = max_idx for fun

    while fun apears more than hoarses
    
    '''

    i = 0
    while i < len(candidates):
        max_idx = i
        j = i + 1
        while j < len(candidates):
            # Compare frequencies via list lengths
            if len(an_index[candidates[j]]) > len(an_index[candidates[max_idx]]):
                max_idx = j
            j += 1
        # Swap places
        temp = candidates[i] # temp for temporary
        candidates[i] = candidates[max_idx]
        candidates[max_idx] = temp
        i += 1
        
    # Return up to the top 5 elements
    return candidates[:5]


# =============================================================================
# Uppgift 3c: Huvudprogram med felhantering
# =============================================================================
def main() -> None:
    """Prompts users for a file, processes its important words, and displays them safely."""
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
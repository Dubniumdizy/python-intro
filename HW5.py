# =============================================================================
# Uppgift 1: Klassen DnaSeq
# =============================================================================

# Ny syntax: 'class' definierar en ritning (blueprint) för att skapa egna objekt.
# Detta kallas för objektorienterad programmering (OOP).
# Likt en dictionary men istället för att spara strängar så sparar man attribut & metoder som kallas på med objekt
class DnaSeq:
    """Represents a DNA sequence extracted from a FASTA file layout."""

    # Ny syntax: '__init__' är en konstruktor. Det är en metod som skapar attribut
    # (double underscore) som anropas automatiskt när vi skapar ett nytt objekt.
    # 'self' representerar det specifika objektet som vi håller på att skapa just nu.
    def __init__(self, accession, sequence):
        """Initializes a DNA sequence object with an identifier and bases.

        Step-by-Step Execution Workflow:
        1. Checks if the accession identifier is empty or None.
        2. Checks if the sequence string is empty or None.
        3. Raises a ValueError if either input parameter is invalid.
        4. Saves the accession identifier to the object instance as self.accession.
        5. Saves the sequence string to the object instance as self.sequence.

        Trace Example Scenario:
            Given an accession "s1" and sequence "ACGT":
            - Passes validation checks because both strings are populated.
            - Creates object attributes: self.accession = "s1" and self.sequence = "ACGT".

            Given an accession "" and sequence "ACGT":
            - First check triggers: "accession == ''" is True.
            - Raises a ValueError with a descriptive error message.

        Args:
            accession: A string identifier code (e.g., "s123").
            sequence: A string containing the DNA nucleotide bases (A, C, G, T).
        """
        # Ny syntax: 'or' utvärderar om något av villkoren på sidorna är sant.
        # 'is None' kontrollerar om en variabel saknar värde helt och hållet.
        # 'raise' kastar medvetet ett felmeddelande (ValueError) för att stoppa programmet.
        if accession == "" or accession is None:
            raise ValueError("Accession identifier cannot be empty or None.")
            
        if sequence == "" or sequence is None:
            raise ValueError("DNA sequence cannot be empty or None.")
            
        self.accession = accession
        self.sequence = sequence

    # Ny syntax: '__len__' låter oss använda Pythons inbyggda len()-funktion direkt
    # på våra egna objekt (t.ex. len(mitt_dna_objekt)).
    def __len__(self):
        """Returns the total number of nucleotide bases in the DNA sequence.

        Step-by-Step Execution Workflow:
        1. Accesses the string stored in self.sequence.
        2. Counts the length of that string using Python's built-in len().
        3. Returns the integer length value.

        Trace Example Scenario:
            Given a DnaSeq object containing self.sequence = "GATTACA":
            - len(dna_object) -> Returns 7.

        Returns:
            An integer representing the length of the sequence attribute.
        """
        return len(self.sequence)

    # Ny syntax: '__str__' bestämmer hur vårt objekt ska visas som text när vi
    # skickar det till print() eller gör om det till en sträng med str().
    def __str__(self):
        """Returns a user-friendly string representation of the DNA sequence.

        Step-by-Step Execution Workflow:
        1. Fetches the accession identifier.
        2. Fetches the sequence length.
        3. Formats them into the required template: "accession <length>".

        Trace Example Scenario:
            Given a DnaSeq object with accession "s123" and sequence "ACGT":
            - str(dna_object) -> Returns "s123 <4>".

        Returns:
            A formatted label string.
        """
        # Ny syntax: F-strings (f"...") låter oss sätta in variabler och uttryck 
        # direkt i en sträng genom att omsluta dem med måsvingar {}.
        return f"{self.accession} <{len(self.sequence)}>"


# =============================================================================
# Uppgift 2: read_fasta
# =============================================================================

def read_fasta(filename):
    """Parses a FASTA file and extracts a list of DnaSeq objects.

    Step-by-Step Execution Workflow:
    1. Initializes an empty list named 'sequence_list' to store the results.
    2. Opens the target FASTA file in read-only mode.
    3. Initializes temporary trackers 'current_accession' and 'current_sequence_accumulator'.
    4. Loops through each line in the file:
       - If a line starts with '>', it indicates a new accession header:
         * If we already have a gathered sequence in our accumulator, we package 
           the previous sequence into a DnaSeq object and append it to our list.
         * We then extract the new accession identifier (stripping '>' and whitespace).
         * We reset the sequence accumulator string to be empty.
       - If the line does not start with '>', it is part of the DNA sequence:
         * We clean whitespace and append the sequence characters to the accumulator.
    5. After the loop ends, we package the very last sequence block into a DnaSeq object.
    6. Closes the file and returns the completed list of DnaSeq objects.

    Trace Example Scenario:
        Given a file containing:
        >seq1
        ACG
        TG
        >seq2
        AAAA

        - Line 1: Starts with '>'. 'current_accession' becomes "seq1".
        - Line 2: No '>'. 'current_sequence_accumulator' becomes "ACG".
        - Line 3: No '>'. 'current_sequence_accumulator' becomes "ACGTG".
        - Line 4: Starts with '>'. We package DnaSeq("seq1", "ACGTG") and append.
                  'current_accession' becomes "seq2", accumulator resets.
        - Line 5: No '>'. 'current_sequence_accumulator' becomes "AAAA".
        - File Ends: We package the last item DnaSeq("seq2", "AAAA") and append.
        - Returns: [DnaSeq("seq1", "ACGTG"), DnaSeq("seq2", "AAAA")].

    Args:
        filename: A string containing the path of the FASTA file to read.

    Returns:
        A list of DnaSeq objects parsed from the file content.
    """
    # Ny syntax: Hakparenteser [] skapar en tom lista för att lagra objekt i sekvens.
    sequence_list = []
    
    # Ny syntax: 'open()' öppnar en fil. Parametern "r" betyder read-only (läsläge).
    input_file = open(filename, "r")
    
    current_accession = None
    current_sequence_accumulator = ""
    
    # Ny syntax: 'for line in input_file:' läser igenom filen rad för rad automatiskt.
    for line in input_file:
        # Ny syntax: '.strip()' tar bort osynliga tecken som radbrytningar (\n) 
        # och extra mellanslag från början och slutet av en sträng.
        cleaned_line = line.strip()
        
        # Ny syntax: 'if' utvärderar ett villkor. 'startswith()' kontrollerar 
        # om en sträng börjar med ett visst tecken eller ord.
        if cleaned_line.startswith(">"):
            # Om vi redan har samlat in en sekvens från föregående block, spara den först
            if current_accession is not None:
                # Skapa ett nytt DnaSeq-objekt och lägg till det i vår lista
                dna_object = DnaSeq(current_accession, current_sequence_accumulator)
                sequence_list.append(dna_object)
                
            # Ny syntax: Slicing [1:] plockar bort det allra första tecknet (index 0, dvs '>') 
            # och returnerar resten av strängen.
            current_accession = cleaned_line[1:].strip()
            current_sequence_accumulator = ""
        else:
            # Lägg till radens baser till vår pågående DNA-sträng
            current_sequence_accumulator = current_sequence_accumulator + cleaned_line
            
    # Glöm inte att spara den allra sista DNA-sekvensen i filen när loopen är klar
    if current_accession is not None:
        dna_object = DnaSeq(current_accession, current_sequence_accumulator)
        sequence_list.append(dna_object)
        
    # Det är viktigt att alltid stänga filer vi har öppnat för att frigöra systemresurser.
    input_file.close()
    return sequence_list


# =============================================================================
# Uppgift 3: check_overlap
# =============================================================================

def check_overlap(dna_seq_one, dna_seq_two, overlap_length):
    """Determines if the suffix of the first sequence matches the prefix of the second.

    Step-by-Step Execution Workflow:
    1. Extracts the last 'overlap_length' characters (the suffix) from dna_seq_one.sequence.
    2. Extracts the first 'overlap_length' characters (the prefix) from dna_seq_two.sequence.
    3. Compares the suffix and prefix strings.
    4. Returns True if they match exactly, False otherwise.

    Trace Example Scenario:
        Given:
        dna_seq_one = DnaSeq("s1", "GATTACA")
        dna_seq_two = DnaSeq("s2", "TACAGGG")
        overlap_length = 4

        - Suffix extraction: dna_seq_one.sequence[-4:] -> "TACA"
        - Prefix extraction: dna_seq_two.sequence[:4]  -> "TACA"
        - Comparison: "TACA" == "TACA" -> Returns True.

    Args:
        dna_seq_one: The first DnaSeq object (the left sequence).
        dna_seq_two: The second DnaSeq object (the right sequence).
        overlap_length: An integer specifying the number of bases to compare.

    Returns:
        A boolean value (True or False) indicating if an overlap exists.
    """
    # Ny syntax: Negativ slicing [-k:] plockar ut de sista k tecknen i en sträng.
    suffix = dna_seq_one.sequence[-overlap_length:]
    
    # Ny syntax: Vanlig slicing [:k] plockar ut de första k tecknen i en sträng.
    prefix = dna_seq_two.sequence[:overlap_length]
    
    # Ny syntax: '==' är en jämförelseoperator som kontrollerar om två värden är exakt lika.
    return suffix == prefix


# =============================================================================
# Uppgift 4: find_overlaps
# =============================================================================

def find_overlaps(dna_list, overlap_length):
    """Finds all overlapping sequence pairs of a given length in a collection.

    Step-by-Step Execution Workflow:
    1. Initializes an empty list named 'overlap_results'.
    2. Loops through every sequence in 'dna_list' using a variable 'dna_one'.
    3. Loops through every sequence in 'dna_list' again using a variable 'dna_two'.
    4. Ensures we do not compare a sequence with itself by checking 'dna_one != dna_two'.
    5. Calls 'check_overlap(dna_one, dna_two, overlap_length)' for each valid pair.
    6. If an overlap is found, saves the details as a tuple containing:
       (dna_one.accession, dna_two.accession, overlap_length)
    7. Returns the accumulated list of overlap tuples.

    Trace Example Scenario:
        Given:
        dna_list = [DnaSeq("s1", "GATTACA"), DnaSeq("s2", "TACAGGG")]
        overlap_length = 4

        - Step 1: Compare s1 and s2 -> check_overlap(s1, s2, 4) -> Returns True.
          * Appends ("s1", "s2", 4) to results.
        - Step 2: Compare s2 and s1 -> check_overlap(s2, s1, 4)
          * Suffix s2 ("AGGG") != Prefix s1 ("GATT") -> Returns False.
        - Returns: [("s1", "s2", 4)]

    Args:
        dna_list: A list of DnaSeq objects to inspect.
        overlap_length: An integer representing the target overlap length.

    Returns:
        A list of tuples, where each tuple represents an identified overlap:
        (left_accession, right_accession, length)
    """
    overlap_results = []
    
    # Vi använder nästlade loopar (en loop inuti en loop) för att jämföra alla med alla
    for dna_one in dna_list:
        for dna_two in dna_list:
            # Ny syntax: '!=' betyder 'inte lika med'. Vi får inte jämföra ett objekt med sig själv.
            if dna_one != dna_two:
                # Kontrollera om slutet på sekvens ett överlappar med början på sekvens två
                if check_overlap(dna_one, dna_two, overlap_length):
                    # Ny syntax: En tupel (parenteser runt värden) är en oföränderlig datastruktur 
                    # som är perfekt för att gruppera relaterad data som hör ihop.
                    overlap_info = (dna_one.accession, dna_two.accession, overlap_length)
                    overlap_results.append(overlap_info)
                    
    return overlap_results
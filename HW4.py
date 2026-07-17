# Nyckelordet import hämtar in externa moduler och kodbibliotek som inte ingår i standard-Python.
# 'as' skapar ett kortare smeknamn (alias) så att vi slipper skriva hela namnet varje gång.
from matplotlib import pyplot as plt


# =============================================================================
# Uppgift 4.1 & 4.3: Läsa in och validera simuleringsdata från fil
# =============================================================================

def read_simulation_data(file_path):
    """Reads numerical values from a data file and stores them into a clean list.

    Step-by-Step Execution Workflow:
    1. Initializes an empty list named 'data_values_list' to accumulate numbers.
    2. Opens the requested data file in read-only mode using 'open()'.
    3. Loops line-by-line through the text content.
    4. Cleans whitespace characters and breaks from each line using '.strip()'.
    5. Checks if the line is empty. If it is, it skips processing.
    6. Converts the text string number into a native decimal number via float().
    7. Appends the decimal value to our storage list.
    8. Closes the file connection and returns the populated list.

    Trace Example Scenario:
    Given a file containing:
    10.5
    20.0

    - Step 1: data_values_list = []
    - Line 1: "10.5" -> Cleans text -> float("10.5") becomes 10.5 -> data_values_list = [10.5]
    - Line 2: "20.0" -> Cleans text -> float("20.0") becomes 20.0 -> data_values_list = [10.5, 20.0]
    - Returns: [10.5, 20.0]
    """
    data_values_list = []
    
    # open() öppnar en anslutning till en textfil på datorn. Parametern "r" står för read-only.
    input_file_handle = open(file_path, "r")
    
    # En for-loop med 'in' går igenom samlingar sekventiellt, rad för rad i det här fallet.
    for raw_line in input_file_handle:
        # .strip() rensar bort osynliga tecken som blanksteg och radbrytningar (\n) från ändarna av en sträng.
        cleaned_line = raw_line.strip()
        
        # Jämförelseoperatören '==' kontrollerar om värdet på vänster sida är exakt lika med höger sida.
        if cleaned_line == "":
            # Nyckelordet 'continue' hoppar omedelbart över resten av koden i loopen och börjar om med nästa rad.
            continue
            
        # float() omvandlar en textsträng (t.ex. "10.5") till ett decimaltal i datorminnet.
        numerical_value = float(cleaned_line)
        # .append() lägger till ett nytt element längst bak i en befintlig lista.
        data_values_list.append(numerical_value)
        
    # .close() stänger filen så att andra program eller operativsystemet kan komma åt den igen.
    input_file_handle.close()
    # Nyckelordet 'return' skickar tillbaka det slutgiltiga beräknade värdet från en funktion till anroparen.
    return data_values_list


# =============================================================================
# Uppgift 4.3: Beräkna Batch Means (Gruppmedelvärden)
# =============================================================================

def compute_batch_means(data_values_list, batch_size):
    """Groups elements into chunks of a given size and computes the average for each.

    Step-by-Step Execution Workflow:
    1. Initializes an empty list named 'batch_averages_list'.
    2. Calculates the total count of numbers inside 'data_values_list' via len().
    3. Initializes a tracking variable 'current_start_index' at 0.
    4. Runs a while-loop as long as there are enough elements left to form a full batch.
    5. Extracts a sub-slice from the list starting at 'current_start_index' and ending 
       at 'current_start_index + batch_size'.
    6. Adds all numbers inside the sub-slice together using sum() and divides by 'batch_size'.
    7. Appends the computed average value into 'batch_averages_list'.
    8. Increments 'current_start_index' forward by the value of 'batch_size'.
    9. Returns the completed list of averages.

    Trace Example Scenario:
    Given data_values_list = [10, 20, 30, 40], and batch_size = 2:
    - Pass 1: start_index = 0. Slice = [10, 20]. Sum = 30. Average = 30 / 2 = 15.0. 
      List becomes: [15.0]
    - Pass 2: start_index = 2. Slice = [30, 40]. Sum = 70. Average = 70 / 2 = 35.0. 
      List becomes: [15.0, 35.0]
    - Pass 3: start_index = 4. Condition 4 <= 4 is False. Loop ends.
    - Returns: [15.0, 35.0]
    """
    batch_averages_list = []
    # len() är en inbyggd funktion som räknar ut det totala antalet element i en lista eller tecken i en sträng.
    total_elements_count = len(data_values_list)
    current_start_index = 0
    
    # En while-loop fortsätter exekvera sitt block så länge villkoret efter nyckelordet utvärderas till True.
    # Operatören '+' adderar tal, och '<=' kontrollerar om vänster sida är mindre än eller lika med höger sida.
    while current_start_index + batch_size <= total_elements_count:
        # List-slicing med [start:stopp] klipper ut en del av en lista från startindex fram till stoppindex.
        current_batch_slice = data_values_list[current_start_index : current_start_index + batch_size]
        
        # sum() är en inbyggd funktion som adderar alla numeriska värden inuti en lista.
        # Operatören '/' utför en helt vanlig matematisk division och ger alltid ett decimaltal som svar.
        computed_average_value = sum(current_batch_slice) / batch_size
        batch_averages_list.append(computed_average_value)
        
        # Operatören '+=' ökar det nuvarande värdet på en variabel med det angivna talet (samma som index = index + storlek).
        current_start_index += batch_size
        
    return batch_averages_list


# =============================================================================
# Uppgift 4.4: Visualisering med Matplotlib
# =============================================================================

def plot_batch_averages(batch_averages_list):
    """Generates a graphical line plot showing how batch averages fluctuate over time.

    Step-by-Step Execution Workflow:
    1. Takes the list of computed batch medelvärden.
    2. Calls pyplot.plot() to automatically map the indexes on the X-axis and values on Y-axis.
    3. Sets the main title header text using pyplot.title().
    4. Generates label strings for the X-axis and Y-axis via pyplot.xlabel() and ylabel().
    5. Renders the interactive plot graphic window on the screen using pyplot.show().

    Trace Example Scenario:
    Given batch_averages_list = [15.0, 35.0]:
    - Generates a coordinate space.
    - Plots coordinate point 1 at (0, 15.0).
    - Plots coordinate point 2 at (1, 35.0).
    - Draws a clean continuous line between the two coordinates and displays the window interface.
    """
    # Vi anropar funktioner inuti matplotlib via punktsyntaxen baserat på vårt skapade alias 'plt'.
    plt.plot(batch_averages_list)
    plt.title("Batch Means Variation Over Time")
    plt.xlabel("Batch Index Number")
    plt.ylabel("Calculated Average Value")
    plt.show()


# =============================================================================
# Uppgift 4.2 & 4.3: Huvudprogram med robust try-except felhantering
# =============================================================================

def main():
    """Manages the application flow, handling missing files and bad inputs safely."""
    print("Welcome to the Batch Means Processing Tool")
    
    # Try-except block används för felhantering (exception handling) i Python.
    # Koden under 'try:' övervakas. Om något kraschar hoppar Python direkt till 'except:' i stället för att stänga av programmet.
    try:
        user_file_choice = input("Enter the path to the simulation data file: ")
        simulation_data = read_simulation_data(user_file_choice)
        
        # int() omvandlar en textsträng till ett heltal (integer).
        user_batch_size = int(input("Enter the size of each batch group (integer): "))
        
        # Ett logiskt villkor för att kontrollera att användaren inte skickar in noll eller negativa batch-storlekar
        if user_batch_size <= 0:
            print("Error: Batch size must be a positive integer greater than zero.")
            return
            
        calculated_means = compute_batch_means(simulation_data, user_batch_size)
        
        print(f"Successfully processed {len(calculated_means)} data batches.")
        
        # Aktiverar visualiseringsverktyget för att rita upp diagrammet
        plot_batch_averages(calculated_means)
        
    # except fångar upp särfallet 'FileNotFoundError' om filnamnet som skrevs in inte kan hittas på datorn
    except FileNotFoundError:
        print("An error occurred: The requested data file could not be found. Please check the path.")
        
    # except fångar upp 'ValueError' om användaren råkar skriva in bokstäver i stället för siffror i int() eller float()
    except ValueError:
        print("An error occurred: Invalid data format detected. Ensure inputs and file rows contain only numbers.")


# Denna standard-if-sats kontrollerar om filen startas direkt av användaren (inte importeras som en modul av ett annat skript).
# Om den körs direkt utvärderas villkoret till True och vår main()-funktion startas.
if __name__ == "__main__":
    main()
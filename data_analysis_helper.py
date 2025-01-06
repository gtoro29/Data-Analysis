import pandas as pd

# Function to load CSV file
def load_csv(file_path, explanatory_col=None):
    """
    Load a CSV file and optionally display explanatory information.

    Args:
        file_path (str): Path to the CSV file.
        explanatory_col (str): Name of the column to use for explanatory information.
    
    Returns:
        pandas.DataFrame: The loaded data with the explanatory column dropped (if specified).
    """
    try:
        data = pd.read_csv(file_path)
        print(f"\nFile: {file_path}")
        
        # Print explanatory column if provided - Initially thought I needed this but leaving for if forked and needed
        if explanatory_col and explanatory_col in data.columns:
            print(f"Dataset Description ({explanatory_col}):")
            print(data[explanatory_col].unique())
            data = data.drop(columns=[explanatory_col])  # Drop the column after explanation
        
        print("Columns:", data.columns.tolist())
        return data
    except Exception as e:
        print(f"Error loading file {file_path}: {e}")
        return None

# Display the dataset as a grid
def display_data(data, max_rows=10):
    """
    Display the dataset in a grid/table format with column headers.

    Args:
        data (pandas.DataFrame): The dataset to display.
        max_rows (int): Maximum number of rows to display.
    """
    if data is not None:
        print("\nDataset Preview:")
        with pd.option_context('display.max_rows', max_rows, 'display.max_columns', None):
            print(data.head(max_rows).to_string(index=False))
    else:
        print("No data available to display.")

# Summarize the dataset
def summarize_data(data):
    """
    Display summary statistics for numerical columns in the dataset.

    Args:
        data (pandas.DataFrame): The dataset to summarize.
    """
    if data is not None:
        print("\nDataset Summary (Numerical Columns):")
        print(data.describe())
    else:
        print("No data available to summarize.")

# Interactively select specific columns for viewing
def select_columns(data):
    """
    Allow the user to select specific columns to display.

    Args:
        data (pandas.DataFrame): The dataset.
    
    Returns:
        pandas.DataFrame: The dataset with only the selected columns.
    """
    print("\nAvailable Columns:", data.columns.tolist())
    columns = input("Enter the columns you want to select (comma-separated): ").split(',')
    columns = [col.strip() for col in columns]  # Remove any extra spaces
    if all(col in data.columns for col in columns):
        return data[columns]
    else:
        print("One or more selected columns are not in the dataset.")
        return data

# Main script
if __name__ == "__main__":
    # List of CSV files to process
    csv_files = {
        "1": "//Users/glorimartoro/Documents/data-analysis/Respiratory Data from CDC/ILINet.csv",
        "2": "/Users/glorimartoro/Documents/data-analysis/Respiratory Data from CDC/WH3O_NREVSS_Clinical_Labs.csv",
        "3": "/Users/glorimartoro/Documents/data-analysis/Respiratory Data from CDC/WHO_NREVSS_Public_Health_Labs.csv"
    }

    # Name of the explanatory column (set to None to skip)
    explanatory_col = None  # Adjust if you have a specific metadata column - I removed them from these datasets

    try:
        while True:
            # Menu for file selection
            print("\nSelect a file to interact with:")
            for key, value in csv_files.items():
                print(f"{key}. {value.split('/')[-1]}")
            print("4. Exit Program")

            file_choice = input("Enter the number corresponding to your choice: ").strip()
            if file_choice in csv_files:
                file_path = csv_files[file_choice]

                # Load the dataset
                data = load_csv(file_path, explanatory_col=explanatory_col)

                if data is not None:
                    while True:
                        # Menu for actions
                        print("\nOptions:")
                        print("1. Display Data")
                        print("2. Summarize Data")
                        print("3. Select Columns")
                        print("4. Back to File Selection")

                        choice = input("Enter your choice: ").strip()
                        if choice == '1':
                            display_data(data, max_rows=10)
                        elif choice == '2':
                            summarize_data(data)
                        elif choice == '3':
                            filtered_data = select_columns(data)
                            print("\nFiltered Dataset Preview:")
                            display_data(filtered_data, max_rows=10)
                        elif choice == '4':
                            print("\nYou have exited this file's interactive menu. Returning to file selection...\n")
                            break
                        else:
                            print("Invalid choice. Please select a valid option.")
            elif file_choice == '4':
                print("\nYou have exited the program. Goodbye!\n")
                break
            else:
                print("Invalid choice. Please select a valid file or exit.")
    except KeyboardInterrupt:
        print("\n\nProgram interrupted by the user. Exiting gracefully. Goodbye!")
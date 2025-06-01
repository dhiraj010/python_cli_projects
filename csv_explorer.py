import pandas as pd

# Step 1: Ask user for CSV file path
file_path = input("Enter the path to your CSV file: ")

try:
    # Step 2: Load CSV
    data = pd.read_csv(file_path)
    
    # Step 3: Show basic info
    print(f"\n✅ File loaded successfully!")
    print(f"📊 Number of rows: {data.shape[0]}")
    print(f"📊 Number of columns: {data.shape[1]}\n")
    
    # Step 4: Show top 5 rows
    print("🔍 Top 5 rows:")
    print(data.head())

    # Step 5: Ask user if they want to filter
    filter_choice = input("\nDo you want to filter the data by a column? (yes/no): ").lower()

    if filter_choice == 'yes':
        print("\n🧩 Available columns:")
        print(list(data.columns))

        column_name = input("Enter the column name to filter by: ")

        if column_name in data.columns:
            filter_value = input(f"Enter the value to filter in '{column_name}': ")

            # Step 6: Filter the data
            filtered_data = data[data[column_name].astype(str) == filter_value]
            print("\n✅ Filtered Data:")
            print(filtered_data)

            # Step 7 (Bonus): Save filtered data
            save_choice = input("\nDo you want to save this filtered data? (yes/no): ").lower()
            if save_choice == 'yes':
                output_file = input("Enter a name for the new CSV file (e.g., result.csv): ")
                filtered_data.to_csv(output_file, index=False)
                print(f"📁 Saved to {output_file}")
        else:
            print("❌ Column not found.")
    else:
        print("👍 Done without filtering.")

except FileNotFoundError:
    print("❌ File not found. Please check the path and try again.")
except pd.errors.ParserError:
    print("❌ Could not parse the CSV file. Ensure it is properly formatted.")

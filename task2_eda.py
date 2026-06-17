import pandas as pd

try:
    # Task 1-la generate aagura CSV file-ah read panrom
    df = pd.read_csv('extracted_books_data.csv')
    
    print("--- 1. Dataset Preview ---")
    print(df.head(), "\n")
    
    print("--- 2. Data Structure & Types ---")
    print(df.info(), "\n")
    
    print("--- 3. Statistical Summary (Price Details) ---")
    print(df.describe(), "\n")
    
    # Data insights unique-ah find panrom
    highest_price = df['Price_In_Pounds'].max()
    most_expensive_book = df[df['Price_In_Pounds'] == highest_price]['Book_Title'].values[0]
    avg_price = df['Price_In_Pounds'].mean()
    
    print("--- 4. Key Insights & Findings ---")
    print(f"• Total books analyzed: {len(df)}")
    print(f"• Average price of books: £{avg_price:.2f}")
    print(f"• Most expensive book: '{most_expensive_book}' (£{highest_price})")
    print("\n✓ TASK 2 Completed Successfully!")

except FileNotFoundError:
    print("Error: 'extracted_books_data.csv' file not found. Run Task 1 first.")

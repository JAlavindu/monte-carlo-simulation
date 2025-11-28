from hitting_probability import hitting_prob
import pandas as pd
import os

def excel_writer(total_throws, total_hitting_count):
    # Ensure inputs are lists to support multiple rows
    if not isinstance(total_throws, list):
        total_throws = [total_throws]
    if not isinstance(total_hitting_count, list):
        total_hitting_count = [total_hitting_count]

    data = {
        'total throws': [],
        'total hitting count': [],
        'hitting probability (%)': [],
        'estimated value of Pi': []
    }

    for t, h in zip(total_throws, total_hitting_count):
        hitting_probability = hitting_prob(h, t)
        pi = (hitting_probability / 100) * 4
        
        data['total throws'].append(t)
        data['total hitting count'].append(h)
        data['hitting probability (%)'].append(round(hitting_probability, 2))
        data['estimated value of Pi'].append(round(pi, 6))

    new_df = pd.DataFrame(data)
    file_name = f'dart_simulation_.xlsx'
    
    if os.path.exists(file_name):
        try:
            existing_df = pd.read_excel(file_name)
            
            for index, row in new_df.iterrows():
                # Check if 'total throws' exists in the existing dataframe
                mask = existing_df['total throws'] == row['total throws']
                
                if mask.any():
                    # Update existing row
                    for col in new_df.columns:
                        existing_df.loc[mask, col] = row[col]
                else:
                    # Append new row
                    existing_df = pd.concat([existing_df, pd.DataFrame([row])], ignore_index=True)
            
            df = existing_df
            
        except Exception as e:
            print(f"Could not read existing file: {e}")
            df = new_df
    else:
        df = new_df

    try:
        df.to_excel(file_name, index=False)
        print(f"Data saved to {file_name}")
    except PermissionError:
        print(f"Error: Permission denied. Please close '{file_name}' if it is open in Excel and try again.")
    except Exception as e:
        print(f"An error occurred while saving the file: {e}")


from hitting_probability import hitting_prob
import pandas as pd

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

    df = pd.DataFrame(data)
    file_name = f'dart_simulation.xlsx'
    df.to_excel(file_name, index=False)
    print(f"Data saved to {file_name}")




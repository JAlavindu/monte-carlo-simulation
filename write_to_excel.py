from hitting_probability import hitting_prob
import pandas as pd

def excel_writer(total_throws, total_hitting_count):
    hitting_probability = hitting_prob(total_hitting_count, total_throws)
    pi = (hitting_probability / 100) * 4

    data = {
        'total throws': [total_throws],
        'total hitting count': [total_hitting_count],
        'hitting probability (%)': [round(hitting_probability, 2)],
        'estimated value of Pi': [round(pi, 6)]
    }

    df = pd.DataFrame(data)
    file_name = f'dart_simulation_{total_throws}_throws.xlsx'
    df.to_excel(file_name, index=False)




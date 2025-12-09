import pandas as pd

if __name__ == '__main__':
    df = pd.read_csv('result.csv')
    rating_length = df.groupby('rating')['length']\
                        .mean()\
                        .reset_index()
    rating_length.to_csv('rating_length.csv', index=False)
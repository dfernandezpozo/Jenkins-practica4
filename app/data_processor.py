import pandas as pd

def process_data(data):
    df = pd.DataFrame(data)
    return df.describe()

if __name__ == "__main__":
    data = {
        "age": [20, 25, 30, 16],
        "height": [170, 165, 180, 160]
    }
    result = process_data(data)
    print(result)

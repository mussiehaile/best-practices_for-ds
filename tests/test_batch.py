import pandas as pd
from datetime import datetime

def dt(hour, minute, second=0):
    return datetime(2022, 1, 1, hour, minute, second)

def test_prepare_data():
    data = [
        (None, None, dt(1, 2), dt(1, 10)),
        (1, None, dt(1, 2), dt(1, 10)),
        (1, 2, dt(2, 2), dt(2, 3)),
        (None, 1, dt(1, 2, 0), dt(1, 2, 50)),
        (2, 3, dt(1, 2, 0), dt(1, 2, 59)),
        (3, 4, dt(1, 2, 0), dt(2, 2, 1)),     
    ]

    columns = ['PULocationID', 'DOLocationID', 'tpep_pickup_datetime', 'tpep_dropoff_datetime']
    df = pd.DataFrame(data, columns=columns)

    expected_output = pd.DataFrame([
        (1, 2, dt(2, 2), dt(2, 3)),
        (2, 3, dt(1, 2, 0), dt(1, 2, 59)),
    ], columns=columns)

    result = data(df)

    assert result.equals(expected_output)

if __name__ == '__main__':
    test_prepare_data()

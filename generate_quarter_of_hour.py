from datetime import datetime, timedelta
import pandas
from credentials import *

#
# basic script to map numeric time to coresponding quarter of hour
# example: 1=2025-07-21 06:00, 2=2025-07-21 06:15
#

def generate_quarter_hours():
    start_time = datetime.strptime("2025-07-21 06:00", "%Y-%m-%d %H:%M")
    end_time = datetime.strptime("2025-07-22 05:59", "%Y-%m-%d %H:%M")

    current_time = start_time

    quarter_hours = []

    while current_time <= end_time:
        quarter_hours.append(current_time)
        current_time += timedelta(minutes=15)

    print(quarter_hours)

    return quarter_hours


def append_quater_of_hour(path, file):

    quarter_hours = generate_quarter_hours()

    pairs = []
    i = 1
    for qh in quarter_hours:
        pairs.append((i, qh))
        i = i + 1

    print(pairs)

    df = pandas.DataFrame(pairs, columns=["time", "quarter_of_hour"])

    df["time"] = df["time"].astype(str)

    print(df)

    df_output_spec2 = pandas.read_csv(
        path + "\\" + file, header=0, dtype=str, delimiter=",", encoding="UTF-8"
    )

    result = pandas.merge(df_output_spec2, df, how="left", on=["time"])

    result.to_csv(
        path + "\\" + "result_spec2_quarter_of_hour_with_quarter.csv",
        header=True,
        index=False,
    )


file = "result_spec2_quarter_of_hour.csv"
append_quater_of_hour(path, file)

from datetime import datetime
from pathlib import Path

import pandas as pd
import numpy as np

filepath = Path('../out.csv')
filepath.parent.mkdir(parents=True, exist_ok=True)

from helpers.environment_variables import CHANNELS

recording_buffer = list()
COLUMN_NAMES = [str(x) for x in range(CHANNELS - 6)]
COLUMN_NAMES.extend(["IMU_W", "IMU_X", "IMU_Y", "IMU_Z", "Buffer_Usage", "Counter"])


def add_recording(data: list[int]):
    recording_buffer.append(data)
    # can add live plotting here


def persist_recordings():
    print("""
        Persist Recording
        """)
    dataframe = pd.DataFrame(data=recording_buffer, columns=COLUMN_NAMES)
    timestamp = datetime.now().strftime("%Y-%m-%d-%H:%M:%S")
    print(dataframe.head(10))
    # dataframe.to_parquet("data/" + timestamp + ".parquet")
    print("""
            Saving data
            """)
    dataframe.to_csv(filepath)

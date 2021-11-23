from datetime  import datetime 
import pandas

def get_dataframe_from_json(json_dict):
    dataframe = pandas.json_normalize(json_dict)
    dataframe.index =  pandas.to_datetime(dataframe['date'])

    # drop unix timestamps & just use ISO8601 datetimes
    dataframe = dataframe.loc['1999-01-01':]
    return dataframe

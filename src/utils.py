
import pandas as pd 

def data_import(filepath : str) :

    data_import_df = pd.read_csv(filepath)
    return data_import_df 


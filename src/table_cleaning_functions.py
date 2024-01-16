''' Helper functions that can be imported in other scripts to clean table formatted data.
'''

import pandas as pd 
import re 
import json

PREFIX_MAP_PATH = '../mapping_data/prefix_map.json'
with open(PREFIX_MAP_PATH) as f:
    PREFIX_MAP = json.load(f)

def clean_prefixes(source_column: pd.Series) -> pd.Series:
    ''' Cleans the prefixes in the given dataframe column.

    Parameters
    ----------
    source_column: pd.Series
        The dataframe column to clean.
    
    Returns
    -------
    pd.Series
        The cleaned dataframe column.
    '''
    return source_column.apply(lambda x: x.replace(x.split(':')[0], PREFIX_MAP[x.split(':')[0].lower()]).strip() if pd.notnull(x) and x.split(':')[0].lower() in PREFIX_MAP else x)

def clean_parantheticals(source_column: pd.Series) -> pd.Series:
    ''' Cleans the parantheticals in the given dataframe column.

    Parameters
    ----------
    source_column: pd.Series
        The dataframe column to clean.
    
    Returns
    -------
    pd.Series
        The cleaned dataframe column.
    '''
    return source_column.apply(lambda x: re.sub(r'\([^)]*\)', '', x).strip() if isinstance(x, str) else x)
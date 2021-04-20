def create(df,column,list_):
    """
    Creates a subdataframe with those values of the given column present in the given list 
    Args:
        df (dataframe): dataframe to work with 
        column (series): column of the dataframe to be filtered on
        list_ (list): list with the values that are used for filtering 
    Returns:
        The subdataframe
    """
    return df[df[column].isin(list_)]

def replace(datafr, regex_countries, to_change, new_colum, old_column):
    datafr[new_column] = datafr[old_column].str.lower().replace(regex_countries, to_change, regex=True)
    return datafr
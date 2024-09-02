import numpy as np
import pandas as pd
from hopp.utilities import load_yaml
import os 

def get_filename_from_partial_name(directory: str, search_string: str):
    """This function finds and returns the first filepath in the 
    given directory that contains the given search string. This function
    was generated by ChatGPT 20240902 and edited by Jared Thomas

    Args:
        directory (str): path to directory to search
        search_string (str): string to use to find the desired filename

    Returns:
        str: relative path to file
    """
    # List all files in the given directory
    for filename in os.listdir(directory):
        # Check if the search_string is in the filename
        if search_string in filename:
            # Construct the full path to the file
            file_path = os.path.join(directory, filename)
            # Return the path of the found file
            return file_path
    
    raise(ValueError("No file found containing the string:", search_string))

def comparison_table(designs_to_compare=["01", "02", "03", "04", "05"]):
    ref_sys_path = "../reference-systems/"
    plant_files_path = "greenHEART/input-files/plant/"

    # get all reference design names
    reference_design_names = os.listdir(ref_sys_path)

    # define QOIs

    # loop over designs
    for design in designs_to_compare:
        # get full design name
        design_name = [s for s in reference_design_names if design in s][0]

        # load input files
        greenheart_input = load_yaml(get_filename_from_partial_name(ref_sys_path+design_name+"/"+plant_files_path, "greenheart"))
        hopp_input = load_yaml(get_filename_from_partial_name(ref_sys_path+design_name+"/"+plant_files_path, "hopp"))
        
        # combine the input dictionaries
        combined_inputs = hopp_input | greenheart_input

        # keep only QOIs
        # create dataframe
        # combine dataframes of all designs

    # print latex table
    

    return 0

if __name__ == "__main__":

    comparison_table()
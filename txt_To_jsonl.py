import os
import json
import glob

def process_text_file(input_file, output_file):
    with open(input_file, encoding="latin-1") as fin: 
        text = fin.read().replace('\n', ' ').replace('\\','').replace('"','')
        # Replace the '\"' with ''

        # Replace three spaces in a row with one
        while "   " in text:
            text = text.replace("   ", " ")

    # Get the name of the file 
    file_name = os.path.splitext(os.path.basename(input_file))[0]

    data_obj = {"text": text}

    with open(output_file, "a") as fout:
        json.dump(data_obj, fout)
        fout.write('\n')

def process_files_in_directory(directory):
    for file in glob.glob(os.path.join(directory, "*.txt")):
        output_file = "output.jsonl"
        process_text_file(file, output_file)

    for subdir in os.listdir(directory):
        subdir_path = os.path.join(directory, subdir)
        if os.path.isdir(subdir_path):
            process_files_in_directory(subdir_path)

if __name__ == "__main__":
    input_directory = "C:/Users/Sara Cardona/OneDrive/Escritorio/Bible Project_v4" 
    # Replace with the path of the directory
    # The script has to be in the folder in which you want to search the txt files
    process_files_in_directory(input_directory)

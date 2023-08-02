## Python Script Documentation

### Introduction

The Python script provided in this document serves one main task that consist in convert txt files into jsonl.

**Note 1.0** The script has to be in the folder so it knows where to search the txt files

**Note 1.1** The output can show the file names, just have to replace `"text"` for `file_name` in `the data_obj = {"text": text}`  

### Requirements

- Python 3.x installed on the system.

**Functionality:**

1. The function `process_text_file` Replace the line breaks, spaces in a row, and the characters '\' '"', Then it processes the text and saves it in a dictionary with the key "Text" (writes the jsonl)
2. The function `process_files_in_directory` takes a directory as input and processes all .txt text files in that directory.  (Finds the files to process)

**Parameters:**

- `directory` / `input_directory` (str): The path to the folder containing the text files.

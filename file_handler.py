def read_file(filename):
    """Reads the content of a file and returns it."""
    try:
        with open(filename, 'r') as file:
            content = file.readlines()
        return content
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
        return None
    except IOError:
        print(f"Error: Cannot read the file '{filename}'.")
        return None

def write_file(filename, content):
    """Writes the modified content to a new file."""
    try:
        with open(filename, 'w') as file:
            file.writelines(content)
        print(f"Content written to '{filename}' successfully.")
    except IOError:
        print(f"Error: Cannot write to the file '{filename}'.")

def modify_content(content):
    """Modifies the content by appending ' - modified' to each line."""
    return [line.strip() + ' - modified\n' for line in content]

def main():
    input_filename = 'input.txt'
    output_filename = 'output.txt'

    # Read the content from the input file
    content = read_file(input_filename)
    
    if content is not None:
        # Modify the content
        modified_content = modify_content(content)
        
        # Write the modified content to the output file
        write_file(output_filename, modified_content)

if __name__ == "__main__":
    main()
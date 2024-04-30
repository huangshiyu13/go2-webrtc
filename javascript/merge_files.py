from pathlib import Path
def main():
    input_dir = Path("./")
    output_file = Path("./merged.txt")
    if output_file.exists():
        output_file.unlink()

    read_suffix_list = [".js",".html"]

    files = input_dir.glob("*")
    for file in files:
        if file.is_file() and file.suffix in read_suffix_list:
            text = file.read_text()
            with open(output_file, "a") as f:
                f.write(f"File name: {file.name}\n" )
                f.write("File Content Start:\n")
                f.write(text)
                f.write("\nFile Content End\n\n")



if __name__ == '__main__':
    main()
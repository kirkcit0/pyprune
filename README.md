# PyPrune

PyPrune is a Python script designed to organize and clean up Wii game files within the `wbfs` directory of an SD card or USB drive used with a Wii console. The script moves `.wbfs`, `.wbf1`, and `.wbf2` files into their respective folders based on their base filenames and cleans up the filenames by extracting and retaining relevant content within brackets.

## Features

- Organizes `.wbfs`, `.wbf1`, and `.wbf2` files into folders named after their base filenames.
- Cleans up filenames by removing unwanted characters and retaining content within brackets.
- Skips macOS metadata files.
- Handles file not found errors gracefully.

## Requirements

- Python 3.x

## Usage

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/pyprune.git
   cd pyprune
   ```

2. **Ensure your Wii game files are in the `wbfs` directory:**

   Place your `.wbfs`, `.wbf1`, and `.wbf2` files in the `wbfs` directory within the cloned repository.

3. **Run the script:**

   ```bash
   python pyprune.py
   ```

   The script will process the files in the `wbfs` directory, organize them into folders, and clean up the filenames.

## How It Works

1. **Specify the Target Directory:**

   The script targets the `./wbfs` directory, which should contain the Wii game files.

2. **First Pass - Gather Files by Base Name:**

   The script scans the `wbfs` directory for `.wbfs`, `.wbf1`, and `.wbf2` files, skipping any macOS metadata files. It groups files by their base names.

3. **Create Folders and Move Files:**

   For each set of files with the same base name, the script creates a folder named after the base file (excluding the extension) and moves the files into the newly created folder.

4. **Clean the Filenames:**

   The script cleans the filenames by extracting content within brackets and removing unwanted characters. It then renames the files inside their respective folders with the cleaned filenames.

## Example

Before running the script:

```
wbfs/
├── Example Game [ID1234].wbfs
├── Example Game [ID1234].wbf1
├── Another Game [ID5678].wbfs
```

After running the script:

```
wbfs/
├── Example Game ID1234/
│   ├── Example Game ID1234.wbfs
│   ├── Example Game ID1234.wbf1
├── Another Game ID5678/
│   ├── Another Game ID5678.wbfs
```

## Notes

- Ensure the `wbfs` directory exists and contains your Wii game files before running the script.
- The script skips files starting with `._`, which are macOS metadata files.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.
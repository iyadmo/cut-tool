# Python Cut Utility

A lightweight Python implementation of the Unix `cut` command.

This project allows users to extract specific fields from delimited text files or standard input, similar to the Linux `cut` utility.

## Features

- Extract one or more fields
- Supports custom delimiters using `-d`
- Reads from files
- Reads from standard input (stdin)
- Simple command-line interface
- Written entirely in Python

## Usage

### Extract a single field

```bash
python3 cut.py -f1 sample.tsv
```

### Extract multiple fields

```bash
python3 cut.py -f"1 2" sample.tsv
```

### Use a custom delimiter

```bash
python3 cut.py -d, -f2 fourchords.csv
```

### Read from standard input

```bash
tail -n5 fourchords.csv | python3 cut.py -d, -f"1 2"
```

or

```bash
tail -n5 fourchords.csv | python3 cut.py -d, -f"1 2" -
```

## Project Structure

```
cut/
│── cut.py              # Main program
│── sample.tsv          # Sample tab-separated file
│── fourchords.csv      # Sample CSV file
```

## Technologies Used

- Python 3
- Command Line Interface (CLI)

## Learning Objectives

This project demonstrates:

- Command-line argument parsing
- File handling
- Reading from standard input
- String manipulation
- Delimited text processing
- Basic implementation of Unix utilities

## Example

Input (`sample.tsv`)

```
Name    Age    City
Alice   21     London
Bob     19     Paris
```

Command

```bash
python3 cut.py -f1 sample.tsv
```

Output

```
Name
Alice
Bob
```

## Future Improvements

- Support field ranges (`-f1-3`)
- Support field lists (`-f1,3,5`)
- Better error handling
- Unit tests
- Improved argument parsing with `argparse`

## License

This project is intended for educational purposes.

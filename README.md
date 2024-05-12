# Questions Data Parser

This Python script is designed to parse raw question data stored in a specific format and convert it into a structured JSON format. It particularly caters to extracting questions, options, correct answers, and solutions from a given text file.

## Requirements

- Python 3.10+
- Regular Expression library (`re`)
- JSON library (`json`)

## Usage

1. **Input Data**: Ensure you have the raw questions data stored in a text file named `raw_questions_data.txt`.
   
2. **Run the Script**: Execute the Python script `questions_parser.py`.

3. **Output**: After successful execution, the script will generate a JSON file named `json_formatted_questions.json` containing the parsed questions data in a structured format.

Keep the `"raw_questions_data.txt"` and the python script ( `questions_parser.py` ) inside the same folder

### Run the script in your terminal using python3: `python3 questions_parser.py`

## Functionality

- **parse_question() Function**: This function takes the raw question data as input and parses each question along with its options, correct answers, and solutions. It utilizes Regular Expressions to extract relevant information from the text.

- **JSON Conversion**: The parsed questions are then converted into JSON format using the `json.dumps()` method with indentation for better readability.

- **File I/O Operations**: The script reads data from `raw_questions_data.txt`, processes it, and writes the formatted JSON data to `json_formatted_questions.json`.



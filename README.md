---

# SQL Injection Detection Tool

This tool is designed to detect SQL injection vulnerabilities in web forms on a given website or URL. It scans the HTML forms present on the webpage, manipulates input fields, and analyzes server responses to determine potential vulnerabilities.

## Prerequisites

- Python 3.x
- `pip` package manager
- `virtualenv` (optional but recommended)

## Installation

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/code-1819/SQL-Injection-Detection-Tool.git
    ```

2. Navigate to the project directory:

    ```bash
    cd Sql-Injection-Detection-Tool
    ```

3. (Optional) Set up a virtual environment:

    ```bash
    virtualenv venv
    source venv/bin/activate  # On Windows, use venv\Scripts\activate
    ```

4. To deactivate the virtual environment do this:

    ```bash
    deactivate  # On Windows, it's the same
    ```

## Usage

1. Run the `scan.py` script:

    ```bash
    python scan.py 
    ```

2. The tool will scan all forms present on the provided URL and display whether any vulnerabilities are detected.

## Example

```bash
python scan.py
```

```bash
Enter the URL to scan: <Enter the url which you want to scan>
```

## Contributing

  Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or create a pull request.

## License

  This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

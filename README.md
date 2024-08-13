# Downloads Cleaner

A Python script to automate the cleanup of your Downloads folder by removing files and directories older than a specified threshold. 

## Features

- **Automatic Cleanup**: Removes files and directories older than a user-defined threshold (default: 30 days).
- **Logging**: Records details of deleted items in a log file for future reference.
- **Cross-Platform**: Works on Linux systems (tested on Fedora) and can be easily adapted for other platforms.

## Requirements

- Python 3.x
- `shutil` (part of Python's standard library)
- `os` (part of Python's standard library)
- `time` (part of Python's standard library)
- `datetime` (part of Python's standard library)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/downloads-cleaner.git
    cd downloads-cleaner
    ```

2. (Optional) Create and activate a virtual environment:

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install any dependencies (none required for this project).

## Usage

1. **Run the Script**:

    To clean up files in your Downloads folder that are older than 30 days:

    ```bash
    python clean_downloads.py
    ```

2. **Customize the Age Threshold**:

    You can modify the `age_threshold` variable within the script to change the age limit for deletion.

3. **View the Log**:

    After running the script, check the log file (`~/clean_downloads_log.txt`) to see which files and directories were deleted.

## Automating with Cron (Linux)

You can set up a cron job to run this script periodically. For example, to run the script every Sunday at midnight:

1. Open the crontab editor:

    ```bash
    crontab -e
    ```

2. Add the following line:

    ```bash
    0 0 * * 0 /usr/bin/python3 /path/to/clean_downloads.py
    ```

    Make sure to replace `/path/to/clean_downloads.py` with the actual path to your script.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [shutil](https://docs.python.org/3/library/shutil.html) - Used for file operations.
- [os](https://docs.python.org/3/library/os.html) - Used to interact with the operating system.
- [datetime](https://docs.python.org/3/library/datetime.html) - Used to handle date and time operations.
- [cron](https://man7.org/linux/man-pages/man5/crontab.5.html) - Useful for scheduling tasks in Unix-based systems.



### English Version

# Nuclio Function Management Tool

This project provides a set of Python scripts for managing and deploying [Nuclio](https://nuclio.io/) Serverless functions. You can quickly obtain lists of Nuclio projects and functions, and deploy new functions using these scripts.

## Features

- Retrieve lists of Nuclio functions and projects.
- Deploy new Serverless functions.
- Get detailed information about specific functions.

## Usage

1. Ensure Python and the `requests` library are installed in your environment.
2. Configure the `nuclio_dashboard_url` variable to point to your Nuclio dashboard.
3. Run the script and invoke different functions as needed.

## Installation Requirements

Ensure the following are installed in your system:

- Python 3.6+
- `requests` library

You can install `requests` using the following command:

```bash
pip install requests

## Future Optimization Plans

- Add error handling mechanisms to make the script more robust in case of API call failures.
- Provide more extensive configuration options to make the script more flexible.
- Enhance user interface by offering a command-line tool or graphical interface for users to choose from.
- Implement security enhancements, such as support for HTTPS connections and API key management.

## Contact

If you have any questions or suggestions, please contact us through GitHub Issues.

## References
[Nuclio Github](https://github.com/nuclio/nuclio)

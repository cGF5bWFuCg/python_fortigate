# FortiPay
## Add Objects from a CSV File

The `fortipay_add_obj_csv.py` script allows you to add FortiGate objects from a CSV file. Follow the steps below to set up and run the script:
Prerequisites

+ Install Python: Ensure you have Python 3 installed. You can download it from python.org.

+ Install Required Library: You need the requests library to make API `requests` to the FortiGate firewall. Install it using pip:

    `pip install requests`

## Generate API Token on FortiGate

    1. Log in to your FortiGate device.
    2. Navigate to System > Administrators > Create New.
    3. Set the type to API.
    4. Generate an API token and note it for later use.

## Running the Script

To run the script, use the following command with appropriate arguments:

`python3 fortipay_add_obj_csv.py -h`

### Usage

`usage: fortipay_add_obj_csv.py [-h] --ip IP --token TOKEN --file FILE`

### Options

    -h, --help Show this help message and exit
    --ip IP FortiGate IP address
    --token TOKEN FortiGate API token
    --file FILE Path to the CSV file

The --help or -h flag displays this help message, which is automatically provided by the argparse module when you define arguments in your script.

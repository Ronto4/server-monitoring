# server-monitoring

This is a small Python tool used to trigger actions depending on conditions.

## Usage

1. Clone this repo to your target machine.
1. Copy [`config.json.example`](./config.json.example) to `config.json`.
1. Adjust `config.json` to suit your needs.
1. (Optional) Create a virtual environment and activate it.
1. Install requirements: `pip install -r requirements.txt`.
1. (For manual testing) Run `main.py`: `python3 main.py`.
1. (For regular execution) Add `python3 main.py` (or, preferably using a fully qualified path for both Python (if using a virtual environment) and `main.py`) to your crontab. Choose your preferred execution interval, e.g. every minute.

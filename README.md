## Overview
Agent for saving humidity and tempearture information to influxdb
## Setup
- Open a terminal in the root repo directory.
- Ensure you have [Python](https://www.python.org/downloads/) with pip installed.
- `pip install -r requirements.txt`
- `pip install -e .`

This will install the package in "developer mode".  Subsequent changes to the files will automatically be reloaded.

## Running
- Open a terminal
- `python humidity_agent`
To run in test mode:
- `python humidity_agent -t`


## Running with Docker
- `docker build . -t humidity-agent`
- `docker run --name humidity-agent --privileged humidity-agent`
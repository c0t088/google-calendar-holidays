## google-calendar-holidays

Simple implementation to retrieve Panamanian holidays from Google Calendar API

## Configuration

Refer to this website for the necessary **python** configurations for Google Calendar API

https://developers.google.com/docs/api/quickstart/python

Once all necessary configurations are done, credentials must be stored as:

- credentials.json

## Modules

### holidays.py

Connects to Google Calendar API and retrieve panamanian holiday dates for the current year and saves it to **holidays.json**. This module contains an adapted version  of **quick start.py**, found on Google API Documentation Python Quickstart (https://developers.google.com/docs/api/quickstart/python)

### extract.py

Extracts dates from **holidays.json** and saves them as **dates.txt**

## License

MIT License

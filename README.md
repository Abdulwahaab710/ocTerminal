[![Build Status](https://travis-ci.org/Abdulwahaab710/ocTerminal.svg?branch=master)](https://travis-ci.org/Abdulwahaab710/ocTerminal)
#ocTerminal
![screenshot](https://github.com/Abdulwahaab710/ocTerminal/raw/master/screenshot.png)

ocTerminal is a python script that allows you to check the bus schedule from the terminal

To use the script you will need to get an API key from [OC transpo](http://www.octranspo.com/developers), and then add the api key to the json file.

## Installation
First clone the repository
```bash
 git clone https://github.com/Abdulwahaab710/ocTerminal
```
Rename **.env-sample** => **.env**
```bash
  mv .env-sample .env
```
Add you API_KEY and APP_ID to the .env file

## Run
To run ocTerminal:
```bash
  python ocTerminal <bus stop\station number>
```
Example
```bash
  python pcTerminal 8400
```

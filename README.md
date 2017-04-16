# ocTerminal [![Build Status](https://travis-ci.org/Abdulwahaab710/ocTerminal.svg?branch=master)](https://travis-ci.org/Abdulwahaab710/ocTerminal)

## Screenshots
| Screenshot with bus specifications |
| ---------------------------------- |
|![Screenshot with bus specifications](https://raw.githubusercontent.com/Abdulwahaab710/ocTerminal/master/screeenshot-with-bus-specifications.png)|

| Screenshot without bus specifications |
| ------------------------------------- |
|![Screenshot without bus specifications](https://raw.githubusercontent.com/Abdulwahaab710/ocTerminal/master/screeenshot-without-bus-specifications.png)|

ocTerminal is a python script that allows you to check the bus schedule from the terminal

To use the script you will need to get an API key from [OC transpo](http://www.octranspo.com/developers), and then add the api key to the **.env file**.

## Installation
First clone the repository
```bash
 git clone https://github.com/Abdulwahaab710/ocTerminal
```
Rename **.env-sample** => **.env**
```bash
  mv .env-sample .env
  # Adding the directory to the PATH
  path=$(pwd)/ocTerminal
  PATH=~$path:$PATH
```
Add you API_KEY and APP_ID to the .env file

## Run
To run ocTerminal:
```bash
  python ocTerminal <bus stop\station number> [<bus numbers>]
```
Example
```bash
  python pcTerminal 3000 85 95 98
```

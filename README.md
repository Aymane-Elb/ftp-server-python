# Phone FTP Cloud Backup

A lightweight Python tool that connects to a phone over FTP and automatically browses directories to prepare file backups (such as photos, videos, and documents) from the device storage.

This project was created to simplify transferring and backing up files from a mobile device to a local computer using a direct network connection.

## Overview

Many mobile FTP server applications expose device storage over a local network. This script connects to the FTP server running on the phone and allows the user to:

* Navigate phone directories
* Detect files and folders
* Prepare automated backups
* Download files from the phone to the computer

The project uses the `ftputil` library to simplify FTP operations and provides filesystem-like navigation similar to Python's `os` module.

## Features

* Connect to a phone FTP server over local network
* Navigate directories on the device
* Detect files and folders
* Prepare recursive backups
* Download files from specific directories (e.g. `DCIM/Camera`)
* Simple and minimal Python implementation

## Example Use Cases

* Backup phone photos to a local computer
* Sync media folders
* Inspect phone storage remotely
* Build automated backup scripts

## Requirements

Python 3.9+

Required library:

```
pip install ftputil
```

You also need an FTP server running on your phone (for example WiFi FTP Server or similar apps).

## Configuration

Update the connection parameters in the script:

```
host = "192.168.10.29"
port = 7812
user = "your_username"
password = "your_password"
```

Make sure your phone and computer are connected to the same WiFi network.

## Usage

Run the script:

```
python cloud.py
```

The script will connect to the FTP server and list files and directories from the exposed storage.

Example output:

```
['device']
Directory path: device/DCIM
Files: ['IMG001.jpg', 'IMG002.jpg']
```

## Project Structure

```
cloud_backup/
│
├── cloud.py
├── README.md
```

## Future Improvements

* Automatic recursive backup
* File change detection
* Incremental backup system
* Progress bar for downloads
* CLI interface
* Scheduling backups

## Security Notes

FTP is not encrypted. This project is intended for use on trusted local networks only.

## License

MIT License
:

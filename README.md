# Python Security & Reconnaissance Tools

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white)
![Security](https://img.shields.io/badge/Focus-Offensive%20Security-red?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Educational-green?style=for-the-badge)

## Overview
This repository contains a collection of custom command-line interface (CLI) tools developed during my studies in **Systems Science**. The main focus is to automate reconnaissance tasks, practice network programming with **Sockets**, and implement efficient data extraction using **RegEx**.

These tools demonstrate practical application of:
* **Multi-threading** for performance optimization.
* **Socket Programming** for raw network communication.
* **Argparse** for robust CLI interaction.
* **OSINT** methodologies.

---

## Included Tools

### 1. Network Reconnaissance Tool (recon-tool.py)
A multi-threaded scanner designed to map out networks and identify active services. It handles **port scanning**, **ICMP host discovery**, and **web status checks**.

**Features:**
* **Multi-threaded Scanning:** Scans ports concurrently to minimize execution time.
* **OS Detection:** Automatically adjusts ping commands based on the operating system (Windows/Linux).
* **Port & Web Scanning:** Checks for open ports and verifies HTTP status codes (200 OK).
* **Logging:** Implements the `logging` module for debugging and tracking.

**Usage:**
```bash
# Scan specific ports on a target IP
python recon-tool.py portscan -ip 192.168.1.1 -s 20 -e 80

# Check active hosts in a network range
python recon-tool.py hostscan -s 192.168.1.1 -e 192.168.1.254

# Check a list of websites
python recon-tool.py webcheck -u google.com github.com
```
### 2. OSINT Data Extractor (Email-extractror.py)
An automation script for Open Source Intelligence (OSINT) gathering. It parses large, unstructured text files to extract valuable contact information using Regular Expressions.

Key Concepts:

re module for complex pattern matching.

File I/O handling for reading and processing datasets.

Usage:

```Bash
python Email-extractror.py
# Follow the prompt to enter the filename you wish to scan
```
### 3. Website Availability Checker (website_checker.py)
A utility script to monitor the uptime of multiple web endpoints simultaneously using the requests library and threading.

Tech Stack
Language: Python 3

Libraries: socket, threading, argparse, requests, re, platform, logging

Tools: Wireshark (used for traffic analysis during development)

Disclaimer
These tools are developed for educational purposes and ethical security testing only. Usage of these tools for attacking targets without prior mutual consent is illegal. I assume no liability and am not responsible for any misuse or damage caused by this program.

Contact
Marcus Inal LinkedIn Profile

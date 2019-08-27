#!/usr/bin/env bash
sudo apt update && sudo apt full-upgrade
sudo apt install python3-mysqldb
git init
git clone https://github.com/dannbleeker/SearchForPrimeNumbers
python3 runPrimeSearch.py


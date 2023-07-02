#!/bin/bash
This script accepts a URL, sends a GET request to the URL and displays the body of the response
curl -s -L "$1"

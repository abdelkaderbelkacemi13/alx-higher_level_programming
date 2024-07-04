#!/bin/bash
#a script that sends a delete request to a URL and displays the body of the response
curl -sX DELETE "$1"

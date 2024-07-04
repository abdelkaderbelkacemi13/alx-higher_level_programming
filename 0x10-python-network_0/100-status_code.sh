#!/bin/bash
#a script that displays only the status code of the response of a request to a URL.
curl -s -o /dev/null -w "%{http_code}" "$1"

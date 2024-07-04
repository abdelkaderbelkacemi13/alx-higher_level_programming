#!/bin/bash
#a script takes a url and displays the body of the response of a POST request.
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"

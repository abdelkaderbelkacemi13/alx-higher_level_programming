#!/bin/bash
#a script that takes a URL and display all the methods that  the server accept.
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-

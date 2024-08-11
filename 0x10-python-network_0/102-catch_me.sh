#!/bin/bash
#a script that make a request and displays the response as "You got me!"
curl -sL -X PUT -H "Origin: HolbertonSchool" -d "user_id=98" 0.0.0.0:5000/catch_me

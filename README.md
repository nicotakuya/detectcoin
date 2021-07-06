# detectcoin

## Overview
This device can automatically count 100-yen coins.

- Jetson Nano 2GB Developer Kit
- Web camera (Logitech/Logicool C270)

## How to use
You need "jetson-inference" to run this program.
[jetson-inference](https://github.com/dusty-nv/jetson-inference)

Place the models folder in the same directory as program.
Execute the this command.

    python3 detectcoin.py

The total amount is displayed at the top of the screen.

## Movie
https://www.youtube.com/watch?v=maS8FidMF-A

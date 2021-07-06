# detectcoin

## Overview
This device can automatically count 100-yen coins.

- Jetson Nano 2GB Developer Kit
- Web camera (Logitech/Logicool C270)
- Loupe
![detectcoin1](https://user-images.githubusercontent.com/5597377/124542820-145f9580-de5f-11eb-8d4c-c6938e0ca141.jpg)
## How to use
You need "[jetson-inference](https://github.com/dusty-nv/jetson-inference)" to run this program.

Place the models folder in the same directory as program(detectcoin.py).
Execute the this command.

    python3 detectcoin.py

The total amount is displayed at the top of the screen.
![detectcoin2](https://user-images.githubusercontent.com/5597377/124541994-8931d000-de5d-11eb-8470-31ce6ba4c7ec.jpg)

## Movie
https://www.youtube.com/watch?v=maS8FidMF-A

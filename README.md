blinkenPi
---------

Because LEDs are fun.

Initiall this will display the space status on our small jumbotron but will also reflect current space life in the future

Dependencies
------------

```
sudo apt-get install python-imaging python3-pip python-requests python3-requests
sudo pip-3.2 install pillow

mkdir ~/bin

# Initialize submodules in repo
git submodule update --init
cd rpi-rgb-led-matrix/
make
cp rgbmatrix.so ../
cp led-matrix text-example ~/bin

# testing time
sudo ./minimal-example
sudo ./led-matrix -D 0
sudo python matrixtest.py
```

```
# the current way to start the script is:
# /etc/rc.local running directly lcd.sh as root
# lcd.sh starts the matrix display in an endless loop
# future: run lcd.sh earlier in boot process instead of at the end
```

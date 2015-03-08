blinkenPi
---------

Because LEDs are fun.

Initiall this will display the space status on our small jumbotron but will also reflect current space life in the future

Dependencies
------------

```
sudo apt-get install python-imaging

# Initialize submodules in repo
git submodule update --init
cd rpi-rgb-led-matrix/
make
cp rgbmatrix.so ../
sudo ./minimal-example
sudo ./led-matrix -D 0
sudo python matrixtest.py
```


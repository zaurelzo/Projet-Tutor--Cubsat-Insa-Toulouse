# Projet-Tutore-Cubsat-Insa-Toulouse
Prototype of a test platform using a raspberry pi.

Authors:
 * Abdillah Ahamada
 * Marc Bestmann
 * Amandine Djelassi
 * Pierre Murez

For this project, we have developed a test plateform using a raspberry pi. The main goal was to be able to generate spi,uart and I2C
packets using the raspberry pi. So whe have developed in python a GUI to remotely configure the number and type of packect to generate.
To be sure that our raspberry pi generate the number and type of packets that we have specified, we have added to our interface a way to configure
a saleae Logic Analyzer.

## What you need to install 
  Firstly download saleae software from this link :https://www.saleae.com/downloads
  You also need to intall few libraries:
  
  ```bash
      sudo apt-get install python3-tk #install tkinter library
      sudo pip3 install saleae #library to use saleae api
  ```

## To run

  ```bash
    cd GUI-AND-CLIENT-SERVER/
    python3 Cubsat_Gui.py 
  ```

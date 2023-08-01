# microscope-grid-gcode
GCODE-Generator for USB-microscope on klipper

Python script to generate GCODE for use with the AI3M XCarriage Microscope attachment posted here:
https://www.printables.com/model/539741-usb-microscope-mount-for-anycubic-i3mega-xcarriage

## Requirements: 
- Klipper equipped printer
- klipper-timelapse plugin
- python3

## Limitations:
This script currently does not have an interface, you need to edit variables in the code to use it.

## What it does:
This very simple script generates a GCODE file, which will make your printer move a USB-microscope over the buildplate 
and anything interesting on it, pausing every few millimeters to take a picture using the klipper-timelapse plugin.
When it's done, you can download the images in bulk and assemble them in photoshop or any other editor of your choice 
into a image of whatever you put on your buildplate. 
This works great when reverse engineering or debugging PCBs for example.

## How to use:
Open the python script in your favorite text editor and edit the variables to suit your printer and camera setup.
These are the main values to change:
area_width_mm - width of your scanarea/buildplate in mm
area_height_mm - height of your scanarea/buildplate in mm
start_pos_x - first scan position and lower limit on the x-axis
start_pos_y - first scan position and lower limit on the y-axis
cell_width_mm - width of the visible area of your camera in mm
cell_height_mm - height of the visible area of your camera in mm
pcb_clearance_mm - the height of the pcb or object under the microscope in mm, 
                   to avoid crashing into it the gcode will keep the printhead above this height.

The script will create a new file imageGrid.gcode inside of your working directory.

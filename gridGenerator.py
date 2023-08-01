#ImageGrid GCODE generator
#2023 by fluetke <github@fluetke.eu>

if __name__ == '__main__':

    area_width_mm=200
    area_height_mm=80
    start_pos_x = posx = 0
    start_pos_y = posy = 8
    cell_width_mm=5
    cell_height_mm=4.8
    pcb_clearance_mm=8
    start_gcode="M73 P0 R107\nM107\n;TYPE:Custom\nG90 ; use absolute coordinates\nG28 ; home all\nM501;\nM420 S\n"
    image_macro="TIMELAPSE_TAKE_FRAME\n"
    wait_macro_pre="M400\nG4 P5000\n"
    wait_macro_post="G4 P500\n"
    initial_position="G1 X" + str(start_pos_x) +" Y" + str(start_pos_y) + " Z" + str(pcb_clearance_mm) + " F1000 ; move print head up to give some clearance for pcb components\n"

    with open("./imageGrid.gcode", "w") as outputGCODE:

        outputGCODE.write(start_gcode)
        outputGCODE.write(initial_position)
        outputGCODE.write(wait_macro_pre)

        while True:
            while True:
                outputGCODE.write(image_macro)
                outputGCODE.write(wait_macro_post)
                posx += cell_width_mm
                outputGCODE.write("G1 X" + str(posx) + " F1000\n")
                outputGCODE.write(wait_macro_pre)
                if posx <= start_pos_x or posx >= area_width_mm-1:
                    break

            outputGCODE.write(image_macro)
            outputGCODE.write(wait_macro_post)
            posy += cell_height_mm
            if posy > area_height+0.1:
                break
            outputGCODE.write("G1 Y" + str(posy) + " F1000\n")
            outputGCODE.write(wait_macro_pre)
            cell_width_mm *= -1


        gcode = "G1 X" + str(start_pos_x) + " Y" + str(start_pos_y) + " Z" + str(pcb_clearance_mm+15) + " F1000\n"
        outputGCODE.write(gcode)

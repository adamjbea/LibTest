import helper.Detection as detect  # type: ignore
import numpy as np
import cv2
import helper.Tools as tools
import helper.Analyze as analyze  # type: ignore
import helper.Visualization as visual  # type: ignore
import helper.Beadcount as bc  # type: ignore


def Brightfield_Controller(dire, Output_Image_Browser):
    uploaded = []
    return_list = []
    uploaded, filenames = tools.all_imgs_directory(dire)
    filenames = [filename.replace(dire + "/", '') for filename in filenames]
    if filenames:
        img_bw = []

        for key in uploaded:
            if key == None:
                break
            img = np.asarray(key)
            color = detect.Color_Detection(img)
            if color == 'grey':
                img_bw.append(img)

        if len(img_bw) > 0:
            try:
                analysisdata, analyzed_imgs_bf, analyzed_figs = Brightfield_Analysis(
                    img_bw, Output_Image_Browser)
                i = 0
                for picturedata in analysisdata:
                    filename = filenames[i]
                    img_name = filename.replace(dire, '')
                    filename.replace('filename', '')
                    save_name = dire + "/Analyzed_BF_" + img_name
                    if len(analysisdata) == len(analyzed_imgs_bf):
                        image_to_write = cv2.cvtColor(
                            analyzed_imgs_bf[i], cv2.COLOR_RGB2BGR)
                        cv2.imwrite(save_name, image_to_write)
                    csvappend = [img_name, dire, save_name]
                    return_data = csvappend + [analyzed_figs[i]] + picturedata
                    return_list.append(return_data)
                    i += 1
                return return_list
            except Exception as e:
                return e

# Handles all brightficeld actions
# Calls all analysis and detection functions
# Also is in charge of formatting and presenting information to user
###############################################################################


def Brightfield_Analysis(img_bw, Output_Image_Browser):
    if img_bw is not None:
        fig_list = []
        analyzed_img = []
        accurate_circles = []
        data_collection = []
        volume_mergers = []
        circles_with_beads = []

        for img_set in range(len(img_bw)):
            BAD_IMAGE = False
            processed_img = tools.Incoming_Image_Processing(img_bw[img_set])
            accuracy_img_copy = processed_img.copy()
            bead_img_copy = processed_img.copy()

            circles_grey, zoom = detect.Circle_Finder(processed_img, 'grey')

            if circles_grey is not None and zoom != "ERROR":

                bead_load = ""
                bead_count = ""
                nobead_count = ""

                if zoom == "large":
                    accurate_circles = detect.Circle_Finder_Improve(
                        circles_grey, processed_img)
                    bead_count = 0
                    nobead_count = 0
                    bead_count, nobead_count, circles_with_beads = bc.Bead_Counting(
                        accurate_circles, bead_img_copy)
                    total_drops = bead_count + nobead_count
                    if total_drops == 0:
                        BAD_IMAGE = True
                        total_drops = 1
                        bead_count = 1
                    else:
                        bead_load = str(
                            round((bead_count/total_drops)*100))+"%"
                else:
                    accurate_circles = circles_grey[0]

                key_points = detect.Blob_Detect(processed_img, zoom)
                kp_read = tools.Readable_Key_Points(key_points)

                filter = len(accurate_circles)
                if filter > 50 and BAD_IMAGE == False:
                    circles_img = visual.Draw_Circles(
                        processed_img, accurate_circles, circles_with_beads)
                    return_data = analyze.Analytics_Display(
                        accurate_circles, kp_read, zoom)
                    img_blobs = visual.Draw_Blobs(circles_img, key_points)
                    analyzed_img.append(img_blobs)
                    fig = visual.Radius_Histogram(circles_grey[0])
                    fig_list.append(fig)
                    return_data.append(bead_load)
                    return_data.append(bead_count)
                    return_data.append(nobead_count)
                    data_collection.append(return_data)
                else:
                    return_data = (
                        ['Brightfield', "", "", "", "", "", "", "", "", ""])
                    return_data.append(bead_load)
                    return_data.append(bead_count)
                    return_data.append(nobead_count)
                    return_data.append(
                        "THIS IMAGE WAS PARTLY PROCESSED DUE TO POOR QUALITY")
                    data_collection.append(return_data)

            else:
                data_collection.append(
                    ["COULD NOT DETECT ANYTHING IN THIS IMAGE"])
                analyzed_img.append(processed_img)
    return data_collection, analyzed_img, fig_list

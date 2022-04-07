"""
Gregg Hebert – 1657892 – NSM - Undergraduate
Mubashir Khan - 1521657 - NSM - Undergraduate
George Coll Rodriguez - 1529011 – NSM – Undergraduate

Instructions:
-  Make sure the two .mp4 files are in the same folder as this script.
-  Make sure all necessary libraries are installed.
-  Run the program.
-  Once the first video ends, it will close automatically.
-  Close the first histogram after you are done observing it by clicking the 'X' in the top right corner.
-  The second set of video and histogram will persue automatically.
-  Once the second video ends, it will close automatically.
-  Close the second histogram after you are done observing it by clicking the 'X' in the top right corner.
-  Two .png files of the histograms will be added to the folder after closing the last histogram.

Note: press q at any time while the video is running to stop script.
"""
import numpy as np
import matplotlib.pyplot as plt
import cv2
import time

# parameters(the .mp4 video, number of frames in video (can be adjusted), type of perfusion(as string))


def getData(capture, numFrames, typePerfusion):
    i = 0
    x, y = [], []

    while True:
        (grabbed, frame) = capture.read()

        if not grabbed:
            break
        # Resize frame to width, if specified.
        if resizeWidth > 0:
            (height, width) = frame.shape[:2]
            resizeHeight = int(float(resizeWidth / width) * height)
            frame = cv2.resize(frame, (resizeWidth, resizeHeight),
                               interpolation=cv2.INTER_AREA)

        # Normalize histograms based on number of pixels per frame.
        numPixels = np.prod(frame.shape[:2])

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow(typePerfusion + ' Perfusion', gray)

        x.append(i/numFrames)

        # append the number of white pixels to array y
        y.append(np.count_nonzero(gray == 255))

        # plot in real-time with video
        ax.plot(x, y, color='b')
        fig.canvas.draw()

        i += 1

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    capture.release()
    cv2.destroyAllWindows()
    fig.savefig(typePerfusion+'.png')
    plt.show()


capture1 = cv2.VideoCapture('Normal_Perfusion.mp4')

color = 'gray'
typePerfusion = 'Normal'

# rough estimate of amount of frames/sec
numFrames = 15

# set width - can be adjusted fit your screen
resizeWidth = 700

# Label the plot axies and title
fig = plt.figure("Angiography Normal Perfusion Histrogram")
ax = fig.add_subplot(111)
ax.set_title('Normal Perfusion')
ax.set_xlabel('Time (s)')
ax.set_ylabel('Signal Strength (px count)')
fig.show()
getData(capture1, numFrames, typePerfusion)

capture2 = cv2.VideoCapture('Abnormal_Perfusion.mp4')

color = 'gray'
typePerfusion = 'Abnormal'
resizeWidth = 700

# Label the plot axies and title
fig = plt.figure("Angiography Abnormal Perfusion Histogram")
ax = fig.add_subplot(111)
ax.set_title('Abnormal Perfusion')
ax.set_xlabel('Time (s)')
ax.set_ylabel('Signal Strength (px count)')
fig.show()
getData(capture2, numFrames, typePerfusion)

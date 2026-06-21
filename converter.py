from PIL import Image
import numpy as np
import time
import os

gscale = '@%#*+=-:. '

def makeFile(imgFile, cols, scale, outFile):
    aimg = convertToASCII(imgFile, cols, scale)

    f = open(outFile, "w")

    print("Converting to ASCII...")

    for row in aimg:
        f.write(row + "\n")
    f.close()

    print("Done! File is ready at " + outFile + ".txt")

def getAvg(image):
    img = np.array(image)
    w, h = img.shape
    return np.average(img.reshape(w * h))

def convertToASCII(filename, cols, scale,):
    image = Image.open(filename).convert('L')

    W, H = image.size

    w = W / cols
    h = w / scale

    rows = int(H / h)

    aimg = []

    for row in range(rows):
        y1 = int(row * h)
        y2 = H if row == rows - 1 else int((row + 1) * h)

        aimg.append("")

        for col in range(cols):
            x1 = int(col * w)
            x2 = W if col == cols - 1 else int((col + 1) * w)

            img = image.crop((x1, y1, x2, y2))

            avg = int(getAvg(img))

            gsval = gscale[int(avg * (len(gscale) - 1) / 255)]

            aimg[row] += gsval

    return aimg

def main():
    print("Welcome to Matteo's Img2ASCII!")

    while True:
        simpleChoice = input("""    1. Simple mode
    2. Advanced mode
    0. Exit
    """)

        if simpleChoice == "1":
            while True:
                imgFile = input("Enter image path: ").strip('"')

                if os.path.isfile(imgFile):
                    break

                print("File not found. Please enter a valid path.")
                time.sleep(1)

            scale = 0.43
            cols = 80
            outFile = "ASCIIoutput.txt"
            makeFile(imgFile, cols, scale, outFile)

        elif simpleChoice == "2":
            while True:
                imgFile = input("Enter image path: ").strip('"')

                if os.path.isfile(imgFile):
                    break

                print("File not found. Please enter a valid path.")
                time.sleep(1)

            while True:
                outFile = input("Enter output filename: ").strip('"').strip()

                if outFile:
                    break

                print("Enter a valid output filename.")
                time.sleep(1)

            while True:
                cols = input("Enter number of columns: ").strip('"').strip()

                if cols:
                    if cols.isdigit():
                        cols = int(cols)-1
                        break
                    else:
                        print("Please enter a valid number of columns.")
                        time.sleep(1)

                print("Enter a valid number of columns.")

            while True:
                scale = input("Enter scale factor (0 to 1): ").strip('"').strip()

                if scale:
                    if scale.isdigit():
                        scale = float(scale)
                        if scale > 0 and scale <= 1:
                            break
                        else:
                            print("Please enter a valid scale factor.")
                    else:
                        print("Please enter a valid scale factor.")
                        time.sleep(1)

                print("Please enter a valid scale factor.")

            makeFile(imgFile, cols, scale, outFile)

        elif simpleChoice == "0":
            exit(0)

        else:
            print("Please enter a valid choice.")
            time.sleep(1)

if __name__ == "__main__":
    main()
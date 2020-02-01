# == Code by 21 rats#2113 | Worms by verenacafern#8203 == #
# Free to use, provided all derivatives are free & open source
# Appreciated but not required if you show me what you're using my code for owo


# == What The Heck is This? == #
# Takes a bunch of worm pictures you add, and randomly generates from them.


# === Imports === #

from PIL import Image       # Lets us do cool stuff with our worm images
import random               # Lets us randomise worm parts
import os

# === Variables === #
basePath = "input/base/"
eyePath = "input/eye/"
patternPath = "input/pattern/"
baseCount = 24
eyeCount = 12
patternCount = 4
variantNumber = 0

wormsMade = 0
createdWorms = [""]
tempFile = ""
outputFolder = "output"
done = False


# ======== Main Loop ========#
while not done:
    wormQuantity = int(input("How many worms would you like today? "))
    batchName = input("What batch of worms is this? This name affects the output filename. ")

    while wormsMade < wormQuantity:
        print("\n[INFO] Starting new worm loop. " + str(wormsMade) + " worms made so far.")
        variantNumber = random.randint(1, 2)            # Picks a random base from all of them
        # ======== Base A ======== #
        if variantNumber == 1:
            baseNum = random.randint(1, 12)             # Generates random base
            eyeNum = random.randint(1, 6)               # Generates random eye
            patternNum = random.randint(1, 2)           # Generates random pattern
            # TODO: make check each variants count, see issue #2 on github

            baseFile = basePath + "baseA" + str(baseNum) + ".png"              # Finds correct path
            eyeFile = eyePath + "eyeA" + str(eyeNum) + ".png"                  # Finds correct path
            patternFile = patternPath + "patternA" + str(patternNum) + ".png"  # Finds correct path

            saveFile = str(batchName) + "_worm_A_b" + str(baseNum) + "_e" + str(eyeNum) + "_p" + str(patternNum) + ".png"
            savePath = os.path.join(outputFolder, saveFile)      # Calculates save path for later
            base = Image.open(baseFile).convert('RGBA')          # Open file as RGB image with transparency
            eye = Image.open(eyeFile).convert('RGBA')            # Open file as RGB image with transparency
            pattern = Image.open(patternFile).convert('RGBA')    # Open file as RGB image with transparency

            tempFile = Image.alpha_composite(base, eye)          # Combines base and eye images
            tempFile = Image.alpha_composite(tempFile, pattern)  # Combines (base and eye) and pattern images

            if str(saveFile) in createdWorms:        # If the generated worm was already generated
                print("[WARN] Generated worm already exists, creating new worm...")
                continue
            elif str(saveFile) not in createdWorms:  # If the generated worm is unique
                tempFile = tempFile.save(savePath)   # Save it to the path previously calculated
                print("[INFO] Saved file to " + str(savePath) + ".")
                createdWorms.append(str(saveFile))   # Add file to list of existing worms
            else:
                print("[ERROR] Whatever you changed, change it back dude.")
                continue

        # ======== Base B ======== #
        elif variantNumber == 2:
            baseNum = random.randint(1, 12)             # Generates random base
            eyeNum = random.randint(1, 6)               # Generates random eye
            patternNum = random.randint(1, 2)           # Generates random pattern
            # TODO: make check each variants count, see issue #2 on github

            baseFile = basePath + "baseB" + str(baseNum) + ".png"              # Finds correct path
            eyeFile = eyePath + "eyeB" + str(eyeNum) + ".png"                  # Finds correct path
            patternFile = patternPath + "patternB" + str(patternNum) + ".png"  # Finds correct path

            saveFile = str(batchName) + "_worm_B_b" + str(baseNum) + "_e" + str(eyeNum) + "_p" + str(patternNum) + ".png"
            savePath = os.path.join(outputFolder, saveFile)      # Calculates save path for later

            base = Image.open(baseFile).convert('RGBA')          # Open file as RGB image with transparency
            eye = Image.open(eyeFile).convert('RGBA')            # Open file as RGB image with transparency
            pattern = Image.open(patternFile).convert('RGBA')    # Open file as RGB image with transparency

            tempFile = Image.alpha_composite(base, eye)          # Combines base and eye images
            tempFile = Image.alpha_composite(tempFile, pattern)  # Combines (base and eye) and pattern images

            if str(saveFile) in createdWorms:         # If the generated worm was already generated
                print("[WARN] Generated worm already exists, creating new worm...")
                continue
            elif str(saveFile) not in createdWorms:   # If the generated worm is unique
                tempFile = tempFile.save(savePath)    # Save it to the path previously calculated
                print("[INFO] Saved file to " + str(savePath) + ".")
                createdWorms.append(str(saveFile))    # Add file to list of existing worms
            else:
                print("[ERROR] Whatever you changed, change it back dude.")
                continue
        else:
            print("[ERROR] variantNumber did not match any existing variants.")
            continue
        wormsMade = wormsMade + 1
        print("[INFO] Loop completed, " + str(wormsMade) + " worms made so far.")
    print("\n[INFO] Worm creation finished. " + str(wormsMade) + " worms were made without any errors.\n[WARN] Exiting...")
    done = True

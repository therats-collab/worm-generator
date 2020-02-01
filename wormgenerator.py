# == Code by 21 rats#2113 | Worms by verenacafern#8203 == #
# Free to use, provided all derivatives are free & open source
# Appreciated but not required if you show me what you're using my code for owo


# == What The Heck is This? == # 
# Takes a bunch of worm pictures you add, and randomly generates from them.
# Expects all images to be the same size, and .png format. "Types" of worm (aka A worms, B worms) should be designed so every part fits with every other part of that type
# Also, everything that isn't the base MUST be transparent. The base is optionally transparent uwu
# Naming scheme defaults to baseX00.png / eyesX00.png, etc.
# === Imports === #

from PIL import Image # Lets us do cool stuff with our worm images
import random         # Lets us randomise worm parts
import glob           # Lets us do cool file stuff
import os             # Lets us do cool file stuff part 2

# === Variables === #
baseACount = 0
baseBCount = 0
for name in glob.glob('baseA*.png'):            # Figures out how many "A" bases there are
    baseACount = baseACount + 1       
for name in glob.glob('baseB*.png'):            # Figures out how many "B" bases there are
    baseBCount = baseBCount + 1       
baseCount = (baseACount + baseBCount)           # Figures out total number of bases

eyeACount = 0
eyeBCount = 0
for name in glob.glob('eyesA*.png'):            # Figures out how many "A" eyes there are
    eyeACount = eyeACount + 1         
for name in glob.glob('eyesB*.png'):            # Figures out how many "B" eyes there are
    eyeBCount = eyeBCount + 1         
eyeCount = (eyeACount + eyeBCount)              # Figures out total number of eyes

patternACount = 0
patternBCount = 0
for name in glob.glob('patternA*.png'):         # Figures out how many "A" patterns there are
    patternACount = patternACount + 1         
for name in glob.glob('patternB*.png'):         # Figures out how many "B" patterns there are
    patternBCount = patternBCount + 1         
patternCount = (patternACount + patternBCount)  # Figures out total number of patterns

wormsMade = 0
createdWorms = [""]
tempFile = ""
outputFolder = "output"
done = False


# ======== Main Loop ========#
while not done: 
    wormQuantity = int(input("How many worms would you like today? ")) # How many worms should it generate? Expects a digit (5, not "five")
    batchName = input("What batch of worms is this? This name affects the output filename. ") # What to put at the start of the name

    while wormsMade < wormQuantity:                         # Does this over and over again, until it's made as many as you asked for
        print("\n[INFO] Starting new worm loop. " + str(wormsMade) + " worms made so far.")
        baseNum = random.randint(1, (baseCount))            # Picks a random base from all of them
        # ======== Base A ======== #
        if baseNum <= baseACount:                           # Treats base A as the starting option. If theres 2 baseA and 3 baseB, 1 = A, 4 = B.
            eyeNum = random.randint(1,eyeACount)            # Uses a random eye (between 1 and the highest eye number in the folder)
            patternNum = random.randint(1,patternACount)
            
            baseFile = "baseA" + str(baseNum) + ".png"          # Finds the right base file path name
            eyeFile = "eyesA" + str(eyeNum) + ".png"            # Finds the right eye file path name
            patternFile = "patternA" + str(patternNum) + ".png" # Finds the right pattern file path name
            print("[INFO] Files to be combined are " + str(baseFile) + ", " + str(eyeFile) + " and " + str(patternFile) + ".")
            saveFile = str(batchName) + "_worm_A_b" + str(baseNum) + "_e" + str(eyeNum) + "_p" + str(patternNum) + ".png" # Figures out where to save the generated worm image
            savePath = os.path.join(outputFolder, saveFile)
            base = Image.open(baseFile).convert('RGBA')         # Magics the worm base into a format the code likes
            eye = Image.open(eyeFile).convert('RGBA')           # Magic the worm eyes into a format the code likes
            pattern = Image.open(patternFile).convert('RGBA')   # Magics the worm pattern into a format the code likes
                                                                # (basically "open this as an RGB image with transparency")

            tempFile = Image.alpha_composite(base, eye)                         # Mushes the two files together
            tempFile = Image.alpha_composite(tempFile, pattern)                 # Mushes THAT file and the pattern together

            if str(saveFile) in createdWorms:                                   # If the generated worm was already generated
                print("[WARN] Generated worm already exists, creating new worm...")    # Warn the user
                continue
            elif str(saveFile) not in createdWorms:
                tempFile = tempFile.save(savePath)
                print("[INFO] Saved file to " +str(savePath) +".")                         # Due to a limitation of the plugin, you can only combine 2 at a time
                createdWorms.append(str(saveFile))
            else:
                print("[ERROR] Yeah, idk whats happening chief.")
                continue

        # ======== Base B ======== #
        elif (baseNum > baseACount) & (baseNum <= baseCount):                           # Treats base A as the starting option. If theres 2 baseA and 3 baseB, 1 = A, 4 = B.
            eyeNum = random.randint(1,eyeBCount)           # Uses a random eye (between 1 and the highest eye number in the folder)
            patternNum = random.randint(1,patternBCount)
            baseNum = (baseNum-baseACount)                 # Needs to be added, otherwise it would be too high
            
            baseFile = "baseB" + str(baseNum) + ".png"     # Finds the right base file path name
            eyeFile = "eyesB" + str(eyeNum) + ".png"                    # Finds the right eye file path name
            patternFile = "patternB" + str(patternNum) + ".png"         # Finds the right pattern file name
            print("[INFO] Files to be combined are " + str(baseFile) + ", " + str(eyeFile) + " and " + str(patternFile) + ".")

            saveFile = str(batchName) + "_worm_B_b" + str(baseNum) + "_e" + str(eyeNum) + "_p" + str(patternNum) + ".png" # Figures out where to save the generated worm image
            savePath = os.path.join(outputFolder, saveFile)
            
            base = Image.open(baseFile).convert('RGBA')         # Magics the worm base into a format the code likes
            eye = Image.open(eyeFile).convert('RGBA')           # Magics the worm eyes into a format the code likes
            pattern = Image.open(patternFile).convert('RGBA')   # Magics the worm pattern into a format the code likes
                                                                # (basically "open this as an RGB image with transparency")

            tempFile = Image.alpha_composite(base, eye)                         # Mushes the two files together
            tempFile = Image.alpha_composite(tempFile, pattern)                 # Due to the limitation of the plugin, you can only combine 2 at a time
            if str(saveFile) in createdWorms:                                   # If the generated worm was already generated
                print("[WARN] Generated worm already exists, creating new worm...")    # Warn the user
                continue
            elif str(saveFile) not in createdWorms:
                tempFile = tempFile.save(savePath)
                print("[INFO] Saved file to " +str(savePath) +".")                         # Due to a limitation of the plugin, you can only combine 2 at a time
                createdWorms.append(str(saveFile))
            else:
                print("[ERROR] Yeah, idk whats happening chief.")
                continue
        else:
            print("[ERROR] " + str(baseNum) + " out of " + str(baseCount) + "; it looks like baseNum was too high. Check the code, something broke")                   # Catch when something else happen. It shouldn't.
            continue
        wormsMade = wormsMade + 1
        print("[INFO] Loop completed, " + str(wormsMade) + " worms made so far.")
    print("\n[INFO] Worm creation finished. " + str(wormsMade) + " worms were made without any errors.\n[WARN] Exiting...")
    done = True

# GredigLabFileRenamer
Standalone Executable that allows for easy file renaming for AFM images captured using the Cypher AFM

# Limitations
The program requires an input file name of the form: IIYYMMDDSS##_ADD****.ibw 

(Example: RM230126Si01_Pos0001.ibw)

where II is the initials of the user, YY is the last 2 digits of the year, MM is the month number, DD is the day number, SS is the sample substrate, ## is the sample number of the series. ADD is a 3 letter blurb for additional information. The **** will be added automatically by the igor Pro software that is used to control the Cypher AFM in the Gredig Lab.

Any 3 letter word will fit in the additional information section (Example: Pre). "Pos" will change to "Post", and "Pra" will change to "Practice" as they have been often used.

The naming convention that this program aims to fit to is outlined in Dr. Gredigs "Join Research Group" github page located at https://github.com/thomasgredig/JoinResearchGroup. Where AFM file names should have the form of 

Date_Project_Initials_Tool_Sample_AddInfo.ibw

# Anthony Krivonos
# covr.py
# 12.04.17

import os
import sys
import pyperclip
dir_path = os.path.dirname(os.path.realpath(__file__))

# Config Variables
TXT_INPUT = "txt_input/"
RPL_INPUT = "rpl_input/"
OUT_FILE = "txt_output/"

# Global Variables
errorCount = 0


# Read Code

def readFlagFromCmd(flag):
    for arg in sys.argv:
        if flag + "=" in arg and len(arg.split("=")) == 2:
            return arg.split("=")[1].strip()
    return ""


def readRplFromFile(fileName):
    with open(RPL_INPUT + fileName, mode='r') as input:
        reader = input.readlines()
        rpl = {row.split(",")[0].strip():row.split(",")[1].strip() for row in reader}
        return rpl


def readTxtFromFile(fileName):
    with open(TXT_INPUT + fileName, mode='r') as input:
        txt = input.read()
        return txt


# Writing Code


def writeOutToFile(fileName, txt):
    with open(OUT_FILE + fileName, mode='w') as output:
        txt = txt.replace("\r?\n", "\n")
        output.write(txt)
        return txt


# Templating Code

def template(txt, rpl):
    if rpl == {}:
        return txt
    txt = txt.replace("{{ ", "{{")
    txt = txt.replace(" }}", "}}")
    for key, value in rpl.items():
        preRpl = txt
        txt = txt.replace("{{" + key + "}}", value)
        if preRpl == txt:
            errorPrint("Could not find template {{" + key + "}}")
    return txt


# Utility Code
def errorPrint(err):
    errorAppend = "ERROR " + str(++errorCount) + ": "
    error = errorAppend + err
    print(error)
    return error


def copyToClipboard(txt):
    pyperclip.copy(unicode(txt, 'utf-8'))
    print("Output copied to clipboard")


# Run Code
def main():
    input = readFlagFromCmd("input") or readFlagFromCmd("i") or ""
    if input == "":
        return errorPrint("Could not read input file")
    replace = readFlagFromCmd("replacement") or readFlagFromCmd("replace") or readFlagFromCmd("rpl") or readFlagFromCmd("r") or ""
    output = readFlagFromCmd("output") or readFlagFromCmd("o") or ""
    if output == "":
        return errorPrint("Could not read output file")
    txt = readTxtFromFile(input)
    rpl = readRplFromFile(replace);
    tmpl = template(txt, rpl)
    replacedTxt = writeOutToFile(output, tmpl)
    copy = readFlagFromCmd("copy") == 'true' or readFlagFromCmd("c") == 'true' or False
    if copy:
        copyToClipboard(replacedTxt)
    print("Output created at " + output)
    return replacedTxt


main()

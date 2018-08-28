import os

import subprocess

import StringIO

import csv


def taskKill(imageName):
    return runCmd(['taskkill', '/im', imageName])


def taskList(imageName):
    (exitcode, stdout, stderr) = runCmd(['tasklist', '/nh', '/fo', 'csv', '/fi', "IMAGENAME eq %s" % imageName])

    if exitcode != 0:
        return []

    f = StringIO.StringIO(stdout)

    reader = csv.reader(f, delimiter=',', quoting=csv.QUOTE_ALL)

    toReturn = []

    for row in reader:

        if len(row) == 5:
            toReturn.append(row[1])

    return toReturn;


def runCmd(cmdArgs):
    process = subprocess.Popen(cmdArgs, stdout=subprocess.PIPE, shell=True)

    stdout, stderr = process.communicate()

    exitcode = process.wait()

    return (exitcode, stdout, stderr)
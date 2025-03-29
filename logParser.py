from datetime import datetime
import csv
import logging


def parseLogFile(filePath):
    """
    Parses logs from CSV file and extract job information.

    CSV file has 4 columns in the following order:
    - Timestamp: HH:MM:SS format.
    - Decription: a string describing the job.
    - Status: indicating "START" or "END" of the job.
    - PID: unique identifier for each job.

    Args:
        filepath (str): CSV log file path.

    Returns: dict: a dictionary mapping each PID(str) to job data, which includes:
                 - "start": datetime object indicating the job start time
                 - "end": datetime object indicating the job end time
                 - "description": job description string
    """
    with open(filePath, newline='') as csvFile:
        jobs = {}
        reader = csv.reader(csvFile)

        for row in reader:
            if not row:
                continue
            row = [column.strip() for column in row]
            if len(row) != 4:
                continue

            jobTimeStr, jobDescr, jobStatus, jobPid = row[0], row[1], row[2], row[3]

            # parse jobTimeStr to timestamp
            try:
                jobTime = datetime.strptime(jobTimeStr, "%H:%M:%S") # expecting format HH:MM:SS
            except ValueError as e:
                continue

            # checks if jobPid has been stored, otherwise tracks the job information
            if jobPid not in jobs:
                jobs[jobPid] = {"START": None, "END": None, "description": jobDescr}

            jobStatus = jobStatus.upper()
            # records the timestamp as start time for START status and end time for END status
            if jobStatus == "START":
                jobs[jobPid]["START"] = jobTime
            elif jobStatus == "END":
                jobs[jobPid]["END"] = jobTime
        return jobs

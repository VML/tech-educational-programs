import sys
sys.path.append('../')

from datetime import datetime as dt

class Program:
    """A tech educational program"""
    id = -1

    def __init__(self, id, row):
        self.id = id
        self.date_added = dt.strptime(row[1], '%m/%d/%Y')

        self.program_company = row[2]
        self.program_name = row[3]
        self.mission_purpose = row[4]
        self.race_identity = row[5]
        self.ethnic_identity = row[6]
        self.sexual_orientation = row[7]
        self.gender_identity = row[8]
        self.hours_per_week = row[9]
        self.program_duration = row[10]
        self.attendance_requirements = row[11]
        self.tech_focus = row[12]
        self.cost = row[13]
        self.contact_info = row[14]
        self.flagged_as_outdated = row[15]
        self.flagged_as_invalid = row[16]

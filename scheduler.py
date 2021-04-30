from events import Task, BusyBlock, WorkBlock

"""
  schedule() will use a modified version of the Earliest Deadline First (EDF)
    algorithm to schedule blocks of time to complete all tasks by their 
    deadlines while avoiding scheduling over pre-existing busy blocks of time.
  tasks : Task list
  busy_blocks : BusyBlock list
  day_start_time : datetime.time
  day_end_time : datetime.time
  
  requires: tasks and busy_blocks must be sorted in time increasing order
"""


def schedule(tasks, busy_blocks, day_start_time, day_end_time):
    return []

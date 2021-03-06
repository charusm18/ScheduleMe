""" 
Task is an assignment or job which must be completed by a specific due date.
    name : string
    due : datetime
    expected_time : datetime.time - the total time it is expected to take to 
      complete this task
    num_blocks : int - the amount of scheduled WorkBlocks this task will need to 
      be completed
"""


class Task:
    def __init__(self, name, due, expected_time, num_blocks):
        self.name = name
        self.expected_time = expected_time
        self.num_blocks = num_blocks


""" 
BusyBlock is a block of time which is pre-allotted in the user's calendar and 
  should not be scheduled over.
    name : string
    start_time : datetime
    end_time : datetime
"""


class BusyBlock:
    def __init__(self, name, start_time, end_time):
        self.name = name
        self.start_time = start_time
        self.end_time = end_time


""" 
WorkBlock is a block of time which is scheduled for a specific task. 
    start_time : datetime
    end_time : datetime
    task : Task - the task which should be worked on in this time block
    task_block_num : int - the nth occourance of a time block to work on the 
      specified task
"""


class WorkBlock:
    def __init__(self, start_time, end_time, task, task_block_num):
        self.start_time = start_time
        self.end_time = end_time
        self.task = task
        self.task_block_num = task_block_num

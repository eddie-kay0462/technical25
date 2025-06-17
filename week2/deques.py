"""
Deques are double-ended queues.
They are a generalization of stacks and queues.
They are a list-like data structure that allows you to add and remove elements from both ends.
Deques are thread-safe, meaning that multiple threads can operate on a deque simultaneously.
They are useful when you want to keep track of list of last seen items. For example, if you are building a web browser, you might want to keep track of the last 100 visited URLs. The maxlen parameter is used to limit the size of the deque.


"""

from collections import deque

#keep track of last 5 activities
recent_activities  = deque(maxlen=5)
actions= [
    "login", 
    "view dashboard",
    "click_report", 
    "download_pdf",
    "logout",
    "login_again",
    "change_password"
]


for action in actions:
    recent_activities.appendleft(action)
    print(f"Action {action} -> Recent : {list(recent_activities)}" )

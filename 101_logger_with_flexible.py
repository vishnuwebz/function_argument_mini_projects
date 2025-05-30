# 5 logger with flexible arguments

def event_logger(event_type, *details, **extra):
    print(f"[{event_type}")
    for d in details:
        print("-", d)
    for key, value in extra.items():
        print(f"{key.title()}: {value}")\

event_logger("INFOR", "User Logged In", "session_started", user="Vishnu", location= "India")

"""

- User Logged In
- session_started
User: Vishnu
Location: India
"""
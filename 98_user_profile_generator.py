# 2 User profile generator (using **kwargs)

def create_profile(**kwargs):
    print("User Profile")
    for key,value in kwargs.items():
        print(f"{key.title()}: {value}")

create_profile(name="Vishnu", age=27, city="Chennai")


"""
User Profile
Name: Vishnu
Age: 27
City: Chennai
"""
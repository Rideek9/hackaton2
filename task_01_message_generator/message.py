

def more_task(missing_task):
    if missing_task <= 1:
        return 'task'
    else:
        return 'tasks'


def rating_max(rating, task):
    if rating < 6:
        return f'Your rating will up to {rating+1}, when you give me overdue {task} {more_task(task)} '
    else:
        return ""


def hello(first_name, last_name):
    print(f"""
        Hi {first_name} {last_name}""")

def signature():
    print(f"""
        Good Luck 
        Teresa Rosberg
        """)

def have_tasks(task, rating):
    if task != 0:
        print(f"""
            I remind you that haven't finished {task} {more_task(task)}.
            You must send me this {more_task(task)} to next week.
            
            {rating_max(rating,task)}""")
    else:
        print(f"""
            You don't have any tasks, your rating is {rating}""")

def good_student(tasks,ratting):
    print(f"""
            You have {ratting}, congratulations.
            You received a scholarship of $1000 a mounth.""")



def message(firstname, lastname, missing_task, rating, email):
    print('\nsend email to:' ,email)
    if rating < 6:
        return f"""
            {hello(firstname,lastname)}
            {have_tasks(missing_task,rating)}
            {signature()}
        """
    else:
        return f"""
            {hello(firstname,lastname)}
            {good_student(missing_task,rating)}
            {signature()}
        """




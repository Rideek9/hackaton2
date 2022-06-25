# Message generator for teacher

This program is used to send multiple message at once. 

Below I present the operation of the program.
Program use cvs file to send message.

If you need a form, download it here. The form is a xlsx format. If you save the file, you must save as cvs format.

    place for link

    
## Sings
* Class - class where attended student
* First_Name - First Name of student
* Last_Name - Last Name od student
* Missing_Tasks - tasks that the student must give up
* Rating - final grade of the student
* Email - student email

!!!  REMEMBER YOU MAST COMPLETE ALL FIELDS !!!

If you don't have complited all row, app generated message about you and created file where you heve information what row is empty.
You must have completed all row, then app send messages to student.

## Message module

It's a module where apllication have messages to student.
In this module use function to insert relevant messages.
We have same messages to generate personality for student.

#### Example 1

Student have 0 missing_tasks and have rating at 6.

We send message with gratulations and information about scholarships.

#### Example 2

Student have 2 missing_tasks and have rating at 4

We send message with he must send tasks to next week and when he send his rating is up to one.

### Algorithm

1. When student have more than missing_tasks at 0 he must giv up tasks, when he give up tasks his rating is up to one
2. When student haven't missing_tasks then his rating is this in file
3. When student have rating at 6 he has scholarships

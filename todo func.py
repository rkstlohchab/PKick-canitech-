todo_list = []

def todo_l(*args):
    for i in args:
        work = i
        todo_list.append(work)
todo_l("eat", "repeat")

def done():
    work_done = input("Enter your work which is finished")
    todo_list.remove(work_done)
done()

def works():
    length = len(todo_list)
    print(length)
    print(todo_list)
works()
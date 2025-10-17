task_lists = []

    
try:
    while True:
        print("Select from one of the following options")
        print("options 1.Add task 2. Remove task 3. View task 4. Exit ")
        options = input("Enter an  option: ")
        
        if options == '1':
            task = input("Enter a task you would like to add: ")
            task_lists.append(task)
            print(task_lists)
        elif options == '2':
            task = input("Enter a task: ")
            task_lists.remove(task)
            print(task_lists)
        elif options == '3':
            for task in task_lists:
                print(task)
        elif options == '4':
            print("That will be all. Exiting the app")
            break
        else:
            print("Invalid input try again.")
except ValueError as e:
    print(e)
        
def menu():
    loop = 0
    print("******** Welcome to the Python Data Anaylysis App ********\n")

    while loop == 0:
        print("1. Population Data\n"
              "2. Housing Data\n"
              "3. Exit the Program\n")

        usr_choice = input("Select the file you want to analyze: ")
        if usr_choice == '1':
            print("You have entered Population Data. \n")
            print("a. Pop Apr 1 \n"
                  "b. Pop Jul 1 \n"
                  "c. Change Pop \n"
                  "d. Exit Column \n")

            usr_choice_loop = 0
            while usr_choice_loop < 1:
                usr_choice = input("Select the Column you want to analyze: ")

                if usr_choice == 'a':
                    count = 0
                    mean = 0
                    std_deviation = 0
                    min = 0
                    max = 0
                    print("You selected Pop Apr 1 \n"
                          "The statisitcs for this column are: \n"
                          "Count = count\n"
                          "Mean = \n"
                          "Stanard Deviation = \n"
                          "Min = \n"
                          "Max = \n"
                          "The Histogram of this columb is now displayed \n")
                    loop = 1


                elif usr_choice == 'b':
                    print("You selected Pop Jul 1")
                    loop = 1




                elif usr_choice == 'c':
                    print("You selected Change Pop")
                    loop = 1



                elif usr_choice == 'd':
                    print("You selected Exit Column")
                    loop = 1



                else:
                    print("Not a valid choice, try again\n")
                    break









        elif usr_choice == '2':
            print("2")
            break
        elif usr_choice == '3':
            print("3")
            break
        else:
            print("Not a valid choice, try again\n")


menu()

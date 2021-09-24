"""
Dameon Cole
SDEV300
Lab 5
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def menu():
    """
main menu loop
    """
    print("1. Population Data")
    print("2. Housing Data")
    print("3. Exit the Program\n")


def csv_loader(filepath):
    """
    :param filepath:csv file string
    :return: cvs file data
    """
    csv_file = pd.read_csv(filepath)
    return csv_file


def csv_column_loader(csv_file, column):
    """
    :param csv_file:
    :param column: cvs column selected
    :return: column data
    """
    column_data = csv_file[column]

    return column_data


def calculate_stats(column_data):
    """

    :param column_data: calculate the count,
    mean, standard deviation, minimum, maximum
    """

    column_data = np.array(column_data).flatten()
    count = column_data.shape[0]
    mean = np.mean(column_data)
    std_dev = np.std(column_data)
    mini = min(column_data)
    maxi = max(column_data)

    print(f"count : {count} \nmean : {mean} \n"
          f"standard_deviation : {std_dev} \nmin : {mini}\nmax : {maxi}\n")

    mu = mean  # Mean of data
    sigma = std_dev  # Standard Deviation of data
    x = mu + sigma * np.random.randn(10000)
    plt.hist(x, 25, density=True, facecolor='b', alpha=0.75, edgecolor='red')
    plt.grid(True)

    # plt.savefig("{}{}".format(title, ".svg"))

    plt.show()


def population(column_name):
    """

    :param column_name:
    """
    csv = csv_loader("PopChange.csv")
    apl1_pop = csv[column_name]
    calculate_stats(apl1_pop)


def housing(column_name):
    """

    :param column_name:
    """
    csv = csv_loader("Housing.csv")
    apl1_pop = csv[column_name]
    calculate_stats(apl1_pop)


def pop_menu():
    """
gghj
    """

    usr_choice = 1

    while usr_choice != 0:
        print("You have entered Population Data. \n")
        print("a. Pop Apr 1 ")
        print("b. Pop Jul 1 ")
        print("c. Change Pop ")
        print("d. Exit Column \n")
        usr_choice = input("Select the Column you want to analyze: ")

        if usr_choice == 'a':
            column_name = 'Pop Apr 1'
            population(column_name)
        elif usr_choice == 'b':
            column_name = 'Pop Jul 1'
            print("You selected " + column_name)
            population(column_name)
        elif usr_choice == 'c':
            column_name = 'Change Pop'
            print("You selected " + column_name)
            population(column_name)
        elif usr_choice == 'd':
            print("You selected Exit Column\n")
            usr_choice = 0
        else:
            print("Not a valid choice, try again\n")


def housing_menu():
    """
kl
    """
    usr_choice = 1

    while usr_choice != 0:
        print("You have entered Housing Data. \n")
        print("a. AGE ")
        print("b. BEDRMS ")
        print("c. BUILT ")
        print("d. ROOMS")
        print("e. UTILITY")
        print("f. Exit Column \n")
        usr_choice = input("Select the Column you want to analyze: ")

        if usr_choice == 'a':
            column_name = 'AGE'
            housing(column_name)
        elif usr_choice == 'b':
            column_name = 'BEDRMS'
            print("You selected " + column_name)
            housing(column_name)
        elif usr_choice == 'c':
            column_name = 'BUILT'
            print("You selected " + column_name)
            housing(column_name)
        elif usr_choice == 'd':
            column_name = 'ROOMS'
            print("You selected " + column_name)
            housing(column_name)
        elif usr_choice == 'e':
            column_name = 'UTILITY'
            print("You selected " + column_name)
            housing(column_name)
        elif usr_choice == 'f':
            print("You selected Exit Column\n")
            usr_choice = 0
        else:
            print("Not a valid choice, try again\n")


def program():
    """
k
    """
    print("******** Welcome to the Python Data Analysis App ********\n\n")

    usr_choice = 1

    while usr_choice != 0:
        try:
            menu()
            usr_choice = int(input("Select a file you want to analyze: "))

            if usr_choice == 1:
                pop_menu()

            elif usr_choice == 2:
                housing_menu()

            elif usr_choice == 3:
                print("\n\n\t       Thank You for using \n")
                print(" ******* The Python Data Analysis App ********")
                usr_choice = 0
            else:
                pass
        except ValueError:
            print("Not a valid choice, try again\n")


program()


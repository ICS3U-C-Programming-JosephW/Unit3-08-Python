#!/usr/bin/env python3
# Created By: Joseph Wondimagnehu
# Date: Apr. 5, 2025
# This program determines whether a year entered by the user
# is a leap year or not. Includes exceptions and negative
# integer handling.


# Define the main function.
def main():
    # Get the year from the user.
    year_as_str = input("Please, enter the desired year: ")

    # Try to check the validity of the inputted
    # year and whether it is a leap year or not.
    try:
        # Attempt to convert the string-type year input into an integer.
        year_as_int = int(year_as_str)

        # Check if the year is less than zero.
        if year_as_int < 0:
            # Display to the user that they cannot enter a negative year.
            print(f"\n{year_as_int} is negative. " "Negative years do not count.")
        # Otherwise, continue to leap year detection.
        else:
            # Check if the year is divisible by 4.
            if year_as_int % 4 == 0:
                # Check if the year is divisible by 100.
                if year_as_int % 100 == 0:
                    # Check if the year is divisible by 400.
                    if year_as_int % 400 == 0:
                        # Display to the user that the year is a leap year.
                        print(f"\n{year_as_int} is a leap year. " "It has 366 days.")

                    # Otherwise, it is not a leap year because it is a
                    # century year that is not divisible by 400.
                    else:
                        # Display to the user that the year is not a leap year.
                        print(
                            f"\n{year_as_int} is not a leap year. " "It has 365 days."
                        )
                # Otherwise, it is a leap year because it is
                # divisible by 4 but not 100.
                else:
                    # Display to the user that the year is a leap year.
                    print(f"\n{year_as_int} is a leap year. " "It has 366 days.")
            # Otherwise, it is not a leap year because all leap
            # years must be divisible by 4.
            else:
                # Display to the user that the year is not a leap year.
                print(f"\n{year_as_int} is not a leap year. " "It has 365 days.")
    # Runs if int() could not convert the user's input value to an integer.
    except:
        # Display to the user that their inputted year is not an integer.
        print(f"\n{year_as_str} is not an integer.")
    # Finally, run the last block of code in the try statement.
    finally:
        # Display a message thanking the user for using the program.
        print("Thanks for using the program!")


# Check if the special name of the file is __main__.
if __name__ == "__main__":
    # Run the main function if so.
    main()

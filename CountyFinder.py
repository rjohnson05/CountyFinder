class CountyFinder:
    """
    Program allowing the user query the county name and seat city of a number.

    After providing a number corresponding to a legitimate Montana county, the user can display the county name,
    seat city, or both. Upon completing the query, the user may repeat the process until quitting.

    Author: Ryan Johnson
    """

    def __init__(self):
        self.counties_dict = {}
        self.load_counties()
        self.done = False

    def load_counties(self):
        """
        Reads the county data from a .csv file and places it into a dictionary, with the county number as the key and
        an array containing the county name and seat city as the value.
        """
        file = open("./MontanaCounties.csv", 'r')
        for line in file:
            if "County" not in line:
                line_list = line.split(',')
                self.counties_dict[line_list[2].strip()] = [line_list[0], line_list[1]]

    def get_number(self):
        """
        Gets the county number from the user.

        :return: Integer representing the county number
        """
        valid = False
        while not valid:
            county_num = input("Enter the county number from the license plate: ")
            if county_num not in self.counties_dict.keys():
                print("Invalid county number. Please try a different number.")
                continue
            return county_num

    def get_result_prefs(self):
        """
        Gets the user's query preferences (whether they want to know the county name, seat city, or both).

        :return: Char representing the user's preferences ('c' for county name, 's' for seat city, and 'b' for both)
        """
        valid = False
        while not valid:
            result_prefs = input("Would you like to get the county name (c), seat city (s), or both (B)?")
            if result_prefs.lower() not in ['c', 's', 'b']:
                print("Invalid input. Please enter 'C', 'S', or 'B' to continue.")
                continue
            return result_prefs

    def find_results(self, county_num, result_prefs):
        """
        Gets the county name, seat city, or both from the counties_dict dictionary for displaying to the user.

        :param county_num:   Integer representing the county number from the user's license plate
        :param result_prefs: Char representing whether the user wants to know the county name, seat city, or both for a
                             county number
        """
        if result_prefs.lower() not in ['c', 's', 'b']:
            print("Invalid preferences. Please try again.")
        county_name = self.counties_dict[county_num][0]
        county_seat = self.counties_dict[county_num][1]
        match result_prefs:
            case 'c':
                print(f"The license plate is from {county_name} County.")
            case 's':
                print(f"The license plate is from {county_seat}.")
            case 'b':
                print(f"The license plate is from {county_name} County, where {county_seat} is the county seat.")

    def get_repeat(self):
        """
        Determines whether the user wants to query another county number or not.
        """
        repeat = input("Would you like to query another county number? (Y/N)")
        if repeat.lower() == 'n':
            self.done = True
        elif repeat.lower() != 'y':
            print("Invalid Input. Please Enter 'Y' to query another county number or 'N' to quit.")

    def exit(self):
        """
        Ends the program and notifies the user of the program's ending.
        """
        print("You have successfully exited.")

    def run(self):
        """
        Runs the program in a loop until the user chooses to end it.
        """
        while not counties.done:
            county_num = self.get_number()
            result_prefs = self.get_result_prefs()
            self.find_results(county_num, result_prefs)
            self.get_repeat()
        self.exit()


if __name__ == "__main__":
    counties = CountyFinder()
    counties.run()

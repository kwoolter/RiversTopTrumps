import csv
import logging

class Food():
    def __init__(self, name : str, category : str):
        self.name = name
        self.category = category
        self.attributes = {}

    def __str__(self):
        s = "{0} ({1}): {2} attributes".format(self.name, self.category, len(self.attributes))
        return s

    def add_attribute(self, attribute_name : str, attribute_value):
        new_value = is_numeric(attribute_value)
        self.attributes[attribute_name] = new_value

    def get_attribute(self, attribute_name : str):
        if attribute_name not in self.attributes.keys():
            raise Exception("Attribute {} not set for {}".format(attribute_name, self.name))

        value = self.attributes[attribute_name]

        if value is None:
            value_str = "0"
        elif value < 10:
            value_str = "{:0.1f}".format(value)
        else:
            value_str = "{:0.0f}".format(value)

        return value_str

    def print_card(self):
        print("{0} ({1})".format(self.name, self.category))
        attributes = sorted(list(self.attributes.keys()))
        for attribute in attributes:
            attribute_value = self.attributes[attribute]

            if attribute_value is not None:
                print("\t{0}: {1:.2f}".format(attribute, attribute_value))
            else:
                print("\t{0}: NONE".format(attribute))


class FoodFactory():
    def __init__(self):
        self.items = {}


    def load(self):
        print("\nLoading foods...")

        # Attempt to open the file
        with open(".\\data\\foods.csv", 'r') as object_file:

            # Load all rows in as a dictionary
            reader = csv.DictReader(object_file)

            # Get the list of column headers
            header = reader.fieldnames

            # For each row in the file....
            for row in reader:

                item_name = row.get("Item")
                item_category = row.get("Category")
                new_item = Food(item_name, item_category)

                if item_name not in self.items.keys():
                    self.items[item_name] = new_item

                # loop through all of the header fields except the first 2 columns...
                for i in range(2, len(header)):

                    attribute_name = header[i]
                    attribute_value = row.get(attribute_name)
                    new_item.add_attribute(attribute_name, attribute_value)


            # Close the file
            object_file.close()

    def print(self):
        for item in self.items.values():
            #print(str(item))
            item.print_card()


def pick(object_type: str, objects: list, auto_pick: bool = False):
    '''pick() -  Function to present a menu to pick an object from a list of objects
    auto_pick means if the list has only one item then automatically pick that item'''

    selected_object = None
    choices = len(objects)
    vowels = "AEIOU"
    if object_type[0].upper() in vowels:
        a_or_an = "an"
    else:
        a_or_an = "a"

    # If the list of objects is no good the raise an exception
    if objects is None or choices == 0:
        raise (Exception("No %s to pick from." % object_type))

    # If you selected auto pick and there is only one object in the list then pick it
    if auto_pick is True and choices == 1:
        selected_object = objects[0]

    # While an object has not yet been picked...
    while selected_object == None:

        # Print the menu of available objects to select
        print("Select %s %s:-" % (a_or_an, object_type))

        for i in range(0, choices):
            print("\t%i) %s" % (i + 1, str(objects[i])))

        # Along with an extra option to cancel selection
        print("\t%i) Cancel" % (choices + 1))

        # Get the user's selection and validate it
        choice = input("%s?" % object_type)
        if is_numeric(choice) is not None:
            choice = int(choice)

            if 0 < choice <= choices:
                selected_object = objects[choice - 1]
                logging.info("pick(): You chose %s %s." % (object_type, str(selected_object)))
            elif choice == (choices + 1):
                raise (Exception("You cancelled. No %s selected" % object_type))
            else:
                print("Invalid choice '%i' - try again." % choice)
        else:
            print("You choice '%s' is not a number - try again." % choice)

    return selected_object


def is_numeric(s):
    try:
        x = int(s)
    except:
        try:
            x = float(s)
        except:
            x = None
    return x

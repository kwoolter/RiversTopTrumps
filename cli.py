import cli

import cmd
import model
import view

class FoodCLI(cmd.Cmd):

    intro = "Welcome to the Food Top Trumps.\nType 'start' to get going!\nType 'help' for a list of commands."
    prompt = "What next?"

    def __init__(self):

        super(FoodCLI, self).__init__()

        self.model = None
        self.view = None

    def do_start(self, args):
        """Load all of the fixtures and predictions"""
        try:
            self.model = model.FoodFactory()
            self.model.load()
            self.view = view.FoodHTMLView()
            self.view.initialise()
        except Exception as err:
            print(str(err))

    def do_print(self, args):
        """Print all of the loaded details"""
        try:
            self.model.print()

            for item in self.model.items.values():
                print(self.view.render(item))


        except Exception as err:
            print(str(err))

    def do_quit(self, args):
        '''End the session'''
        print("bye bye")
        exit(0)
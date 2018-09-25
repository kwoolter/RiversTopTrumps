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
        """Load all of the foods"""
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
        except Exception as err:
            print(str(err))

    def do_render(self, args):
        """Render all of the loaded details"""
        try:
            items = sorted(list(self.model.items.keys()))
            for item_name in items:
                item = self.model.items[item_name]
                print(self.view.render(item))
        except Exception as err:
            print(str(err))

    def do_quit(self, args):
        '''End the session'''
        print("bye bye")
        exit(0)
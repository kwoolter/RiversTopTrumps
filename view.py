from jinja2 import Environment, PackageLoader, select_autoescape, FileSystemLoader
import model

class FoodHTMLView():

    def __init__(self):
        self.env = None

    def initialise(self):
        templateLoader = FileSystemLoader(searchpath="./view")
        self.env = Environment(loader=templateLoader)

        self.template = self.env.get_template('card_template.html')


    def render(self, food : model.Food):


        html = self.template.render(item_name = food.name,
                                    item_category = food.category,
                                    energy = food.get_attribute("Energy"),
                                    protein = food.get_attribute("Protein"),
                                    carbohydrate = food.get_attribute("Carbohydrate"),
                                    fat_total = food.get_attribute("Total Fat"),
                                    fibre=food.get_attribute("Total Dietary Fibre"),
                                    calcium=food.get_attribute("Calcium"),
                                    iron=food.get_attribute("Iron"),
                                    fat_saturated=food.get_attribute("Fat saturated"),
                                    sugar=food.get_attribute("Total Sugar"),
                                    salt=food.get_attribute("Sodium")
                                    )
        print(str(html))
        html = ""
        return(html)

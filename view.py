from jinja2 import Environment, PackageLoader, select_autoescape, FileSystemLoader
import model

class RiverHTMLView():

    def __init__(self):
        self.env = None
        self.template = None

    def initialise(self):
        templateLoader = FileSystemLoader(searchpath="./view")
        self.env = Environment(loader=templateLoader)
        self.template = self.env.get_template("card_template_new2.html")

    def render(self, river : model.River):


        length = "{:,}".format(int(river.get_attribute("Length (km)")))
        drainage_area = "{:,}".format(int(river.get_attribute("Drainage area")))
        country_count = "{:,}".format(river.get_attribute("Country Count"))
        average_discharge = "{:,}".format(int(river.get_attribute("Average discharge")))


        html = self.template.render(name = river.name,
                                    continent= river.continent,
                                    outflow = river.outflow,
                                    image = river.image_url,
                                    length = length,
                                    country_count = country_count,
                                    drainage_area = drainage_area,
                                    average_discharge = average_discharge
                                    )

        return(html)


from app.tools.base_tool import BaseTool
from app.tools.weather_tool.waether_arguments import WeatherArguments

class Weathertool(BaseTool[WeatherArguments]):

    name='weather'
    description="return the temperature and waether condition of the city"
    argument_model=WeatherArguments

    def execute(self, arguments)->dict:
        return {
            "temperature":23,
            "condition":"hot",
            "city":arguments.city
        }
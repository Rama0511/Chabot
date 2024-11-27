from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests

class ActionProvideWeather(Action):
    def name(self) -> Text:
        return "action_provide_weather"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:


        user_message = tracker.latest_message.get("text").lower()
        
        cities = [
    "jakarta", "surabaya", "bandung", "medan", "yogyakarta", "makassar", 
    "semarang", "palembang", "malang", "bali", "samarinda", "batam", 
    "bogor", "denpasar", "tangerang", "balikpapan", "bandar lampung", 
    "pekanbaru", "makasar", "ambon", "manado", "banjarmasin", "mataram", 
    "kupang", "pontianak", "cirebon", "tasikmalaya", "jambi", "lampung", 
    "banjarbaru", "sorong", "palu", "banda aceh",

    "new york", "los angeles", "chicago", "houston", "miami", 
    "san francisco", "boston", "dallas", "seattle", "las vegas", 
    "atlanta", "washington, d.c.", "austin", "denver", "orlando", 
    "philadelphia", "phoenix", "san diego", "portland", "detroit", 
    "minneapolis", "cleveland", "charlotte", "indianapolis", "tampa", 
    "salt lake city", "sacramento", "nashville", "kansas city", 
    "new orleans", "cincinnati", "st. louis", "buffalo", "raleigh",

    "london", "paris", "berlin", "madrid", "rome", "amsterdam", "vienna", 
    "zurich", "copenhagen", "brussels", "oslo", "stockholm", "warsaw", 
    "athens", "lisbon", "barcelona", "milan", "istanbul", "dubai", 
    "tokyo", "seoul", "shanghai", "beijing", "hong kong", "singapore", 
    "sydney", "bangkok", "mumbai", "melbourne", "rio de janeiro", 
    "sao paulo", "cape town", "buenos aires", "lagos", "lima", 
    "mexico city", "kuala lumpur"]
        location = None
        for city in cities:
            if city in user_message:
                location = city
                break

        if location:
            api_key = "7f6b1e365356a9cc6643f6ef8e91e677" 
            url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
            response = requests.get(url)

            if response.status_code == 200:
                data = response.json()
                temperature = data["main"]["temp"]
                description = data["weather"][0]["description"]
                response_message = (
                    f"It’s {temperature}°C currently in {location.title()}. "
                    f"The weather can be described as {description.capitalize()}."
                )
            else:
                response_message = f"Sorry, I couldn't retrieve the weather for {location.title()}."
        else:
            response_message = f"I'm sorry, I couldn't recognize the location.{location.title()}"

        dispatcher.utter_message(text=response_message)
        return []

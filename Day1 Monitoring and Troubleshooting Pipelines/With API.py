import requests
import pandas as pd
import logging

# Configure logging
logging.basicConfig(filename="weather_pipeline.log", level=logging.INFO, 
                    format="%(asctime)s - %(levelname)s - %(message)s")

api_key = "a08d5c0641b1cf05e1ce374de17f68d0"  
api_url = "http://api.weatherstack.com/current"

# List of cities in Egypt
cities = [
    "Cairo","Al Azbakeyah", "Al Basatin", "Tebin", "El-Khalifa", "El darrasa", 
    "Aldarb Alahmar", "Zawya al-Hamra", "El-Zaytoun", "Sahel", "El Salam", 
    "Sayeda Zeinab", "El Sharabeya", "Shorouk", "El Daher", "Ataba", 
    "New Cairo", "El Marg", "Ezbet el Nakhl", "Matareya", "Maadi", 
    "Maasara", "Mokattam", "Manyal", "Mosky", "Nozha", "Waily", 
    "Bab al-Shereia", "Bolaq", "Garden City", "Hadayek El-Kobba", "Helwan", 
    "Dar Al Salam", "Shubra", "Tura", "Abdeen", "Abaseya", "Ain Shams", 
    "Nasr City", "New Heliopolis", "Masr Al Qadima", "Mansheya Nasir", 
    "Badr City", "Obour City", "Cairo Downtown", "Zamalek", "Kasr El Nile", 
    "Rehab", "Katameya", "Madinty", "Rod Alfarag", "Sheraton", "El-Gamaleya", 
    "10th of Ramadan City", "Helmeyat Alzaytoun", "New Nozha", "Capital New", 
    "Giza", "Sixth of October", "Cheikh Zayed", "Hawamdiyah", "Al Badrasheen", 
    "Saf", "Atfih", "Al Ayat", "Al-Bawaiti", "ManshiyetAl Qanater", "Oaseem", 
    "Kerdasa", "Abu Nomros", "Kafr Ghati", "Manshiyet Al Bakari", "Dokki", 
    "Agouza", "Haram", "Warraq", "Imbaba", "Boulaq Dakrour", 
    "Al Wahat Al Baharia", "Omraneya", "Moneeb", "Bin Alsarayat", "Kit Kat", 
    "Mohandessin", "Faisal", "Abu Rawash", "Hadayek Alahram", "Haraneya", 
    "Hadayek October", "Saft Allaban", "Smart Village", "Ard Ellwaa", 
    "Abu Qir", "Al Ibrahimeyah", "Azarita", "Anfoushi", "Dekheila", 
    "El Soyof", "Ameria", "El Labban", "Al Mafrouza", "El Montaza", "Mansheya", 
    "Naseria", "Ambrozo", "Bab Sharq", "Bourj Alarab", "Stanley", "Smouha", 
    "Sidi Bishr", "Shads", "Gheet Alenab", "Fleming", "Victoria", 
    "Camp Shizar", "Karmooz", "Mahta Alraml", "Mina El-Basal", "Asafra", 
    "Agamy", "Bakos", "Boulkly", "Cleopatra", "Glim", "Al Mamurah", 
    "Al Mandara", "Moharam Bek", "Elshatby", "Sidi Gaber", 
    "North Coast/sahel", "Alhadra", "Alattarin", "Sidi Kerir", "Elgomrok", 
    "Al Max", "Marina", "Mansoura", "Talkha", "Mitt Ghamr", "Dekernes", 
    "Aga", "Menia El Nasr", "Sinbillawin", "El Kurdi", "Bani Ubaid", 
    "Al Manzala", "tami al'amdid", "aljamalia", "Sherbin", "Mataria", 
    "Belqas", "Meet Salsil", "Gamasa", "Mahalat Damana", "Nabroh", 
    "Hurghada", "Ras Ghareb", "Safaga", "El Qusiar", "Marsa Alam", 
    "Shalatin", "Halaib", "Aldahar", "Damanhour", "Kafr El Dawar", "Rashid", 
    "Edco", "Abu al-Matamir", "Abu Homs", "Delengat", "Mahmoudiyah", 
    "Rahmaniyah", "Itai Baroud", "Housh Eissa", "Shubrakhit", "Kom Hamada", 
    "Badr", "Wadi Natrun", "New Nubaria", "Alnoubareya", "Fayoum", 
    "Fayoum El Gedida", "Tamiya", "Snores", "Etsa", "Epschway", 
    "Yusuf El Sediaq", "Hadqa", "Atsa", "Algamaa", "Sayala", "Tanta", 
    "Al Mahalla Al Kobra", "Kafr El Zayat", "Zefta", "El Santa", "Qutour", 
    "Basion", "Samannoud", "Ismailia", "Fayed", "Qantara Sharq", 
    "Qantara Gharb", "El Tal El Kabier", "Abu Sawir", "Kasasien El Gedida", 
    "Nefesha", "Sheikh Zayed", "Shbeen El Koom", "Sadat City", "Menouf", 
    "Sars El-Layan", "Ashmon", "Al Bagor", "Quesna", "Berkat El Saba", "Tala", 
    "Al Shohada", "Minya", "Minya El Gedida", "El Adwa", "Magagha", 
    "Bani Mazar", "Mattay", "Samalut", "Madinat El Fekria", "Meloy", 
    "Deir Mawas", "Abu Qurqas", "Ard Sultan", "Banha", "Qalyub", 
    "Shubra Al Khaimah", "Al Qanater Charity", "Khanka", "Kafr Shukr", 
    "Tukh", "Qaha", "Obour", "Khosous", "Shibin Al Qanater", "Mostorod", 
    "El Kharga", "Paris", "Mout", "Farafra", "Balat", "Dakhla", "Suez", 
    "Alganayen", "Ataqah", "Ain Sokhna", "Faysal", "Aswan", "Aswan El Gedida", 
    "Drau", "Kom Ombo", "Nasr Al Nuba", "Kalabsha", "Edfu", "Al-Radisiyah", 
    "Al Basilia", "Al Sibaeia", "Abo Simbl Al Siyahia", "Marsa Alam", 
    "Assiut", "Assiut El Gedida", "Dayrout", "Manfalut", "Qusiya", "Abnoub", 
    "Abu Tig", "El Ghanaim", "Sahel Selim", "El Badari", "Sidfa", 
    "Bani Sweif", "Beni Suef El Gedida", "Al Wasta", "Naser", "Ehnasia", 
    "beba", "Fashn", "Somasta", "Alabbaseri", "Mokbel", "PorSaid", 
    "Port Fouad", "Alarab", "Zohour", "Alsharq", "Aldawahi", "Almanakh", 
    "Mubarak", "Damietta", "New Damietta", "Ras El Bar", "Faraskour", 
    "Zarqa", "alsaru", "alruwda", "Kafr El-Batikh", "Azbet Al Burg", 
    "Meet Abou Ghalib", "Kafr Saad", "Zagazig", "Al Ashr Men Ramadan", 
    "Minya Al Qamh", "Belbeis", "Mashtoul El Souq", "Qenaiat", "Abu Hammad", 
    "El Qurain", "Hehia", "Abu Kabir", "Faccus", "El Salihia El Gedida", 
    "Al Ibrahimiyah", "Deirb Negm", "Kafr Saqr", "Awlad Saqr", "Husseiniya", 
    "san alhajar alqablia", "Manshayat Abu Omar", "Al Toor", "Sharm El-Shaikh", 
    "Dahab", "Nuweiba", "Taba", "Saint Catherine", "Abu Redis", "Abu Zenaima", 
    "Ras Sidr", "Kafr El Sheikh", "Kafr El Sheikh Downtown", "Desouq", "Fooh", 
    "Metobas", "Burg Al Burullus", "Baltim", "Masief Baltim", "Hamol", "Bella", 
    "Riyadh", "Sidi Salm", "Qellen", "Sidi Ghazi", "Marsa Matrouh", "El Hamam", 
    "Alamein", "Dabaa", "Al-Nagila", "Sidi Brani", "Salloum", "Siwa", "Marina", 
    "North Coast", "Luxor", "New Luxor", "Esna", "New Tiba", "Al ziynia", 
    "Al Bayadieh", "Al Qarna", "Armant", "Al Tud", "Qena", "New Qena", 
    "Abu Tesht", "Nag Hammadi", "Deshna", "Alwaqf", "Qift", "Farshout",
]

weather_data = []

# Step 2: Loop through cities and fetch weather data
for city in cities:
    try:
        logging.info(f"Fetching weather data for {city}...")
        params = {
            "access_key": api_key,
            "query": city
        }
        response = requests.get(api_url, params=params)
        response.raise_for_status()
        
        logging.info(f"Response for {city}: {response.text}")  # Print raw response
        data = response.json()

        if "current" in data:
            weather_info = data["current"]
            weather_data.append({
                "City": city,
                "Observation Time":weather_info["observation_time"],
                "Temperature": weather_info["temperature"],
                "Humidity": weather_info["humidity"],
                "Weather": weather_info["weather_descriptions"][0],
                "Wind Speed":weather_info["wind_speed"],
                "Cloud Coverage:":weather_info["cloudcover"],
                "Pressure":weather_info["pressure"],
                "Precipitation":weather_info["precip"],
                "Visibility":weather_info["visibility"],
                "Wind Direction":weather_info["wind_dir"],
                })
        else:
            logging.error(f"Invalid data for {city}. Skipping.")
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching data for {city}: {e}")

# Step 3: Transform data into DataFrame
try:
    logging.info("Transforming data into DataFrame...")
    df = pd.DataFrame(weather_data)
    logging.info("Data transformation successful!")
except Exception as e:
    logging.error(f"Error transforming data: {e}")
    exit()

# Step 4: Save data to CSV
try:
    logging.info("Saving weather data to CSV...")
    df.to_csv("egypt_weather_data.csv", mode='a', index=False)
    logging.info("Weather data saved successfully!")
except Exception as e:
    logging.error(f"Error saving data: {e}")
    exit()


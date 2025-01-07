import streamlit as st
import requests

st.title("MyWeatherApp 🌤️")
st.write("בדף זה תוכלו לגלות את תחזית מזג האוויר בכל מקום בעולם !")

location=st.text_input("הזינו את שם העיר:")
if location:
    api_key= "4b2ab83e953225c381808309a1881d7c"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric&lang=he"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()

        city = data["name"]
        temp = data["main"]["temp"]
        weather_desc = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind_speed = data["wind"]["speed"]
        icon_code = data["weather"][0]["icon"]


        st.write(f"### תחזית מזג האוויר ב-{city}")
        st.write(f"🌡️ טמפרטורה: {temp}°C")
        st.write(f"☁️ תיאור: {weather_desc}")
        st.write(f"💧 לחות: {humidity}%")
        st.write(f"🔴 לחץ אטמוספירי: {pressure} ")
        st.write(f"🍃 מהירות רוח: {wind_speed} מטר/שנייה")

        icon_url= f"http://openweathermap.org/img/wn/{icon_code}@2x.png"
        st.image(icon_url, caption = "אייקון מזג אוויר", width = 300)

    else:
        st.error("אין מקום כזה בעולם. אנא וודא שהזנת שם נכון")

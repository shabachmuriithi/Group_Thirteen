fun main() {
   
 val weatherApp = WeatherForecastApp()


    weatherApp.addCity("Nairobi", 22.5f, 60, 5.0f)
    weatherApp.addCity("Mombasa", 25.0f, 50, 3.5f)
    weatherApp.addCity("Kisumu", 18.0f, 70, 4.0f)

    weatherApp.WeatherData()
}

data class WeatherInfo(
    val cityName: String,
    var temperature: Float,
    var humidity: Int,
    var windSpeed: Float
)
class WeatherForecastApp {
    val weatherData: MutableList<WeatherInfo> = mutableListOf()

   
    fun addCity(cityName: String, temperature: Float, humidity: Int, windSpeed: Float) {
        val newCityWeather = WeatherInfo(cityName, temperature, humidity, windSpeed)
        weatherData.add(newCityWeather)
        println("Added weather data for city: $cityName")
    }


    fun WeatherData() {
        for (weather in weatherData) {
            println("City: ${weather.cityName}, Temperature: ${weather.temperature}degrees celsius, Humidity: ${weather.humidity}%, Wind Speed: ${weather.windSpeed} m/s")
        }
    }
}

class WeatherApp {
  constructor() {
    this.cities = [];
  }
  addCity(cityName, temperature, humidity, windSpeed) {
    this.cities.push({
      name: cityName,
      temperature: temperature,
      humidity: humidity,
      windSpeed: windSpeed
    });
  }
  getCities() {
    return this.cities;
  }
}


// Example usage:
const app = new WeatherApp();
app.addCity("Mekelle", 21, 65, 12);
app.addCity("Addis Ababa", 25, 55, 10);
console.log(app.getCities());
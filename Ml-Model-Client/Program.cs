using System;
using System.Net.Http;
using System.Net.Http.Json;
using System.Text.Json;
using System.Threading.Tasks;

class Program
{
    static async Task Main(string[] args)
    {
        // Define the API endpoint URL
        var apiUrl = "http://localhost:4000/predict";

        // Input data for prediction
        var input = new { data = new[] { 1500 } }; // Example input data (sqft_living)

        using HttpClient client = new HttpClient();
        try
        {
            var response = await client.PostAsJsonAsync(apiUrl, input);

            if (response.IsSuccessStatusCode)
            {
                var predictedPrice = JsonSerializer.Deserialize<double[]>(await response.Content.ReadAsStringAsync());
                Console.WriteLine($"Predicted Price: {string.Join(", ", predictedPrice)}");
            }
            else
            {
                Console.WriteLine("Request failed with status code: " + response.StatusCode);
            }
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Error: {ex.Message}");
        }
    }
}
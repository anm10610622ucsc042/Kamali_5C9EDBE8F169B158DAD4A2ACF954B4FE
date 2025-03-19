DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Weather Dashboard</title>
</head>
<body>
    <h1>Weather Dashboard</h1>
    <form method="post">
        <input type="text" name="city" placeholder="Enter city name" required>
        <button type="submit">Search</button>
    </form>
{% if weather %}
{% if "error" in weather %}
            <p style="color: red;">{{ weather.error }}</p>
        {% else %}
            <h2>City: {{ weather.city }}</h2>
            <p>Temperature: {{ weather.temperature }}°C</p>
            <p>Humidity: {{ weather.humidity }}%</p>
            <p>Condition: {{ weather.description }}</p>
        {% endif %}
    {% endif %}
</body>
</html>

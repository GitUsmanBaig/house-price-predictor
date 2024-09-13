document.getElementById('predictionForm').addEventListener('submit', function(e) {
    e.preventDefault();

    // Gather form data
    let formData = {
        area: document.getElementById('area').value,
        bedrooms: document.getElementById('bedrooms').value,
        bathrooms: document.getElementById('bathrooms').value,
        stories: document.getElementById('stories').value,
        mainroad: document.getElementById('mainroad').value.toLowerCase() === 'yes',
        guestroom: document.getElementById('guestroom').value.toLowerCase() === 'yes',
        basement: document.getElementById('basement').value.toLowerCase() === 'yes',
        hotwaterheating: document.getElementById('hotwaterheating').value.toLowerCase() === 'yes',
        airconditioning: document.getElementById('airconditioning').value.toLowerCase() === 'yes',
        parking: parseInt(document.getElementById('parking').value),
        prefarea: document.getElementById('prefarea').value.toLowerCase() === 'yes',
        furnishingstatus: document.getElementById('furnishingstatus').value
    };

    // Send data to Flask API
    fetch('http://localhost:5000/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(formData)
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('result').innerHTML = `Predicted Price: ${data.prediction}`;
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('result').innerHTML = `Error: ${error.message}`;
    });
});

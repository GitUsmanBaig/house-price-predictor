document.getElementById('predictionForm').addEventListener('submit', function(e) {
    e.preventDefault();

    // Gather form data
    let formData = {
        area: document.getElementById('area').value,
        bedrooms: document.getElementById('bedrooms').value,
        bathrooms: document.getElementById('bathrooms').value,
        stories: document.getElementById('stories').value,
        mainroad: document.getElementById('mainroad').value,
        guestroom: document.getElementById('guestroom').value,
        basement: document.getElementById('basement').value,
        hotwaterheating: document.getElementById('hotwaterheating').value,
        airconditioning: document.getElementById('airconditioning').value,
        parking: document.getElementById('parking').value,
        prefarea: document.getElementById('prefarea').value,
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
    .catch(error => console.error('Error:', error));
});

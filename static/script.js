document.getElementById('predictionForm').addEventListener('submit', function(e) {
    e.preventDefault();

    // Gather form data
    let formData = {
        area: document.getElementById('area').value,
        bedrooms: parseInt(document.getElementById('bedrooms').value),
        bathrooms: parseInt(document.getElementById('bathrooms').value),
        stories: parseInt(document.getElementById('stories').value),
        mainroad: document.getElementById('mainroad').value,
        guestroom: document.getElementById('guestroom').value,
        basement: document.getElementById('basement').value,
        hotwaterheating: document.getElementById('hotwaterheating').value,
        airconditioning: document.getElementById('airconditioning').value,
        parking: parseInt(document.getElementById('parking').value),
        prefarea: document.getElementById('prefarea').value,
        furnishingstatus: document.getElementById('furnishingstatus').value
    };

    console.log("Sending Data:", formData); // Log the data being sent

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
        if(data.error) {
            console.error('Error:', data.error);
            document.getElementById('result').innerHTML = `Error: ${data.error}`;
        } else {
            document.getElementById('result').innerHTML = `Predicted Price: ${data.prediction}`;
        }
    })
    .catch(error => {
        console.error('Fetch Error:', error);
        document.getElementById('result').innerHTML = `Fetch Error: ${error.message}`;
    });
});

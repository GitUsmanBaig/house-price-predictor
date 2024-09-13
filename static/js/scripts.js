document.getElementById('priceForm').addEventListener('submit', function(e) {
    e.preventDefault();

    const formData = {
        features: [
            parseFloat(document.getElementById('medianIncome').value),
            parseInt(document.getElementById('houseAge').value),
            parseFloat(document.getElementById('roomsPerHousehold').value),
            parseFloat(document.getElementById('bedroomsPerHousehold').value),
            parseInt(document.getElementById('population').value),
            parseFloat(document.getElementById('households').value),
            parseFloat(document.getElementById('latitude').value),
            parseFloat(document.getElementById('longitude').value)
        ]
    };

    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData)
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('result').innerHTML = 'Predicted Price: $' + data.prediction[0].toFixed(2);
    })
    .catch(error => {
        console.error('Error:', error);
    });
});

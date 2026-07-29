async function predictPrice() {

    const button = document.querySelector("button");
    const result = document.getElementById("result");
    const predictionStatus = document.getElementById("predictionStatus");

    const houseImage = document.getElementById("houseImage");
    const houseType = document.getElementById("houseType");

    // =============================
    // Collect Data
    // =============================

    const data = {

        location: document.getElementById("location").value,

        Status: document.getElementById("status").value,

        Transaction: document.getElementById("transaction").value,

        Furnishing: document.getElementById("furnishing").value,

        facing: document.getElementById("facing").value,

        overlooking: document.getElementById("overlooking").value,

        Ownership: document.getElementById("ownership").value,

        Floor: Number(document.getElementById("floor").value),

        Bathroom: Number(document.getElementById("bathroom").value),

        Balcony: Number(document.getElementById("balcony").value),

        carpet_area_sqft: Number(document.getElementById("area").value),

        Car_Parking: Number(document.getElementById("parking").value)

    };

    // =============================
    // Validation
    // =============================

    if (
        !data.location ||
        !data.Status ||
        !data.Transaction ||
        !data.Furnishing ||
        !data.facing ||
        !data.overlooking ||
        !data.Ownership
    ) {

        alert("Please complete all fields.");
        return;

    }

    // =============================
    // Loading
    // =============================

    button.disabled = true;

    button.innerHTML =
        '<i class="fa-solid fa-spinner fa-spin"></i> Predicting...';

    result.innerHTML = "⌛";

    predictionStatus.innerHTML = "Contacting AI Model...";

    houseType.innerHTML = "Analyzing Property...";

    try {

        const response = await fetch(
            "http://127.0.0.1:8000/predict",
            {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(data)
            }
        );

        const prediction = await response.json();

        console.log("API Response:", prediction);

        if (!response.ok) {
            throw new Error(JSON.stringify(prediction));
        }

        const price = Number(prediction["Predicted Price"]);

        if (isNaN(price)) {
            throw new Error("Invalid prediction value");
        }

        // =============================
        // Display Price
        // =============================

        result.innerHTML =
            "₹ " +
            price.toLocaleString("en-IN", {
                maximumFractionDigits: 2
            });

        predictionStatus.innerHTML =
            "✅ Prediction Completed Successfully";

        // =============================
        // House Classification
        // =============================

        if (price < 2000000) {

            houseImage.src =
                "https://img.icons8.com/fluency/240/home.png";

            houseType.innerHTML =
                "🏠 Budget House";

            result.style.color = "#27ae60";

        }

        else if (price < 5000000) {

            houseImage.src =
                "https://img.icons8.com/fluency/240/cottage.png";

            houseType.innerHTML =
                "🏡 Family House";

            result.style.color = "#f39c12";

        }

        else {

            houseImage.src =
                "https://img.icons8.com/fluency/240/city-buildings.png";

            houseType.innerHTML =
                "🏛 Luxury Villa";

            result.style.color = "#e74c3c";

        }

    }

    catch (error) {

        console.error(error);

        result.innerHTML = "❌";

        predictionStatus.innerHTML = "❌ API Connection Failed";

        houseImage.src =
            "https://img.icons8.com/fluency/240/error.png";

        houseType.innerHTML =
            "Prediction Failed";

    }

    // =============================
    // Restore Button
    // =============================

    button.disabled = false;

    button.innerHTML =
        '<i class="fa-solid fa-calculator"></i> Predict House Price';

}
<?php
// Database connection details
$servername = "localhost";
$username = "root"; // Default username for XAMPP MySQL
$password = "";     // Default password is empty in XAMPP MySQL
$dbname = "MedEaseDB";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Check if form data has been submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Get form data
    $patient_name = $_POST['patient-name'];
    $phone = $_POST['phone'];
    $city = $_POST['city'];
    $symptoms = $_POST['symptoms'];
    $doctor = $_POST['doctor'];
    $location = $_POST['location'];

    // Prepare SQL statement
    $stmt = $conn->prepare("INSERT INTO appointments (patient_name, phone, city, symptoms, doctor, location) VALUES (?, ?, ?, ?, ?, ?)");
    $stmt->bind_param("ssssss", $patient_name, $phone, $city, $symptoms, $doctor, $location);

    // Execute SQL statement
    if ($stmt->execute()) {
        echo "Appointment scheduled successfully!";
    } else {
        echo "Error: " . $stmt->error;
    }

    // Close statement and connection
    $stmt->close();
}

$conn->close();
?>

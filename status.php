<?php

// Path to store the configuration (e.g., website URL)
$configFile = "/home/fpp/media/plugins/FPP-Status-plugin/config.ini";

// Save settings if the form is submitted
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $website_url = trim($_POST['website_url']);
    
    // Write to config file
    file_put_contents($configFile, "website_url={$website_url}\n");
    echo "<p>Configuration saved!</p>";
}

// Load the current configuration
$website_url = "";
if (file_exists($configFile)) {
    $config = parse_ini_file($configFile);
    $website_url = $config['website_url'] ?? '';
}

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>FPP Status Plugin Configuration</title>
</head>
<body>
    <h1>FPP Status Plugin Configuration</h1>
    <form method="POST">
        <label for="website_url">Website URL to update song info:</label><br>
        <input type="text" id="website_url" name="website_url" value="<?php echo htmlspecialchars($website_url); ?>" required><br><br>
        <input type="submit" value="Save">
    </form>
</body>
</html>
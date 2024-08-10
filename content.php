if (isset($_GET['command']) && $_GET['command'] == 'run_script') {
    $output = [];
    $return_var = 0;

    // Execute the Python script
    exec("python3 /home/fpp/media/plugins/<YourPluginName>/scripts/script.py", $output, $return_var);

    echo "<h3>Script Output:</h3>";
    echo "<pre>" . implode("\n", $output) . "</pre>";
    echo "<p>Return status: " . $return_var . "</p>";
}
# Code that needs to be added to basic_demo.ipynb
import requests 
import tempfile

url = "https://raw.githubusercontent.com/wDushanin/WNTR/refs/heads/main/examples/networks/Net3.inp"

# Fetch the INP file from GitHub
response = requests.get(url)

# Create a temporary file to save the INP content
with tempfile.NamedTemporaryFile(delete=False, suffix=".inp") as temp_inp_file:
    temp_inp_file.write(response.content)
    temp_file_path = temp_inp_file.name

# Create a WaterNetworkModel from the temporary INP file
wn = wntr.network.WaterNetworkModel(temp_file_path)
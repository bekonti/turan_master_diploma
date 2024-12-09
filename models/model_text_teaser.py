import requests

def run(input_text):
    # Make a POST request to the TextTeaser API
    response = requests.post("http://www.textteaser.com/api", data={"text": input_text})

    # Extract and output the summary from the API response
    summary = response.text
    print("Original Text:")
    print(input_text)
    print("\nSummary:")
    print(summary)

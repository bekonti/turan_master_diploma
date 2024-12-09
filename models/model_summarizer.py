from summarizer import Summarizer

def run(input_text):
    summarizer = Summarizer()

    # Generate the summary
    summary = summarizer(input_text, min_length=50, max_length=150)  # You can adjust the min_length and max_length parameters

    # Output the summary
    print("Original Text:")
    print(input_text)
    print("\nSummary:")
    print(summary)

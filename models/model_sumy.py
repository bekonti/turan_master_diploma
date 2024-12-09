from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

def run(input_text):
    parser = PlaintextParser.from_string(input_text, Tokenizer("russian"))

    # Create an LSA summarizer
    summarizer = LsaSummarizer()

    # Generate the summary
    summary = summarizer(parser.document, sentences_count=3)  # You can adjust the number of sentences in the summary

    # Output the summary
    print("Original Text:")
    print(input_text)
    print("\nSummary:")
    for sentence in summary:
        print(sentence)

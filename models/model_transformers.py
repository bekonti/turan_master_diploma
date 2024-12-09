from transformers import pipeline


def run(text):
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

    # Создаем краткое описание текста
    summary = summarizer(text, max_length=50, min_length=25, do_sample=False)

    # Выводим результат
    print("Краткое описание:")
    print(summary[0]['summary_text'])

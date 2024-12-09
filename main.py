from fastapi import FastAPI, Request, HTTPException
import models.model_bart
import models.model_summarizer
import models.model_sumy
import models.model_T5
import models.model_text_teaser
import models.model_gensim
import models.model_transformers
from googletrans import Translator

app = FastAPI()


# def run_bot():
#     asyncio.set_event_loop(asyncio.new_event_loop())  # Создаём новый цикл событий
#     start_bot()


# @app.on_event("startup")
# def start_polling_bot():
#     bot_thread = Thread(target=run_bot)
#     bot_thread.start()

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/generate")
async def say_hello(request: Request):
    if not request:
        raise HTTPException(status_code=400, detail="No text provided")
    request_body = await request.json()  # Parse the JSON body
    text = request_body.get("text", None)
    fromModel = models.model_bart.run(text)
    translated_text = translate_text(fromModel, src_lang="en", dest_lang="ru")
    if "Алматский" in translated_text:
        translated_text = translated_text.replace("Алматский", "Алматинский")
    if "Альмати" in translated_text:
        translated_text = translated_text.replace("Альмати", "Алматинский")
    # if "." in translated_text:
    #     translated_text = translated_text.replace("Альмати", "Алматинский")
    print("Translated to English:", translated_text)

    # models.model_summarizer.run(text)
    # models.model_sumy.run(text)
    # models.model_T5.run(text)
    # models.model_text_teaser.run(text)
    # models.model_transformers.run(text)
    return {"message": translated_text, "fromModel": fromModel, "initText": text}


def translate_text(text, src_lang, dest_lang):
    translator = Translator()
    try:
        translation = translator.translate(text, src=src_lang, dest=dest_lang)
        return translation.text
    except Exception as e:
        return f"Error: {e}"

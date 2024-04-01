import nltk
import os
import logging
from nltk.sentiment import SentimentIntensityAnalyzer


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    desired_location = os.getcwd()
    try:
        logging.info("Downloading packege ...")
        nltk.download("vader_lexicon", download_dir=desired_location)
        logging.info(f"The vader_lexicon has been downloaded in {desired_location}!")
    except Exception as e:
        logging.error(f"An error: {e}")

    try:
        logging.info("Testing with  a very simple text")
        texto = "I am so happy today!"
        sia = SentimentIntensityAnalyzer()
        sentimento = sia.polarity_scores(texto)
        if sentimento['compound'] > 0:
            logging.info(f"O sentimento é positivo: {sentimento['compound']}")
        elif sentimento['compound'] < 0:
            logging.info(f"O sentimento é negativo:{sentimento['compound']}")
        else:
            logging.info(f"O sentimento é neutro: {sentimento['compound']}")
    
    except Exception as e:
        logging.error(f"An error: {e}")
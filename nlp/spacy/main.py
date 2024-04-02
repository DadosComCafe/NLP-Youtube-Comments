import logging
from spacy import cli, load, util, tokens

def get_model(model_name: str = "pt_core_news_md") -> bool:
    """Get the model if it there isn't in python environment.

    Args:
        model_name (str, optional): The desired model names. Defaults to "pt_core_news_md".

    Raises:
        Exception: Raise an Exception in model download failure.

    Returns:
        bool: True if execution was fine.
    """
    if util.is_package(model_name):
        logging.info(f"O modelo {model_name} já está instalado.")
    else:
        logging.info(f"O modelo {model_name} ainda não está instalado.")
        try:
            cli.download("pt_core_news_md")
            logging.info(f"Modelo {model_name} baixado com sucesso!")
            return True
        except Exception as e:
            raise Exception(f"An error: {e}!")

def generate_token(text: str, model_name: str = "pt_core_news_md") -> tokens.doc.Doc:
    """Generates the token that will make possible to do an analyses above the given `text`. 

    Args:
        text (str): The text you want to analyze. 
        model_name (str, optional): The model used in spacy to get the text as token. Defaults to "pt_core_news_md".

    Returns:
        tokens.doc.Doc: The given `text` as a token object.
    """
    get_model(model_name=model_name)
    nlp = load(model_name)
    doc = nlp(text)
    return doc


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    generate_token("A very simple text!")

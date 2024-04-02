import logging
from spacy import cli, load, util

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


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    get_model()

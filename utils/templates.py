from jinja2 import Environment, FileSystemLoader, select_autoescape
import logging


logging.basicConfig(level=logging.INFO)


def load_template(name: str) -> str | None:
    '''
    Loads a Jinja2 template based on the provided name.

    Args:
        name (str): The name of the template to load.

    Returns:
        str | None: Returns the loaded template content.
        If an error occurs, returns None.
    '''
    env = Environment(
        loader=FileSystemLoader('templates'),
        autoescape=select_autoescape(['html'])
    )

    if name is None:
        logging.error('Template name cannot be null')
        return None

    try:
        return env.get_template(name)
    except FileNotFoundError:
        logging.error('Template "%s" not found', name)
        return None
    except Exception as e:
        logging.error('An error occurred while loading the template: %s', e)
        return None

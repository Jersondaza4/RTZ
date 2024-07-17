from django_components import component


@component.register('button_icon')
class ButtonIcon(component.Component):
    """A button component with an icon.

    Parameters:
    - text (str): The aria text for the button (required).
    - type_button (str): The type of button (default: 'button').
        Options: 'button', 'submit'.
    - color (str): The color of the button (default: 'primary').
        Options: 'primary', 'secondary', 'tertiary'.
    - size (str): The size of the button (default: 'md'). Options: 'xs', 'sm', 'md', 'lg'.
    - extras (dict): Extra options for the button.
        - class (str): Extra class for the button.

    Returns:
    - dict: A django template component.
    """

    template_name = 'button/icon/icon.html'

    def get_context_data(self, text, type_button='button', color='primary', size='md', **extras):
        return {
            'text': text,
            'type_button': type_button,
            'color': color,
            'size': size,
            'extras': extras,
        }

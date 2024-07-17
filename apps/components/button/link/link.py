from django_components import component


@component.register('button_link')
class ButtonLink(component.Component):
    """A component that renders a button as a link.

    Parameters:
        - text (str): The text to display on the button (required).
        - link (str): The URL to link to (required).
        - color (str): The color of the button:
            Can be 'primary', 'secondary', or 'tertiary' (default: 'primary').
        - size (str): The size of the button. Can be 'xs', 'sm', 'md', or 'lg' (default: 'md').
        - extras (dict): Any extra attributes to add to the button element (optional).
            - class (str): Extra CSS classes to add to the button element.
            - target (str): The target attribute for the link.
    """

    template_name = 'button/link/link.html'

    def get_context_data(self, text, link, color='primary', size='md', **extras):
        return {'text': text, 'link': link, 'color': color, 'size': size, 'extras': extras}

from django_components import component


@component.register('button_link_icon')
class ButtonIconLink(component.Component):
    """A component that renders a button with an icon and a link.

    Parameters:
        - text (str): The aria text for the button (required).
        - link (str): The link text for the button (required).
        - color (str): The color of the button:
            (default: 'primary', options: 'primary', 'secondary', 'tertiary').
        - size (str): The size of the button (default: 'md', options: 'xs', 'sm', 'md', 'lg').
        - extras (dict): Extra options for the button.
            - class (str): Extra class for the button.
            - target (str): Target attribute for the button.

    Returns:
        - dict: A django template component.
    """

    template_name = 'button/link_icon/link_icon.html'

    def get_context_data(self, text, link, color='primary', size='md', **extras):
        return {'text': text, 'link': link, 'color': color, 'size': size, 'extras': extras}

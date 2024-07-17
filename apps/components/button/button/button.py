from django_components import component


@component.register('button')
class Button(component.Component):
    """A class representing a button component.

    Parameters:
        text : str
            The text to display on the button. Required.
        type_button : str, optional
            The type of button. Can be 'button' or 'submit'. Default is 'button'.
        color : str, optional
            The color of the button.
            Can be 'primary', 'secondary', or 'tertiary'. Default is 'primary'.
        size : str, optional
            The size of the button. Can be 'xs', 'sm', 'md', or 'lg'. Default is 'md'.
        extras : dict, optional
            Extra options for the button. Can include 'class' for an extra class.

    Returns:
        - A django component template.
    """

    template_name = 'button/button/button.html'

    def get_context_data(self, text, type_button='button', onclick=None, color='primary', size='md', **extras):
        context = {
            'text': text,
            'type_button': type_button,
            'color': color,
            'size': size,
            'extras': extras,
        }
        if onclick is not None:
            context['onclick'] = onclick
        return context

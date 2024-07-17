from django_components import component


@component.register('content_two_columns')
class ButtonIcon(component.Component):
    """A component that displays content in two columns.

    Attributes:
        - template_name (str): The name of the template to use for rendering.
        - title_section (str): The main title of the page.
        - title_aside (str): The title of the aside content.

    Methods:
        - get_context_data(title_section, title_aside): Returns a dictionary containing the
        title_section and title_aside.
    """

    template_name = 'content_two_columns/content_two_columns.html'

    def get_context_data(self, title_section, title_aside):
        """Returns a dictionary containing the title_section and title_aside.

        Args:
        - title_section (str): The main title of the page.
        - title_aside (str): The title of the aside content.

        Returns:
        - A django template fragment.
        """
        return {'title_section': title_section, 'title_aside': title_aside}

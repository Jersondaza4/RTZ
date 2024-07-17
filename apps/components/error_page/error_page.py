from django_components import component


@component.register('error_page')
class ErrorPage(component.Component):
    """A component that renders an error page with a title and text.

    Parameters:
    - title (str): The title of the error page. Required.
    - text (str): The text to display on the error page. Required.
    """

    template_name = 'error_page/error_page.html'

    def get_context_data(self, title, text):
        """Returns a component template fragment."""
        return {
            'title': title,
            'text': text,
        }

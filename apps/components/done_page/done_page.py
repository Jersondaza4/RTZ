from django_components import component


@component.register('done_page')
class DonePage(component.Component):
    """A component that renders a page with a title, text, button, and status.

    Parameters:
    - title (str): The title of the page (required).
    - text (str): The text to display on the page (required).
    - button_text (str): The text to display on the button (required).
    - button_link (str): The link to follow when the button is clicked (required).
    - extras (dict): Extra options for the page.
        - status (str): The status of the page (success or error).

    Returns:
    - dict: A django template component fragment.
    """

    template_name = 'done_page/done_page.html'

    def get_context_data(self, title, text, button_text, button_link, **extras):
        status = 'success'

        if extras.get('status'):
            status = extras['status']

        return {
            'title': title,
            'text': text,
            'button_text': button_text,
            'button_link': button_link,
            'status': status,
        }

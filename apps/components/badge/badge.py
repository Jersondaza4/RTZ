from django_components import component


@component.register('badge')
class Badge(component.Component):
    """A component that represents a badge with text and a color variant.

    This component takes two parameters, a text string and a color variant string to
    show in the template

    Attributes:
        template_name (str): The name of the template to use for rendering the badge.
    """

    template_name = 'badge/badge.html'

    #
    def get_context_data(self, text, color_variant, **extras):
        """Returns a dictionary containing the text and color variant to be rendered.

        Args:
            text (str): The text to display in the badge.
            color_variant (str): The color variant to use for the badge.
            badge_id (str): The id to use for the badge.

        Returns:
            dict: A django template component.
        """
        badge_id = False
        if extras.get('badge_id'):
            badge_id = extras['badge_id']

        return {
            'text': text,
            'color_variant': color_variant,
            'badge_id': badge_id,
        }

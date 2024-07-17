from django_components import component


@component.register('profile_photo')
class PhotoText(component.Component):
    """A component that displays a profile photo with the user's initials and name."""

    template_name = 'profile_photo/profile_photo.html'

    def get_context_data(self, initials, url, name):
        """Returns a dictionary containing the context data for rendering the component.

        Args:
        - initials (str): The initials of the user's name, only 2 letters.
        - url (str): The URL of the user's profile photo.
        - name (str): The name of the user, first name and last name.

        Returns:
        - A component html fragment.
        """
        return {
            'initials': initials,
            'url': url,
            'name': name,
        }

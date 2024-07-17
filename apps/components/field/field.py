import re

from django import forms
from django_components import component


@component.register('field')
class Field(component.Component):
    """A component that generates HTML form fields based on the type of input.

    Templates for this component:
    - input.html = Inputs type: text, url, email, number, password, color, date, datetime-local,
      month, search, tel, time, week, range
    - select.html = Input type select
    - textarea.html = Input type textarea
    - radio.html = Input type radio button
    - checkbox.html = Input type checkbox (one checkbox)
    - checkbox_list.html = Input type checkbox (list of checkbox)

    Args:
        element (form element): Required. The form element to generate the field for.
        show_label (bool): Optional. Whether to show the field with a label. Defaults to True.
        show_help_text (bool): Optional. Whether to show the help text. Defaults to True.
        **extras: Optional. Extra options to customize the field.
            - label: Change the label text.
            - help_text: Change or add the help text.
            - type: Change the type of the input (e.g. text, number, email, etc.).
            - placeholder: Change or add a placeholder to the input.
            - class: Add a class to the input.
            - input_position: Show the input on the left or right (only for checkbox and radios).

    Returns:
        dict: A dictionary containing the context data for the field.
            - element: The form element.
            - show_label: Whether to show the label.
            - show_help_text: Whether to show the help text.
            - input_position: The position of the input (only for checkbox and radios).
    """

    def get_template_name(self, context):
        template_name = 'input'

        template_list = {
            'input': 'field/input.html',
            'select': 'field/select.html',
            'textarea': 'field/textarea.html',
            'radio': 'field/radio.html',
            'checkbox': 'field/checkbox.html',
            'checkbox_list': 'field/checkbox_list.html',
        }

        if hasattr(context['element'].field.widget, 'input_type'):
            input_type = context['element'].field.widget.input_type

            template_name = input_type

            if input_type == 'checkbox' and hasattr(context['element'].field, 'choices'):
                template_name = 'checkbox_list'

        elif isinstance(context['element'].field.widget, forms.Textarea):
            template_name = 'textarea'

        return template_list.get(template_name, template_list['input'])

    def get_context_data(self, element, show_label=True, show_help_text=True, **extras):
        """Get the context data for the field.

        Args:
            element (form element): Required. The form element to generate the field for.
            show_label (bool): Optional. Whether to show the field with a label. Defaults to True.
            show_help_text (bool): Optional. Whether to show the help text. Defaults to True.
            **extras: Optional. Extra options to customize the field.
                - label: Change the label text.
                - help_text: Change or add the help text.
                - type: Change the type of the input (e.g. text, number, email, etc.).
                - placeholder: Change or add a placeholder to the input.
                - class: Add a class to the input.
                - input_position: Show the input on the left/right (only for checkbox and radios).

        Returns:
            dict: A dictionary containing the context data for the field.
                - element: The form element.
                - show_label: Whether to show the label.
                - show_help_text: Whether to show the help text.
                - input_position: The position of the input (only for checkbox and radios).
        """
        if extras.get('label'):
            element.label = extras['label']

        if extras.get('help_text'):
            element.help_text = extras['help_text']

        if extras.get('type'):
            element.field.widget.input_type = extras['type']

        if extras.get('placeholder'):
            element.field.widget.attrs['placeholder'] = extras['placeholder']

        if extras.get('class'):
            class_list = re.findall(r'\S+', element.field.widget.attrs.get('class', ''))
            class_list += re.findall(r'\S+', extras['class'])
            element.field.widget.attrs['class'] = ' '.join(class_list)

        # Only for checkbox / radio button
        input_position = 'left'
        if extras.get('input_position'):
            input_position = extras['input_position']

        return {
            'element': element,
            'show_label': show_label,
            'show_help_text': show_help_text,
            'input_position': input_position,
        }

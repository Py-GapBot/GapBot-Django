import json


class FormField:
    def __init__(self, name=None, _type=None, label=None):
        self.name = name
        self._type = _type
        self.label = label


class FormTextField(FormField):
    def __init__(self, name=None, label=None):
        super().__init__(name=name, _type='text', label=label)
        self.field = dict(name=self.name, type=self._type, label=self.label)

    def get_field(self):
        return self.field

    def __repr__(self):
        return json.dumps(self.field)


class FormTextAreaField(FormField):
    def __init__(self, name=None, label=None):
        super().__init__(name=name, _type='textarea', label=label)
        self.field = dict(name=self.name, type=self._type, label=self.label)

    def get_field(self):
        return self.field

    def __repr__(self):
        return json.dumps(self.field)


class FormCheckboxField(FormField):
    def __init__(self, name=None, label=None):
        super().__init__(name=name, _type='checkbox', label=label)
        self.field = dict(name=self.name, type=self._type, label=self.label)

    def get_field(self):
        return self.field

    def __repr__(self):
        return json.dumps(self.field)


class FormSubmitButton(FormField):
    def __init__(self, label=None):
        super().__init__(_type='submit', label=label)
        self.field = dict(type=self._type, label=self.label)

    def get_field(self):
        return self.field

    def __repr__(self):
        return json.dumps(self.field)


class FormRadio(FormField):
    def __init__(self, name=None, label=None, options=None):
        super().__init__(name=name, _type='radio', label=label)
        if isinstance(options, dict):
            self.options = [{item: options[item]} for item in options]
        else:
            raise Exception('options must be of type Dict')
        self.field = dict(name=self.name,
                          type=self._type,
                          label=self.label,
                          options=self.options)

    def get_field(self):
        return self.field

    def __repr__(self):
        return json.dumps(self.field)


class FormSelect(FormField):
    def __init__(self, name=None, label=None, options=None):
        super().__init__(name=name, _type='select', label=label)
        if isinstance(options, dict):
            self.options = [{item: options[item]} for item in options]
        else:
            raise Exception('options must be of type Dict')
        self.field = dict(name=self.name,
                          type=self._type,
                          label=self.label,
                          options=self.options)

    def get_field(self):
        return self.field

    def __repr__(self):
        return json.dumps(self.field)

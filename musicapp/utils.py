header_menu = {
    'Upload track': 'upload-track',
}


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        context['header_menu'] = header_menu
        return context

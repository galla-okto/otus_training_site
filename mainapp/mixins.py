class PageNameMixin:
    page_name = ''

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = self.page_name
        return context

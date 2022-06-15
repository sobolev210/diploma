class DefaultCreateMixin:
    template_name = "core/base_form.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["title_str"] = self.model.genitive_case
        return ctx

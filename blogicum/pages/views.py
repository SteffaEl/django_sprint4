from django.shortcuts import render
from django.views.generic import TemplateView


class AboutView(TemplateView):
    template_name = 'pages/about.html'


class RulesView(TemplateView):
    template_name = 'pages/rules.html'


def csrf_failure(request, reason="",
                 template_name="pages/403csrf.html", exception=None):
    context = {
        'reason': reason,
        'exception': exception,
    }

    return render(request, template_name, context, status=403)


def page_not_found(request, exception):
    """Кастомная страница ошибки 404."""
    return render(request, 'pages/404.html', status=404)


def server_error(request):
    """Кастомная страница ошибки 500."""
    return render(request, 'pages/500.html', status=500)

from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView, TemplateView, UpdateView


class NewsHomeView(TemplateView):
    model = Articles
    template_name = 'newsapp/news.html'

    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex['news_data'] = Articles.objects.order_by('-date')
        return contex


class NewsDetailView(DetailView):
    model = Articles
    template_name = 'newsapp/news_detail.html'
    context_object_name = 'news_data'


class NewsUpdateView(UpdateView):
    model = Articles
    template_name = 'newsapp/update.html'
    context_object_name = 'news_data'
    form_class = ArticlesForm


def news_home(request):
    """ Example of using functions instead of class """
    news_data = Articles.objects.order_by('-date')
    return render(request, 'newsapp/news.html', {'news_data': news_data})


def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            object = form.save(commit=False)
            if request.user.is_authenticated:
                object.author = request.user
            else:
                object.author = None
            object.save()
            return redirect('news')
        else:
            error = 'Invalid form'

    form = ArticlesForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'newsapp/create.html', data)


def news_delete(request, id):
    article = Articles.objects.get(id=id)
    article.delete()
    return HttpResponseRedirect("/news")

from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView, ListView, DeleteView

from tags.form import TagModelForm
from tags.models import Tag


# Create your views here.


class TagCreateView(CreateView):
    model = Tag
    form_class = TagModelForm
    template_name = 'new_tag.html'
    context_object_name = 'tags'

    def get_success_url(self):
        next_url = self.request.GET.get("next")
        if next_url:
            return next_url
        return reverse("tags_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TagLisTView(ListView):
    model = Tag
    template_name = 'tags_list.html'
    context_object_name = 'tags'

    def get_queryset(self):
        return Tag.objects.filter(user=self.request.user)


class TagDeleteView(DeleteView):
    model = Tag
    template_name = 'delete_tag.html'
    context_object_name = 'tags'
    success_url = '/tags/'

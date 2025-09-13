from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from tasks.form import TaskModelForm
from tasks.models import Task


# Create your views here.


class TaskListView(ListView):
    model = Task
    template_name = 'tasks.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        tasks = Task.objects.filter(user=self.request.user)

        search = self.request.GET.get('search')
        if search:
            tasks = tasks.filter(Q(title__icontains=search) | Q(description__icontains=search))

        status = self.request.GET.get('status')
        if status:
            tasks = tasks.filter(status__icontains=status)

        priority = self.request.GET.get('priority')
        if priority:
            tasks = tasks.filter(priority__icontains=priority)

        return tasks


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskModelForm
    template_name = 'new_task.html'
    success_url = '/tasks/'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TaskDetailView(DetailView):
    model = Task
    template_name = 'detail_task.html'


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskModelForm
    template_name = 'update_task.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user  # passa o user para o form
        return kwargs

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('detail_task', kwargs={'pk': self.object.pk})


class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'delete_task.html'
    success_url = '/tasks/'

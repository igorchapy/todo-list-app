from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from .models import Task, Tag
from .forms import TaskForm, TagForm


class HomeView(ListView):
    model = Task
    template_name = 'tasks/home.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        return Task.objects.all().order_by('is_done', '-created_at')


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/form.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add Task'
        return context


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/form.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update Task'
        return context


class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy('home')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class ToggleTaskStatusView(View):
    def post(self, request, task_id):
        task = get_object_or_404(Task, id=task_id)
        task.is_done = not task.is_done
        task.save()
        return redirect('home')


class TagListView(ListView):
    model = Tag
    template_name = 'tasks/tag_list.html'
    context_object_name = 'tags'


class TagCreateView(CreateView):
    model = Tag
    form_class = TagForm
    template_name = 'tasks/form.html'
    success_url = reverse_lazy('tag_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add Tag'
        return context


class TagUpdateView(UpdateView):
    model = Tag
    form_class = TagForm
    template_name = 'tasks/form.html'
    success_url = reverse_lazy('tag_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update Tag'
        return context


class TagDeleteView(DeleteView):
    model = Tag
    success_url = reverse_lazy('tag_list')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

from django.shortcuts import render

from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)
from django.http import JsonResponse
from django.views.decorators.http import require_POST

from .models import Task
from .forms import TaskForm


def task_list(request):
    tasks = Task.objects.order_by("-created_at")
    form = TaskForm()

    return render(
        request,
        "tasks/task_list.html",
        {
            "tasks": tasks,
            "form": form,
        }
    )


@require_POST
def add_task(request):
    form = TaskForm(request.POST)

    if form.is_valid():
        form.save()

    return redirect("task_list")


@require_POST
def toggle_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    task.is_completed = not task.is_completed
    task.save()

    return redirect("task_list")


@require_POST
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    task.delete()

    return redirect("task_list")


def health_check(request):
    return JsonResponse({"status": "ok"})

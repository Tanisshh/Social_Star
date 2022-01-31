from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views import generic
from django.urls import reverse
from group.models import Group, GroupMember


class CreatePost(LoginRequiredMixin, generic.CreateView):
    fields = ('name', 'description')
    model = Group

class SingleGroup(generic.DetailView):
    model = Group

class ListGroup(generic.ListView):
    model= Group

from django.utils import timezone
from django import forms
from todolist.models import Task, Tag


class TaskSearchForm(forms.Form):
    content = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by task..."})
    )


class TaskForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
    deadline = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={"type": "datetime-local"}),
        required=False
    )

    class Meta:
        model = Task
        fields = "__all__"

    def clean_deadline(self):
        deadline = self.cleaned_data.get("deadline", "")
        if deadline:
            now = timezone.localtime(timezone.now())
            if deadline <= now + timezone.timedelta(hours=1):
                raise forms.ValidationError(
                    f"The deadline should be in an hour from current time"
                    f"({now.strftime('%d.%m.%Y %H:%M')}) or more.")


class TagForm(forms.ModelForm):

    class Meta:
        model = Tag
        fields = "__all__"


class TagSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by name..."})
    )
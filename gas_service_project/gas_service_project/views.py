from django.shortcuts import redirect


def home(request):
    return redirect("/admin/login/?next=/admin/")

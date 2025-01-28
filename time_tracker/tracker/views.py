import json
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.db.models import Q
from .models import TimeLog
from .forms import TimeLogForm
from datetime import datetime, timedelta
from django.core.paginator import Paginator


@login_required
def index(request):
    return render(request, 'tracker/index.html')


@login_required
def time_logs(request):
    query = request.GET.get('q', '')
    time_logs = TimeLog.objects.filter(user=request.user)

    if query:
        time_logs = time_logs.filter(Q(description__icontains=query))

    paginator = Paginator(time_logs, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'tracker/time_logs.html', {
        'page_obj': page_obj,
        'query': query,
    })


@login_required
def manual_entry(request):
    if request.method == 'POST':
        form = TimeLogForm(request.POST)
        if form.is_valid():
            time_log = form.save(commit=False)
            time_log.user = request.user
            time_log.save()
            return redirect('time_logs')
    else:
        form = TimeLogForm()

    return render(request, 'tracker/manual_entry.html', {'form': form})


@login_required
def save_time_log(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)  # Chargez les données JSON
            print("Received data:", data)  # Ajoutez cette ligne pour le débogage

            start_time = data.get('start_time').replace('Z', '')  # Retirez le suffixe Z
            end_time = data.get('end_time').replace('Z', '')  # Retirez le suffixe Z
            description = data.get('description')

            # Vérifiez si les valeurs sont présentes
            if not start_time or not end_time or not description:
                return JsonResponse({'status': 'error', 'message': 'Missing data'}, status=400)

            # Convertir les chaînes en objets datetime
            start_time = datetime.fromisoformat(start_time)
            end_time = datetime.fromisoformat(end_time)

            TimeLog.objects.create(
                user=request.user,
                start_time=start_time,
                end_time=end_time,
                description=description,
                duration=end_time - start_time
            )

            return JsonResponse({'status': 'success'})
        except Exception as e:
            print("Error:", str(e))  # Ajoutez cette ligne pour le débogage
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
    return JsonResponse({'status': 'error'}, status=400)
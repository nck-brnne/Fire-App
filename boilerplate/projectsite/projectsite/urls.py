from django.contrib import admin
from django.urls import path

from fire.views import HomePageView, ChartView, PieCountbySeverity, LineCountbyMonth, MultilineIncidentTop3Country, multipleBarbySeverity, map_station, fire_incident_map
from fire.views import firestationListView, firestationCreateView, firestationUpdateView, firestationDeleteView
from fire.views import IncidentListView, IncidentCreateView, IncidentUpdateView, IncidentDeleteView


urlpatterns = [
    
    path("admin/", admin.site.urls),
    path('', HomePageView.as_view(), name='home'),
    path('dashboard_chart', ChartView.as_view(), name='dashboard-chart'),
    path('chart/', PieCountbySeverity, name='chart'),
    path('lineChart/', LineCountbyMonth, name='chart'),
    path('multilineChart/', MultilineIncidentTop3Country, name='chart'),
    path('multiBarChart/', multipleBarbySeverity, name='chart'),
    path('stations/', map_station, name='map-station'),  
    path('fire_incident_map/', fire_incident_map, name='fire-incidents-map'),
    
    path('firestation_list/', firestationListView.as_view(), name='station-list'),
    path('firestation_list/add', firestationCreateView.as_view(), name='firestation-add'),
    path('firestation_list/<pk>', firestationUpdateView.as_view(), name='firestation-update'),
    path('firestation_list/<pk>/delete/', firestationDeleteView.as_view(), name='firestation-delete'),

    path('Incident_list/',  IncidentListView.as_view(), name='incident-list'),
    path('Incident_list/add', IncidentCreateView.as_view(), name='incident-add'),
    path('Incident_list/<pk>', IncidentUpdateView.as_view(), name='incident-update'),
    path('Incident_list/<pk>/delete/', IncidentDeleteView.as_view(), name='incident-delete'),


]

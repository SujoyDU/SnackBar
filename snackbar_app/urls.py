from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from rest_framework_jwt import views as jwt_views

from . import views

router = DefaultRouter()
# router.register('profile', views.UserProfileViewSet)
# router.register('login', views.LoginViewSet, base_name='login')
# router.register('project', views.ProjectViewSet, base_name='projects')
# router.register('db_c', views.DatabCViewSet)

# router.register('workboard', views.WorkboardViewSet)
# router.register('dashboard', views.DashboardViewSet)
# # router.register('dashboard_workboard/(?P<dashboard>.+)', views.DashboardWorkboardViewSet)
# router.register('dashboard_workboard', views.DashboardWorkboardViewSet)
# router.register('email_attachment', views.EmailAttachmentViewSet)
# router.register('analysis_type', views.AnalysisTypeViewSet)
# router.register('selected_variables', views.SelectedVariablesViewSet)
# router.register('chart_style', views.ChartStyleViewSet)

urlpatterns = [
    url(r'', include(router.urls)),
    url(r'^auth/', include('djoser.urls')),
    url(r'^auth/login/', jwt_views.obtain_jwt_token, name='login'),
    url(r'^auth/logout/', jwt_views.obtain_jwt_token, name='logout'),

]

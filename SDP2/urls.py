"""SDP2 URL Configuration"""
from django.contrib import admin
from django.urls import path, include
from Dash.views import home_page_view, camera_view, PrintTrackDataDetail, DashPanelDataDetail, dash_panel_view
from UserReg.views import UserFormView, UserLogin, logout_user , user_page
from Print.views import NewPrintView, print_file_view, print_details_view, print_create_view, print_update_view, print_delete_view

from django.contrib import admin

admin.site.site_header = 'Administration Panel'         
admin.site.index_title = 'Features area'                
admin.site.site_title = 'Administration Panel'          

urlpatterns = [
    path('admin/',         admin.site.urls),
    path('',               home_page_view,          name='home'           ),
    path('register/',      UserFormView.as_view(),  name='register'       ),
    path('login/',         UserLogin.as_view(),     name='login'          ),
    path('logout/',        logout_user,             name='logout'         ),
    path('startNewPrint/', NewPrintView.as_view(),  name='start-new-print'),
    path('camera/',        camera_view,             name='camera'         ),
    #Create New Print api
    path('api/print-files/',                 print_file_view,    name='api-print-files'  ),
    path('api/print-files/details/<str:pk>', print_details_view, name='api-print-details'),
    path('api/print-files/create',           print_create_view,  name='api-print-create' ),
    path('api/print-files/<str:pk>/update',  print_update_view,  name='api-print-update' ),
    path('api/print-files/<str:pk>/delete',  print_delete_view,  name='api-print-delete' ),
    #Dash panel api
    path('api/print-data-track/<str:pk>',     PrintTrackDataDetail.as_view() , name='api-print-track-data'),
    path('api/print-dash-panel/<str:pk>',     DashPanelDataDetail.as_view()  , name='api-dash-pane-data'),
    path('api/print-dash-panel/'        ,     dash_panel_view                , name='api-dash-pane-list'),
]

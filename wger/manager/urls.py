from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy

from wger.manager.views.workout import WorkoutEditView
from wger.manager.views.workout import WorkoutDeleteView
from wger.manager.views.log import WorkoutLogDetailView
from wger.manager.views.log import WorkoutLogUpdateView
from wger.manager.views.day import DayEditView
from wger.manager.views.day import DayCreateView

from wger.workout_manager.constants import USER_TAB


urlpatterns = patterns('wger.manager.views',

    # The landing page
    url(r'^$', 'misc.index', name='index'),

    # The dashboard
    url(r'^dashboard$', 'misc.dashboard', name='dashboard'),


    # User
    url(r'^logout$', 'user.logout', name='logout'),
    url(r'^user/registration$', 'user.registration', name='registration'),
    url(r'^user/demo-account$',
        'user.create_demo_user',
        name='demo-account'),

    url(r'^user/preferences$', 'user.preferences', name='preferences'),

    # Workout
    url(r'^workout/overview$', 'workout.overview'),
    url(r'^workout/add$', 'workout.add'),
    url(r'^workout/(?P<pk>\d+)/copy/$',
        'workout.copy_workout',
        name='workout-copy'),

    url(r'^workout/(?P<pk>\d+)/edit/$',
        login_required(WorkoutEditView.as_view()),
        name='workout-edit'),
    url(r'^workout/(?P<pk>\d+)/delete/$',
        login_required(WorkoutDeleteView.as_view()),
        name='workout-delete'),
    url(r'^workout/(?P<id>\d+)/view/$',
        'workout.view_workout',
        name='workout-view'),
    url(r'^workout/(?P<pk>\d+)/log/$',
        login_required(WorkoutLogDetailView.as_view()),
        name='workout-log'),
    url(r'^workout/log/edit-entry/(?P<pk>\d+)$',
        login_required(WorkoutLogUpdateView.as_view()),
        name='workout-log-edit'),


    # Days
    url(r'^workout/day/(?P<pk>\d+)/edit/$',
        login_required(DayEditView.as_view()),
        name='day-edit'),
    url(r'^workout/(?P<workout_pk>\d+)/day/add/$',
        login_required(DayCreateView.as_view()),
        name='day-add'),
    url(r'^workout/(?P<id>\d+)/delete/day/(?P<day_id>\d+)$', 'day.delete_day'),
    url(r'^workout/day/view/(?P<id>\d+)$', 'day.view_day'),
    url(r'^workout/day/(?P<pk>\d+)/log/add/$',
        'log.workout_log_add',
        name='day-log'),

    # Sets and Settings
    url(r'^workout/(?P<id>\d+)/day/(?P<day_id>\d+)/edit/set/(?P<set_id>\w*)$', 'set.edit_set'),
    url(r'^workout/(?P<id>\d+)/day/(?P<day_id>\d+)/delete/set/(?P<set_id>\d+)$', 'set.delete_set'),
    url(r'^workout/(?P<id>\d+)/set/(?P<set_id>\d+)/exercise/(?P<exercise_id>\d+)/edit/setting/(?P<setting_id>\w*)$', 'setting.edit_setting'),
    url(r'^workout/(?P<id>\d+)/set/(?P<set_id>\d+)/exercise/(?P<exercise_id>\d+)/delete/setting$', 'setting.delete_setting'),

    # AJAX
    url(r'^workout/api/edit-set$', 'set.api_edit_set'),
    url(r'^workout/api/edit-settting$', 'setting.api_edit_setting'),
    url(r'^workout/api/user-preferences$', 'user.api_user_preferences'),
)

# PDF stuff is in a different file
urlpatterns = urlpatterns + patterns('wger.manager.pdf',
     url(r'^workout/(?P<id>\d+)/pdf/$', 'workout_log'))

# Password reset is implemented by Django, no need to cook our own soup here
# (besides the templates)
urlpatterns = urlpatterns + patterns('',
    url(r'^login/$',
        'django.contrib.auth.views.login',
        {'template_name': 'user/login.html',
         'extra_context': {'active_tab': USER_TAB}},
        name='login'),

    url(r'^user/password/change$',
        'django.contrib.auth.views.password_change',
        {'template_name': 'user/change_password.html',
          'post_change_redirect': reverse_lazy('index'),
          'extra_context': {'active_tab': USER_TAB}},
        name='change-password'),

    url(r'^user/password/reset/$',
        'django.contrib.auth.views.password_reset',
        {'template_name': 'user/password_reset_form.html'},
        name='password_reset'),

    url(r'^user/password/reset/done/$',
        'django.contrib.auth.views.password_reset_done',
        {'template_name': 'user/password_reset_done.html'},
        name='password_reset_done'),

    url(r'^user/password/reset/check/(?P<uidb36>[0-9A-Za-z]{1,13})-(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        'django.contrib.auth.views.password_reset_confirm',
        {'template_name': 'user/password_reset_confirm.html'},
        name='password_reset_confirm'),

    url(r'^user/password/reset/complete/$',
        'django.contrib.auth.views.password_reset_complete',
        {'template_name': 'user/password_reset_complete.html'},
        name='password_reset_complete'),
    )
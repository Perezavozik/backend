from django.urls import include, path

urlpatterns = [
    path('projects/', include('detail_pages_components.our_projects.urls')),
    path('events/', include('detail_pages_components.events.urls')),
    path('awards/', include('detail_pages_components.awards.urls')),
    path('society/', include('detail_pages_components.society.urls')),
    path('history/', include('detail_pages_components.history.urls')),
    path('culture/', include('detail_pages_components.culture.urls')),
    path('language/', include('detail_pages_components.language.urls')),
    path('news-on-main/', include('detail_pages_components.news_on_main.urls')),
    path('candidate_awards/', include('detail_pages_components.awards_candidate.urls')),
    path('documents/', include('documents.urls')),
    path('congresses/', include('content_list.congresses.urls')),
    path('contacts/', include('contacts.urls')),
    path('reports/', include('reports.urls')),
    path('about/', include('about_us.urls')),
    path('media-library/', include('media_library.urls')),
    path('feedback-form/', include('feedback_form.urls')),
    path('telegram-feed/', include('telegram_feed.urls')),
    path('search/', include('search.urls'))
]

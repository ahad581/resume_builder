# Python
from django.urls import path
from .views import (
    ResumeListView, ResumeDetailView,
    EducationAddView, WorkExperienceAddView, TechnicalSkillAddView, ProjectAddView,
    CertificationAddView, AwardAddView, LanguageAddView, ResumeSectionAddView,
    ResumeCreateView, ResumeUpdateView, ResumeDeleteView
)

urlpatterns = [
    path('resumes/', ResumeListView.as_view(), name='resume_list'),
    path('resumes/add/', ResumeCreateView.as_view(), name='resume_create'),
    path('resumes/<int:pk>/', ResumeDetailView.as_view(), name='resume_detail'),
    path('resumes/<int:pk>/edit/', ResumeUpdateView.as_view(), name='resume_update'),
    path('resumes/<int:pk>/delete/', ResumeDeleteView.as_view(), name='resume_delete'),
    path('resumes/<int:pk>/add-education/', EducationAddView.as_view(), name='add_education'),
    path('resumes/<int:pk>/add-work-experience/', WorkExperienceAddView.as_view(), name='add_work_experience'),
    path('resumes/<int:pk>/add-technical-skill/', TechnicalSkillAddView.as_view(), name='add_technical_skill'),
    path('resumes/<int:pk>/add-project/', ProjectAddView.as_view(), name='add_project'),
    path('resumes/<int:pk>/add-certification/', CertificationAddView.as_view(), name='add_certification'),
    path('resumes/<int:pk>/add-award/', AwardAddView.as_view(), name='add_award'),
    path('resumes/<int:pk>/add-language/', LanguageAddView.as_view(), name='add_language'),
    path('resumes/<int:pk>/add-section/', ResumeSectionAddView.as_view(), name='add_resume_section'),
]
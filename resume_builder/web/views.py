# Python
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from resume_builder.models import WorkExperience, Education, ResumeTemplate, Resume, ResumeSection, TechnicalSkill, Technology, Project, Certification, Award, Language
from resume_builder.forms import WorkExperienceForm, EducationForm, ResumeTemplateForm, ResumeForm, ResumeSectionForm, TechnicalSkillForm, TechnologyForm, ProjectForm, CertificationForm, AwardForm, LanguageForm
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from resume_builder.models import Resume, Education, WorkExperience, TechnicalSkill, Project, Certification, Award, Language, ResumeSection
from resume_builder.forms import ResumeForm, EducationForm, WorkExperienceForm, TechnicalSkillForm, ProjectForm, CertificationForm, AwardForm, LanguageForm

class WorkExperienceListView(LoginRequiredMixin, ListView):
    model = WorkExperience
    template_name = 'resume_builder/work_experience/work_experience_list.html'
    context_object_name = 'experiences'

    def get_queryset(self):
        return WorkExperience.objects.filter(resume__user=self.request.user)

class WorkExperienceCreateView(LoginRequiredMixin, CreateView):
    model = WorkExperience
    form_class = WorkExperienceForm
    template_name = 'resume_builder/work_experience/work_experience_form.html'
    success_url = reverse_lazy('work_experience_list')

    def form_valid(self, form):
        # Ensure the resume belongs to the user
        resume = form.cleaned_data['resume']
        if resume.user != self.request.user:
            form.add_error('resume', 'You do not own this resume.')
            return self.form_invalid(form)
        return super().form_valid(form)

class WorkExperienceUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = WorkExperience
    form_class = WorkExperienceForm
    template_name = 'resume_builder/work_experience/work_experience_form.html'
    success_url = reverse_lazy('work_experience_list')

    def test_func(self):
        return self.get_object().resume.user == self.request.user

class WorkExperienceDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = WorkExperience
    template_name = 'resume_builder/work_experience/work_experience_confirm_delete.html'
    success_url = reverse_lazy('work_experience_list')

    def test_func(self):
        return self.get_object().resume.user == self.request.user

class WorkExperienceDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = WorkExperience
    template_name = 'resume_builder/work_experience/work_experience_detail.html'
    context_object_name = 'experience'

    def test_func(self):
        return self.get_object().resume.user == self.request.user

class EducationListView(LoginRequiredMixin, ListView):
    model = Education
    template_name = 'resume_builder/education/education_list.html'
    context_object_name = 'educations'

    def get_queryset(self):
        return Education.objects.filter(resume__user=self.request.user)

class EducationCreateView(LoginRequiredMixin, CreateView):
    model = Education
    form_class = EducationForm
    template_name = 'resume_builder/education/education_form.html'

    def form_valid(self, form):
        resume = form.cleaned_data['resume']
        if resume.user != self.request.user:
            form.add_error('resume', 'You do not own this resume.')
            return self.form_invalid(form)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('resume_detail', args=[self.object.resume.pk])

class EducationUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Education
    form_class = EducationForm
    template_name = 'resume_builder/education/education_form.html'

    def test_func(self):
        return self.get_object().resume.user == self.request.user

    def get_success_url(self):
        return reverse('resume_detail', args=[self.object.resume.pk])

class EducationDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Education
    template_name = 'resume_builder/education/education_confirm_delete.html'

    def test_func(self):
        return self.get_object().resume.user == self.request.user

    def get_success_url(self):
        return reverse('resume_detail', args=[self.object.resume.pk])

class EducationDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Education
    template_name = 'resume_builder/education/education_detail.html'
    context_object_name = 'education'

    def test_func(self):
        return self.get_object().resume.user == self.request.user

# ResumeTemplate Views
class ResumeTemplateListView(LoginRequiredMixin, ListView):
    model = ResumeTemplate
    template_name = 'resume_builder/resumetemplate/resumetemplate_list.html'
    context_object_name = 'templates'

class ResumeTemplateCreateView(LoginRequiredMixin, CreateView):
    model = ResumeTemplate
    form_class = ResumeTemplateForm
    template_name = 'resume_builder/resumetemplate/resumetemplate_form.html'
    success_url = reverse_lazy('resumetemplate_list')

class ResumeTemplateUpdateView(LoginRequiredMixin, UpdateView):
    model = ResumeTemplate
    form_class = ResumeTemplateForm
    template_name = 'resume_builder/resumetemplate/resumetemplate_form.html'
    success_url = reverse_lazy('resumetemplate_list')

class ResumeTemplateDeleteView(LoginRequiredMixin, DeleteView):
    model = ResumeTemplate
    template_name = 'resume_builder/resumetemplate/resumetemplate_confirm_delete.html'
    success_url = reverse_lazy('resumetemplate_list')

class ResumeTemplateDetailView(LoginRequiredMixin, DetailView):
    model = ResumeTemplate
    template_name = 'resume_builder/resumetemplate/resumetemplate_detail.html'
    context_object_name = 'template'

# Resume Views
class ResumeListView(LoginRequiredMixin, ListView):
    model = Resume
    template_name = 'resume_builder/resume/resume_list.html'
    context_object_name = 'resumes'

    def get_queryset(self):
        return Resume.objects.filter(user=self.request.user)

class ResumeCreateView(LoginRequiredMixin, CreateView):
    model = Resume
    form_class = ResumeForm
    template_name = 'resume_builder/resume/resume_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('resume_list')

class ResumeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Resume
    form_class = ResumeForm
    template_name = 'resume_builder/resume/resume_form.html'

    def test_func(self):
        return self.get_object().user == self.request.user

    def get_success_url(self):
        return reverse('resume_detail', args=[self.object.pk])

class ResumeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Resume
    template_name = 'resume_builder/resume/resume_confirm_delete.html'
    success_url = reverse_lazy('resume_list')

    def test_func(self):
        return self.get_object().user == self.request.user

class ResumeDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Resume
    template_name = 'resume_builder/resume/resume_detail.html'
    context_object_name = 'resume'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        resume = self.object
        context['educations'] = resume.educations.all()
        context['work_experiences'] = resume.work_experiences.all()
        context['technical_skills'] = resume.technical_skills.all()
        context['projects'] = resume.projects.all()
        context['certifications'] = resume.certifications.all()
        context['awards'] = resume.awards.all()
        context['languages'] = resume.languages.all()
        context['sections'] = resume.sections.all()
        return context

    def test_func(self):
        return self.get_object().user == self.request.user

# ResumeSection Views
class ResumeSectionListView(LoginRequiredMixin, ListView):
    model = ResumeSection
    template_name = 'resume_builder/resumesection/resumesection_list.html'
    context_object_name = 'sections'

    def get_queryset(self):
        return ResumeSection.objects.filter(resume__user=self.request.user)

class ResumeSectionCreateView(LoginRequiredMixin, CreateView):
    model = ResumeSection
    form_class = ResumeSectionForm
    template_name = 'resume_builder/resumesection/resumesection_form.html'
    success_url = reverse_lazy('resumesection_list')

class ResumeSectionUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = ResumeSection
    form_class = ResumeSectionForm
    template_name = 'resume_builder/resumesection/resumesection_form.html'
    success_url = reverse_lazy('resumesection_list')

    def test_func(self):
        return self.get_object().resume.user == self.request.user

class ResumeSectionDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = ResumeSection
    template_name = 'resume_builder/resumesection/resumesection_confirm_delete.html'
    success_url = reverse_lazy('resumesection_list')

    def test_func(self):
        return self.get_object().resume.user == self.request.user

class ResumeSectionDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = ResumeSection
    template_name = 'resume_builder/resumesection/resumesection_detail.html'
    context_object_name = 'section'

    def test_func(self):
        return self.get_object().resume.user == self.request.user

# TechnicalSkill Views
class TechnicalSkillListView(LoginRequiredMixin, ListView):
    model = TechnicalSkill
    template_name = 'resume_builder/technicalskill/technicalskill_list.html'
    context_object_name = 'skills'

    def get_queryset(self):
        return TechnicalSkill.objects.filter(resume__user=self.request.user)

class TechnicalSkillCreateView(LoginRequiredMixin, CreateView):
    model = TechnicalSkill
    form_class = TechnicalSkillForm
    template_name = 'resume_builder/technicalskill/technicalskill_form.html'
    success_url = reverse_lazy('technicalskill_list')

class TechnicalSkillUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = TechnicalSkill
    form_class = TechnicalSkillForm
    template_name = 'resume_builder/technicalskill/technicalskill_form.html'
    success_url = reverse_lazy('technicalskill_list')

    def test_func(self):
        return self.get_object().resume.user == self.request.user

class TechnicalSkillDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = TechnicalSkill
    template_name = 'resume_builder/technicalskill/technicalskill_confirm_delete.html'
    success_url = reverse_lazy('technicalskill_list')

    def test_func(self):
        return self.get_object().resume.user == self.request.user

class TechnicalSkillDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = TechnicalSkill
    template_name = 'resume_builder/technicalskill/technicalskill_detail.html'
    context_object_name = 'skill'

    def test_func(self):
        return self.get_object().resume.user == self.request.user

# Technology Views
class TechnologyListView(LoginRequiredMixin, ListView):
    model = Technology
    template_name = 'resume_builder/technology/technology_list.html'
    context_object_name = 'technologies'

class TechnologyCreateView(LoginRequiredMixin, CreateView):
    model = Technology
    form_class = TechnologyForm
    template_name = 'resume_builder/technology/technology_form.html'
    success_url = reverse_lazy('technology_list')

class TechnologyUpdateView(LoginRequiredMixin, UpdateView):
    model = Technology
    form_class = TechnologyForm
    template_name = 'resume_builder/technology/technology_form.html'
    success_url = reverse_lazy('technology_list')

class TechnologyDeleteView(LoginRequiredMixin, DeleteView):
    model = Technology
    template_name = 'resume_builder/technology/technology_confirm_delete.html'
    success_url = reverse_lazy('technology_list')

class TechnologyDetailView(LoginRequiredMixin, DetailView):
    model = Technology
    template_name = 'resume_builder/technology/technology_detail.html'
    context_object_name = 'technology'

# Project Views
class ProjectListView(LoginRequiredMixin, ListView):
    model = Project
    template_name = 'resume_builder/project/project_list.html'
    context_object_name = 'projects'

    def get_queryset(self):
        return Project.objects.filter(resume__user=self.request.user)

class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'resume_builder/project/project_form.html'
    success_url = reverse_lazy('project_list')

class ProjectUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = 'resume_builder/project/project_form.html'
    success_url = reverse_lazy('project_list')

    def test_func(self):
        return self.get_object().resume.user == self.request.user

class ProjectDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Project
    template_name = 'resume_builder/project/project_confirm_delete.html'
    success_url = reverse_lazy('project_list')

    def test_func(self):
        return self.get_object().resume.user == self.request.user

class ProjectDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Project
    template_name = 'resume_builder/project/project_detail.html'
    context_object_name = 'project'

    def test_func(self):
        return self.get_object().resume.user == self.request.user

# Certification Views
class CertificationListView(LoginRequiredMixin, ListView):
    model = Certification
    template_name = 'resume_builder/certification/certification_list.html'
    context_object_name = 'certifications'

    def get_queryset(self):
        return Certification.objects.filter(resume__user=self.request.user)

class CertificationCreateView(LoginRequiredMixin, CreateView):
    model = Certification
    form_class = CertificationForm
    template_name = 'resume_builder/certification/certification_form.html'
    success_url = reverse_lazy('certification_list')

class CertificationUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Certification
    form_class = CertificationForm
    template_name = 'resume_builder/certification/certification_form.html'
    success_url = reverse_lazy('certification_list')

    def test_func(self):
        return self.get_object().resume.user == self.request.user

class CertificationDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Certification
    template_name = 'resume_builder/certification/certification_confirm_delete.html'
    success_url = reverse_lazy('certification_list')

    def test_func(self):
        return self.get_object().resume.user == self.request.user

class CertificationDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Certification
    template_name = 'resume_builder/certification/certification_detail.html'
    context_object_name = 'certification'

    def test_func(self):
        return self.get_object().resume.user == self.request.user

# Award Views
class AwardListView(LoginRequiredMixin, ListView):
    model = Award
    template_name = 'resume_builder/award/award_list.html'
    context_object_name = 'awards'

    def get_queryset(self):
        return Award.objects.filter(resume__user=self.request.user)

class AwardCreateView(LoginRequiredMixin, CreateView):
    model = Award
    form_class = AwardForm
    template_name = 'resume_builder/award/award_form.html'
    success_url = reverse_lazy('award_list')

class AwardUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Award
    form_class = AwardForm
    template_name = 'resume_builder/award/award_form.html'
    success_url = reverse_lazy('award_list')

    def test_func(self):
        return self.get_object().resume.user == self.request.user

class AwardDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Award
    template_name = 'resume_builder/award/award_confirm_delete.html'
    success_url = reverse_lazy('award_list')

    def test_func(self):
        return self.get_object().resume.user == self.request.user

class AwardDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Award
    template_name = 'resume_builder/award/award_detail.html'
    context_object_name = 'award'

    def test_func(self):
        return self.get_object().resume.user == self.request.user

# Language Views
class LanguageListView(LoginRequiredMixin, ListView):
    model = Language
    template_name = 'resume_builder/language/language_list.html'
    context_object_name = 'languages'

    def get_queryset(self):
        return Language.objects.filter(resume__user=self.request.user)

class LanguageCreateView(LoginRequiredMixin, CreateView):
    model = Language
    form_class = LanguageForm
    template_name = 'resume_builder/language/language_form.html'
    success_url = reverse_lazy('language_list')

class LanguageUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Language
    form_class = LanguageForm
    template_name = 'resume_builder/language/language_form.html'
    success_url = reverse_lazy('language_list')

    def test_func(self):
        return self.get_object().resume.user == self.request.user

class LanguageDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Language
    template_name = 'resume_builder/language/language_confirm_delete.html'
    success_url = reverse_lazy('language_list')

    def test_func(self):
        return self.get_object().resume.user == self.request.user

class LanguageDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Language
    template_name = 'resume_builder/language/language_detail.html'
    context_object_name = 'language'

    def test_func(self):
        return self.get_object().resume.user == self.request.user

class WorkExperienceAddView(LoginRequiredMixin, CreateView):
    model = WorkExperience
    form_class = WorkExperienceForm
    template_name = 'resume_builder/work_experience/work_experience_form.html'

    def dispatch(self, request, *args, **kwargs):
        self.resume = get_object_or_404(Resume, pk=kwargs['pk'], user=request.user)
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.resume = self.resume
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('resume_detail', args=[self.resume.pk])

class TechnicalSkillAddView(LoginRequiredMixin, CreateView):
    model = TechnicalSkill
    form_class = TechnicalSkillForm
    template_name = 'resume_builder/technical_skill/technical_skill_form.html'

    def dispatch(self, request, *args, **kwargs):
        self.resume = get_object_or_404(Resume, pk=kwargs['pk'], user=request.user)
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.resume = self.resume
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('resume_detail', args=[self.resume.pk])

class ProjectAddView(LoginRequiredMixin, CreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'resume_builder/project/project_form.html'

    def dispatch(self, request, *args, **kwargs):
        self.resume = get_object_or_404(Resume, pk=kwargs['pk'], user=request.user)
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.resume = self.resume
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('resume_detail', args=[self.resume.pk])

class CertificationAddView(LoginRequiredMixin, CreateView):
    model = Certification
    form_class = CertificationForm
    template_name = 'resume_builder/certification/certification_form.html'

    def dispatch(self, request, *args, **kwargs):
        self.resume = get_object_or_404(Resume, pk=kwargs['pk'], user=request.user)
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.resume = self.resume
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('resume_detail', args=[self.resume.pk])

class AwardAddView(LoginRequiredMixin, CreateView):
    model = Award
    form_class = AwardForm
    template_name = 'resume_builder/award/award_form.html'

    def dispatch(self, request, *args, **kwargs):
        self.resume = get_object_or_404(Resume, pk=kwargs['pk'], user=request.user)
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.resume = self.resume
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('resume_detail', args=[self.resume.pk])

class LanguageAddView(LoginRequiredMixin, CreateView):
    model = Language
    form_class = LanguageForm
    template_name = 'resume_builder/language/language_form.html'

    def dispatch(self, request, *args, **kwargs):
        self.resume = get_object_or_404(Resume, pk=kwargs['pk'], user=request.user)
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.resume = self.resume
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('resume_detail', args=[self.resume.pk])

class ResumeSectionAddView(LoginRequiredMixin, CreateView):
    model = ResumeSection
    form_class = ResumeSectionForm
    template_name = 'resume_builder/resume_section/resume_section_form.html'

    def dispatch(self, request, *args, **kwargs):
        self.resume = get_object_or_404(Resume, pk=kwargs['pk'], user=request.user)
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.resume = self.resume
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('resume_detail', args=[self.resume.pk])

class EducationAddView(LoginRequiredMixin, CreateView):
    model = Education
    form_class = EducationForm
    template_name = 'resume_builder/education/education_form.html'

    def dispatch(self, request, *args, **kwargs):
        self.resume = get_object_or_404(Resume, pk=kwargs['pk'], user=request.user)
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['resume'] = self.resume
        return context

    def form_valid(self, form):
        form.instance.resume = self.resume
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('resume_detail', args=[self.resume.pk])
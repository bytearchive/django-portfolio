from django.views.generic.list_detail import object_detail, object_list
from models import Project, Skill, Category

def project_detail(request, slug, template_name='portfolio/project_detail.html', extra_context={}):
    return object_detail(
        request,
        template_name = template_name,
        extra_context = extra_context,
        slug = slug,
        slug_field = 'slug',
        queryset = Project.objects.all(),
        )

def category_detail(request, slug, template_name='portfolio/category_detail.html', extra_context={}):
    return object_detail(
        request,
        template_name = template_name,
        extra_context = extra_context,
        slug = slug,
        slug_field = 'slug',
        queryset = Category.objects.all(),
        )

def category_list(request, template_name='portfolio/category_list.html', extra_context={}):
    return object_list(
        request,
        template_name = template_name,
        extra_context = extra_context,
        queryset = Category.objects.active(),
        )

def skill_detail(request, slug, template_name='portfolio/skill_detail.html', extra_context={}):
    return object_detail(
        request,
        template_name = template_name,
        extra_context = extra_context,
        slug = slug,
        slug_field = 'slug',
        queryset = Skill.objects.all(),
        )


def skill_list(request, template_name='portfolio/skill_list.html', extra_context={}):
    return object_list(
        request,
        template_name = template_name,
        extra_context = extra_context,
        queryset = Skill.objects.active(),
        )

from django.shortcuts import render
from .models import Profile, Skills, Education, Projects, Experience, Extra_Curri, Language


# Create your views here.
def index(request):
    profile = Profile.objects.all()
    skill = Skills.objects.all()
    edu = Education.objects.all()
    proj = Projects.objects.all()
    exp = Experience.objects.all()
    extra = Extra_Curri.objects.all()
    lang = Language.objects.all()
    return render(request, 'index.html', {'profile': profile, 'skill': skill, 'edu': edu, 'proj': proj, 'exp': exp, 'extra': extra, 'lang': lang})
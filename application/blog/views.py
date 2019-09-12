from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import generic
from .models import Article
from .forms import ArticleForm
from .forms import LoginForm
from .forms import AddressForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import Permission, User
from django.contrib.auth import logout
from django.urls import reverse, reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
#---------------importation pour pdf------------------------
from django.views.generic import View
from django.utils import timezone
from .render import Render
#---------------------------------------
from django.views.generic import View
#importing get_template from loader
from django.template.loader import get_template
from .forms import SignUpForm
#--------------filter------------------
from .filters import ArticleFilter
#--------------paginator------------------
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger




#--------------filter + search + paginator (stack)------------------
class IndexView(generic.ListView):
    template_name = 'blog/pages/index.html'
    def get(self, request):
        article_list = Article.objects.all().order_by('-date')
        article_filter = ArticleFilter(request.GET, queryset=article_list)
        if (request.GET.get('customer') or request.GET.get('date_min') or request.GET.get('titre')):
            self.search = 'search'
            return render(request, self.template_name, {
                'articles': article_filter.qs,
                'filter': article_filter.form,
                'article_list' : article_list,
                'search' : self.search,
            })
        else:
            paginator = Paginator(article_filter.qs, 2)
            page = request.GET.get('page')
            try:
                articles = paginator.page(page)
            except PageNotAnInteger:
                articles = paginator.page(1)
            except EmptyPage:
                articles = paginator.page(paginator.num_pages)
            index = paginator.page_range.index(articles.number)
            max_index = len(paginator.page_range)
            start_index = index - 5 if index >= 5 else 0
            end_index = index + 5 if index <= max_index - 5 else max_index
            page_range = paginator.page_range[start_index:end_index]

            return render(request, self.template_name, {
                'articles': articles,
                'filter': article_filter.form,
                'page_range': page_range,
                'article_list':article_list,
            })

#--------------filter------------------
#un code plus cours sans pagination.       

# class IndexView(generic.ListView):
#     model = Article
#     template_name = 'blog/pages/index.html'
#     paginate_by = 2
#     ordering = ['-date']

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['filter'] = ArticleFilter(self.request.GET, queryset=self.get_queryset())
#         return context 

class DetailView(generic.DetailView):
    model = Article
    template_name = 'blog/pages/detail_article.html' 

class ArticleCreate(CreateView):
    model = Article
    fields = ['titre', 'contenu', 'image']
    template_name = 'blog/pages/create_article.html'
    success_url = 'http://localhost:8000/blog/'

    def form_valid(self, form):
        # form.instance.customer = self.request.user
        form.instance.customer_id = self.request.user.id
        return super().form_valid(form)

class ArticleUpdate(UpdateView):
    model = Article
    fields = ['titre', 'contenu', 'image']
    template_name = 'blog/pages/article_update.html'
    success_url = 'http://localhost:8000/blog/'

class ArticleDelete(DeleteView):
    model = Article
    template_name = 'blog/pages/delete_confirm.html'
    success_url = reverse_lazy('blog:index')

def log_in(request):
	form = LoginForm(request.POST or None)

	if form.is_valid(): 
		username = form.cleaned_data['username']
		password = form.cleaned_data['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
		    login(request, user)
		    # Redirect to a success page.
		    return redirect('blog:index')
		else:
		    # Return an 'invalid login' error message.
		    return render(request, 'blog/pages/login.html',  {'form':form})
	return render(request, 'blog/pages/login.html', {'form':form})

def log_out(request):
    logout(request)
    return redirect('blog:index')

# def register (request):
# 	if request.method == "POST":
# 		form = UserCreationForm(request.POST)
# 		if form.is_valid():
# 			form.save()
# 			return redirect ('blog:log_in')
# 	else:
# 		form = UserCreationForm()

# 	return render(request, 'blog/pages/register.html', {'form':form})

# def register (request):
#   if request.method == "POST":
#       form = SignUpForm(request.POST)
#       if form.is_valid():
#           form.save()
#           return redirect ('blog:log_in')
#   else:
#       form = SignUpForm()

#   return render(request, 'blog/pages/register.html', {'form':form})

def register(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.author.anniv = form.cleaned_data.get('anniv')
            user.author.pdp = form.cleaned_data.get('pdp')
            user.save()
            return redirect('blog:log_in')
    else:
        form = SignUpForm()
    return render(request, 'blog/pages/register.html', {'form': form})

#generate pdf view
class RenderPdf(View):

    def get(self, request):
        articles = Article.objects.all()
        today = timezone.now()
        params = {
            'today': today,
            'articles': articles,
            'request': request
        }
        return Render.render('blog/pages/renderpdf/pdf.html', params)


def forms (request):
    form = AddressForm()
    return render(request, 'blog/pages/forms.html',{'form': form})
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView
from aplicatie2.models import Company


class CompanyView(LoginRequiredMixin, ListView):
    model = Company
    template_name = 'aplicatie2/companies_index.html'
    paginate_by = 5
    queryset = model.objects.all().order_by('id')

    def get_context_data(self, *args, **kwargs):
        data = super().get_context_data()
        data['page'] = self.request.GET.get('page') if self.request.GET.get('page') else 1
        return data


class CreateCompanyView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Company
    fields = ['name', 'website', 'location']
    template_name = 'aplicatie2/companies_form.html'
    # TODO: look into permissions
    permission_required = 'user_profile.add_pontaj'

    def get_success_url(self):
        return reverse('companies:list_companies')


class UpdateCompanyView(LoginRequiredMixin, UpdateView):
    model = Company
    fields = ['name', 'website', 'location']
    template_name = 'aplicatie2/companies_form.html'

    def get_success_url(self):
        return reverse('companies:list_companies')


@login_required
def delete_company(request, pk):
    Company.objects.filter(id=pk).delete()
    return redirect(f'/companies/?page={request.GET.get("page")}')


@login_required
def deactivate_company(request, pk):
    Company.objects.filter(id=pk).update(active=0)
    return redirect(f'/companies/?page={request.GET.get("page")}')


@login_required
def activate_company(request, pk):
    Company.objects.filter(id=pk).update(active=1)
    return redirect(f'/companies/?page={request.GET.get("page")}')

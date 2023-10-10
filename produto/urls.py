from django.urls import path
from .views import home, CategoriaView, InformacoesProdutoView, sobre, RegistroClienteView, endereco, \
    ProfileView, AtualizarEndereco, add_ao_carrinho, mostrar_carrinho, plus_cart, minus_cart, remove_cart, \
    remove_desejo, add_lista_desejos, mostrar_lista_desejos \

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view
from .forms import LoginForm, AlterarSenhaForm, ResetarSenhaForm, RedefinitionsForm

urlpatterns = [
    # urls referente ao produto
    path('', home, name='home'),
    path('sobre/', sobre, name='sobre'),
    path('categoria/<slug:val>', CategoriaView.as_view(), name='categoria'),
    path('informacoes_produto/<int:pk>', InformacoesProdutoView.as_view(), name='informacoes_produto'),
    path('add-ao-carrinho/', add_ao_carrinho, name='add_ao_carrinho'),
    path('carrinho/', mostrar_carrinho, name='carrinho'),
    path('add_lista_desejos/', add_lista_desejos, name='lista_desejos'),
    path('lista_desejos/', mostrar_lista_desejos, name='lista_desejos'),
    path('plus_cart/', plus_cart, name='plus_cart'),
    path('minus_cart/', minus_cart, name='minus_cart'),
    path('remove_cart/', remove_cart, name='remove_cart'),
    path('remove_desejo/', remove_desejo, name='remove_desejo'),

    # urls referente ao usuario e autenticações no sistema
    path('registrar_conta/', RegistroClienteView.as_view(), name='registro_conta'),
    path('conta/login/', auth_view.LoginView.as_view(template_name='usuario/login.html', authentication_form=LoginForm),
         name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('endereco/', endereco, name='endereco'),
    path('endereco/<int:pk>', AtualizarEndereco.as_view(), name='atualizar_endereco'),

    path('alterar_senha/',
         auth_view.PasswordChangeView.as_view(template_name='usuario/alterar_senha.html', form_class=AlterarSenhaForm,
                                              success_url='/senha_alterada'), name='alterar_senha'),

    path('senha_alterada/', auth_view.PasswordChangeDoneView.as_view(template_name='usuario/senha_redefinida.html'),
         name='senha_alterada'),

    path('logout/', auth_view.LogoutView.as_view(next_page='login'), name='sair_da_conta'),

    path('password-reset/',
         auth_view.PasswordResetView.as_view(template_name='usuario/password_reset.html', form_class=ResetarSenhaForm),
         name='password_reset'),

    path('password-reset/done/',
         auth_view.PasswordResetDoneView.as_view(template_name='usuario/password_reset_done.html'),
         name='password_reset_done'),

    path('password-reset-confirm/<uidb64>/<token>/',
         auth_view.PasswordResetConfirmView.as_view(template_name='usuario/password_reset_confirm.html',
                                                    form_class=RedefinitionsForm), name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_view.PasswordResetCompleteView.as_view(template_name='usuario/password_reset_complete.html'),
         name='password_reset_complete'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

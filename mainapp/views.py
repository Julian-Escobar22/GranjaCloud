from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.urls import reverse
from productos.models import Producto, CategoriaProducto
from .forms import CustomUserCreationForm

def index(request):
    categorias = CategoriaProducto.objects.all()
    productos = Producto.objects.filter(publico=True)
    # Verifica si el usuario ha iniciado sesión
    if request.user.is_authenticated:
        # Si el usuario está autenticado, obtén todos los productos
        productos = Producto.objects.all()
    cattmp = Producto.objects.filter(categoria=1)
    return render(request, 'mainapp/index.html', {
        'titulo': 'Home',
        'categorias': categorias,
        'productos': productos,
        'cattmp': cattmp
    })

def iniciar_sesion(request):
    if request.method == 'POST':
        # Si se envió el formulario de inicio de sesión
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Si la autenticación es exitosa, vuelve a cargar la página actual
            return render(request, 'mainapp/index.html')
        else:
            # Manejar el caso en que la autenticación falla
            # Por ejemplo, puedes mostrar un mensaje de error
            error_message = 'Usuario o contraseña incorrectos'
            return render(request, 'mainapp/index.html', {'error_message': error_message})
    else:
        # Manejar la solicitud GET (mostrar el formulario de inicio de sesión)
        return render(request, 'mainapp/index.html')

def registro(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            # Almacenar los datos del usuario en la sesión
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            if 'users' not in request.session:
                request.session['users'] = []
            request.session['users'].append({'username': username, 'email': email})
            return redirect(reverse('index'))  # Redirige a la página principal
    else:
        form = CustomUserCreationForm()
    return render(request, 'mainapp/registro.html', {'form': form})

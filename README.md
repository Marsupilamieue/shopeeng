# Shopeeng

<hr>

# Tugas 2

1. Membuat virtual environment dengan perintah
   ```
   python -m venv env
   ```
3. Masuk ke dalam virtual environment dengan perintah
   ```
   source env/bin/activate
   ```
5. Menginstall beberapa add on pada django dengan menggunakan requirements.txt yang berisi
```
  django
  gunicorn
  whitenoise
  psycopg2-binary
  requests
  urllib3
```
  Kemudian menginstall requirements dengan perintah
  ```
  pip install -r requirements.txt
```
7. Membuat project django
   ```
   django-admin startproject shopeeng .
   ```
9. Untuk keperluan deployment diperlukan menambahkan "*" di setting.py pada Allowed Host
    ```
    ALLOWED_HOSTS = ["*"]
    ```
11. Membuat app dengan nama main
```
   python manage.py startapp main
```
13.Membuat routing agar dapat melakukan routing ke aplikasi main dari root URL
```
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', include('main.urls')),
]
```
   - menambahkan include dan path 'main/'.
14. Membuat model pada folder main, seperti berikut
```
from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    price = models.IntegerField()
    description = models.TextField()
```
15. Menambahkan method show_main pada views.py pada folder main untuk mengatasi request yang masuk ketika URL dihit
```
from django.shortcuts import render
def show_main(request):
    context = {
        'name': 'Faris Zhafir Faza',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)
```
   - context berisi nama dan kelas yang kemudian mengembalikan context dan juga main.html untuk merespon request dengan suatu halaman website

16.  Membuat urls.py pada folder main untuk keperluan routing dengan isi berikut
```
from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]
```
  - Melakukan import show_main dari main.views. show_main nantinya akan diimplementasikan pada tahap selanjutnya untuk menampilkan apa yang akan di tampilkan jika kita berada pada url 'main/'.
  - app_name merupakan nama unik yang akan menjadi pola URL aplikasi
17. Melakukan deployment di adaptable

Bagan Hubungan antara views, urls, models, dan berkas html
<img width="600" alt="Screenshot 2023-09-06 at 19 03 41" src="https://github.com/Marsupilamieue/shopeeng/assets/111985990/395ab835-8989-49ea-a9dd-2a8c9e6d9fe6">

- Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
   Menggunakan virtual environment sangatlah penting karena dengan adanya virtual environment, project django akan lebih stabil, mudah direproduksi, dan bersifat portable. Adanya virtual environment juga membuat project django kita terpisah atau dengan kata lain, project yang dibuat terisolasi agar tidak mengganggu proyek yang lain. Pembuatan proyek django tanpa menggunakan virtual environment tetap bisa dilakukan, tetapi jika tidak menggunakan virtual environment kemungkinan akan terjadi konflik antara proyek django.

- Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya
   - MVC (Model-View-Controller):
     
   Model: Merupakan komponen yang mengatur data dan logika bisnis.
   View: Bertanggung jawab untuk menampilkan tampilan yang diberikan kepada pengguna.
   Controller: Bertindak sebagai perantara antara model dan view.
   
   - MVT (Model-View-Template):

   Model: Merupakan komponen yang mengatur data dan logika bisnis.
   View: Menangani tampilan yang diberikan kepada pengguna.
   Template: Komponen yang mengelola tampilan HTML atau template yang disajikan kepada pengguna.

   - MVVM (Model-View-ViewModel):

   Model: Merupakan komponen yang mengatur data dan logika bisnis.
   View: Ini adalah tampilan yang diberikan kepada pengguna.
   ViewModel: Komponen yang berfungsi sebagai perantara antara model dan view. ViewModel mengubah data dari model ke format yang sesuai       untuk tampilan.

Perbedaan utama antara ketiga pendekatan ini terletak pada cara mereka mengatur dan mengelola komunikasi antara model, tampilan, dan logika pengendali. MVC adalah pola desain yang lebih tua dan umumnya digunakan dalam pengembangan berbasis server, sedangkan MVT adalah MVC, tetapi memiliki perbedaan beberapa nama untuk beberapa komponen. MVVM adalah pola yang lebih modern dan umumnya digunakan dalam pengembangan aplikasi berbasis klien (seperti aplikasi web dengan JavaScript) untuk mengelola tampilan dan interaksi pengguna.

<hr>

# TUGAS 3

1. Apa perbedaan antara form POST dan form GET dalam Django?
   
   form POST adalah method untuk mengirim suatu data ke dalam database, sedangkan form GET adalah method untuk mendapatkan data dari database.

2. Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?

   JSON: JSON sangat mudah untuk dimengerti. JSON digunakan pada banyak aplikasi web maupun mobile, yaitu untuk menyimpan dan mengirimkan data. Format JSON berbentuk text sehingga kode untuk membaca dan membuat JSON banyak terdapat dibanyak bahasa pemrograman.

   XML: XML adalah self-descriptive, jadi dengan membaca XML tersebut kita bisa mengerti informasi apa yang ingin disampaikan dari data yang tertulis. XML digunakan pada banyak aplikasi web maupun mobile, yaitu untuk menyimpan dan mengirimkan data. XML berisi informasi yang dibungkus di dalam tag.
   
   HTML: HTML digunakan untuk menampilkan informasi dalam bentuk halaman web yang dapat dilihat oleh pengguna akhir. Ini adalah format yang digunakan untuk merender tampilan dan konten dalam browser web. HTML bukan format yang cocok untuk pertukaran data struktural, tetapi lebih untuk presentasi dan tampilan.

3. Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?

   Karena JSON didesain menjadi self-describing, sehingga JSON sangat mudah untuk dimengerti, selain itu JSON berbentuk text, sehingga kode untuk membaca dan membuat JSON banyak terdapat dibanyak bahasa pemrograman

<hr>

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)

1. Membuat file forms.py pada folder main untuk membuat struktur form.
```
from django.forms import ModelForm
from main.models import Item

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ["name", "price", "amount", "description"]

```
```model = Item ```
artinya adalah model yang dipakai adalah model Item. Fields menunjukan apa saja yang akan menjadi input user. date_add tidak ditambahkan karena dari models, date_add sudah di auto ditambahkan saat item tersebut dibuat.

2. Mengimport beberapa moddule dan juga membuat fungsi untuk menghasilkan form yang dapat menambahkan item saat button submit ditekan
```
from django.http import HttpResponseRedirect
from main.forms import ProductForm
from django.urls import reverse

def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_item.html", context)

```
```form = ItemForm(request.POST or None)``` artinya dalah membuat ItemForm baru berdasarkan input dari user. Kemudian form yang telah diisi akan dicek kevalidnya, jika form yang diisi valid dan requestnya adalah POST, maka form yang telah diisi akan disave dan akan langsung redirect ke page root.

4. Menambah dua line kode di method show_main pada views.py
```
def show_main(request):
    items = Item.objects.all() # menambah kode ini
    total_items = Item.objects.count()
    context = {
        'name': 'Faris Zhafir Faza',
        'class': 'PBP C',
        'items' : items, # menambah kode ini
        'total_items' : total_items
    }

    return render(request, "main.html", context)
```
```items = Item.objects.all()``` berfungsi untuk mendapatkan semua item yang disimpan dalam Item, ```'items' : items,``` mengeset variable items yang mempunyai isi items di dalam context yang kemudian dikirim ke main.html.

5. Membuat create_item.html untuk halaman pada saat menambahkan item.
```
{% extends 'base.html' %} 

{% block content %}
<h1>Add New Item</h1>

<form method="POST">
    {% csrf_token %}
    <table>
        {{ form.as_table }}
        <tr>
            <td></td>
            <td>
                <input type="submit" value="Add Item"/>
            </td>
        </tr>
    </table>
</form>

{% endblock %}
```
method = "POST" mengindikasikan bahwa form digunakan saat request berjenis POST. csrf_token adalah token untuk security dan form.as_table adalah menampilkan forms yang telah dibuat pada forms.py. Tag input adalah tombol input yang jika ditekan akan mengirimkan request ke views.py dan masuk ke dalam create_item dengan parameter request yang berhasal dari input user.

6. Menambahkan button di root page agar dapat menambah item.
```
  <a href="{% url 'main:create_item' %}">
      <button>
          Add New Product
      </button>
  </a>
```

7. Menambahkan url pada urls.py agar dapat menampilkan halaman saat membuat item.
```
path('create-item', create_item, name='create_item'),
```
kemudian mengimport create_item 

8. Menambahkan kode yang akan menampilkan item-item yang sudah pernah diinput.
```
   <table>
      <tr>
          <th>Name</th>
          <th>Price</th>
          <th>Amount</th>
          <th>Description</th>
          <th>Date Added</th>
      </tr>
  
    <hr>
      
      <p>Kamu menyimpan {{total_items}} item pada aplikasi ini</p>
      {% for item in items %}
          <tr>
              <td>{{item.name}}</td>
              <td>{{item.price}}</td>
              <td>{{item.amount}}</td>
              <td>{{item.description}}</td>
              <td>{{item.date_added}}</td>
          </tr>
      {% endfor %}
  </table>
```

9. Membuat method show_xml untuk menampilkan item yang ada dengan format xml
```
def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
```
data akan berisi semua item yang ada yang kemudian mengirimkan response dengan format xml yang ditunjukkan 
dengan content-type yang sudah divalidasi.

10. Membuat method show_json untuk menampilkan item yang ada dengan format json
```
def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```
data akan berisi semua item yang ada yang kemudian mengirimkan response dengan format json yang ditunjukkan dengan content-type yang sudah divalidasi.

11. Membuat method show_json_by_id untuk menampilkan item yang ada dengan format json berdasarkan id dari item tersebut
```
def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```
Berbeda dari method show_json, method ini memerlukan tambahan parameter yaitu parameter id. Data akan berisi item dengan id, id didapatkan dari url, kemudian mengirimkan response dengan format json yang ditunjukkan dengan content-type yang sudah divalidasi.

12. Membuat method show_xml_by_id untuk menampilkan item yang ada dengan format xml berdasarkan id dari item tersebut
```
def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
```
Berbeda dari method show_xml, method ini memerlukan tambahan parameter yaitu parameter id. Data akan berisi item dengan id, id didapatkan dari url, kemudian mengirimkan response dengan format xml yang ditunjukkan dengan content-type yang sudah divalidasi.

13. Membuat method show_html untuk menampilkan item yang ada dengan format xml berdasarkan id dari item tersebut
```
def show_html(request):
    data = Item.objects.all()
    return render(request, 'items.html', {'items': data})
```
Berbeda dari method show_xml dan show_json, method ini memerlukan file html yang akan digunakan untuk menampilkan data yang telah dibungkus dengan html. Data akan berisi semua item, kemudian mengirimkan response dengan format html dengan mengirimkan variabel items yang berisi data.

14. Membuat file html untuk menampilkan data 

15. 
```
<!DOCTYPE html>
<html>
<head>
    <title>Items List</title>
</head>
<body>
    <h1>Items List</h1>
    <ul>
        {% for item in items %}
            <li>{{ item.name }} - {{ item.description }}</li>
        {% endfor %}
    </ul>
</body>
</html>

```

16. Menambahkan route terhadap views yang telah dibuat
```
path('xml/', show_xml, name='show_xml'), 
path('html/', show_html, name='show_html'), 
path('json/', show_json, name='show_json'), 
path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
path('html/<int:id>/', show_html_by_id, name='show_html_by_id'),
```
Untuk path yang perlu mangambil value id (dynamic url) maka perlu ditambahkan '/<int:id>/'.

<hr>

Screenshot saat menembak url ``` http://localhost:8000/json```
<img width="1440" alt="Screenshot 2023-09-13 at 16 40 23" src="https://github.com/Marsupilamieue/shopeeng/assets/111985990/88a8e184-9104-488f-be35-4aa13f91863f">

Screenshot saat menembak url ``` http://localhost:8000/xml```
<img width="1440" alt="Screenshot 2023-09-13 at 16 40 29" src="https://github.com/Marsupilamieue/shopeeng/assets/111985990/5632652c-2002-4c86-a916-90c2ebed610b">

Screenshot saat menembak url ``` http://localhost:8000/html```
<img width="1440" alt="Screenshot 2023-09-13 at 16 40 15" src="https://github.com/Marsupilamieue/shopeeng/assets/111985990/658bd5be-ff68-4868-9adc-32c7d70f8459">

Screenshot saat menembak url ``` http://localhost:8000/html/1```
<img width="1440" alt="Screenshot 2023-09-13 at 16 40 48" src="https://github.com/Marsupilamieue/shopeeng/assets/111985990/9c98aedc-ec1a-4b2d-910a-6f4bf3dc4a7f">

Screenshot saat menembak url ``` http://localhost:8000/xml/1```
<img width="1440" alt="Screenshot 2023-09-13 at 16 40 40" src="https://github.com/Marsupilamieue/shopeeng/assets/111985990/b0533d34-8bdd-4e3e-b6f9-d4a6e0ece266">

<hr>

# TUGAS 4

1. Apa itu Django UserCreationForm, dan jelaskan apa kelebihan dan kekurangannya?<br>
Jawab: Django UserCreationForm adalah formulir bawaan django dalam pendaftaran pengguna dalam sebuah aplikasi web.
Kelebihan: Pengguna baru dapat mendaftar dengan mudah di aplikasi web tanpa menulis kode dari awal.
Kekurangan: Tampilan dari Django UserCreationForm kurang enak dilihat, banyak dari element atau text pada form tersebut masih sangat raw sehingga tampilanya kurang bagus.

2. Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?
Jawab: Otentikasi bertujuan untuk memastikan identitas pengguna, sedangkan otorisasi bertujuan untuk menentukan hak akses pengguna terhadap fitur-fitur tertentu. Keduanya sangatlah penting karena berkaitan dengan keamanan data dan dapat mencegah terjadinya penyalahgunaan aplikasi.

3. Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?
Jawab: Dalam konteks aplikasi web, cookies adalah file teks yang disimpan di browser pengguna dan digunakan untuk menyimpan informasi tentang penggunaan situs web. Cookies dapat digunakan untuk mengidentifikasi pengguna dan menyimpan data sesi pengguna. Django menggunakan cookies untuk mengelola data sesi pengguna. Ketika pengguna masuk ke situs web Django, Django akan membuat cookie yang berisi ID sesi unik untuk pengguna. Cookie ini kemudian dikirim ke browser pengguna dan disimpan di browser. Setiap kali pengguna melakukan permintaan ke situs web Django, cookie akan dikirim ke server Django bersama dengan request. Server Django kemudian menggunakan ID sesi yang terkandung dalam cookie untuk mengambil data sesi pengguna dari penyimpanan server.

4. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?
Jawab: Tidak aman, cookies berisi data-data sensitif seperti informasi login, token otentikasi, atau informasi pribadi lainnya. Jika cookies tidak dienkripsi dengan benar maka akan timbul berbagai risiko, contohnya sebagai berikut:  
* Data tersebut bisa dicuri oleh pihak yang tidak berwenang.

* Kebocoran Data, Cookies dapat bocor jika tidak diatur dengan benar. Ada risiko potensial bahwa skrip yang berjalan di browser dapat mencuri informasi dari cookies, seperti token otentikasi.
* Kebocoran Informasi, Cookies dapat mengandung informasi penting yang dapat membocor jika tidak diatur dengan benar. Misalnya, jika cookies mengandung ID pengguna, ada risiko informasi ini bisa dicuri.

#### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

1. Membuat Registration Form
    #### - Melakukan import pada views.py yang terletak pada folder main
    ```
        from django.shortcuts import redirect
        from django.contrib.auth.forms import UserCreationForm
        from django.contrib import messages  
    ```
    ```redirect``` digunakan untuk mendirect ke halaman atau page tertentu.
    ```UserCreationForm``` adalah form otomatis yang telah dibuat oleh django.
    ```messages``` digunakan untuk mengirimkan message jika sudah berhasil mendaftar pada login page
    #### - Menambahkan fungsi ```register``` pada views.py yang digunakan untuk pendaftaran akun
    ```
    def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)
    ```
    ```form = UserCreationForm()``` adalah mengassign form yang telah dibuat oleh java yang kemudian jika request yang masuk adalah POST, berarti form akan diberikan parameter request.POST. Request POST digunakan karena register pada dasarnya adalah membuat sebuah User. Jika form sudah diisi dan divalidasi maka form akan disave dan kemudian akan mengirimkan messages success yang kemudian web akan menuju ke halaman login. 
    
    #### - Membuat tampilan untuk register. 
    ```
    {% extends 'base.html' %}

    {% block meta %}
        <title>Register</title>
    {% endblock meta %}

    {% block content %}  

    <div class = "login">
    
    <h1>Register</h1>  

        <form method="POST" >  
            {% csrf_token %}  
            <table>  
                {{ form.as_table }}  
                <tr>  
                    <td></td>
                    <td><input type="submit" name="submit" value="Daftar"/></td>  
                </tr>  
            </table>  
        </form>

    {% if messages %}  
        <ul>   
            {% for message in messages %}  
                <li>{{ message }}</li>  
                {% endfor %}  
        </ul>   
    {% endif %}

    </div>  

    {% endblock content %}
    ```
    #### - Menambahkan path untuk register.
    Di dalam urls.py pada main, diperlukan untuk mengimport method register agar method tersebut dapat dipanggil di urls.py.
    ```
    from main.views import ....., register
    ```
    Kemudian menambahkan path register ke dalam url patterns
    ```
    path('register/', register, name='register'), 
    ```

2. Membuat Login Form
    #### - Melakukan import pada views.py yang terletak pada folder main.
    ```
    from django.contrib.auth import authenticate, login
    ```
    ```authenticate``` digunakan untuk melakukan autentikasi user dan ```login``` digunakan untuk login jika berhasil di autentikasi oleh sistem.
    #### - Menambahkan method login_user pada views.py.
    ```
    def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main:show_main')
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)
    ```
    Method tersebut melakukan method get untuk mendapatkan value dari username dan password dari form yang diisi oleh user. Kemudian method melakukan autentikasi, apakah ada user dengan username dan password yang diberikan. Value dari autentikasi tersebut dipass ke variabel user yang kemudian dicek, jika ada user tersebut maka user tersebut dapat masuk ke halaman main dan jika tidak, maka page akan menampilkan message yang berisi gagal login. 
    #### - Membuat tampilan login page.
    ```
    {% extends 'base.html' %}

    {% block meta %}
        <title>Login</title>
    {% endblock meta %}

    {% block content %}

    <div class = "login">

    <h1>Login</h1>

    <form method="POST" action="">
        {% csrf_token %}
        <table>
            <tr>
                <td>Username: </td>
                <td><input type="text" name="username" placeholder="Username" class="form-control"></td>
            </tr>
                    
            <tr>
                <td>Password: </td>
                <td><input type="password" name="password" placeholder="Password" class="form-control"></td>
            </tr>

            <tr>
                <td></td>
                <td><input class="btn login_btn" type="submit" value="Login"></td>
            </tr>
        </table>
    </form>

    {% if messages %}
        <ul>
            {% for message in messages %}
                <li>{{ message }}</li>
            {% endfor %}
        </ul>
    {% endif %}     
        
    Don't have an account yet? <a href="{% url 'main:register' %}">Register Now</a>

    </div>

    {% endblock content %}
    ```
    #### - Menambahkan Path untuk login_user.
    Di dalam urls.py pada main, diperlukan untuk mengimport method login_user agar method tersebut dapat dipanggil di urls.py.
    ```
    from main.views import ....., login_user
    ```
    Kemudian menambahkan path register ke dalam url patterns
    ```
    path('login/', login_user, name='login'),
    ```
3. Membuat Fungsi Logout
    #### - Melakukan import pada views.py yang terletak pada folder main.
    ```
    from django.contrib.auth import logout
    ```
    #### - Menambahkan method logout_user pada views.py.
    ```
    def logout_user(request):
        logout(request)
        return redirect('main:login')
    ```
    ```logout(request)``` digunakan untuk mengambil sesi user saat ini, kemudian menghapus sesinya yang kemudian kembali ke halaman login
    #### -  Menambahkan Button Logout pada tampilan main.
    ```
    <a href="{% url 'main:logout' %}">
        <button>
            Logout
        </button>
    </a>
    ```
    Saat button logout diclick, maka akan langsung menjalankan method logout_user yang berada di views.py
    #### - Menambahkan Path untuk logout_user.
    Di dalam urls.py pada main, diperlukan untuk mengimport method logout_user agar method tersebut dapat dipanggil di urls.py.
    ```
    from main.views import ....., logout_user
    ```
    Kemudian menambahkan path register ke dalam url patterns
    ```
    path('logout/', logout_user, name='logout'),
    ```
4. Restriksi Pengguna
    Agar pengguna yang belum terautentikasi tidak dapat masuk ke halaman main, kita perlu melakukan restriksi pengguna. 

    #### - Mengimport login_required
    ```
    from django.contrib.auth.decorators import login_required
    ```
    ```login_required``` digunakan untuk mencegah pengguna asing yang ingin mengakses suatu page, pengguna asing tersebut harus login terlebih dahulu jika ingin mengaksesnya. Penggunaanya adalah cukup menambahkan baris 
    ```
    @login_required(login_url='/login')
    ```
    di atas method yang ingin direstriksi.

5. Membuat dummy akun dan disetiap akun tersebut terdapat tiga dummy item.
    #### - Membuat akun
    Membuat akun dengan melakukan registrasi sebanyak dua kali untuk membuat dua dummy user.
    #### - Menambahkan dummy item di setiap akun
    Menambahkan tiga item di setiap akun.

    Akun pertama 
        ![Alt text](image.png)
    Akun kedua
        ![Alt text](image-1.png)
6. Menghubungkan model Item dengan User.
    #### - Mengimport model User
    ```
    from django.contrib.auth.models import User
    ```
    #### - Menambahkan variabel user pada model Item
    ```
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ```
    Mengubungkan satu item dengan satu user pada model Item dan biasa disebut one to one relationship
    #### - Memodifikasi method create_item
    ```
    ...
    if form.is_valid() and request.method == "POST":
     item = form.save(commit=False)
     item.user = request.user
     item.save()
     return HttpResponseRedirect(reverse('main:show_main'))
    ...
    ```
    ```commit=False``` digunakan untuk mencegah Django langsung menyimpan objek yang dibuat ke database. Kemudian ```item.user = request.user``` berarti item yang dibuat merupakan milik user yang sedang login.
    #### - Memodifikasi method show_main
    ```
    ...
    items = Item.objects.filter(user=request.user)
    total_items = Item.objects.filter(user=request.user).count()
    context = {
        'name': request.user.username,
        ...
    ...
    ```
    ```items = Item.objects.filter(user=request.user)``` item yang ditampilkan pada main page merupakan item kepimilikan dari user yang sedang login. Maka dari itu, item di filter berdasarkan user. ```'name': request.user.username,``` mendapatkan nama dari user yang sekarang sudah login.
    #### - Melakukan migrasi 
    Migrasi diperlukan karena kita mengubah models.py

7. Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last login pada halaman utama aplikasi. 
    #### - Mengimpor beberapa package
    ```
    import datetime
    from django.http import HttpResponseRedirect
    ```
    ```datetime``` digunakan untuk mengambil waktu.
    #### - Mengganti kode yang ada pada blok ```if user is not None```
    ```
    ...
    if user is not None:
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main")) 
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response
    ...
    ```
    User melakukan login terlebih dahulu. Kemudian membuat response dengan variabel response yang juga mendirect user ke halaman main. Kemudian ```response.set_cookie('last_login', str(datetime.datetime.now()))```  berguna untuk membuat last_login pada cookie dengan waktu saat login. 
    #### - Mengubah context pada method show_main
    ```
    ...
    'last_login': request.COOKIES['last_login'],
    ...
    ```
    tambahan line tersebut berfungsi menambahkan informasi cookie last_login pada response yang akan ditampilkan di halaman web.
    #### - Mengubah main.html untuk menambahkan informasi last login
    ```
    ...
    <h5>Sesi terakhir login: {{ last_login }}</h5>
    ...
    ```
    last_login didapatkan dari context pada show_main
    
<hr>
   
   
   

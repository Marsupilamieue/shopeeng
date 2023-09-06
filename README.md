# Shopeeng
# Link : shopeeng.adaptable.app/main/

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







   
   
   

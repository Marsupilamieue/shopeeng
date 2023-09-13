# Shopeeng

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

1. Apa perbedaan antara form POST dan form GET dalam Django?
   
   form POST adalah method untuk mengirim suatu data ke dalam database, sedangkan form GET adalah method untuk mendapatkan data dari database.

2. Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?

   JSON: JSON sangat mudah untuk dimengerti. JSON digunakan pada banyak aplikasi web maupun mobile, yaitu untuk menyimpan dan mengirimkan data. Format JSON berbentuk text sehingga kode untuk membaca dan membuat JSON banyak terdapat dibanyak bahasa pemrograman.
   XML: XML adalah self-descriptive, jadi dengan membaca XML tersebut kita bisa mengerti informasi apa yang ingin disampaikan dari data yang tertulis. XML digunakan pada banyak aplikasi web maupun mobile, yaitu untuk menyimpan dan mengirimkan data. XML berisi informasi yang dibungkus di dalam tag.
   HTML: HTML digunakan untuk menampilkan informasi dalam bentuk halaman web yang dapat dilihat oleh pengguna akhir. Ini adalah format yang digunakan untuk merender tampilan dan konten dalam browser web. HTML bukan format yang cocok untuk pertukaran data struktural, tetapi lebih untuk presentasi dan tampilan.
3. Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?

   Karena JSON didesain menjadi self-describing, sehingga JSON sangat mudah untuk dimengerti, selain itu JSON berbentuk text, sehingga kode untuk membaca dan membuat JSON banyak terdapat dibanyak bahasa pemrograman

<hr>

# Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)

1. Membuat file forms.py pada folder main untuk membuat struktur form.
```
from django.forms import ModelForm
from main.models import Item

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ["name", "price", "amount", "description"]

```
```
model = Item 
```
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








   
   
   

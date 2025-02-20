# Proyek Klasifikasi Gambar: Brain MRI Alzheimer Classification

Full Resource available here: https://drive.google.com/file/d/1MIUdu4iSSlrasrNtNF27WyQJSD63mi2G/view?usp=drive_link

**Project Impelementation**:

![implementasi tfjs](test-inferensi-tfjs.gif)

## Deskripsi Proyek  
Proyek ini bertujuan untuk mengembangkan model klasifikasi gambar untuk mendeteksi tipe alzheimer berdasarkan MRI Otak pasien. Dari percobaan yang dilakukan didapati arsitektur **VGG16** memberikan akurasi testing dan training dataset mencapai **>95%**. Model ini digunakan untuk mengidentifikasi tingkat keparahan **penyakit Alzheimer** berdasarkan citra **MRI otak**. Model awalnya dibuat dan dilatih menggunakan **TensorFlow (Python)**, kemudian dikonversi ke beberapa format yakni **SavedModel, TF-Lite, dan TensorFlow.js** agar dapat digunakan dalam berbagai aplikasi. Salah satu pengujian yang sudah dilakukan menggunakan web.  

## Tentang Dataset  
Dataset yang digunakan adalah **Alzheimer's Disease Multiclass Dataset**, yang berisi sekitar **44.000 gambar MRI otak** yang dikategorikan ke dalam **empat kelas** berdasarkan tingkat keparahan penyakit Alzheimer. Dataset ini telah diproses untuk menghilangkan jaringan non-otak sehingga hanya menyisakan bagian otak yang relevan.  

### Struktur Dataset  
Dataset ini terdiri dari empat kelas utama:  
1. **NonDemented**: 12.800 gambar MRI dari individu tanpa tanda-tanda demensia.  
2. **VeryMildDemented**: 11.200 gambar MRI dari individu dengan gejala demensia yang sangat ringan.  
3. **MildDemented**: 10.000 gambar MRI dari individu dengan demensia ringan.  
4. **ModerateDemented**: 10.000 gambar MRI dari individu dengan demensia sedang.  

### Pengolahan Dataset  
Dalam proyek ini, dataset diambil sample sebanyak 20.000 untuk mengurangi beban pelatihan model, dengan membagi untuk masing-masing label sebanyak 5000 gambar.

### **Evaluasi model**
Pada proyek ini digunakan metrik **akurasi, presisi, recall, dan F1-score**.  dimana didapati akurasi untuk training, testing, dan validasi diatas 95%  

## Struktur Direktori  
```
Alzheimer_Disease_Brain_MRI_Image_Classification
│── brain_mri_alzheimer/       # Folder dataset orisinil
│── Dataset_Final/             # Dataset hasil sampling
│── inferensi-tfjs/            # file web inferensi tfjs
│── saved_model/               # folder SavedModel
│── tfjs_model2/               # hasil konversi ke tfjs
│── alzheimer-mri-classification-main.ipynb # notebook pengembangan
│── best_model_vgg16.tflite    # file tflite dari model
│── best_vgg16.keras           # file keras dari model
│── best_model_vgg16.h5        # file h5 dari model
│── test-inferensi-tfjs.gif    # implementasi tfjs
│── web.png                    # tampilan
│── requirements.txt           # depedencies
∟ README.md                    # file README
```

## Kontak dan Kontribusi  
Jika ingin berkontribusi atau memiliki pertanyaan, silakan hubungi melalui: 
- **GitHub:** [github.com/Haniff-Toha]  

Terima kasih.

# Laporan Proyek Machine Learning - Muhammad Haniff
---
## **Domain Proyek**

Employee attrition atau tingkat keluarnya karyawan dari perusahaan merupakan tantangan kritis bagi organisasi yang ingin mempertahankan stabilitas dan produktivitas tenaga kerja. Tingginya tingkat attrition dapat menyebabkan peningkatan biaya rekrutmen, hilangnya pengetahuan institusional, serta gangguan pada operasi bisnis. Dengan memprediksi kemungkinan attrition, perusahaan dapat mengambil langkah proaktif untuk meningkatkan kepuasan karyawan, mengoptimalkan strategi retensi, dan mengalokasikan sumber daya secara lebih efisien.

Dalam beberapa tahun terakhir, solusi berbasis data semakin relevan dalam mengatasi berbagai tantangan organisasi. Prediksi attrition karyawan menggunakan data historis tenaga kerja untuk mengidentifikasi pola dan faktor yang memengaruhi turnover karyawan. Menurut penelitian yang dipublikasikan dalam *International Journal of Human Resource Studies*, faktor seperti kepuasan kerja, keseimbangan kerja-kehidupan, dan kompensasi memiliki pengaruh signifikan terhadap keputusan karyawan untuk tetap bertahan atau keluar dari perusahaan.

Proyek ini bertujuan untuk memanfaatkan analisis prediktif dalam mengatasi tantangan attrition karyawan. Dengan mengidentifikasi karyawan yang berisiko keluar, organisasi dapat mengembangkan intervensi yang lebih terfokus untuk meningkatkan retensi, mengurangi biaya, dan menciptakan budaya kerja yang positif.  

**Referensi:**  
- [Suriati, et.al (2024). "Effective Strategies for Retaining and Nurturing employees in Organizations" *Advances Jurnal Ekonomi & Bisnis*](https://www.researchgate.net/publication/381099401_Effective_Strategies_for_Retaining_and_Nurturing_employees_in_Organizations)  
- [Walid A.A, et.al (2021). "Employee Turnover: Causes, Importance and Retention Strategies" *European Journal of Business Management and Research*](https://www.researchgate.net/publication/352390912_Employee_Turnover_Causes_Importance_and_Retention_Strategies)  

---

## **Business Understanding**

### **Problem Statements**  
1. Apa saja faktor utama yang mendorong attrition karyawan dalam organisasi?  
2. Bagaimana cara memprediksi secara akurat apakah seorang karyawan kemungkinan akan keluar dari perusahaan?  (Akurasi)
3. Bagaimana organisasi dapat mengurangi risiko kehilangan karyawan berkualitas tinggi (keluarnya karyawan yang berkualitas)?  (Presisi) mereduksi FN dan mereduksi FP (Recall)
4. Bagaimana predictive analysis dapat membantu menekan biaya rekrutmen dan pelatihan akibat attrition?  

### **Goals**  
- Mengembangkan model prediksi untuk mengidentifikasi karyawan yang berisiko keluar.
- Memahami fitur-fitur utama yang memengaruhi attrition, terutama faktor-faktor yang memicu keluarnya karyawan berkualitas tinggi.
- Memberikan wawasan yang dapat ditindaklanjuti bagi tim HR untuk mengurangi biaya rekrutmen dan pelatihan akibat attrition.
- Meningkatkan strategi retensi karyawan berbasis data guna menciptakan lingkungan kerja yang lebih stabil dan produktif.

### **Solution Statement**  
Untuk mencapai tujuan tersebut, solusi berikut akan diterapkan:  
1. **Pengembangan Model Predictive**  
   - Melatih dan mengevaluasi setidaknya dua algoritma machine learning, seperti *logistic regression* dan *random forest*, untuk memprediksi kemungkinan attrition karyawan.  
   - Menggunakan algoritma tambahan seperti *gradient boosting* untuk membandingkan hasil model dan memilih yang paling optimal.  
2. **Pengoptimalan Model**  
   - Melakukan *feature engineering* untuk memastikan data yang relevan dipertimbangkan dalam model.  
   - Melakukan *hyperparameter tuning* untuk meningkatkan performa model dasar (baseline model), sehingga mencapai akurasi, recall, dan precision yang maksimal.  
3. **Evaluasi dan Implementasi**  
   - Mengevaluasi model menggunakan metrik seperti precision, recall, F1-score, dan AUC-ROC untuk memastikan solusi yang kuat dan andal.  
   - Memberikan rekomendasi berbasis data kepada tim HR untuk mengidentifikasi karyawan berisiko tinggi dan mengembangkan program retensi yang lebih efektif.

---
## Data Understanding
Dataset yang diganakan terdiri dari 1.470 data karyawan dengan 35 fitur yang mencakup berbagai informasi, seperti usia, departemen, status pernikahan, pendapatan bulanan, lama bekerja di perusahaan, dan status attrition. Dataset ini berisi kombinasi data numerik dan kategorikal yang relevan untuk menganalisis faktor-faktor yang memengaruhi retensi dan keluarnya karyawan. Dengan menggunakan dataset ini, kita dapat mengidentifikasi pola dan hubungan antara karakteristik karyawan dan attrition untuk membantu perusahaan mempertahankan talenta terbaik dan mengurangi biaya akibat pergantian karyawan. Dataset ini diambil dari Kaggle dan dapat diakses melalui tautan berikut:  
[Employee Attrition Dataset - Kaggle](https://www.kaggle.com/datasets/patelprashant/employee-attrition/data)
 
- **Kondisi Data:**  
  - Tidak ada nilai *null* atau *missing* pada kolom manapun.  

#### **Deskripsi Variabel atau Fitur**  

| **Nama Fitur**               | **Tipe Data** | **Deskripsi**                                                                 |
|-------------------------------|---------------|-------------------------------------------------------------------------------|
| Age                          | Numerik       | Usia karyawan                                                                |
| Attrition                    | Kategorikal   | Apakah karyawan keluar (*Yes/No*)                                            |
| BusinessTravel               | Kategorikal   | Frekuensi perjalanan bisnis karyawan                                         |
| DailyRate                    | Numerik       | Gaji harian                                                                  |
| Department                   | Kategorikal   | Departemen tempat karyawan bekerja                                           |
| DistanceFromHome             | Numerik       | Jarak dari rumah ke tempat kerja (dalam satuan km atau mil)                  |
| Education                    | Numerik       | Tingkat pendidikan (1 = rendah, 5 = tinggi)                                  |
| EducationField               | Kategorikal   | Bidang pendidikan karyawan                                                   |
| EmployeeCount                | Numerik       | Jumlah total karyawan (konstan)                                              |
| EmployeeNumber               | Numerik       | ID unik karyawan                                                             |
| EnvironmentSatisfaction      | Numerik       | Tingkat kepuasan terhadap lingkungan kerja (1 = rendah, 4 = tinggi)          |
| Gender                       | Kategorikal   | Jenis kelamin karyawan                                                       |
| HourlyRate                   | Numerik       | Gaji per jam                                                                 |
| JobInvolvement               | Numerik       | Tingkat keterlibatan dalam pekerjaan (1 = rendah, 4 = tinggi)                |
| JobLevel                     | Numerik       | Tingkat jabatan (1 = rendah, 5 = tinggi)                                     |
| JobRole                      | Kategorikal   | Peran/jabatan karyawan di perusahaan                                         |
| JobSatisfaction              | Numerik       | Tingkat kepuasan terhadap pekerjaan (1 = rendah, 4 = tinggi)                 |
| MaritalStatus                | Kategorikal   | Status pernikahan (Single/Married/Divorced)                                  |
| MonthlyIncome                | Numerik       | Gaji bulanan                                                                 |
| MonthlyRate                  | Numerik       | Total gaji bulanan                                                           |
| NumCompaniesWorked           | Numerik       | Jumlah perusahaan tempat karyawan pernah bekerja                             |
| Over18                       | Kategorikal   | Apakah karyawan berusia di atas 18 tahun (*Yes*)                             |
| OverTime                     | Kategorikal   | Apakah karyawan sering bekerja lembur (*Yes/No*)                             |
| PercentSalaryHike            | Numerik       | Persentase kenaikan gaji karyawan                                            |
| PerformanceRating            | Numerik       | Penilaian kinerja (1 = rendah, 4 = tinggi)                                   |
| RelationshipSatisfaction     | Numerik       | Tingkat kepuasan terhadap hubungan kerja (1 = rendah, 4 = tinggi)            |
| StandardHours                | Numerik       | Jam kerja standar (konstan: 80)                                              |
| StockOptionLevel             | Numerik       | Tingkat opsi saham karyawan (0 = rendah, 3 = tinggi)                         |
| TotalWorkingYears            | Numerik       | Total tahun pengalaman kerja karyawan                                        |
| TrainingTimesLastYear        | Numerik       | Jumlah pelatihan yang diikuti tahun lalu                                     |
| WorkLifeBalance              | Numerik       | Tingkat keseimbangan kerja-kehidupan (1 = rendah, 4 = tinggi)                |
| YearsAtCompany               | Numerik       | Lama bekerja di perusahaan saat ini (tahun)                                  |
| YearsInCurrentRole           | Numerik       | Lama menjalani peran/jabatan saat ini (tahun)                                |
| YearsSinceLastPromotion      | Numerik       | Lama waktu sejak terakhir kali mendapat promosi (tahun)                      |
| YearsWithCurrManager         | Numerik       | Lama bekerja dengan manajer saat ini (tahun)                                 |

---

#### **Eksplorasi Data (Exploratory Data Analysis)**  

Untuk memahami data lebih lanjut, beberapa langkah berikut akan dilakukan:  
1. **Visualisasi Data**:  
   - Membuat histogram untuk melihat distribusi fitur numerik seperti usia, gaji bulanan, dan tahun pengalaman.  
   - Menggunakan diagram batang (bar chart) untuk fitur kategorikal seperti *Attrition*, *Gender*, dan *JobRole*.  
   - Membuat *boxplot* untuk mengidentifikasi outlier pada fitur numerik seperti *MonthlyIncome* dan *DailyRate*.  

2. **Analisis Korelasi**:  
   - Menghitung korelasi antara fitur numerik untuk mengidentifikasi hubungan potensial, terutama dengan fitur target *Attrition*.  
   - Membuat heatmap untuk memvisualisasikan korelasi antar fitur.  

3. **Analisis Bivariat**:  
   - Menganalisis hubungan antara *Attrition* dan fitur utama seperti *OverTime*, *JobSatisfaction*, dan *WorkLifeBalance*.  
   - Menggunakan diagram silang (cross-tabulation) untuk fitur kategorikal.  

4. **Ringkasan Statistik**:  
   - Menggunakan statistik deskriptif (mean, median, standard deviation) untuk memahami distribusi data.  

---

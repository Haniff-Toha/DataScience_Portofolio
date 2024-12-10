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
2. Bagaimana cara memprediksi secara akurat apakah seorang karyawan kemungkinan akan keluar dari perusahaan?  
3. Bagaimana organisasi dapat mengurangi risiko kehilangan karyawan berkualitas tinggi (keluarnya karyawan yang berkualitas)?  
4. Bagaimana wawasan prediktif dapat membantu menekan biaya rekrutmen dan pelatihan akibat attrition?  

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

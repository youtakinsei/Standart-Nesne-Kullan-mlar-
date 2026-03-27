import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout, 
                             QHBoxLayout, QCheckBox, QComboBox, QLabel, 
                             QInputDialog, QMessageBox, QStackedWidget)
from PyQt5.QtCore import Qt

class AnaSayfa(QWidget):
    def __init__(self, degistir_fonk):
        super().__init__()
        layout = QVBoxLayout()
        self.btn_gecis = QPushButton("BİLGİ SAYFASINA GEÇ")
        self.btn_gecis.setFixedSize(200, 50)
        self.btn_gecis.clicked.connect(degistir_fonk)
        
        layout.addWidget(self.btn_gecis, alignment=Qt.AlignCenter)
        self.setLayout(layout)

class BilgiSayfasi(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.chk_film = QCheckBox("Film")
        self.cb_film = QComboBox()
        self.cb_film.addItems(["Aksiyon", "Komedi", "Dram"])
        self.cb_film.setEnabled(False)

        self.chk_muzik = QCheckBox("Müzik")
        self.cb_muzik = QComboBox()
        self.cb_muzik.addItems(["Rock", "Pop", "Caz"])
        self.cb_muzik.setEnabled(False)

        self.chk_film.stateChanged.connect(lambda: self.cb_film.setEnabled(self.chk_film.isChecked()))
        self.chk_muzik.stateChanged.connect(lambda: self.cb_muzik.setEnabled(self.chk_muzik.isChecked()))


        h_layout = QHBoxLayout()
        self.btn_isim = QPushButton("İsim Girişi")
        self.lbl_isim = QLabel("Merhaba ...............")
        self.btn_isim.clicked.connect(self.isim_al)
        h_layout.addWidget(self.btn_isim)
        h_layout.addWidget(self.lbl_isim)


        self.btn_goster = QPushButton("Bilgileri Göster")
        self.btn_goster.clicked.connect(self.bilgileri_onayla)


        layout.addWidget(self.chk_film)
        layout.addWidget(self.cb_film)
        layout.addWidget(self.chk_muzik)
        layout.addWidget(self.cb_muzik)
        layout.addLayout(h_layout)
        layout.addWidget(self.btn_goster)
        
        self.setLayout(layout)

    def isim_al(self):
        isim, ok = QInputDialog.getText(self, "Giriş", "Lütfen isminizi giriniz:")
        if ok and isim:
            self.lbl_isim.setText(f"Merhaba {isim}")

    def bilgileri_onayla(self):
        soru = QMessageBox.question(self, "Onay", "Bilgileri Görmek İstiyor musunuz?", 
                                    QMessageBox.Yes | QMessageBox.No)
        
        if soru == QMessageBox.Yes:
            film_durum = "Film Seçili" if self.chk_film.isChecked() else "Film Seçilmedi"
            muzik_durum = "Müzik Seçili" if self.chk_muzik.isChecked() else "Müzik Seçilmedi"
            isim = self.lbl_isim.text()
            
            mesaj = f"{isim}\n\n"
            mesaj += f"{film_durum} (Tür: {self.cb_film.currentText()})\n"
            mesaj += f"{muzik_durum} (Tür: {self.cb_muzik.currentText()})"
            
            QMessageBox.information(self, "Bilgiler", mesaj)

class PencereYonetici(QStackedWidget):
    def __init__(self):
        super().__init__()
        self.ana_sayfa = AnaSayfa(self.bilgi_sayfasina_gec)
        self.bilgi_sayfasi = BilgiSayfasi()
        
        self.addWidget(self.ana_sayfa)
        self.addWidget(self.bilgi_sayfasi)
        
        self.setWindowTitle("Etkinlik Uygulaması")
        self.setFixedSize(400, 300)

    def bilgi_sayfasina_gec(self):
        self.setCurrentIndex(1)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    pencere = PencereYonetici()
    pencere.show()
    sys.exit(app.exec_())

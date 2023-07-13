import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog, QLabel, QMessageBox
from PySide6.QtGui import QIcon, QPixmap, Qt
from merge_files import MergeFiles

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Gerador de PDF')
        self.setWindowIcon(QIcon('src\imgs\icon.png'))

        layout = QVBoxLayout()

        # Adicionando a logo
        logo_label = QLabel(self)
        pixmap = QPixmap('src\imgs\logo.png')
        pixmap = pixmap.scaled(pixmap.width() * 0.4, pixmap.height() * 0.4)
        logo_label.setPixmap(pixmap)
        logo_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(logo_label)

        self.button = QPushButton('Selecionar Arquivos', self)
        self.button.clicked.connect(self.select_files)
        layout.addWidget(self.button)

        self.file_label = QLabel(self)
        layout.addWidget(self.file_label)

        self.save_button = QPushButton('Gerar e Salvar PDF', self)
        self.save_button.clicked.connect(self.generate_pdf)
        layout.addWidget(self.save_button)

        self.setLayout(layout)

        self.selected_files = []
        
        self.update_file_label()

    def select_files(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        files, _ = QFileDialog.getOpenFileNames(self, 'Selecionar Arquivos', '', 'Todos os Arquivos (*.*)', options=options)
        self.selected_files = files

        self.update_file_label()

    def update_file_label(self):
        if self.selected_files:
            file_text = '\n'.join(self.selected_files)
        else:
            file_text = 'Nenhum arquivo selecionado.'

        self.file_label.setText(file_text)

    def generate_pdf(self):
        if self.selected_files:
            save_options = QFileDialog.Options()
            save_options |= QFileDialog.ReadOnly
            file_path, _ = QFileDialog.getSaveFileName(self, 'Salvar PDF', '', 'PDF Files (*.pdf)', options=save_options)
            MergeFiles().juntar_arquivos_em_pdf(self.selected_files, file_path)
            self.selected_files = []
            self.update_file_label()
            QMessageBox.information(self, 'PDF Gerado', 'O PDF foi gerado com sucesso.')
        else:
            print('Nenhum arquivo selecionado.')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

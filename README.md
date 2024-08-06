napis profesionalni a stylovy popisek aplikace na github : import sys
import subprocess

# Funkce pro kontrolu nainstalovaných balíčků
def check_and_install(package):
    try:
        __import__(package)
    except ImportError:
        subprocess.check_call([sys.executable, "install.py"])

# Seznam balíčků ke kontrole
required_packages = [
    "PyQt5",
    "selenium",
    "webdriver-manager"
]

# Kontrola a instalace balíčků
for package in required_packages:
    check_and_install(package)

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QCheckBox, QSpinBox, QDoubleSpinBox, QMessageBox, QFormLayout, QFileDialog, QTextEdit, QGroupBox, QHBoxLayout
from PyQt5.QtGui import QIcon
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class InstaBotApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Instagram Bot')
        self.setWindowIcon(QIcon('C:\\Users\\pozor\\Pictures\\icon.png'))
        self.setGeometry(100, 100, 400, 800)

        layout = QVBoxLayout()
        form_layout = QFormLayout()

        # Základní nastavení
        self.username_label = QLabel('Uživatelské jméno:')
        self.username_input = QLineEdit(self)
        form_layout.addRow(self.username_label, self.username_input)

        self.password_label = QLabel('Heslo:')
        self.password_input = QLineEdit(self)
        self.password_input.setEchoMode(QLineEdit.Password)
        form_layout.addRow(self.password_label, self.password_input)

        self.like_checkbox = QCheckBox('Automatické lajkování', self)
        form_layout.addRow(self.like_checkbox)

        self.follow_checkbox = QCheckBox('Automatické sledování', self)
        form_layout.addRow(self.follow_checkbox)

        self.comment_checkbox = QCheckBox('Automatické komentování', self)
        form_layout.addRow(self.comment_checkbox)

        self.photo_checkbox = QCheckBox('Automatické nahrávání fotek', self)
        form_layout.addRow(self.photo_checkbox)

        self.num_actions_label = QLabel('Počet akcí:')
        self.num_actions_spinbox = QSpinBox(self)
        self.num_actions_spinbox.setRange(1, 1000)
        form_layout.addRow(self.num_actions_label, self.num_actions_spinbox)

        # Základní možnosti viditelné při spuštění
        self.like_delay = self.create_spinbox(form_layout, 'Zpoždění mezi lajky (s):', 10)
        self.unlike_delay = self.create_spinbox(form_layout, 'Zpoždění mezi unlajky (s):', 10)
        self.follow_delay = self.create_spinbox(form_layout, 'Zpoždění mezi sledováním (s):', 30)
        self.unfollow_delay = self.create_spinbox(form_layout, 'Zpoždění mezi unfollow (s):', 30)
        self.comment_delay = self.create_spinbox(form_layout, 'Zpoždění mezi komentáři (s):', 60)
        self.whitelist = self.create_lineedit(form_layout, 'Whitelist soubor:')
        self.blacklist = self.create_lineedit(form_layout, 'Blacklist soubor:')
        self.comments_file = self.create_lineedit(form_layout, 'Comments soubor:')
        self.stop_words = self.create_lineedit(form_layout, 'Stop slova (oddělené čárkou):')

        # Vybrání fotek
        self.photo_paths = []
        self.photo_button = QPushButton('Vybrat fotky k nahrání', self)
        self.photo_button.clicked.connect(self.select_photos)
        form_layout.addRow(self.photo_button)

        # Seznam uživatelů k sledování
        self.follow_users_label = QLabel('Seznam uživatelů k sledování (oddělené čárkou):')
        self.follow_users_input = QTextEdit(self)
        form_layout.addRow(self.follow_users_label, self.follow_users_input)

        # Tlačítko pro zobrazení rozšířeného nastavení
        self.advanced_button = QPushButton('Rozšířené nastavení', self)
        self.advanced_button.clicked.connect(self.toggle_advanced_settings)
        form_layout.addRow(self.advanced_button)

        # Rozšířené možnosti
        self.advanced_settings_group = QGroupBox()
        advanced_layout = QFormLayout()

        self.max_likes_per_day = self.create_spinbox(advanced_layout, 'Max lajků za den:', 1000)
        self.max_unlikes_per_day = self.create_spinbox(advanced_layout, 'Max unlajků za den:', 1000)
        self.max_follows_per_day = self.create_spinbox(advanced_layout, 'Max sledování za den:', 350)
        self.max_unfollows_per_day = self.create_spinbox(advanced_layout, 'Max unfollow za den:', 350)
        self.max_comments_per_day = self.create_spinbox(advanced_layout, 'Max komentářů za den:', 100)
        self.max_likes_to_like = self.create_spinbox(advanced_layout, 'Max lajků k lajkování:', 200)
        self.filter_users = self.create_checkbox(advanced_layout, 'Filtrovat uživatele:')
        self.max_followers_to_follow = self.create_spinbox(advanced_layout, 'Max followerů k sledování:', 2000)
        self.min_followers_to_follow = self.create_spinbox(advanced_layout, 'Min followerů k sledování:', 10)
        self.max_following_to_follow = self.create_spinbox(advanced_layout, 'Max following k sledování:', 10000)
        self.min_following_to_follow = self.create_spinbox(advanced_layout, 'Min following k sledování:', 10)
        self.max_followers_to_following_ratio = self.create_double_spinbox(advanced_layout, 'Max followers/following poměr:', 10)
        self.max_following_to_followers_ratio = self.create_double_spinbox(advanced_layout, 'Max following/followers poměr:', 2)
        self.min_media_count_to_follow = self.create_spinbox(advanced_layout, 'Min počet médií k sledování:', 3)
        self.max_following_to_block = self.create_spinbox(advanced_layout, 'Max following k blokování:', 2000)

        self.advanced_settings_group.setLayout(advanced_layout)
        self.advanced_settings_group.setVisible(False)  # Skryjeme rozšířené nastavení při spuštění
        layout.addWidget(self.advanced_settings_group)

        # Startovací tlačítko
        self.start_button = QPushButton('Start', self)
        self.start_button.clicked.connect(self.start_bot)
        layout.addLayout(form_layout)
        layout.addWidget(self.start_button)

        self.setLayout(layout)

    def create_spinbox(self, layout, label_text, default_value):
        label = QLabel(label_text)
        spinbox = QSpinBox(self)
        spinbox.setRange(0, 10000)
        spinbox.setValue(default_value)
        layout.addRow(label, spinbox)
        return spinbox

    def create_double_spinbox(self, layout, label_text, default_value):
        label = QLabel(label_text)
        spinbox = QDoubleSpinBox(self)
        spinbox.setRange(0, 100)
        spinbox.setValue(default_value)
        layout.addRow(label, spinbox)
        return spinbox

    def create_checkbox(self, layout, label_text):
        checkbox = QCheckBox(label_text, self)
        layout.addRow(checkbox)
        return checkbox

    def create_lineedit(self, layout, label_text):
        label = QLabel(label_text)
        lineedit = QLineEdit(self)
        layout.addRow(label, lineedit)
        return lineedit

    def select_photos(self):
        options = QFileDialog.Options()
        files, _ = QFileDialog.getOpenFileNames(self, "Vybrat fotky k nahrání", "", "Images (*.png *.xpm *.jpg);;All Files (*)", options=options)
        if files:
            self.photo_paths = files
            QMessageBox.information(self, 'Fotky vybrány', f'Vybráno {len(files)} fotek.')

    def toggle_advanced_settings(self):
        self.advanced_settings_group.setVisible(not self.advanced_settings_group.isVisible())

    def start_bot(self):
        username = self.username_input.text()
        password = self.password_input.text()
        num_actions = self.num_actions_spinbox.value()
        like = self.like_checkbox.isChecked()
        follow = self.follow_checkbox.isChecked()
        comment = self.comment_checkbox.isChecked()
        photo = self.photo_checkbox.isChecked()

        if not username or not password:
            QMessageBox.warning(self, 'Chyba', 'Prosím, vyplňte uživatelské jméno a heslo.')
            return

        follow_users = self.follow_users_input.toPlainText().split(',')

        bot = InstaBot(username, password, {
            'max_likes_per_day': self.max_likes_per_day.value(),
            'max_unlikes_per_day': self.max_unlikes_per_day.value(),
            'max_follows_per_day': self.max_follows_per_day.value(),
            'max_unfollows_per_day': self.max_unfollows_per_day.value(),
            'max_comments_per_day': self.max_comments_per_day.value(),
            'max_likes_to_like': self.max_likes_to_like.value(),
            'filter_users': self.filter_users.isChecked(),
            'max_followers_to_follow': self.max_followers_to_follow.value(),
            'min_followers_to_follow': self.min_followers_to_follow.value(),
            'max_following_to_follow': self.max_following_to_follow.value(),
            'min_following_to_follow': self.min_following_to_follow.value(),
            'max_followers_to_following_ratio': self.max_followers_to_following_ratio.value(),
            'max_following_to_followers_ratio': self.max_following_to_followers_ratio.value(),
            'min_media_count_to_follow': self.min_media_count_to_follow.value(),
            'max_following_to_block': self.max_following_to_block.value(),
            # následující možnosti jsou při spuštění odkryté
            'like_delay': self.like_delay.value(),
            'unlike_delay': self.unlike_delay.value(),
            'follow_delay': self.follow_delay.value(),
            'unfollow_delay': self.unfollow_delay.value(),
            'comment_delay': self.comment_delay.value(),
            'whitelist': self.whitelist.text(),
            'blacklist': self.blacklist.text(),
            'comments_file': self.comments_file.text(),
            'stop_words': self.stop_words.text().split(','),
            'photo_paths': self.photo_paths,
            'follow_users': follow_users
        })

        try:
            bot.login()
            if like:
                bot.like_timeline(num_actions)
            if follow:
                bot.follow_users(num_actions)
            if comment:
                bot.comment_hashtag('examplehashtag', num_actions)
            if photo:
                for photo_path in self.photo_paths:
                    bot.upload_photo(photo_path, 'Caption for photo')
            QMessageBox.information(self, 'Hotovo', 'Bot dokončil své akce.')
        except Exception as e:
            QMessageBox.critical(self, 'Chyba', f'Nastala chyba: {e}')

class InstaBot:
    def __init__(self, username, password, params):
        self.username = username
        self.password = password
        self.params = params
        self.driver = None

    def login(self):
        print(f"Logging in user {self.username}")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(3)

        username_input = self.driver.find_element(By.NAME, 'username')
        password_input = self.driver.find_element(By.NAME, 'password')

        username_input.send_keys(self.username)
        password_input.send_keys(self.password)
        password_input.send_keys(Keys.RETURN)

        time.sleep(5)  # Počkejte, než se přihlášení dokončí

        if "challenge" in self.driver.current_url:
            raise Exception("Instagram vyžaduje další ověření. Prosím, přihlaste se ručně.")

        print("Successfully logged in")
        print(f"Using parameters: {self.params}")

    def like_timeline(self, num_actions):
        print(f"Performing {num_actions} like actions on timeline")

    def follow_users(self, num_actions):
        print(f"Performing {num_actions} follow actions")

    def comment_hashtag(self, hashtag, num_actions):
        print(f"Performing {num_actions} comment actions on hashtag: {hashtag}")

    def upload_photo(self, photo_path, caption):
        print(f"Uploading photo: {photo_path} with caption: {caption}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = InstaBotApp()
    ex.show()
    sys.exit(app.exec_())

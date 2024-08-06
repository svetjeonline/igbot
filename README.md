# Instagram Bot 🤖📸

![Instagram Bot](igbot.png)

Tento projekt je Instagram Bot postavený pomocí PyQt5 a Selenium, který umožňuje automatizaci různých akcí na Instagramu, jako je lajkování, sledování, komentování a nahrávání fotek.

## Funkce
- Automatické lajkování příspěvků
- Automatické sledování uživatelů
- Automatické komentování příspěvků
- Automatické nahrávání fotek
- Pokročilé možnosti nastavení pro filtrování uživatelů a nastavení zpoždění mezi akcemi

## Požadavky
- Python 3.x
- PyQt5
- Selenium
- Webdriver Manager

## Instalace
Nejprve zkontrolujte, zda máte nainstalované všechny požadované balíčky. Pokud ne, skript `install.py` je automaticky nainstaluje:

```python
import sys
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
```

## Použití
1. Spusťte aplikaci:

    ```bash
    python main.py
    ```

2. Vyplňte požadované údaje v uživatelském rozhraní:
    - Uživatelské jméno a heslo
    - Možnosti automatizace (lajkování, sledování, komentování, nahrávání fotek)
    - Počet akcí
    - Pokročilé možnosti nastavení

3. Klikněte na tlačítko **Start** pro spuštění bota.

## Uživatelské Rozhraní
![User Interface](https://example.com/ui_screenshot.png)

### Základní Nastavení
- **Uživatelské jméno**: Vložte své uživatelské jméno na Instagramu.
- **Heslo**: Vložte své heslo na Instagramu.
- **Automatické lajkování**: Zaškrtněte, pokud chcete automaticky lajkovat příspěvky.
- **Automatické sledování**: Zaškrtněte, pokud chcete automaticky sledovat uživatele.
- **Automatické komentování**: Zaškrtněte, pokud chcete automaticky komentovat příspěvky.
- **Automatické nahrávání fotek**: Zaškrtněte, pokud chcete automaticky nahrávat fotky.
- **Počet akcí**: Nastavte počet akcí, které má bot provést.

### Pokročilé Nastavení
- **Zpoždění mezi akcemi**: Nastavte zpoždění mezi jednotlivými akcemi (lajky, unfollow, sledování, atd.).
- **Filtrovat uživatele**: Filtrování uživatelů na základě různých kritérií (počet followerů, following, poměr followers/following, atd.).
- **Whitelist/Blacklist soubor**: Nastavte soubory pro whitelist a blacklist uživatelů.
- **Stop slova**: Nastavte stop slova, která bot nebude používat v komentářích.

## Příspěvek chyb
Pokud narazíte na chybu, prosím otevřete issue na GitHubu a připojte detailní popis problému včetně chybové zprávy.

## Přispívání
Přispívání do projektu je vítáno! Prosím otevřete pull request s vašimi změnami a popište, co a proč jste změnili.

## Licence
Tento projekt je licencován pod MIT licencí. Podrobnosti naleznete v souboru LICENSE.


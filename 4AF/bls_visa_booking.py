"""
Script de prise de RDV - BLS Spain Visa (Mauritanie)
https://mr.blsspainvisa.com/french/

Utilise Selenium pour automatiser la navigation (contourne les protections anti-bot).
Si un CAPTCHA apparaît, le script fait une pause pour que vous le résolviez manuellement.

Prérequis :
    pip install selenium webdriver-manager
"""

import time
import sys
from datetime import datetime

try:
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait, Select
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.chrome.service import Service
    from selenium.common.exceptions import TimeoutException, NoSuchElementException
    from webdriver_manager.chrome import ChromeDriverManager
except ImportError:
    print("Installez les dépendances : pip install selenium webdriver-manager")
    sys.exit(1)


# ─────────────────────────────────────────────
#  CONFIGURATION — Remplissez vos informations
# ─────────────────────────────────────────────
CONFIG = {
    # Compte BLS (inscription sur le site si pas encore fait)
    "email":    "votre@email.com",
    "password": "votre_mot_de_passe",

    # Type de visa (tel qu'affiché dans le menu déroulant du site)
    "visa_type": "Tourist",        # ex: Tourist, Business, Family Reunion...

    # Nombre de candidats
    "nb_applicants": 1,

    # Vérifier toutes les X secondes si un créneau est dispo
    "check_interval_sec": 30,

    # Mettre True pour réserver automatiquement dès qu'un créneau est trouvé
    # Mettre False pour juste alerter et attendre votre confirmation
    "auto_book": False,
}

LOGIN_URL      = "https://mauritania.blsspainglobal.com/Global/account/login"
DASHBOARD_URL  = "https://mauritania.blsspainglobal.com/Global/account/dashboard"
APPT_URL       = "https://mauritania.blsspainglobal.com/Global/appointment/BLSAppointment"

WAIT = 15  # secondes max pour chaque élément


def make_driver() -> webdriver.Chrome:
    """Crée un driver Chrome avec des options discrètes."""
    options = webdriver.ChromeOptions()
    # Désactiver les indicateurs "piloté par automatisation"
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)
    options.add_argument("--start-maximized")
    # Changer le user-agent pour ressembler à un vrai navigateur
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    )
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    # Masquer webdriver dans le JS
    driver.execute_cdp_cmd(
        "Page.addScriptToEvaluateOnNewDocument",
        {"source": "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"},
    )
    return driver


def wait_for(driver: webdriver.Chrome, by: By, selector: str, timeout: int = WAIT):
    """Attend qu'un élément soit présent et le retourne."""
    return WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((by, selector))
    )


def wait_and_click(driver: webdriver.Chrome, by: By, selector: str, timeout: int = WAIT):
    el = WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable((by, selector))
    )
    el.click()
    return el


def pause_for_captcha(driver: webdriver.Chrome):
    """Détecte si un CAPTCHA est présent et attend la résolution manuelle."""
    captcha_selectors = [
        "iframe[src*='recaptcha']",
        "iframe[src*='hcaptcha']",
        ".g-recaptcha",
        "#captcha",
    ]
    for sel in captcha_selectors:
        try:
            driver.find_element(By.CSS_SELECTOR, sel)
            print("\n⚠️  CAPTCHA détecté — résolvez-le dans le navigateur puis appuyez sur Entrée ici...")
            input()
            return
        except NoSuchElementException:
            continue


def login(driver: webdriver.Chrome) -> bool:
    """Se connecte au portail BLS."""
    print(f"[{now()}] Ouverture de la page de connexion...")
    driver.get(LOGIN_URL)
    time.sleep(2)

    try:
        # Champ email — essai de plusieurs sélecteurs courants
        for sel in ["#email", "input[name='email']", "input[type='email']"]:
            try:
                email_field = driver.find_element(By.CSS_SELECTOR, sel)
                email_field.clear()
                email_field.send_keys(CONFIG["email"])
                break
            except NoSuchElementException:
                continue

        # Champ mot de passe
        for sel in ["#password", "input[name='password']", "input[type='password']"]:
            try:
                pwd_field = driver.find_element(By.CSS_SELECTOR, sel)
                pwd_field.clear()
                pwd_field.send_keys(CONFIG["password"])
                break
            except NoSuchElementException:
                continue

        pause_for_captcha(driver)

        # Bouton de connexion
        for sel in ["button[type='submit']", "input[type='submit']", "#btnLogin", ".login-btn"]:
            try:
                driver.find_element(By.CSS_SELECTOR, sel).click()
                break
            except NoSuchElementException:
                continue

        # Attendre la redirection vers le dashboard
        WebDriverWait(driver, 15).until(lambda d: "dashboard" in d.current_url or "appointment" in d.current_url)
        print(f"[{now()}] Connexion réussie ✓")
        return True

    except TimeoutException:
        print(f"[{now()}] Échec de connexion — vérifiez email/mot de passe ou résolvez le CAPTCHA manuellement.")
        input("Connectez-vous manuellement dans le navigateur, puis appuyez sur Entrée pour continuer...")
        return True
    except Exception as e:
        print(f"[{now()}] Erreur lors de la connexion : {e}")
        return False


def check_and_book(driver: webdriver.Chrome) -> bool:
    """
    Navigue vers la page de prise de RDV et vérifie les créneaux disponibles.
    Retourne True si un RDV a été réservé (ou trouvé si auto_book=False).
    """
    print(f"[{now()}] Vérification des créneaux disponibles...")
    driver.get(APPT_URL)
    time.sleep(3)

    try:
        # ── Sélection du type de visa ──────────────────────────────────────
        visa_dropdowns = driver.find_elements(
            By.CSS_SELECTOR,
            "select[name*='visa'], select[id*='visa'], select[id*='Visa'], select[id*='category']"
        )
        if visa_dropdowns:
            Select(visa_dropdowns[0]).select_by_visible_text(CONFIG["visa_type"])
            time.sleep(1)

        # ── Nombre de candidats ────────────────────────────────────────────
        nb_fields = driver.find_elements(
            By.CSS_SELECTOR,
            "input[name*='applicant'], input[id*='applicant'], input[id*='Applicant'], "
            "select[name*='applicant'], select[id*='NoOfApplicant']"
        )
        if nb_fields:
            tag = nb_fields[0].tag_name
            if tag == "select":
                Select(nb_fields[0]).select_by_value(str(CONFIG["nb_applicants"]))
            else:
                nb_fields[0].clear()
                nb_fields[0].send_keys(str(CONFIG["nb_applicants"]))
            time.sleep(1)

        # ── Cliquer sur "Rechercher" / "Vérifier disponibilité" ───────────
        for sel in [
            "button[type='submit']",
            "input[type='submit']",
            "#btnSearch", "#btnNext", ".btn-primary",
            "button[value='Search']",
        ]:
            try:
                driver.find_element(By.CSS_SELECTOR, sel).click()
                time.sleep(2)
                break
            except NoSuchElementException:
                continue

        pause_for_captcha(driver)
        time.sleep(2)

        # ── Détecter les créneaux disponibles ─────────────────────────────
        # Cherche des éléments de calendrier ou des boutons de sélection de date
        slot_selectors = [
            ".available",
            ".slot-available",
            "td.available",
            "a.available",
            ".calendar-day:not(.disabled):not(.past)",
            "input[type='radio'][value*='slot']",
        ]
        slots = []
        for sel in slot_selectors:
            slots = driver.find_elements(By.CSS_SELECTOR, sel)
            if slots:
                break

        if not slots:
            # Essai générique : chercher des cellules de calendrier cliquables
            slots = driver.find_elements(By.XPATH, "//td[@class and not(contains(@class,'disabled')) and not(contains(@class,'past'))]")

        if not slots:
            print(f"[{now()}] Aucun créneau disponible pour l'instant.")
            return False

        print(f"[{now()}] {len(slots)} créneau(x) trouvé(s) !")

        if not CONFIG["auto_book"]:
            print("   → auto_book=False : confirmez manuellement dans le navigateur.")
            input("   Appuyez sur Entrée après avoir choisi votre créneau dans le navigateur...")
            return True

        # ── Réservation automatique du premier créneau ────────────────────
        slots[0].click()
        time.sleep(1)

        # Confirmer si un bouton de confirmation apparaît
        for sel in ["#btnConfirm", "#btnBook", "button[type='submit']", ".btn-confirm"]:
            try:
                btn = driver.find_element(By.CSS_SELECTOR, sel)
                print(f"[{now()}] Confirmation du RDV...")
                btn.click()
                time.sleep(2)
                break
            except NoSuchElementException:
                continue

        print(f"[{now()}] RDV réservé avec succès ! Vérifiez votre email de confirmation.")
        return True

    except Exception as e:
        print(f"[{now()}] Erreur lors de la vérification : {e}")
        return False


def now() -> str:
    return datetime.now().strftime("%H:%M:%S")


def main():
    print("=" * 55)
    print("  BLS Spain Visa — Robot de prise de RDV (Mauritanie)")
    print("=" * 55)

    # Vérification de la config
    if CONFIG["email"] == "votre@email.com":
        print("\n⚠️  Remplissez d'abord CONFIG (email, password) dans le script.")
        sys.exit(1)

    driver = make_driver()

    try:
        if not login(driver):
            print("Impossible de se connecter. Abandon.")
            return

        attempt = 0
        while True:
            attempt += 1
            print(f"\n── Tentative #{attempt} ──────────────────────────────────")
            booked = check_and_book(driver)

            if booked:
                print("\nRDV trouvé/réservé. Fin du script.")
                break

            print(f"Prochaine vérification dans {CONFIG['check_interval_sec']} secondes...")
            time.sleep(CONFIG["check_interval_sec"])

    except KeyboardInterrupt:
        print("\nInterrompu par l'utilisateur.")
    finally:
        input("\nAppuyez sur Entrée pour fermer le navigateur...")
        driver.quit()


if __name__ == "__main__":
    main()

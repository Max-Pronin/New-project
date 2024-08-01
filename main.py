import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
options = webdriver.ChromeOptions()
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.common import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException


driver = webdriver.Chrome()

driver.maximize_window()

# start_time = time.time()





# carta = input ("Введите ссылку:")
driver.get("http://service.emias.mosreg.ru/prod/medicalrecords/tappage/edit?ticket=71dtUBwQhoUIB%2Fuwe2nFc50iWH5IJun0Kh72OqL%2Fepf7ZeT4Ef%2FegT9jXMxFtgEri8rGp2caKngl2B8K244l3iNXRcaBEhssE7xNkrP1dTlnkRr%2Bgesazycbyk8oP298TigORSBorIes8Pi4ADtz8bx6%2BKqaWD41lq08iC%2Fc%2FOxOoz2DBH%2BUSdPfuhmkEwXIO5LaaNypXXP9Oa1QJ13VIaAe6reRGk8mGxOLdVuInqsBJkeozm3u9qBdicYcVrSnWmaLI%2FsEqz84ouoH5ecc3HTvKjc58A8GZPHMApASr0mjPZaA&mkabId=2830862&dvtId=0&DocPrvdId=3933&doctorId=doctorId%3D3933&doctorGuid=4867ca76-802c-4c45-862d-c820c48a6c4f&doctorTypeGuid=81d86a3b-2c5a-44b0-8ef9-48e34fbce21d&MisUrl=https:%2F%2Fmain.emias.mosreg.ru%2Fmis%2FKorolev_GB1&ReturnUrl=http:%2F%2Fmain.emias.mosreg.ru%2Fmis%2FKorolev_GB1%2FTap&examGuid=3f6a76ee-d41c-4c0a-89af-950b69d98b7b&emdTypeId=94&templateId=16&eventId=11569458&patientId=2830862&eventTypeGuid=523452F6-124E-4D63-94C4-012D71072FD3&patientTypeGuid=E804E486-D7A8-47A1-870D-56BA14D67AB8&recordTypeGuid=f4b78dc7-ebf3-ed11-9448-ee15cc7be9f9&medicalRecordId=0&backToSourceUrlName=Вернуться%20на%20главную&backToSourceUrl=%2Fdisp%2Fcard%2F1518849")
action = ActionChains(driver)

# OGIDANIE_OSMOTRA_SVERHU = WebDriverWait(driver, 7).until(EC.element_to_be_clickable("xpath", "//span[text()='Осмотр, исследование, иное медицинское мероприятие']"))
# KARTA_MEROPRIYTIY = WebDriverWait(driver, 7).until(EC.presence_of_element_located("xpath", "//h1[text()='Карта мероприятий']"))
# KARTA_MEROPRIYTIY2 = WebDriverWait(driver, 7).until(EC.element_to_be_clickable("xpath", "//h1[text()='Карта мероприятий']"))
# PROCENT_VUPOLNENIY = WebDriverWait(driver, 7).until(EC.presence_of_element_located("xpath", "//div[@mattooltip='Процент завершенности диспансеризации']"))
#
# time.sleep(1.5)
# Список элементов для поиска
# elements_to_click = [" Измерение насыщения крови кислородом (сатурация) в покое ", " Спирометрия или спирография "]


# for element_text in elements_to_click:
#     try:
#         driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#         element = WebDriverWait(driver, 3).until(EC.presence_of_element_located(By.XPATH, f"//div[contains(text(), '{element_text}')]"))
#         Если элемент найден, то выполняем действие
        # if driver.find_element("xpath", "//div[text()=' Измерение насыщения крови кислородом (сатурация) в покое ']").is_displayed():
        #     time.sleep(1.5)
        #     WebDriverWait(driver, 0.5).until(EC.element_to_be_clickable("xpath", "//div[text()=' Измерение насыщения крови кислородом (сатурация) в покое ']")).click()
        #     time.sleep(0.3)
        #     driver.find_element("xpath", "//input[@style='text-align: right;']").clear()
        #     time.sleep(0.3)
        #     WebDriverWait(driver, 4).until(EC.element_to_be_clickable("xpath", "//input[@style='text-align: right;']")).send_keys(PsO2)
        #     time.sleep(0.3)
        #     driver.execute_script("window.scrollBy(0, 100);")
        #     time.sleep(0.3)
        #     WebDriverWait(driver, 4).until(EC.element_to_be_clickable("xpath", "//label[text()=' Без отклонений ']")).click()
        #     time.sleep(0.3)
        #     print("сатурация заполнена")
    # except:
    #     print(f"Элемент '{element_text}' не найден")

# time.sleep(1.5)
#
# OGIDANIE_OSMOTRA_SVERHU
# time.sleep(0.3)
# driver.execute_script("window.scrollTo(0, 0);")
# KARTA_MEROPRIYTIY
# time.sleep(0.3)
# KARTA_MEROPRIYTIY2
# time.sleep(0.3)
# print(PROCENT_VUPOLNENIY.text)
# time.sleep(0.5)

# Анкетирование выявления постковидного COVID-19 синдрома
# if " Анкетирование выявления постковидного COVID-19 синдрома " = 1:
#     WebDriverWait(driver, 7).until(EC.element_to_be_clickable(("xpath", "//div[text()=' Анкетирование выявления постковидного COVID-19 синдрома ']"))).click()
#     time.sleep(1.5)
#     driver.find_element("xpath", "//html/body/app-root/ng-component/div/main/app-disp/div/disp-card-edit/card-disp/div[1]/form/app-disp-exams-map/div[2]/div[2]/div[2]/div/app-exam/div/div[3]/div[2]/div/app-medical-records-block/st-expansion-panel/div/div/div[2]/app-st-table/div/table/tbody/tr[1]/td[1]/div/div[1]/button/a").click()
#     time.sleep(2.5)
#     WebDriverWait(driver, 7).until((EC.element_to_be_clickable(("xpath", "//button[text()=' Просмотреть ']")))).click()
#     time.sleep(2.5)
#     WebDriverWait(driver, 7).until(EC.presence_of_element_located(("xpath", "//button[text()=' Подписать и отправить ']")))
#     time.sleep(0.3)
#     WebDriverWait(driver, 7).until((EC.element_to_be_clickable(("xpath", "//button[text()=' Подписать и отправить ']")))).click()
#     time.sleep(2)
#     WebDriverWait(driver, 7).until(EC.presence_of_element_located(("xpath", "//button[text()=' Закрыть ']"))).click()
#     OGIDANIE_OSMOTRA_SVERHU
#     time.sleep(0.5)
#     WebDriverWait(driver, 7).until(EC.presence_of_element_located(("xpath", "//div[text()=' Анкетирование выявления постковидного COVID-19 синдрома ']")))
#     time.sleep(0.2)
#     WebDriverWait(driver, 7).until(EC.element_to_be_clickable(("xpath", "//div[text()=' Анкетирование выявления постковидного COVID-19 синдрома ']"))).click()
#     time.sleep(0.2)
#     WebDriverWait(driver, 7).until(EC.presence_of_element_located(("xpath", "//html/body/app-root/ng-component/div/main/app-disp/div/disp-card-edit/card-disp/div[1]/form/app-disp-exams-map/div[2]/div[2]/div[2]/div/app-exam/div/div[3]/div[2]/div/app-medical-records-block/st-expansion-panel/div/div/div[2]/app-st-table/div/table/tbody/tr[3]/td[1]/div/div[1]/button/a")))
#     time.sleep(0.2)
#     WebDriverWait(driver, 4).until(EC.element_to_be_clickable(("xpath", "//html/body/app-root/ng-component/div/main/app-disp/div/disp-card-edit/card-disp/div[1]/form/app-disp-exams-map/div[2]/div[2]/div[2]/div/app-exam/div/div[3]/div[2]/div/app-medical-records-block/st-expansion-panel/div/div/div[2]/app-st-table/div/table/tbody/tr[3]/td[1]/div/div[1]/button/a"))).click()
#     time.sleep(2)
#     WebDriverWait(driver, 7).until(EC.presence_of_element_located(("xpath", "//button[text()=' Просмотреть ']"))).click()
#     time.sleep(1.5)
#     WebDriverWait(driver, 7).until(EC.presence_of_element_located(("xpath", "//button[text()=' Подписать и отправить ']"))).click()
#     time.sleep(1.5)
#     WebDriverWait(driver, 7).until(EC.presence_of_element_located(("xpath", "//button[text()=' Закрыть ']"))).click()
#     time.sleep(0.5)
#     WebDriverWait(driver, 4).until(EC.element_to_be_clickable(("xpath", "//div[text()=' Анкетирование выявления постковидного COVID-19 синдрома ']"))).click()
#     time.sleep(1.5)
#     driver.execute_script("window.scrollBy(0, 100);")
#     time.sleep(0.2)
#     WebDriverWait(driver, 4).until(EC.element_to_be_clickable(("xpath", "//label[text()=' Без отклонений ']"))).click()
#     time.sleep(0.5)
#     print("Анкетирование COVID-19 заполнено")
#
# сатурация
# if ' Измерение насыщения крови кислородом (сатурация) в покое ' > 1:
#     WebDriverWait(driver, 0.5).until(EC.element_to_be_clickable(("xpath", "//div[text()=' Измерение насыщения крови кислородом (сатурация) в покое ']"))).click()
#     time.sleep(0.3)
#     driver.find_element("xpath", "//input[@style='text-align: right;']").clear()
#     time.sleep(0.3)
#     WebDriverWait(driver, 4).until(EC.element_to_be_clickable(("xpath", "//input[@style='text-align: right;']"))).send_keys(PsO2)
#     time.sleep(0.3)
#     driver.execute_script("window.scrollBy(0, 100);")
#     time.sleep(0.3)
#     WebDriverWait(driver, 4).until(EC.element_to_be_clickable(("xpath", "//label[text()=' Без отклонений ']"))).click()
#     time.sleep(0.3)
#     print("сатурация заполнена")
#
#
# action.move_to_element(driver.find_element("xpath", "//span[text()='Создать пакет направлений']")).perform()
# driver.execute_script("window.scrollBy(0, 500);")
# driver.find_element("xpath", "//span[text()='Создать пакет направлений']").click()

# Невыполненные мероприятия
# WebDriverWait(driver, 4).until(EC.element_to_be_clickable(("xpath", "//label[text()='Невыполненные мероприятия']")))
# time.sleep(0.5)
# driver.find_element("xpath", "//label[text()='Невыполненные мероприятия']").click()
# time.sleep(0.5)

# открытие ВСД, 15/15 и закрытие
# if driver.find_element("xpath","//div[text()=' Измерение внутриглазного давления ']").is_displayed():
#    WebDriverWait(driver, 4).until(EC.element_to_be_clickable(("xpath", "//div[text()=' Измерение внутриглазного давления ']"))).click()
#    print("=> Внутриглазное давление")
#    time.sleep(0.8)
#    WebDriverWait(driver, 4).until(EC.element_to_be_clickable(("xpath", "//input[@style='text-align: right;']")))
#    driver.find_element("xpath","//input[@style='text-align: right;']").send_keys("15")
#    ActionChains(driver).send_keys(Keys.TAB).send_keys("15").perform()
#    driver.find_element("xpath","//label[text()=' Без отклонений ']").click()
#    time.sleep(0.5)
#    driver.find_element("xpath","//button[text()='Сохранить']").click()
# time.sleep(2.5)

# end_time = time.time()
# result = end_time - start_time
# print(result)

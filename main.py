import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver import Keys
options = webdriver.ChromeOptions()
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get('http://service.emias.mosreg.ru/prod/medicalrecords/tappage/edit?ticket=QukiD91ac69oZrUZGwQBSnsXvNoiMKkmXI95d2jaEJhfcIc%2FlRuD36A5BvAC3iyRACCpxxwxXj928FAIypP9CGWvJvZgEMOnyrGkrryLYz3b3pVWQN74ceiX99Im41X4Lx%2FIo2EHJ0vND1lQZiRmz1Apk7vkI0Zs%2FHivJTtFheaoVWhOrmW93BIo4PN%2B0ZUdqkXV1QBUAPo1931TiiHHMUEPzHBHEhWOJSXrNrh7eYTV7c%2Fg0Olod22wnQBuC7T05JuCYJ9mkiToHi9QjeO4e7xmpPpWDglpa0kM8MyOJMoawG1u&mkabId=2830862&dvtId=0&DocPrvdId=3933&doctorId=doctorId%3D3933&doctorGuid=4867ca76-802c-4c45-862d-c820c48a6c4f&doctorTypeGuid=81d86a3b-2c5a-44b0-8ef9-48e34fbce21d&MisUrl=https:%2F%2Fmain.emias.mosreg.ru%2Fmis%2FKorolev_GB1&ReturnUrl=http:%2F%2Fmain.emias.mosreg.ru%2Fmis%2FKorolev_GB1%2FTap&examGuid=3f6a76ee-d41c-4c0a-89af-950b69d98b7b&emdTypeId=94&templateId=16&eventId=11569458&patientId=2830862&eventTypeGuid=523452F6-124E-4D63-94C4-012D71072FD3&patientTypeGuid=E804E486-D7A8-47A1-870D-56BA14D67AB8&recordTypeGuid=f4b78dc7-ebf3-ed11-9448-ee15cc7be9f9&medicalRecordId=0&backToSourceUrlName=Вернуться%20на%20главную&backToSourceUrl=%2Fdisp%2Fcard%2F1518849')

time.sleep(3)
driver.find_element("xpath", "//span[@id='spanMU7']").click()
# WebDriverWait(driver, 0.5).until(EC.element_to_be_clickable("xpath", "//span[@id='spanMU7']")).click()
time.sleep(3)


from selenium import webdriver
from test_locators import locator
#from login_page import login
#from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from time import sleep
driver = webdriver.Chrome("//venv/bin/chromedriver")

driver.get("http://167.172.129.57/login?redirect=%2F")
# driver.get("http://157.230.179.140/login")
driver.maximize_window()
try:
    sleep(10)

    driver.find_element(By.XPATH, locator.login_drop).click()
    driver.find_element(By.XPATH,locator.user_name).send_keys("admin.super")
    driver.find_element(By.XPATH, locator.password).send_keys("conor")
    driver.find_element(By.XPATH, locator.login_button).click()
    sleep(6)
    driver.find_element(By.XPATH, locator.user_management_icon).click()
    sleep(6)
    driver.find_element(By.XPATH, locator.application_role).click()
    sleep(6)
    # driver.find_element(By.XPATH, locator.add).click()
    # sleep(6)
    # driver.find_element(By.XPATH, locator.add_field).click()
    # sleep(6)
    # driver.find_element(By.XPATH, locator.add_dropdown_value1).click()
    # sleep(6)
    # driver.find_element(By.XPATH, locator.add_dropdown_value2).click()
    # sleep(6)
    # driver.find_element(By.XPATH, locator.add_dropdown_value3).click()
    # sleep(6)
    # driver.find_element(By.XPATH, locator.add_dropdown_closure).click()
    # sleep(6)
    # driver.find_element(By.XPATH, locator.add_name).send_keys("TestU")
    # sleep(6)
    # driver.find_element(By.XPATH, locator.add_description).send_keys("Tester")
    # sleep(5)
    # driver.find_element(By.XPATH,locator.add_continue).click()
    # sleep(8)
    # driver.find_element(By.XPATH, locator.add_keyword_search).send_keys("Compliance")
    # sleep(5)
    # driver.find_element(By.XPATH, locator.permission_option1).click()
    # sleep(10)
    # driver.find_element(By.XPATH, locator.permission_option1_selection).click()
    # sleep(10)
    # driver.find_element(By.XPATH, locator.clear_search).click()
    # sleep(10)
    # driver.find_element(By.XPATH, locator.add_keyword_search).send_keys("Meeting")
    # sleep(10)
    # driver.find_element(By.XPATH, locator.permission_option2).click()
    # sleep(10)
    # driver.find_element(By.XPATH, locator.permission_option2_selection).click()
    # sleep(10)
    # driver.find_element(By.XPATH, locator.clear_search).click()
    # sleep(10)
    # driver.find_element(By.XPATH, locator.add_keyword_search).send_keys("Change")
    # sleep(10)
    # driver.find_element(By.XPATH, locator.permission_option3).click()
    # sleep(10)
    # driver.find_element(By.XPATH, locator.permission_option3_selection).click()
    # sleep(10)
    # driver.find_element(By.XPATH, locator.add_finalize).click()
    # sleep(10)
    driver.find_element(By.XPATH, locator.dashboard_search).click()
    # sleep(5)
    driver.find_element(By.XPATH, locator.dashboard_search).send_keys("Automation")
    sleep(10)
    # driver.find_element(By.XPATH, locator.dashboard_export).click()
    # sleep(10)
    # driver.find_element(By.XPATH, locator.export_pdf).click()
    # sleep(10)
    # driver.find_element(By.XPATH, locator.dashboard_export).click()
    # sleep(10)
    # driver.find_element(By.XPATH, locator.export_excel).click()
    # sleep(10)
    # driver.find_element(By.XPATH, locator.dashboard_filter).click()
    # sleep(10)
    # driver.find_element(By.XPATH, locator.filter_column).click()
    # sleep(10)
    # driver.find_element(By.XPATH, locator.filter_column).click()
    # sleep(10)
    # driver.find_element(By.XPATH, locator.filter_value).click()
    # sleep(10)
    # driver.find_element(By.XPATH, locator.filter_operator).click()
    # sleep(10)
    # driver.find_element(By.XPATH, locator.operator_value1).click()
    # sleep(10)
    # driver.find_element(By.XPATH,locator.value).send_keys("Test")
    # sleep(10)
    # driver.find_element(By.XPATH, locator.filter_add).click()
    # sleep(10)
    # driver.find_element(By.XPATH, locator.filter_column).click()
    # sleep(10)
    # driver.find_element(By.XPATH, locator.filter_column).click()
    # sleep(10)
    # driver.find_element(By.XPATH, locator.filter_value).click()
    # sleep(10)
    # driver.find_element(By.XPATH, locator.filter_operator).click()
    # sleep(10)
    # driver.find_element(By.XPATH, locator.operator_value2).click()
    # sleep(10)
    # driver.find_element(By.XPATH, locator.value).send_keys("Vendor")
    # sleep(10)
    # driver.find_element(By.XPATH, locator.filter_add).click()
    # sleep(10)
    # driver.find_element(By.XPATH, locator.apply_filter).click()
    # sleep(10)
    # driver.find_element(By.XPATH, locator.clear_filter).click()
    sleep(10)
    driver.find_element(By.XPATH, locator.page_selection).click()
    sleep(10)
    driver.find_element(By.XPATH, locator.page_selection_value1).click()
    sleep(10)









    # driver.find_element(By.XPATH, locator.department).click()
    # sleep(6)
    # driver.find_element(By.XPATH, locator.application_user).click()
    # sleep(6)
    # driver.find_element(By.XPATH, locator.user_group).click()
    # sleep(6)
    # driver.find_element(By.XPATH, locator.settings).click()
    # sleep(6)
    # driver.find_element(By.XPATH, locator.scorecard_parameters).click()
    # sleep(6)
    # driver.find_element(By.XPATH, locator.scorecard).click()
    # sleep(6)
    # driver.find_element(By.XPATH, locator.home_icon).click()
    # sleep(6)
    # driver.find_element(By.XPATH, locator.vendor_compliance_icon).click()
    # sleep(6)
    # driver.find_element(By.XPATH, locator.suppliers).click()
    # sleep(6)
    # driver.find_element(By.XPATH, locator.factory).click()
    # sleep(6)
    # driver.find_element(By.XPATH, locator.evaluation).click()
    # sleep(6)
    # driver.find_element(By.XPATH, locator.audit).click()
    # sleep(6)
    # driver.find_element(By.XPATH, locator.audit_configuration).click()
    # sleep(6)
    # driver.find_element(By.XPATH,locator.severity_level).click()
    # sleep(6)
    # driver.find_element(By.XPATH, locator.evaluation).click()
    # sleep(6)
    # driver.find_element(By.XPATH, locator.audit).click()
    # sleep(6)
    # driver.find_element(By.XPATH, locator.audit_configuration).click()
    # sleep(6)
    # driver.find_element(By.XPATH, locator.rating_system).click()
    # sleep(6)
    # driver.find_element(By.XPATH, locator.evaluation).click()
    # sleep(6)
    # driver.find_element(By.XPATH, locator.audit).click()
    # sleep(6)
    # driver.find_element(By.XPATH, locator.audit_configuration).click()
    # sleep(6)
    # driver.find_element(By.XPATH, locator.audit_tempelate).click()
    # sleep(6)
    # driver.find_element(By.XPATH, locator.setting_s).click()
    # sleep(6)
    # driver.find_element(By.XPATH,locator.agency).click()
    # sleep(6)
    # driver.find_element(By.XPATH,locator.certification).click()
    # sleep(6)
    # driver.find_element(By.XPATH,locator.document_sec).click()
    # sleep(6)
    # driver.find_element(By.XPATH,locator.document).click()
    # sleep(6)
    # driver.find_element(By.XPATH,locator.entity).click()
    # sleep(6)
    # driver.find_element(By.XPATH,locator.att_type).click()
    # sleep(6)
    # driver.find_element(By.XPATH,locator.green_attribute).click()
    # sleep(6)
    # driver.find_element(By.XPATH,locator.material_type).click()
    driver.close()
    driver.quit()
except Exception as e:
    print(e)









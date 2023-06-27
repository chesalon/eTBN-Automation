from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
from datetime import datetime
import pyautogui


s = Service("C:/Selenium/selenium-java-3.141.59/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=s)

driver.maximize_window()
driver.delete_all_cookies()
driver.get("https://marketplace.etbn.online/login")


class eTBN_Hub():
############################## LOGIN ##############################
    print("eTBN Hub admin \n")
# Enter username
    try:
        driver.find_element(By.ID, "loginid").send_keys("admin@admin.com")
    except NoSuchElementException:   
        print("Error: The element ID 'loginid' does not exist.") 
    else:
        print("Enter Username : admin@admin.com  -  SUCCESS")

# Enter Password
    try:
        driver.find_element(By.ID, "password").send_keys("123321")
    except NoSuchElementException:   
        print("Error: The element ID 'password' does not exist.") 
    else:
        print("Enter Password : 123321  -  SUCCESS")

# Click login button
    try:
        driver.find_element(By.CSS_SELECTOR, ".v-btn--is-elevated > .v-btn__content").click()
    except NoSuchElementException:   
        print("Error: CSS '.v-btn--is-elevated > .v-btn__content' does not exist.") 
    else:
        print("Click on LOGIN button  -  SUCCESS")
        print("User SUCCESSFULLY loggedin \n")
    time.sleep(10)

############################## ORGANIZATION ##############################
# Navigates to Organizations
    try:
        driver.find_element(By.ID, "title-Organizations").click()
    except NoSuchElementException:   
        print("Error: The element ID 'title-Collections' does not exist.") 
    else:
        print("Click on Organizations and navigates to the Organizations page  -  SUCCESS")
        time.sleep(4)

# Click on New Organization button
    try:
        driver.find_element(By.CSS_SELECTOR, "#btnNew > .v-btn__content").click()
    except NoSuchElementException:   
        print("Error: The element ID 'password' does not exist.") 
    else:
        print("Click on New Organization button  -  SUCCESS")
        time.sleep(1)

##### Add a new Organization #####
# Enter Organization Name
    try:
        driver.find_element(By.ID, "OrgName").send_keys("Organization 001")
    except NoSuchElementException:   
        print("Error: The element ID 'OrgName' does not exist.") 
    else:
        print("Enter Organization Name : Organization 001  -  SUCCESS")
        time.sleep(1)

# Enter Organization Description
    try:
        driver.find_element(By.ID, "description").send_keys("Test Organization")
    except NoSuchElementException:   
        print("Error: The element ID 'description' does not exist.") 
    else:
        print("Enter Organization Description : Test Organization  -  SUCCESS")
        time.sleep(1)

# Click on Country dropdown
    try:
        driver.find_element(By.ID, "Country").click()
    except NoSuchElementException:   
        print("Error: The element ID 'Country' does not exist.") 
    else:
        print("Click on select country dropbox  -  SUCCESS")
        time.sleep(2)    

# Select Country
    try:
        driver.find_element(By.XPATH, "//div[(text() = 'Albania' or . = 'Albania')]").click()
    except NoSuchElementException:   
        print("Error: Xpath '//div[(text() = 'Albania' or . = 'Albania')]' does not exist.") 
    else:
        print("Select Country Albania  -  SUCCESS")
    time.sleep(2)

# Enter Organization User Limit
    try:
        driver.find_element(By.ID, "userLimit").send_keys("50")
    except NoSuchElementException:   
        print("Error: The element ID 'userLimit' does not exist.") 
    else:
        print("Enter Organization User Limit : 50  -  SUCCESS")
        time.sleep(2)

# Click on Save button
    try:
        driver.find_element(By.ID, "btnSave").click()
    except NoSuchElementException:   
        print("Error: The element ID 'btnSave' does not exist.") 
    else:
        print("Click on Organization SAVE button  -  SUCCESS")
        print("Organization SUCCESSFULLY Saved \n")
        time.sleep(3)

##### Search Organization #####
# Search organization by name 
    try:
        driver.find_element(By.ID, "textSearch").send_keys("Test Organization")
        time.sleep(1)
        pyautogui.press('enter')
    except NoSuchElementException:   
        print("Error: The element ID 'textSearch' does not exist.") 
    else:
        print("Enter Search Result : Test Organization  -  SUCCESS")
        print("Display Search Result  -  SUCCESS \n")
        time.sleep(2)

##### Delete Organization #####
    try:
        driver.find_element(By.CSS_SELECTOR, "button.v-icon.notranslate.mr-2.icon-delete.v-icon--link.mdi.mdi-delete.theme--light").click()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, "button.v-btn.v-btn--is-elevated.v-btn--has-bg.theme--light.v-size--default.error").click()
    except NoSuchElementException:   
        print("Error: Delete button element does not exist.") 
    else:
        print("Organization SUCCESSFULLY Deleted \n")
        time.sleep(5)

############################## USERS ##############################
# Navigates to Users
    try:
        driver.find_element(By.ID, "content-user").click()
    except NoSuchElementException:   
        print("Error: The element ID 'content-user' does not exist.") 
    else:
        print("Click on Users and navigates to the Users page  -  SUCCESS")
        time.sleep(4)

# Click on New Users button
    try:
        driver.find_element(By.ID, "btnNew").click()
    except NoSuchElementException:   
        print("Error: The element ID 'btnNew' does not exist.") 
    else:
        print("Click on New Ùsers button  -  SUCCESS")
        time.sleep(5)

# Add a new User
# Enter first name
    try:
        driver.find_element(By.ID, "firstName").send_keys("Test")
    except NoSuchElementException:   
        print("Error: The element ID 'firstName' does not exist.") 
    else:
        print("Enter First Name : Test  -  SUCCESS")
        time.sleep(1)

# Enter last name
    try:
        driver.find_element(By.ID, "lastName").send_keys("User")
    except NoSuchElementException:   
        print("Error: The element ID 'lastName' does not exist.") 
    else:
        print("Enter Last Name : User  -  SUCCESS")
        time.sleep(1)

# Enter email
    try:
        driver.find_element(By.ID, "email").send_keys("testuser@chesalon.com")
    except NoSuchElementException:   
        print("Error: The element ID 'email' does not exist.") 
    else:
        print("Enter Email Address : testuser@chesalon.com  -  SUCCESS")
        time.sleep(1)
        
# Enter phone no
    try:
        driver.find_element(By.ID, "phone").send_keys("0123654789")
    except NoSuchElementException:   
        print("Error: The element ID 'phone' does not exist.") 
    else:
        print("Enter Phone No : 0123654789  -  SUCCESS")
        time.sleep(1)

# Enter password hint
    try:
        driver.find_element(By.ID, "passwordHint").send_keys("123321")
    except NoSuchElementException:   
        print("Error: The element ID 'passwordHint' does not exist.") 
    else:
        print("Enter Password Hint : 123321  -  SUCCESS")
        time.sleep(1)

# Enter password
    try:
        driver.find_element(By.ID, "password").send_keys("123321")
    except NoSuchElementException:   
        print("Error: The element ID 'password' does not exist.") 
    else:
        print("Enter Password : 123321  -  SUCCESS")
        time.sleep(1)

# Click on user type
    try:
        driver.find_element(By.ID, "userRole").click()
    except NoSuchElementException:   
        print("Error: The element ID 'userRole' does not exist.") 
    else:
        print("Click on User Type Dropox  -  SUCCESS")
        time.sleep(2)

# Select user type
    try:
        driver.find_element(By.XPATH, "//div[(text() = 'Hub Admin' or . = 'Hub Admin')]").click()
    except NoSuchElementException:   
        print("Error: Xpath '//div[(text() = 'Hub Admin' or . = 'Hub Admin')]' does not exist.") 
    else:
        print("Select Hub Admin  -  SUCCESS")
        time.sleep(2)
        
# Click on Save button
    try:
        driver.find_element(By.ID, "btnSave").click()
    except NoSuchElementException:   
        print("Error: The element ID 'btnSave' does not exist.") 
    else:
        print("Click on User SAVE button  -  SUCCESS")
        print("User SUCCESSFULLY Saved \n")
        time.sleep(3)

##### Search User #####
# Search user by email 
    try:
        driver.find_element(By.ID, "search").send_keys("testautomation@chesalon.com")
        time.sleep(1)
        pyautogui.press('enter')
    except NoSuchElementException:   
        print("Error: The element ID 'search' does not exist.") 
    else:
        print("Enter Search Result : testautomation@chesalon.com  -  SUCCESS")
        print("Display Search Result  -  SUCCESS \n")
        time.sleep(2)

##### Delete Organization #####
    try:
        driver.find_element(By.CSS_SELECTOR, "button.v-icon.notranslate.mr-2.icon-delete.v-icon--link.mdi.mdi-delete.theme--light").click()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, "button.v-btn.v-btn--is-elevated.v-btn--has-bg.theme--light.v-size--default.error").click()
    except NoSuchElementException:   
        print("Error: Delete button element does not exist. \n") 
    else:
        print("User SUCCESSFULLY Deleted \n")
        time.sleep(5)

############################## COLLECTIONS ##############################
# Navigates to Collections
    try:
        driver.find_element(By.ID, "title-Collections").click()
    except NoSuchElementException:   
        print("Error: The element ID 'title-Collections' does not exist.") 
    else:
        print("Click on Collections and navigates to the Collections page  -  SUCCESS")
        time.sleep(4)

# Click on New Collection button
    try:
        driver.find_element(By.ID, "btnNew").click()
    except NoSuchElementException:   
        print("Error: The element ID 'btnNew' does not exist.") 
    else:
        print("Click on New Collection button  -  SUCCESS")
        time.sleep(5)

# Add a new Collection
# Enter Collection Name
    try:
        driver.find_element(By.ID, "name").send_keys("Collection 001")
    except NoSuchElementException:   
        print("Error: The element ID 'name' does not exist.") 
    else:
        print("Enter Collection Name : Collection 001  -  SUCCESS")
        time.sleep(1)

# Enter Collection Description
    try:
        driver.find_element(By.ID, "description").send_keys("Test Collection")
    except NoSuchElementException:   
        print("Error: The element ID 'description' does not exist.") 
    else:
        print("Enter Collection Descripion : Test Collection  -  SUCCESS")
        time.sleep(1)

# Select Publications
    try:
        driver.find_element(By.CSS_SELECTOR, "#btnAddNew18 .v-icon").click()
    except NoSuchElementException:   
        print("Error: CSS '#btnAddNew18 .v-icon' does not exist.") 
    else:
        print("Select a Publication  -  SUCCESS")
    time.sleep(2)

    try:
        driver.find_element(By.CSS_SELECTOR, "#btnAddNew19 .v-icon").click()
    except NoSuchElementException:   
        print("Error: CSS '#btnAddNew19 .v-icon' does not exist.") 
    else:
        print("Select a Publication  -  SUCCESS")
        time.sleep(2)

    try:
        driver.find_element(By.CSS_SELECTOR, "#btnAddNew16 .v-icon").click()
    except NoSuchElementException:   
        print("Error: CSS '#btnAddNew16 .v-icon' does not exist.") 
    else:
        print("Select a Publication  -  SUCCESS")
        time.sleep(2)

# Click on SAVE bitton
    try:
        driver.find_element(By.CSS_SELECTOR, "#btnSave > .v-btn__content").click()
    except NoSuchElementException:   
        print("Error: CSS '#btnSave > .v-btn__content' does not exist.") 
    else:
        print("Click on Collection SAVE button  -  SUCCESS")
        print("Collection SUCCESSFULLY Saved \n")
        time.sleep(5)

##### Search Collection #####
# Search collection by name 
    try:
        driver.find_element(By.ID, "Search").send_keys("Collection 001")
        time.sleep(1)
        pyautogui.press('enter')
    except NoSuchElementException:   
        print("Error: The element ID 'Search' does not exist.") 
    else:
        print("Enter Search Result : Collection 001  -  SUCCESS")
        print("Display Search Result  -  SUCCESS \n")
        time.sleep(2)

##### Delete collection #####
    try:
        driver.find_element(By.CSS_SELECTOR, "button.v-icon.notranslate.mr-2.icon-delete.v-icon--link.mdi.mdi-delete.theme--light").click()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, "button.v-btn.v-btn--is-elevated.v-btn--has-bg.theme--light.v-size--default.error").click()
    except NoSuchElementException:   
        print("Error: Delete button element does not exist.") 
    else:
        print("Collection SUCCESSFULLY Deleted \n")
        time.sleep(5)

############################## Fulfillment eBooks ##############################
# Navigates to Fulfillment eBooks
    try:
        driver.find_element(By.ID, "content-Fulfillment").click()
    except NoSuchElementException:   
        print("Error: The element ID 'content-Fulfillment' does not exist.") 
    else:
        print("Click on Fulfillment  -  SUCCESS")
        time.sleep(1)

    try:
        driver.find_element(By.ID, "content-Fulfillment-eBooks").click()
    except NoSuchElementException:   
        print("Error: The element ID 'content-Fulfillment-eBooks' does not exist.") 
    else:
        print("Click on eBooks and navigates to the eBooks fulfillment  -  SUCCESS")
        time.sleep(2)

# Click on New eBooks fulfillment button
    try:
        driver.find_element(By.ID, "btnNew").click()
    except NoSuchElementException:   
        print("Error: The element ID 'btnNew' does not exist.") 
    else:
        print("Click on New eBooks fulfillment button  -  SUCCESS")
        time.sleep(5)

##### Search Publication to purchase #####
# Search Publication by name 
    try:
        driver.find_element(By.ID, "avaliiableApplicationsSearch").send_keys("Everyday God")
        time.sleep(1)
        pyautogui.press('enter')
    except NoSuchElementException:   
        print("Error: The element ID 'avaliiableApplicationsSearch' does not exist.") 
    else:
        print("Enter Search Result : Everyday God  -  SUCCESS")
        print("Display Search Result  -  SUCCESS \n")
        time.sleep(3)

# Click on Organization list
    try:
        driver.find_element(By.ID, "organizationList").click()
    except NoSuchElementException:   
        print("Error: The element ID 'organizationList' does not exist.") 
    else:
        print("Click on organization list  -  SUCCESS")
        time.sleep(1)

# Select Organization
    try:
        driver.find_element(By.XPATH, "//div[(text() = 'Chesalon' or . = 'Chesalon')]").click()
    except NoSuchElementException:   
        print("Error: The xpath '//div[(text() = 'Chesalon' or . = 'Chesalon')]' does not exist.") 
    else:
        print("Select organization  -  SUCCESS")
        time.sleep(2)
        
# Click on transaction type
    try:
        driver.find_element(By.ID, "purchaseTypeList").click()
    except NoSuchElementException:   
        print("Error: The element ID 'purchaseTypeList' does not exist.") 
    else:
        print("Click on transaction type  -  SUCCESS")
        time.sleep(2)

# Select transaction type
    try:
        driver.find_element(By.XPATH, "//div[(text() = 'Rental 30 days' or . = 'Rental 30 days')]").click()
    except NoSuchElementException:   
        print("Error: The element ID '//div[(text() = 'Rental 30 days' or . = 'Rental 30 days')]' does not exist.") 
    else:
        print("Select transaction type  -  SUCCESS")
        time.sleep(2)

# Ènter no of copies
    try:
        driver.find_element(By.ID, "noOfCopiesQuality").send_keys("5")
    except NoSuchElementException:   
        print("Error: The element ID 'noOfCopiesQuality' does not exist.") 
    else:
        print("Enter No of Copies : 5  -  SUCCESS")
        time.sleep(2)
        
# Click on add to cart button
    try:
        driver.find_element(By.CSS_SELECTOR, "span.v-btn__content > i.v-icon.notranslate.mdi.mdi-cart.theme--light").click()
    except NoSuchElementException:   
        print("Error: The CSS 'span.v-btn__content > i.v-icon.notranslate.mdi.mdi-cart.theme--light' does not exist.") 
    else:
        print("Add to Cart  -  SUCCESS")
        time.sleep(2)

# Click on Next button
    try:
        driver.find_element(By.CSS_SELECTOR, "div.col.d-flex.justify-end > button.v-btn.v-btn--is-elevated.v-btn--has-bg.theme--light.v-size--default.primary").click()
    except NoSuchElementException:   
        print("Error: The Xpath 'div.col.d-flex.justify-end > button.v-btn.v-btn--is-elevated.v-btn--has-bg.theme--light.v-size--default.primary' does not exist.") 
    else:
        print("Click Next button  -  SUCCESS")
        time.sleep(2)

# Review purchased pubs and click on Next button
    try:
        driver.find_element(By.ID, "btnNext").click()
    except NoSuchElementException:   
        print("Error: The Xpath 'btnNext' does not exist.") 
    else:
        print("Review purchased publications and Click Next button  -  SUCCESS")
        time.sleep(2)

# Select current date
    try:
        #current_date = datetime.now()

        driver.find_element(By.ID, "DateOfPayment").send_keys("2023-06-09")
    except NoSuchElementException:   
        print("Error: The element ID 'DateOfPayment' does not exist.") 
    else:
        print("Date of payment selected  -  SUCCESS \n")
        time.sleep(4)

############################## Logout ##############################
# Click on user name
    try:
        driver.find_element(By.CSS_SELECTOR, "button.ml-2.mr-2.v-btn.v-btn--text.theme--dark.v-size--default").click()
    except NoSuchElementException:   
        print("Error: The CSS 'button.ml-2.mr-2.v-btn.v-btn--text.theme--dark.v-size--default' does not exist.") 
    else:
        print("Click on user name  -  SUCCESS")
        time.sleep(1)

# Click on logout
    try:
        driver.find_element(By.XPATH, "//div[(text() = 'Log out' or . = 'Log out')]").click()
    except NoSuchElementException:   
        print("Error: The CSS '//div[(text() = 'Log out' or . = 'Log out')]' does not exist.") 
    else:
        print("Click on Logout button  -  SUCCESS")
        print("User SUCCESSFULLY logout\n\n")
        time.sleep(4)



class eTBN_Portal():
############################## LOGIN ##############################
    print("eTBN Portal Admin \n")
# Enter username
    try:
        driver.find_element(By.ID, "loginid").send_keys("portaladmin@chesalon.com")
    except NoSuchElementException:   
        print("Error: The element ID 'loginid' does not exist.") 
    else:
        print("Enter Username : portaladmin@chesalon.com  -  SUCCESS")

# Enter Password
    try:
        driver.find_element(By.ID, "password").send_keys("123321")
    except NoSuchElementException:   
        print("Error: The element ID 'password' does not exist.") 
    else:
        print("Enter Password : 123321  -  SUCCESS")

# Click login button
    try:
        driver.find_element(By.CSS_SELECTOR, ".v-btn--is-elevated > .v-btn__content").click()
    except NoSuchElementException:   
        print("Error: CSS '.v-btn--is-elevated > .v-btn__content' does not exist.") 
    else:
        print("Click on LOGIN button  -  SUCCESS")
        print("User SUCCESSFULLY loggedin \n")
    time.sleep(10)

    ############################## PUBLICATIONS ##############################
    # Click on Publications
    try:
        driver.find_element(By.CSS_SELECTOR, "button.v-icon.notranslate.v-treeview-node__toggle.v-icon--link.mdi.mdi-menu-down.theme--light").click()
    except NoSuchElementException:   
        print("Error: The CSS 'button.v-icon.notranslate.v-treeview-node__toggle.v-icon--link.mdi.mdi-menu-down.theme--light' does not exist.") 
    else:
        print("Click on Publications  -  SUCCESS")
        time.sleep(1)

    # Click on My Publications
    try:
        driver.find_element(By.ID, "a-Publications-MyPublications").click()
    except NoSuchElementException:   
        print("Error: The ID 'a-Publications-MyPublications' does not exist.") 
    else:
        print("Click on My Publications  -  SUCCESS")
        time.sleep(5)
        
    # Search Publications
    try:
        driver.find_element(By.ID, "search").send_keys("Everyday God")
        time.sleep(1)
        pyautogui.press('enter')
    except NoSuchElementException:   
        print("Error: The ID 'search' does not exist.") 
    else:
        print("Enter Search Result : Everyday God  -  SUCCESS")
        print("Display Search Result  -  SUCCESS")
        time.sleep(4)
    
    # Click My Publication Detailview button
    try:
        driver.find_element(By.CSS_SELECTOR, "button.v-icon.notranslate.v-icon--link.mdi.mdi-domain.theme--light.blue--text.text--darken-2").click()
    except NoSuchElementException:   
        print("Error: The CSS 'button.v-icon.notranslate.v-icon--link.mdi.mdi-domain.theme--light.blue--text.text--darken-2' does not exist.") 
    else:
        print("Click My Publication Detail View Button  -  SUCCESS")
        print("Popup and Display Publication metadata  -  SUCCESS")
        time.sleep(2)

    # Close publication metadata popup
    try:
        driver.find_element(By.CSS_SELECTOR, "button.v-btn.v-btn--text.theme--light.v-size--default.primary--text > span.v-btn__content").click()
    except NoSuchElementException:   
        print("Error: The CSS 'button.v-btn.v-btn--text.theme--light.v-size--default.primary--text > span.v-btn__content' does not exist.") 
    else:
        print("Close publication metadata popup  -  SUCCESS \n")
        time.sleep(4)


############################## COLLECTIONS ##############################
    # Click on Collections
    try:
        driver.find_element(By.XPATH, "(//button[@type='button'])[4]").click()
    except NoSuchElementException:   
        print("Error: The CSS '(//button[@type='button'])[4]' does not exist.") 
    else:
        print("Click on Collections  -  SUCCESS")
        time.sleep(1)

    # Click on Core Collections
    try:
        driver.find_element(By.ID, "a-Collections").click()
    except NoSuchElementException:   
        print("Error: The ID 'a-Collections' does not exist.") 
    else:
        print("Click on Core Collections  -  SUCCESS")
        time.sleep(2)
    
    # Click on Core Collections detail view button
    try:
        driver.find_element(By.CSS_SELECTOR, "i.v-icon.notranslate.mdi.mdi-domain.theme--light.blue--text.text--darken-2").click()
    except NoSuchElementException:   
        print("Error: The CSS 'i.v-icon.notranslate.mdi.mdi-domain.theme--light.blue--text.text--darken-2' does not exist.") 
    else:
        print("Click on Core Collections Detail View Button  -  SUCCESS")
        time.sleep(2)

    # Click on Org Collections
    try:
        driver.find_element(By.ID, "a-OrgCollections").click()
    except NoSuchElementException:   
        print("Error: The ID 'a-OrgCollections' does not exist.") 
    else:
        print("Click on Org Collections  -  SUCCESS")
        time.sleep(2)

    # Click on New Org Collections button
    try:
        driver.find_element(By.ID, "btnNew").click()
    except NoSuchElementException:   
        print("Error: The ID 'btnNew' does not exist.") 
    else:
        print("Click on New Org Collections buttomn  -  SUCCESS")
        time.sleep(2)

    # Add a New Org Collection
    # Enter org collection name
    try:
        driver.find_element(By.ID, "CollectionName").send_keys("Test Org Collection")
    except NoSuchElementException:   
        print("Error: The ID 'CollectionName' does not exist.") 
    else:
        print("Enter Org Collection Name : Test Org Collection  -  SUCCESS")
        time.sleep(2)

    # Enter org collection description
    try:
        driver.find_element(By.ID, "Description").send_keys("Test Org Collection")
    except NoSuchElementException:   
        print("Error: The ID 'Description' does not exist.") 
    else:
        print("Enter Org Collection Name : Test Org Collection  -  SUCCESS")
        time.sleep(2)
        
    # Select Publications
    try:
        driver.find_element(By.CSS_SELECTOR, "#Selected > div.v-input--selection-controls__input > div.v-input--selection-controls__ripple").click()
    except NoSuchElementException:   
        print("Error: CSS '#Selected > div.v-input--selection-controls__input > div.v-input--selection-controls__ripple' does not exist.") 
    else:
        print("Select a Publication  -  SUCCESS")
    time.sleep(2)

    # try:
    #     driver.find_element(By.CSS_SELECTOR, "#btnAddNew19 .v-icon").click()
    # except NoSuchElementException:   
    #     print("Error: CSS '#btnAddNew19 .v-icon' does not exist.") 
    # else:
    #     print("Select a Publication  -  SUCCESS")
    #     time.sleep(2)

    # try:
    #     driver.find_element(By.CSS_SELECTOR, "#btnAddNew16 .v-icon").click()
    # except NoSuchElementException:   
    #     print("Error: CSS '#btnAddNew16 .v-icon' does not exist.") 
    # else:
    #     print("Select a Publication  -  SUCCESS")
    #     time.sleep(2)
    # 
    
    # Save org collection
    try:
        driver.find_element(By.ID, "btnSave").click()
    except NoSuchElementException:   
        print("Error: The ID 'btnSave' does not exist.") 
    else:
        print("Click on Org Collection SAVE button  -  SUCCESS")
        print("Org Collection SUCCESSFULLY Saved \n")
        time.sleep(2)

############################## USER MANAGEMENT ##############################

    try:
        driver.find_element(By.XPATH, "//div[3]/div/button").click()
    except NoSuchElementException:   
        print("Error: The XPATH '//div[3]/div/button' does not exist.") 
    else:
        print("Click on User Management  -  SUCCESS")
        time.sleep(2)

# Click Groups
    try:
        driver.find_element(By.ID, "a-6").click()
    except NoSuchElementException:   
        print("Error: The ID 'a-6' does not exist.") 
    else:
        print("Click and navigates to Groups  -  SUCCESS")
        time.sleep(2)

# Click New Group Button 
    try:
        driver.find_element(By.ID, "btnNew").click()
    except NoSuchElementException:   
        print("Error: The ID 'btnNew' does not exist.") 
    else:
        print("Click on New Group Button  -  SUCCESS")
        time.sleep(2)

# Add New Group
# Enter group name
    try:
        driver.find_element(By.ID, "name").send_keys("Group 001")
    except NoSuchElementException:   
        print("Error: The ID 'name' does not exist.") 
    else:
        print("Enter Group Name : Group 001  -  SUCCESS")
        time.sleep(2)

# Enter group Description
    try:
        driver.find_element(By.ID, "description").send_keys("Group 001 Description")
    except NoSuchElementException:   
        print("Error: The ID 'description' does not exist.") 
    else:
        print("Enter Group Description : Group 001 Description  -  SUCCESS")
        time.sleep(2)
        
# Select User
    try:
        driver.find_element(By.XPATH, "//div[@id='selected']/div/div").click()
    except NoSuchElementException:   
        print("Error: The XPATH '//div[@id='selected']/div/div' does not exist.") 
    else:
        print("Select User  -  SUCCESS")
        time.sleep(2)
        
# Save Group
    try:
        driver.find_element(By.XPATH, "//button[2]").click()
    except NoSuchElementException:   
        print("Error: The XPATH '//button[2]' does not exist.")
    else:
        print("Click on Group SAVE button  -  SUCCESS")
        print("Group SUCCESSFULLY Saved \n")
        time.sleep(2)
        
##### Search Group #####
# Search group by name 
    try:
        driver.find_element(By.ID, "search").send_keys("Group 001")
        time.sleep(2)
        pyautogui.press('enter')
    except NoSuchElementException:   
        print("Error: The element ID 'search' does not exist.") 
    else:
        print("Enter Search Result : Group 001  -  SUCCESS")
        print("Display Search Result  -  SUCCESS \n")
        time.sleep(2)

##### Delete Group #####
    try:
        driver.find_element(By.CSS_SELECTOR, "button.v-icon.notranslate.mr-2.icon-delete.v-icon--link.mdi.mdi-delete.theme--light").click()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR, "button.v-btn.v-btn--is-elevated.v-btn--has-bg.theme--light.v-size--default.error").click()
    except NoSuchElementException:   
        print("Error: Delete button element does not exist.") 
    else:
        print("Group SUCCESSFULLY Deleted \n")
        time.sleep(5)

# Click on Subscription
    try:
        driver.find_element(By.ID, "a-15").click()
    except NoSuchElementException:   
        print("Error: The ID 'a-15' does not exist.") 
    else:
        print("Click and navigates to Subscrition  -  SUCCESS")
        time.sleep(2)

# Click new subscription
    try:
        driver.find_element(By.ID, "btnNew").click()
    except NoSuchElementException:   
        print("Error: The ID 'btnNew' does not exist.") 
    else:
        print("Click on New Subscrition button -  SUCCESS")
        time.sleep(3)

# Click on Groups
    try:
        driver.find_element(By.ID, "Organization").click()
    except NoSuchElementException:   
        print("Error: The ID 'Organization' does not exist.") 
    else:
        print("Click on Groups Dropdown -  SUCCESS")
        time.sleep(2)

# Select Groups
    try:
        driver.find_element(By.XPATH, "//div[(text() = 'ABC Group' or . = 'ABC Group')]").click()
    except NoSuchElementException:   
        print("Error: The XPATH '//div[(text() = 'ABC Group' or . = 'ABC Group')]' does not exist.") 
    else:
        print("Select a Groups  -  SUCCESS")
        time.sleep(2)

# Click on Collections
    try:
        driver.find_element(By.ID, "organizationCollection").click()
    except NoSuchElementException:   
        print("Error: The ID 'organizationCollection' does not exist.") 
    else:
        print("Click on Collection Dropdwn  -  SUCCESS")
        time.sleep(2)

# Select a Collection
    try:
        driver.find_element(By.XPATH, "//div[(text() = 'ABC Collection' or . = 'ABC Collection')]").click()
    except NoSuchElementException:   
        print("Error: The XPATH '//div[(text() = 'ABC Collection' or . = 'ABC Collection')]' does not exist.") 
    else:
        print("Select a collection  -  SUCCESS")
        time.sleep(2)

# Save subscription
    try:
        driver.find_element(By.ID, "btnSave").click()
    except NoSuchElementException:   
        print("Error: The ID 'btnSave' does not exist.") 
    else:
        print("SUCCESSFULLY Subscribed \n")
        time.sleep(5)

# Delete subscription
    try:
        driver.find_element(By.CSS_SELECTOR, "button.v-icon.notranslate.mr-2.icon-delete.v-icon--link.mdi.mdi-delete.theme--light").click()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR, "button.v-btn.v-btn--is-elevated.v-btn--has-bg.theme--light.v-size--default.error > span.v-btn__content").click()
    except NoSuchElementException:   
        print("Error: Delete button element does not exist.") 
    else:
        print("Group SUCCESSFULLY Deleted \n")
        time.sleep(3)

############################## Logout ##############################
# Click on user name
    try:
        driver.find_element(By.CSS_SELECTOR, "button.ml-2.mr-2.v-btn.v-btn--text.theme--dark.v-size--default").click()
    except NoSuchElementException:   
        print("Error: The CSS 'button.ml-2.mr-2.v-btn.v-btn--text.theme--dark.v-size--default' does not exist.") 
    else:
        print("Click on user name  -  SUCCESS")
        time.sleep(1)

# Click on logout
    try:
        driver.find_element(By.XPATH, "//div[(text() = 'Log out' or . = 'Log out')]").click()
    except NoSuchElementException:   
        print("Error: The CSS '//div[(text() = 'Log out' or . = 'Log out')]' does not exist.") 
    else:
        print("Click on Logout button  -  SUCCESS")
        print("User SUCCESSFULLY logout\n\n")
        time.sleep(4)


time.sleep(500)
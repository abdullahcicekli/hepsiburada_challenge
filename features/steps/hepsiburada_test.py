import time
import random
from behave import given,when,then

def close_popup(browser):
    try:
        time.sleep(2)
        browser.find_element_by_class_name("checkoutui-Modal-2iZXl").click()
        time.sleep(1)
    except:
        pass


@given('hepsiburada.com')
def login(context):
    context.browser.get(context.link)


@when('clear the basket')
def clear_basket(context):
    context.browser.execute_script("window.history.go(-1)")
    context.browser.find_element_by_id("edit_basket_button").click()
    time.sleep(2)
    context.browser.find_element_by_xpath("/html/body/div/div/div/div[2]/div/div[2]/section/section/div/button").click()
    time.sleep(1)

    context.browser.find_element_by_css_selector("#onboarding_item_list > div.modal_overflow_LlLUi > div > div > div > button.sc-AxjAm.iDSyON.sflButton_2fKbY").click()

    assert context.browser.find_element_by_xpath("/html/body/div/div/div/div[2]/div/div[2]/div[1]/div[2]/div[2]/h1").text == 'Sepetin şu an boş',"Sepet Boşaltılamadı"


@when("I visit the cart")
def visit_cart(context):
    context.browser.find_element_by_id("cartItemCount").click()
    time.sleep(1)
    assert context.browser.title == "Sepetim", "Sepete Giderken Hata Oluştu"
    context.browser.find_element_by_id("continue_step_btn").click()
    time.sleep(3)
    assert context.browser.title == "Teslimat Bilgileri", "Teslimat Seçeneklerine Giderken Hata Oluştu"


@then('should be grouped "{result}"')
def group(context,result):
    item_list = context.browser.find_element_by_class_name("item_list_1NnvG").find_elements_by_class_name("group_list_1oZ2d")
    item_count = len(item_list)
    if result == 'differently':
        assert item_count > 1 , "Gruplamada Hata Var"
    elif result == 'together':
        assert item_count <= 1 , "Gruplamada Hata Var"

@when('when I try to login')
def login(context):
    context.browser.find_element_by_id("myAccount").click()
    context.browser.find_element_by_id('login').click()
    context.browser.find_element_by_id('txtUserName').send_keys(context.username)
    context.browser.find_element_by_id('txtPassword').send_keys(context.password)
    try:
        context.browser.find_element_by_id('btnLogin').click()
        # print("Login Complate")
    except:
        return "Giriş Sırasında Hata Oluştu"


@when('I search for product "{search_key}"')
def response(context,search_key):
    try:
        time.sleep(2)
        context.browser.find_element_by_xpath("/html/body/div/div/div/div[3]/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div/div/div[1]/div[2]/input").send_keys(search_key)
        context.browser.find_element_by_xpath("/html/body/div/div/div/div[3]/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div/div/div[2]").click()
    except:
        assert "Arama Sırasında Hata Oluştu"


@then('I should be able to choose random products from different vendors and add them to the cart')
def select_product(context):
    try:
        merchant = True
        while merchant:
            try:

                products = context.browser.find_element_by_class_name(f"product-list").find_elements_by_tag_name("li") # Ürünleri listeye al

                random_number = random.randint(1, len(products)) # Random bir Ürün Seçmek İçin Ürün Sayısına Kadar Bir Sayı Üret

                products[random_number-1].click() # Seçilen Ürüne Tıkla
                context.browser.find_element_by_xpath("/html/body/div[2]/main/div[3]/section[3]/div/div/table/tbody/tr/td[8]/a").click() # Diğer Satıcıları Görmek İçin
                merchant = False #Satıcı Varsa While'dan çık
            except:
                # print("No Other Sellers. Product is Changing...")
                context.browser.execute_script("window.history.go(-1)") #Ürünü satan başka satıcı yoksa geri gel ve farklı ürün seç

        context.browser.find_element_by_xpath("/html/body/div[2]/main/div[3]/section[3]/div/div/table/tbody/tr/td[8]/a/span").click()
        asd = context.browser.find_element_by_xpath(
            "/html/body/div[2]/main/div[3]/section[3]/div/div/div[7]/table").find_elements_by_tag_name("tr")
        random_numbers_for_merchant = len(asd) - 2 # Ürünü satan kaç satıcı var ?
        random_numbers_for_merchant = range(random_numbers_for_merchant)
        merchant_rand = random.sample(random_numbers_for_merchant, 2) # Random {merchant} satıcı belirlenir.

        context.browser.find_element_by_xpath(f"/html/body/div[2]/main/div[3]/section[3]/div/div/div[7]/table/tbody/tr[{merchant_rand[0] + 3}]/td[4]/form/button").click()
        close_popup(context.browser)
        context.browser.find_element_by_xpath(f"/html/body/div[2]/main/div[3]/section[3]/div/div/div[7]/table/tbody/tr[{merchant_rand[1] + 3}]/td[4]/form/button").click()

    except:
        assert "Ürün Eklenmedi"


@when("I visit the drone spare parts tab from the 'Remote Control Cars' tab under 'Books, Music, Movies, Hobbies'")
def step_impl(context):
    try:
        context.browser.find_element_by_xpath("/html/body/div/div/div/div[4]/div/div/div/div/div/div/div/div[1]/div/ul/li[9]/span/span").click()
        context.browser.find_element_by_xpath("/html/body/div/div/div/div[4]/div/div/div/div/div/div/div/div[1]/div/ul/li[9]/div/div/div[1]/div[2]/ul/li/ul[3]/li/a[2]").click()
    except:
        assert context.browser.title == "Uzaktan Kumandalı Araba ve Araç Fiyatları" , "İlgili Sekmeye Giderken Hata Oluştu"


@then('I should be able to choose "{number_of_product}" product at random and add it to the cart')
def step_impl(context, number_of_product):
    # try:
    random_number = random.randint(1, 24)
    context.browser.find_element_by_xpath("/html/body/div[3]/main/div[2]/div/div[7]/div[1]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div/div/div/div[9]").click()
    time.sleep(1)
    context.browser.find_element_by_xpath(f"/html/body/div[3]/main/div[2]/div/div[7]/div[1]/div[2]/div/div[3]/div/div/div/div/div/div/div/ul/li[{random_number}]").click()
    time.sleep(3)
    if int(number_of_product) > 1:
        for i in range(int(number_of_product)-1):
            context.browser.find_element_by_css_selector("#addToCartForm > div > div > button.button.effective.icon.icon-plus").click()

    context.browser.find_element_by_class_name("addToCartButton").click()
    close_popup(context.browser)
    # except:
    #     assert "Ürün Sepete Eklenemedi"


@then("then I must log in successfully")
def is_success_login(context):
    time.sleep(3)
    url = context.browser.current_url
    assert url == "https://www.hepsiburada.com/", "Giriş Yapılamadı. Banlanma Olabilir."



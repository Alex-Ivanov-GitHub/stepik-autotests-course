from .pages.product_page import ProductPage
# from .pages.login_page import LoginPage
# from time import sleep

link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear"
link2 = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"


@pytest.mark.need_review
def test_user_can_add_product_to_basket():
    pass


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.check_of_product()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page():
    pass


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page():
    pass

# Created by abdullah at 6.08.2021
Feature: add cart random product

  Scenario: Kullanıcı girişi yapılarak sepete ürün eklenmesi
    # Hepsiburada sisteminde Kullanıcı girişi yapılarak sepete ürün eklenmesi
    Given hepsiburada.com
    When when I try to login
    Then then I must log in successfully
    When I search for product "kablosuz mause logitech"
    Then I should be able to choose random products from different vendors and add them to the cart


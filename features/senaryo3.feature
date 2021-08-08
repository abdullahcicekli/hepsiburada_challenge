# Created by abdullah at 8.08.2021
Feature: # Analiz
  # Teslimat Seçenekleri paket gruplamasının neye
  #göreyapıldığının analiz otomasyonu

  Scenario: Farklı Satıcılardan Gönderilecek Ürünler Ayrı Gruplanmalı
    Given hepsiburada.com
    When when I try to login
    Then then I must log in successfully
    When I search for product "airpods"
    Then I should be able to choose random products from different vendors and add them to the cart
    When I visit the cart
    Then should be grouped "differently"

  Scenario: Aynı Satıcıdan Gönderilecek Ürünler Aynı Grupta Olmalı
    Given hepsiburada.com
    When I visit the cart
    And clear the basket
    Given hepsiburada.com
    When I visit the drone spare parts tab from the 'Remote Control Cars' tab under 'Books, Music, Movies, Hobbies'
    Then I should be able to choose "3" product at random and add it to the cart
    When I visit the cart
    Then should be grouped "together"

#  Scenario: 50 TL ve üzeri kargo bedava olmalı
#  Scenario: Cep telefonu, dizüstü bilgisayar veya tablet alımında 12,99 TL kargo ücreti olmalı
#  Scenario: Yansıtılan kargo ücreti max 12,99 TL olmalı ( Kötüye kullanım olabilir. )
# Created by abdullah at 6.08.2021
Feature: add cart no login

  Scenario: Kullanıcı girişi yapılmadan belirtilen ürünü sepete ekleme
     # Hepsiburada sisteminde Kullanıcı girişi yapılmadan belirtilen ürünü sepete ekleme
    Given hepsiburada.com
    When I visit the drone spare parts tab from the 'Remote Control Cars' tab under 'Books, Music, Movies, Hobbies'
    Then I should be able to choose "5" product at random and add it to the cart
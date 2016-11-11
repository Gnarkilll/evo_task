#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
from test_cases import BaseTestCase
from FavoritesPage import FavoritesPage
from HeaderContentMenu import HeaderContentMenu
from AllProductsPage import GalleryMode, ListMode
from ProductPage import ProductInfoSection, MovableBlock, VisitedBlock


class FavoritesTests(BaseTestCase):

    def test_add_to_favorites_in_gallery_mode_using_link(self):
        self.select_product_using_gallery_mode()
        self.gm.add_using_link()
        self.execute_gallery_asserts_for_add_actions()

    def test_remove_from_favorites_in_gallery_mode_using_link(self):
        self.select_product_using_gallery_mode()
        self.gm.add_using_link()
        self.gm.remove_using_link()
        self.execute_gallery_asserts_for_remove_actions()

    def test_add_to_favorites_in_gallery_mode_using_icon(self):
        self.select_product_using_gallery_mode()
        self.gm.add_using_icon()
        self.execute_gallery_asserts_for_add_actions()

    def test_remove_from_favorites_in_gallery_mode_using_icon(self):
        self.select_product_using_gallery_mode()
        self.gm.add_using_icon()
        self.gm.remove_using_icon()
        self.execute_gallery_asserts_for_remove_actions()

    def test_add_to_favorites_in_list_mode_using_link(self):
        self.select_product_using_list_mode()
        self.lm.add_using_link()
        self.execute_list_asserts_for_add_actions()

    def test_remove_from_favorites_in_list_mode_using_link(self):
        self.select_product_using_list_mode()
        self.lm.add_using_link()
        self.lm.remove_using_link()
        self.execute_list_asserts_for_remove_actions()

    def test_add_to_favorites_in_list_mode_using_icon(self):
        self.select_product_using_list_mode()
        self.lm.add_using_icon()
        self.execute_list_asserts_for_add_actions()

    def test_remove_from_favorites_in_list_mode_using_icon(self):
        self.select_product_using_list_mode()
        self.lm.add_using_icon()
        self.lm.remove_using_icon()
        self.execute_list_asserts_for_remove_actions()

    def test_add_to_favorites_on_product_page_using_link(self):
        self.pis.open_product()
        self.pis.add_using_link()
        self.execute_product_page_asserts_for_add_actions()

    def test_remove_from_favorites_on_product_page_using_link(self):
        self.pis.open_product()
        self.pis.add_using_link()
        self.pis.remove_using_link()
        self.execute_product_page_asserts_for_remove_actions()

    def test_add_to_favorites_on_product_page_using_icon(self):
        self.pis.open_product()
        self.pis.add_using_icon()
        self.execute_product_page_asserts_for_add_actions()

    def test_remove_from_favorites_on_product_page_using_icon(self):
        self.pis.open_product()
        self.pis.add_using_icon()
        self.pis.remove_using_icon()
        self.execute_product_page_asserts_for_remove_actions()

    def test_add_to_favorites_on_product_page_using_scroll_section(self):
        self.pis.open_product()
        self.mpis.scroll_to_movable_block()
        self.mpis.add_in_movable_block()
        self.assertEqual(self.mpis.get_link_text(), u'Убрать из избранного')
        self.assertTrue(self.pis.is_top_icon_active())
        self.assertTrue(self.pis.is_bottom_icon_active())
        self.assertEqual(self.items(), 1)

    def test_remove_from_favorites_on_product_page_using_scroll_section(self):
        self.pis.open_product()
        self.mpis.scroll_to_movable_block()
        self.mpis.add_in_movable_block()
        self.mpis.remove_in_movable_block()
        self.assertEqual(self.mpis.get_link_text(), u'Добавить в избранное')
        self.assertFalse(self.pis.is_top_icon_active())
        self.assertFalse(self.pis.is_bottom_icon_active())
        self.assertEqual(self.items(), 0)

    def test_add_to_favorite_from_last_visited(self):
        self.pis.open_product()
        self.vb.scroll_to_visited_block()
        self.vb.add_in_visited_block()
        self.assertEqual(self.pis.get_link_text(), u'Убрать из избранного')
        self.assertEqual(self.mpis.get_link_text(), u'Убрать из избранного')
        self.assertTrue(self.pis.is_top_icon_active())
        self.assertTrue(self.pis.is_bottom_icon_active())
        self.assertTrue(self.vb.is_icon_active())
        self.assertEqual(self.items(), 1)

    def test_remove_from_favorite_from_last_visited(self):
        self.pis.open_product()
        self.vb.scroll_to_visited_block()
        self.vb.add_in_visited_block()
        self.vb.remove_in_visited_block()
        self.assertEqual(self.pis.get_link_text(), u'Добавить в избранное')
        self.assertEqual(self.mpis.get_link_text(), u'Добавить в избранное')
        self.assertFalse(self.pis.is_top_icon_active())
        self.assertFalse(self.pis.is_bottom_icon_active())
        self.assertFalse(self.vb.is_icon_active())
        self.assertEqual(self.items(), 0)

    @unittest.skip('Impossible to click by button using link in gallery mode')
    def test_redirect_to_favorites_page_in_gallery_mode_using_link(self):
        self.select_product_using_gallery_mode()
        self.gm.redirect_using_link()
        self.assertEqual(self.fp.get_title(), u'Избранное')

    def test_redirect_to_favorites_page_in_gallery_mode_using_icon(self):
        self.select_product_using_gallery_mode()
        self.gm.redirect_using_icon()
        self.assertEqual(self.fp.get_title(), u'Избранное')

    def test_redirect_to_favorites_page_from_header(self):
        self.select_product_using_gallery_mode()
        self.gm.add_using_link()
        self.hcm.open_favorites_page()
        self.assertEqual(self.fp.get_title(), u'Избранное')

    def test_check_that_added_product_displays_on_favorites_page(self):
        self.add_product_and_open_favorites_page_on_category_tab()
        self.assertEqual(self.fp.get_category_tab_title(), u'Велосипедные шины')
        self.assertEqual(self.fp.get_category_tab_counter(), 1)
        self.assertEqual(self.items(), 1)

    def test_check_that_added_product_can_be_remove(self):
        self.add_product_and_open_favorites_page_on_category_tab()
        self.fp.remove_from_favorites()
        self.assertEqual(self.fp.get_category_tab_title(), u'Велосипедные шины')
        self.assertEqual(self.fp.get_category_tab_counter(), 0)
        self.assertEqual(self.items(), 0)

    def test_send_favorites_list_to_email(self):
        self.add_product_and_open_favorites_page_on_category_tab()
        self.fp.open_send_mail_window()
        self.fp.fill_email(10)
        self.fp.send_mail()
        self.assertEqual(self.fp.get_message(), u'Список избранного отправлен на указанный email')

    @unittest.skip('Skip this test')
    def test_send_favorites_list_to_email_if_product_list_is_empty(self):
        # Button that opens send pop-up window is disabled
        pass

    @unittest.skip('Skip this test')
    def test_send_favorites_list_to_fail_email(self):
        # If email is fail the message - "Неверный email адрес." is showed
        pass

    @unittest.skip('Skip this test')
    def test_send_favorites_list_to_empty_email(self):
        # If email is empty the message - "Это обязательное поле." is showed
        pass

    @property
    def gm(self):
        return GalleryMode(self.driver)

    @property
    def lm(self):
        return ListMode(self.driver)

    @property
    def pis(self):
        return ProductInfoSection(self.driver)

    @property
    def mpis(self):
        return MovableBlock(self.driver)

    @property
    def vb(self):
        return VisitedBlock(self.driver)

    @property
    def fp(self):
        return FavoritesPage(self.driver)

    @property
    def hcm(self):
        return HeaderContentMenu(self.driver)

    def items(self):
        return HeaderContentMenu(self.driver).get_amount_of_favorites_items()

    def select_product_using_gallery_mode(self):
        self.gm.gallery_mode()
        self.gm.select_product()

    def select_product_using_list_mode(self):
        self.lm.list_mode()
        self.lm.select_product()

    def add_product_and_open_favorites_page_on_category_tab(self):
        self.select_product_using_gallery_mode()
        self.gm.add_using_link()
        self.hcm.open_favorites_page()
        self.fp.select_category_tab()

    def execute_gallery_asserts_for_add_actions(self):
        self.assertEqual(self.gm.get_link_text(), u'Убрать из избранного')
        self.assertTrue(self.gm.is_top_icon_active())
        self.assertTrue(self.gm.get_icon_status())
        self.assertEqual(self.items(), 1)

    def execute_gallery_asserts_for_remove_actions(self):
        self.assertEqual(self.gm.get_link_text(), u'Добавить в избранное')
        self.assertFalse(self.gm.is_top_icon_active())
        self.assertFalse(self.gm.get_icon_status())
        self.assertEqual(self.items(), 0)

    def execute_list_asserts_for_add_actions(self):
        self.assertEqual(self.lm.get_link_text(), u'Убрать из избранного')
        self.assertTrue(self.lm.is_top_icon_active())
        self.assertTrue(self.lm.get_icon_status())
        self.assertEqual(self.items(), 1)

    def execute_list_asserts_for_remove_actions(self):
        self.assertEqual(self.lm.get_link_text(), u'Добавить в избранное')
        self.assertFalse(self.lm.is_top_icon_active())
        self.assertFalse(self.lm.get_icon_status())
        self.assertEqual(self.items(), 0)

    def execute_product_page_asserts_for_add_actions(self):
        self.assertEqual(self.pis.get_link_text(), u'Убрать из избранного')
        self.assertTrue(self.pis.is_top_icon_active())
        self.assertTrue(self.pis.is_bottom_icon_active())
        self.assertEqual(self.items(), 1)

    def execute_product_page_asserts_for_remove_actions(self):
        self.assertEqual(self.pis.get_link_text(), u'Добавить в избранное')
        self.assertFalse(self.pis.is_top_icon_active())
        self.assertFalse(self.pis.is_bottom_icon_active())
        self.assertEqual(self.items(), 0)


#  ui/tests/test_items.py: Unit tests for item maintenance page UI
#
#  Copyright 2014 Sudaraka Wijesinghe <sudaraka.org/contact>
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Affero General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Affero General Public License for more details.
#
#  You should have received a copy of the GNU Affero General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

""" UI Unit test for item maintenance page """

from ui.tests.base import BaseUnitTestCase


class ItemsPageTest(BaseUnitTestCase):
    """ Item maintenance page unit test """

    uri = '/item-maintenance/'
    template = 'items.html'
    page_title = 'Item Maintenance'

    def test_uri_render_correct_template(self):
        """ Call base class function """

        self.uri_render_correct_template()

    def test_site_title_is_being_passed_to_the_template(self):
        """ Call base class function """

        self.site_title_is_being_passed_to_the_template()

    def test_site_version_is_being_passed_to_the_template(self):
        """ Call base class function """

        self.site_version_is_being_passed_to_the_template()
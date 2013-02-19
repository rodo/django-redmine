# -*- coding: utf-8 -*-
#
# Copyright (c) 2013 Rodolphe Quiédeville <rodolphe@quiedeville.org>
#
#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.
#
#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.
#
#     You should have received a copy of the GNU General Public License
#     along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
"""
List all projects
"""
import logging
from django.conf import settings
from django.core.management.base import BaseCommand
from django_redmine.utils import RedmineClient

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'List all projects'

    def handle(self, *args, **options):
        """
        Handle the munin command
        """
        r = RedmineClient(settings.REDMINE_URL,
                          settings.REDMINE_USERNAME,
                          settings.REDMINE_PASSWORD,
                          '')
        for proj in r.get_projects():
            print "%-3d %s" % (int(proj.get_element('id')),
                               proj.get_element('name'))


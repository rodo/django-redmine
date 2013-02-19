# -*- coding: utf-8 -*-
#
# Copyright (c) 2013 Rodolphe Quiédeville <rodolphe@quiedeville.org>
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
# 3. Neither the name of the University nor the names of its contributors
#    may be used to endorse or promote products derived from this software
#    without specific prior written permission.
#
"""
List all trackers
"""
import logging
from django.conf import settings
from django.core.management.base import BaseCommand
from django_redmine.utils import RedmineClient

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'List all trackers'

    def handle(self, *args, **options):
        """
        Handle the munin command
        """
        r = RedmineClient(settings.REDMINE_URL,
                          settings.REDMINE_USERNAME,
                          settings.REDMINE_PASSWORD,
                          '')
        for track in r.get_trackers():
            print "%-3d %s" % (int(track.get_element('id')),
                               track.get_element('name'))


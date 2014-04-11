#===============================================================================
# Copyright 2014 Jake Ross
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#===============================================================================

#============= enthought library imports =======================
from traits.api import HasTraits, List

#============= standard library imports ========================
from numpy import argmax, array
#============= local library imports  ==========================
# import logging
# logging.basicConfig()
# log=logging.getLogger('plateau')
# from pychron.core.helpers.logger_setup import logging_setup, new_logger
#
# logging_setup('plateau', use_archiver=False)
# log = new_logger('foo')


class Plateau(HasTraits):
    ages = List
    errors = List
    signals = List
    exclude = List

    nsteps = 3
    overlap_sigma = 2

    def find_plateaus(self):

        n = len(self.ages)
        exclude = self.exclude
        ss = [s for i, s in enumerate(self.signals)
              if not i in exclude]

        self.total_signal = float(sum(ss))
        # log.info(self.total_signal)

        idxs = []
        spans = []

        for i in range(n):
            if i in exclude:
                continue
            idx = self._find_plateaus(n, i, exclude)
            if idx:
                # log.debug('found {} {}'.format(*idx))
                idxs.append(idx)
                spans.append(idx[1] - idx[0])

        if spans:
            return idxs[argmax(array(spans))]

        return idxs

    def _find_plateaus(self, n, start, exclude):
        potential_end = None
        for i in range(start, n, 1):
            if i in exclude:
                continue

            if not self.check_overlap(start, i):
                # log.debug('{} {} overlap failed'.format(start, i))
                break

            if not self.check_nsteps(start, i):
                # log.debug('{} {} nsteps failed'.format(start, i))
                continue

            if not self.check_percent_released(start, i):
                # log.debug('{} {} percent failed'.format(start, i))
                continue

            potential_end = i

        if potential_end:
            return start, potential_end

    def check_percent_released(self, start, end):
        s = sum(self.signals[start:end + 1])
        # log.debug('percent {}'.format(s / self.total_signal))
        return s / self.total_signal >= 0.5

    def check_overlap(self, start, end):
        overlap_sigma = self.overlap_sigma
        a1 = self.ages[start]
        a2 = self.ages[end]
        e1 = self.errors[start]
        e2 = self.errors[end]

        e1 *= overlap_sigma
        e2 *= overlap_sigma
        if a1 - e1 < a2 + e2 and a1 + e1 > a2 - e2:
            return True

    def check_nsteps(self, start, end):
        return end - start >= self.nsteps

#============= EOF =============================================


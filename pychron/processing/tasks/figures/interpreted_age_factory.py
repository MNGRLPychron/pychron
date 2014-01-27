#===============================================================================
# Copyright 2013 Jake Ross
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
from traits.api import List
from traitsui.api import View, Item, TableEditor, EnumEditor

#============= standard library imports ========================
#============= local library imports  ==========================
from traitsui.extras.checkbox_column import CheckboxColumn
from traitsui.table_column import ObjectColumn
from pychron.loggable import Loggable


class InterpretedAgeFactory(Loggable):
    groups=List
    def traits_view(self):
        cols=[ObjectColumn(name='identifier', editable=False),
              ObjectColumn(name='preferred_age_kind',
                           editor=EnumEditor(name='preferred_ages')),
              ObjectColumn(name='preferred_age_value', format='%0.3f',editable=False),
              ObjectColumn(name='preferred_age_error', format='%0.4f',editable=False),
              ObjectColumn(name='nanalyses', editable=False),

              CheckboxColumn(name='use',label='Save DB')]
        editor=TableEditor(columns=cols)
        v=View(Item('groups', show_label=False, editor=editor),
               resizable=True,
               title='Set Interpreted Age',
               kind='livemodal',
               buttons=['OK','Cancel'])

        return v

#============= EOF =============================================


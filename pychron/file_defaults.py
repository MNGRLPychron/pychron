# ===============================================================================
# Copyright 2015 Jake Ross
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ===============================================================================

# ============= enthought library imports =======================
# ============= standard library imports ========================
# ============= local library imports  ==========================
"""
This file defines the text for various default files.

Values are used in pychron.paths when building directory structure
"""


DEFAULT_INITIALIZATION = '''<root>
    <globals>
    </globals>
    <plugins>
        <general>
            <plugin enabled="false">Processing</plugin>
            <plugin enabled="false">MediaServer</plugin>
            <plugin enabled="false">PyScript</plugin>
            <plugin enabled="false">Video</plugin>
            <plugin enabled="false">Database</plugin>
            <plugin enabled="false">Entry</plugin>
            <plugin enabled="false">SystemMonitor</plugin>
            <plugin enabled="false">ArArConstants</plugin>
            <plugin enabled="false">Loading</plugin>
            <plugin enabled="false">Workspace</plugin>
            <plugin enabled="false">LabBook</plugin>
            <plugin enabled="false">DashboardServer</plugin>
            <plugin enabled="false">DashboardClient</plugin>
        </general>
        <hardware>
        </hardware>
        <social>
        </social>
    </plugins>
</root>
'''

DEFAULT_STARTUP_TESTS = '''
- plugin: Database
  tests:
    - test_pychron
    - test_pychron_version
    - test_massspec
- plugin: LabBook
  tests:
- plugin: ArArConstants
  tests:
- plugin: ArgusSpectrometer
  tests:
    - test_communication
- plugin: ExtractionLine
  tests:
    - test_valve_communication
    - test_gauge_communication
'''

EXPERIMENT_DEFAULTS = '''
columns:
  - Labnumber
  - Aliquot
  - Sample
  - Position
  - Extract
  - Units
  - Duration (s)
  - Cleanup (s)
  - Beam (mm)
  - Pattern
  - Extraction
  - Measurement
  - Conditionals
  - Comment
'''

IDEOGRAM_DEFAULTS = '''
padding:
 padding_left: 100
 padding_right: 100
 padding_top: 100
 padding_bottom: 100

calculations:
 probability_curve_kind: cumulative
 mean_calculation_kind: 'weighted mean'
display:
 mean_indicator_fontsize: 12
 mean_sig_figs: 2

general:
 index_attr: uage

axes:
 xtick_in: 1
 xtick_out: 5
 ytick_in: 1
 ytick_out: 5
background:
 bgcolor: 239,238,185
 plot_bgcolor: 208,243,241
'''

SPECTRUM_DEFAULTS = '''
padding:
 padding_left: 100
 padding_right: 100
 padding_top: 100
 padding_bottom: 100
plateau:
 plateau_line_width: 1
 plateau_line_color: black
 plateau_font_size: 12
 plateau_sig_figs: 2
 # calculate_fixed_plateau: False
 # calculate_fixed_plateau_start: ''
 # calculate_fixed_plateau_end: ''
 pc_nsteps: 3
 pc_gas_fraction: 50
integrated:
 integrated_font_size: 12
 integrated_sig_figs: 2
legend:
 legend_location: Upper Right
 include_legend: False
 include_sample_in_legend: False
labels:
 display_step: True
 display_extract_value: False
 step_label_font_size: 10
axes:
 xtick_in: 1
 xtick_out: 5
 ytick_in: 1
 ytick_out: 5
background:
 bgcolor: 239,238,185
 plot_bgcolor: 208,243,241
'''
ISOCHRON_DEFAULTS = '''
background:
 bgcolor: 239,238,185
 plot_bgcolor: 208,243,241
'''

INVERSE_ISOCHRON_DEFAULTS = '''
nominal_intercept:
  nominal_intercept_label: Atm
  nominal_intercept_value: 295.5
  show_nominal_intercept: True
  invert_nominal_intercept: True
inset:
  inset_marker_size: 2.5
  inset_marker_color: black
'''

COMPOSITE_DEFAULTS = '''
- padding:
   padding_left: 100
   padding_right: 50
   padding_top: 100
   padding_bottom: 100
- padding:
   padding_left: 50
   padding_right: 100
   padding_top: 100
   padding_bottom: 100

'''

SYSTEM_HEALTH = '''
values:
 - Ar40/Ar36
 - uAr40/Ar36
 - ysymmetry
 - extraction_lens
 - ysymmetry
 - zsymmetry
 - zfocus
 - H2_deflection
 - H1_deflection
 - AX_deflection
 - L1_deflection
 - L2_deflection
 - CDD_deflection
general:
 limit: 100
conditionals:
 -
  attribute: Ar40/Ar36
  function: std
  comparison: x>1
  action: cancel
  min_n: 10
  bin_hours: 6
  analysis_types:
   - air
 -
  attribute: ysymmetry
  function: value
  action: cancel
  analysis_types:
   - air

'''


SCREEN_FORMATTING_DEFAULTS = '''
x_tick_in: 2
x_tick_out: 5
x_title_label_font: Helvetica 12
x_tick_label_font: Helvetica 10

y_tick_in: 2
y_tick_out: 5
y_title_label_font: Helvetica 12
y_tick_label_font: Helvetica 10

'''

PRESENTATION_FORMATTING_DEFAULTS = '''
x_tick_in: 2
x_tick_out: 5
x_title_font: Helvetica 22
x_tick_label_font: Helvetica 14

y_tick_in: 2
y_tick_out: 5
y_title_font: Helvetica 22
y_tick_label_font: Helvetica 14

'''
# ============= EOF =============================================




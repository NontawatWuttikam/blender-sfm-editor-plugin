# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
import bpy
from .main_panel import SFMEditorPanel

# https://wiki.blender.org/wiki/Process/Addons/Guidelines/metainfo
bl_info = {
        "name": "My Awesome Add-on",
        "author": "Aaron Powell",
        "version": (1, 0),
        "blender": (2, 80, 0),
        "location": "View3D > Sidebar",
        "description": "A description of my plugin",
        "category": "Object",
        "warning": "", # used for warning icon and text in add-ons panel
        "wiki_url": "http://my.wiki.url",
        "tracker_url": "http://my.bugtracker.url",
        "support": "COMMUNITY",
        }

def register():
    bpy.utils.register_class(SFMEditorPanel)

def unregister():
    bpy.utils.unregister_class(SFMEditorPanel)

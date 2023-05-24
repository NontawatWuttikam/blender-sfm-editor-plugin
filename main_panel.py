import bpy

class SFMEditorPanel(bpy.types.Panel):
    bl_idname = "SFM_EDITOR_PANEL"
    bl_label = "SFM Editor"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Colmap"

    @classmethod
    def poll(cls, context):
        return (context.object is not None)

    def draw_header(self, context):
        layout = self.layout

    def draw(self, context):
        self.draw_image_box()
        self.draw_covisible_box()
        
    def draw_image_box(self):
        layout = self.layout
        box = layout.box()
        box.label(text="Images")
        box.operator("object.select_all").action = 'TOGGLE'
        row = box.row()
        row.operator("object.select_all").action = 'INVERT'
        row.operator("object.select_random")
    
    def draw_covisible_box(self):
        layout = self.layout
        box = layout.box()
        box.label(text="Co-Visible Features")
# bpy.utils.register_class(SFMEditorPanel)
import Grasshopper as gh
import scriptcontext as sc

def switch_wire_display(display_setting, gh_object):
    if not isinstance(gh_object, gh.Kernel.Parameters.Param_GenericObject):
        return

    sources = list(gh_object.Sources)
    for source in sources:
        if not isinstance(source, gh.Kernel.Parameters.Param_GenericObject):
            return
    
    gh_object.WireDisplay = gh.Kernel.GH_ParamWireDisplay(display_setting)

def set_data_param_display(gh_object):
    if not isinstance(gh_object, gh.Kernel.Parameters.Param_GenericObject):
        return
    gh_object.IconDisplayMode = gh.Kernel.GH_IconDisplayMode.name

def main(setting):
    gh_document = ghenv.Component.OnPingDocument()

    for gh_object in gh_document.Objects:
        switch_wire_display(setting, gh_object)
        set_data_param_display(gh_object)

main(setting)



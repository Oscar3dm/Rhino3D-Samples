def get_layers_with_name(doc, search_name):
    layers = []
    layertable = doc.Layers
    for layer in layertable:
        if layer.IsDeleted: 
            continue
        if layer.Name == search_name:
            layers.append(layer)
    return layers
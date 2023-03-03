from maya import cmds,mel

def RemoveNamespace():
    namespaces = cmds.namespaceInfo(listOnlyNamespaces=True,recurse=True,baseName=True)
    print(namespaces)
    namespaces.remove("UI")
    namespaces.remove("shared")
    print(namespaces)

    for name_space in namespaces:
        cmds.namespace(removeNamespace=name_space,mnr=True)
        pass


# 移动组到大纲 （其中一个组不存在时即失败）
def MoveGroupToOutLineAndExport():
    CharacterChilds = cmds.listRelatives("Group")
    SkeletonGroupName = "DeformationSystem"
    ModelGroupName = "Geometry"
    if SkeletonGroupName in CharacterChilds and ModelGroupName in CharacterChilds:
        cmds.parent(ModelGroupName, w=True)
        cmds.parent(SkeletonGroupName, w=True)
        
        cmds.select((ModelGroupName,SkeletonGroupName))

RemoveNamespace()
MoveGroupToOutLineAndExport()